"""
Fingerprint extraction. Focus: prove that a domain is junk.
Each record receives a page_type — the primary output classifier.
"""
import hashlib
import re
import base64
import struct
from html.parser import HTMLParser


# ---------------------------------------------------------------------------
# SimHash
# ---------------------------------------------------------------------------

def _hash64(s: str) -> int:
    h = hashlib.md5(s.encode("utf-8", errors="replace")).digest()
    return struct.unpack("<q", h[:8])[0]

def simhash(text: str, bits: int = 64) -> str:
    tokens = re.findall(r"\w+", text.lower())
    if not tokens:
        return "0" * (bits // 4)
    v = [0] * bits
    for tok in tokens[:500]:  # first 500 words is sufficient
        h = _hash64(tok)
        for i in range(bits):
            v[i] += 1 if (h >> i) & 1 else -1
    result = sum((1 << i) for i in range(bits) if v[i] > 0)
    return format(result, f"0{bits // 4}x")


# ---------------------------------------------------------------------------
# Favicon MMH3 (Shodan-compatible)
# ---------------------------------------------------------------------------

def _mmh3_32(data: bytes, seed: int = 0) -> int:
    c1, c2 = 0xCC9E2D51, 0x1B873593
    length = len(data)
    h = seed & 0xFFFFFFFF
    for i in range(0, length - 3, 4):
        k = struct.unpack_from("<I", data, i)[0]
        k = (k * c1) & 0xFFFFFFFF
        k = ((k << 15) | (k >> 17)) & 0xFFFFFFFF
        k = (k * c2) & 0xFFFFFFFF
        h ^= k
        h = ((h << 13) | (h >> 19)) & 0xFFFFFFFF
        h = (h * 5 + 0xE6546B64) & 0xFFFFFFFF
    tail = length & 3
    if tail:
        k = 0
        for i in range(tail - 1, -1, -1):
            k = (k << 8) | data[length - tail + i]
        k = (k * c1) & 0xFFFFFFFF
        k = ((k << 15) | (k >> 17)) & 0xFFFFFFFF
        k = (k * c2) & 0xFFFFFFFF
        h ^= k
    h ^= length
    h ^= h >> 16
    h = (h * 0x85EBCA6B) & 0xFFFFFFFF
    h ^= h >> 13
    h = (h * 0xC2B2AE35) & 0xFFFFFFFF
    h ^= h >> 16
    return struct.unpack("i", struct.pack("I", h))[0]

def favicon_mmh3(raw_bytes: bytes) -> int:
    return _mmh3_32(base64.encodebytes(raw_bytes))


# ---------------------------------------------------------------------------
# HTML parser
# ---------------------------------------------------------------------------

class _PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False
        self.favicon_href = ""
        self.form_actions = []
        self.js_srcs = []
        self.meta_generator = ""
        self._text_parts = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "link":
            rel = a.get("rel", "").lower()
            if "icon" in rel:
                self.favicon_href = a.get("href", "")
        elif tag == "form":
            if a.get("action"):
                self.form_actions.append(a["action"])
        elif tag == "script" and a.get("src"):
            self.js_srcs.append(a["src"])
        elif tag == "meta" and a.get("name", "").lower() == "generator":
            self.meta_generator = a.get("content", "")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        stripped = data.strip()
        if stripped:
            self._text_parts.append(stripped)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def visible_text(self) -> str:
        return " ".join(self._text_parts)


# ---------------------------------------------------------------------------
# Page classifiers
# ---------------------------------------------------------------------------

_PARKING_PATTERNS = [
    r"namesilo\.com",
    r"domain\s+(?:is\s+)?(?:parked|for\s+sale|available)",
    r"parked\s+(?:free\s+)?(?:by|at|with|on)",
    r"this\s+domain\s+(?:has\s+been\s+)?parked",
    r"sedo\.com", r"sedo\s+domain\s+parking",
    r"godaddy\.com/domain", r"afternic\.com",
    r"this\s+domain\s+registered\s+via\s+godaddy",
    r"dan\.com", r"undeveloped\.com",
    r"uniregistry\.com",
    r"buy\s+this\s+domain",
    r"domain\s+for\s+sale",
    r"inquire\s+about\s+this\s+domain",
    r"make\s+an\s+offer",
    r"domain\s+may\s+be\s+for\s+sale",
]

_COMING_SOON_PATTERNS = [
    r"coming\s+soon",
    r"under\s+construction",
    r"launch\s+(?:date|coming)",
    r"we[''`]re\s+(?:working|building|launching)",
    r"stay\s+tuned",
    r"website\s+(?:is\s+)?(?:coming|launching)",
]

_DEFAULT_SERVER_PATTERNS = [
    r"apache\s+(?:http\s+server\s+)?test\s+page",
    r"test\s+page\s+for\s+the\s+apache",
    r"nginx\s+welcome",
    r"welcome\s+to\s+nginx",
    r"iis\s+windows\s+server",
    r"it\s+works!",
    r"cpanel.*welcome",
    r"plesk",
    r"directadmin",
]

_EMPTY_TITLES = {
    "", "untitled", "untitled document", "new tab", "index",
    "home", "welcome", "404", "403", "error",
}

_PARKING_SERVICES = {
    "namesilo":   r"namesilo",
    "sedo":       r"sedo\.com",
    "godaddy":    r"godaddy",
    "afternic":   r"afternic",
    "dan":        r"dan\.com",
    "parkingcrew":r"parkingcrew",
    "bodis":      r"bodis\.com",
    "uniregistry":r"uniregistry",
    "above":      r"above\.com",
    "domain_io":  r"domain\.io",
}


def _match_any(text: str, patterns: list) -> bool:
    for p in patterns:
        if re.search(p, text, re.I):
            return True
    return False

def _detect_parking_service(text: str) -> str:
    for name, pat in _PARKING_SERVICES.items():
        if re.search(pat, text, re.I):
            return name
    return ""

def _word_count(text: str) -> int:
    return len(re.findall(r"\w{3,}", text))


# ---------------------------------------------------------------------------
# Main function
# ---------------------------------------------------------------------------

def extract(domain: str, resp_url: str, status: int, headers: dict,
            body: bytes, redirect_chain: list, tls_info: dict) -> dict:

    body_size = len(body)
    text_raw = body.decode("utf-8", errors="replace")
    text_lower = text_raw.lower()

    parser = _PageParser()
    try:
        parser.feed(text_raw[:300_000])
    except Exception:
        pass

    title = re.sub(r"\s+", " ", parser.title).strip()[:200]
    title_lower = title.lower().strip()
    visible_text = parser.visible_text()
    word_count = _word_count(visible_text)

    from urllib.parse import urlparse
    final_domain = urlparse(resp_url).netloc.lstrip("www.") if resp_url else ""
    redirected_away = bool(final_domain and domain not in final_domain)

    parking_service = _detect_parking_service(text_lower + " " + resp_url)
    is_parking = bool(parking_service) or _match_any(text_lower + title_lower, _PARKING_PATTERNS)
    is_for_sale = bool(re.search(r"(?:buy|purchase)\s+this\s+domain|domain\s+for\s+sale|make\s+an\s+offer", text_lower, re.I))
    is_coming_soon = _match_any(title_lower + " " + text_lower[:2000], _COMING_SOON_PATTERNS)
    is_default_server = _match_any(text_lower[:5000], _DEFAULT_SERVER_PATTERNS)
    is_empty = body_size < 2048 or word_count < 20
    has_forms = bool(parser.form_actions)

    if is_parking or parking_service:
        page_type = "parking"
    elif is_for_sale:
        page_type = "for_sale"
    elif is_default_server:
        page_type = "default_server"
    elif is_coming_soon:
        page_type = "coming_soon"
    elif is_empty and not has_forms:
        page_type = "empty"
    elif redirected_away:
        page_type = "redirect_external"
    elif status in (404, 410):
        page_type = "not_found"
    elif status >= 500:
        page_type = "server_error"
    elif word_count > 200 and has_forms:
        page_type = "active_with_forms"
    elif word_count > 200:
        page_type = "active_content"
    else:
        page_type = "low_content"

    server_val   = headers.get("server", "")
    ct_val       = headers.get("content-type", "").split(";")[0].strip()
    xpb_val      = headers.get("x-powered-by", "")
    etag_val     = headers.get("etag", "").strip('"').strip()
    via_val      = headers.get("via", "")
    cache_ctrl   = headers.get("cache-control", "")
    has_cookies  = bool(headers.get("set-cookie"))
    is_cloudflare = bool(headers.get("cf-ray") or "cloudflare" in server_val.lower())

    title_md5 = hashlib.md5(title_lower.encode()).hexdigest()[:16] if title_lower else ""
    server_fp = hashlib.md5(f"{server_val}|{ct_val}|{xpb_val}".encode()).hexdigest()[:12]

    return {
        "domain": domain,
        "final_url": resp_url,
        "status_code": status,
        "redirect_chain": redirect_chain[:5],
        "redirected_away": redirected_away,
        "final_domain": final_domain,

        "page_type": page_type,
        "parking_service": parking_service,
        "is_for_sale": is_for_sale,
        "is_coming_soon": is_coming_soon,
        "is_default_server": is_default_server,

        "title": title,
        "title_md5": title_md5,
        "word_count": word_count,
        "body_size": body_size,
        "body_simhash": simhash(visible_text),
        "body_md5": hashlib.md5(body).hexdigest(),

        "favicon_hint": parser.favicon_href,
        "meta_generator": parser.meta_generator,
        "form_actions": parser.form_actions[:5],
        "js_srcs": parser.js_srcs[:10],

        "server": server_val,
        "server_fp": server_fp,
        "x_powered_by": xpb_val,
        "content_type": ct_val,
        "etag": etag_val,
        "via": via_val,
        "cache_control": cache_ctrl,
        "has_set_cookie": has_cookies,
        "is_cloudflare": is_cloudflare,

        "tls_cn": tls_info.get("cn", ""),
        "tls_issuer": tls_info.get("issuer", ""),
        "tls_not_after": tls_info.get("not_after", ""),
    }
