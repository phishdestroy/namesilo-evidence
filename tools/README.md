<img src="https://capsule-render.vercel.app/api?type=waving&color=0:030810,100:c0a060&height=110&fontColor=ffffff&animation=fadeIn&text=Tools&fontSize=28&desc=NameSilo%20Investigation&descAlignY=62&descSize=13" width="100%"/>

# Tools — reproducible @Phish_Destroy archive infrastructure

Three Python scripts that, together, produce a portable archive of the @Phish_Destroy Twitter / X account using only public archive services.

The same scripts can be turned around against any other public Twitter account (`--handle`).


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## What's here

| Script | Purpose |
|---|---|
| [`inventory.py`](inventory.py) | Discover every publicly-visible tweet ID via Wayback CDX, archive.today, GhostArchive, and DuckDuckGo HTML SERP. Optionally pull live content via twscrape. Writes a structured `out/` directory. |
| [`submit_missing.py`](submit_missing.py) | Read `out/missing.txt` — tweet IDs that are known to exist but have no archive copy yet — and POST each one to Wayback Machine + archive.ph. |
| [`wayback_dump.py`](wayback_dump.py) | Helper to bulk-dump a list of URLs through `https://web.archive.org/save/<URL>`. Used after a fresh batch of tweet IDs is discovered. |


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## Why this matters for the case

The @Phish_Destroy account is currently locked. The tweets that rebutted NameSilo's March 13 statement are no longer publicly visible from the account itself. They are, however, still preserved in:

- Wayback Machine snapshots taken at the moment of publication
- archive.today snapshots from a parallel-discovery pass
- DuckDuckGo's index (which surfaces tweet IDs even after the account is hidden)

The combination of the three is enough to reconstruct the public timeline, in order, with full text. This directory is what makes that reconstruction reproducible by an outside party.


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## Usage

```bash
# Discover and merge across all sources
python3 inventory.py --handle Phish_Destroy --no-archive-today --ddg-pages 30

# Push anything still missing into Wayback + archive.ph
python3 submit_missing.py < out/missing.txt
```

The `--no-archive-today` flag is recommended in environments where Cloudflare blocks the discovery requests; you'll lose archive.ph as a *discovery* source but can still use it as a *submission* target.

For full methodology, see [`../TWITTER_ARCHIVE.md`](../TWITTER_ARCHIVE.md).


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## Dependencies

- Python 3.10+
- Standard library only for the discovery and Wayback paths
- Optional: `pip install twscrape` for the live-scrape path (requires sock accounts)


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## License

Same as the rest of the repository — see [`../LICENSE`](../LICENSE). These scripts are tools, not evidence; reuse them freely on other public-interest cases.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:c0a060,100:030810&height=60&section=footer" width="100%"/>
