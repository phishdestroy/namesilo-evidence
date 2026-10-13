(function () {
  'use strict';
  var $ = function(s, root){return (root || document).querySelector(s);};
  var $$ = function(s, root){return Array.from((root || document).querySelectorAll(s));};
  var page = document.body.dataset.page;
  // An unavailable legacy attachment is labeled, never substituted with invented evidence.
  $$('img[data-original-attachment]').forEach(function(img){img.addEventListener('error',function(){if(img.dataset.failed)return;img.dataset.failed='true';var note=document.createElement('div');note.className='pd-attachment-unavailable';var title=document.createElement('strong');title.textContent=img.alt||'Original source attachment';var text=document.createElement('span');text.textContent='This attachment is currently unavailable at its original source.';note.append(title,text);img.replaceWith(note);});});
  var sidebar = $('#pd-sidebar'), menu = $('#pd-menu'), overlay = $('#pd-overlay');
  var lastFocus = null;
  function icon(name) {
    var paths={search:'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',file:'<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>'};
    return '<svg class="pd-icon" viewBox="0 0 24 24" aria-hidden="true">'+paths[name]+'</svg>';
  }
  function toast(message) {
    var el=$('#pd-toast');el.textContent=message;el.hidden=false;
    clearTimeout(window.pdToastTimer);window.pdToastTimer=setTimeout(function(){el.hidden=true;},2600);
  }
  function closeMenu() {sidebar.classList.remove('pd-open');overlay.classList.remove('pd-open');menu.setAttribute('aria-expanded','false');}
  menu.addEventListener('click',function(){var open=!sidebar.classList.contains('pd-open');sidebar.classList.toggle('pd-open',open);overlay.classList.toggle('pd-open',open);menu.setAttribute('aria-expanded',String(open));});
  overlay.addEventListener('click',closeMenu);
  $$('.pd-nav-link').forEach(function(a){a.addEventListener('click',closeMenu);});
  window.addEventListener('resize',function(){if(innerWidth>800)closeMenu();});
  function openDialog(dialog) {lastFocus=document.activeElement;if(!dialog.open)dialog.showModal();}
  function closeDialog(dialog) {dialog.close();if(lastFocus&&lastFocus.focus)lastFocus.focus();}
  $$('[data-close-dialog]').forEach(function(b){b.addEventListener('click',function(){closeDialog(b.closest('dialog'));});});
  $$('dialog').forEach(function(d){d.addEventListener('click',function(e){if(e.target===d){var r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)closeDialog(d);}});});
  $$('[data-downloads-open]').forEach(function(b){b.addEventListener('click',function(){openDialog($('#pd-downloads'));});});
  $$('[data-refresh]').forEach(function(b){b.addEventListener('click',function(){location.reload();});});
  function route() {
    if(page!=='index')return;
    var hash=decodeURIComponent(location.hash.slice(1))||'overview';
    var target=document.getElementById(hash);
    var names=['overview','evidence','timeline','analytics','resources'];
    var view=names.includes(hash)?hash:hash==='reports'?'overview':target&&target.closest('[data-view]')?target.closest('[data-view]').dataset.view:'overview';
    $$('[data-view]').forEach(function(s){s.hidden=s.dataset.view!==view;});
    $('.pd-intro').hidden=view!=='overview';
    $$('[data-nav]').forEach(function(a){var active=a.dataset.nav===(hash==='reports'?'reports':view);a.classList.toggle('pd-active',active);if(active)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
    $$('.pd-tabs [data-nav]').forEach(function(a){a.classList.toggle('pd-active',a.dataset.nav===view);});
    closeMenu();
    // Existing chart instances are resized after their view becomes visible.
    requestAnimationFrame(function(){
      if(window.Chart&&Chart.instances)Object.values(Chart.instances).forEach(function(c){if(c.canvas&&c.canvas.offsetParent!==null)c.resize();});
      if(target&&hash!=='overview'&&!names.includes(hash))target.scrollIntoView({block:'start'});
      else window.scrollTo({top:0,behavior:'instant'});
    });
  }
  if(page==='index'){
    document.addEventListener('click',function(e){var a=e.target.closest('a[href]');if(!a)return;var u=new URL(a.href);if(u.origin===location.origin&&u.pathname.endsWith('index.html')&&u.hash){e.preventDefault();if(location.hash===u.hash)route();else location.hash=u.hash;}});
    window.addEventListener('hashchange',route);route();
  }
  var searchIndex=[], command=$('#pd-command'), commandInput=$('#pd-command-input'), results=$('#pd-command-results');
  var defaultIndex=[{title:'Investigation overview',href:'index.html#overview',group:'Overview'},{title:'Investigation reports',href:'index.html#reports',group:'6 reports'},{title:'Evidence library',href:'index.html#evidence',group:'Original exhibits'},{title:'Live analytics',href:'index.html#analytics',group:'Live source data'},{title:'IOC explorer',href:'feed-ioc.html',group:'Search domains'},{title:'IOC Domain List',href:'namesilo-domains.html',group:'Domain report'},{title:'PrivacyGuardian Shield',href:'namesilo-privacyguardian.html',group:'Report'},{title:'Timeline',href:'index.html#timeline',group:'Case record'},{title:'Downloads & mirrors',href:'index.html#resources',group:'Resources'}];
  searchIndex=defaultIndex;
  fetch('assets/search-index.json').then(function(r){if(!r.ok)throw new Error('index');return r.json();}).then(function(data){searchIndex=defaultIndex.concat(data);}).catch(function(){});
  function renderSearch() {
    var query=commandInput.value.trim().toLowerCase();
    var matches=query?searchIndex.filter(function(x){return (x.title+' '+x.group).toLowerCase().includes(query);}).slice(0,18):defaultIndex;
    results.replaceChildren();
    if(!matches.length){var empty=document.createElement('div');empty.className='pd-command-empty';empty.textContent='No sections found. Try “domains”, “evidence” or “registration”.';results.appendChild(empty);return;}
    matches.forEach(function(item){var a=document.createElement('a');a.className='pd-command-result';a.href=item.href;a.innerHTML=icon('file');var t=document.createElement('span');t.textContent=item.title;a.appendChild(t);var group=document.createElement('small');group.textContent=item.group;a.appendChild(group);a.addEventListener('click',function(){closeDialog(command);});results.appendChild(a);});
  }
  function openCommand(){commandInput.value='';renderSearch();openDialog(command);commandInput.focus();}
  $$('[data-command-open]').forEach(function(b){b.addEventListener('click',openCommand);});
  commandInput.addEventListener('input',renderSearch);
  command.addEventListener('keydown',function(e){var items=$$('.pd-command-result',results),idx=items.indexOf(document.activeElement);if(e.key==='ArrowDown'){e.preventDefault();if(items.length)items[(idx+1)%items.length].focus();}if(e.key==='ArrowUp'){e.preventDefault();if(idx<=0)commandInput.focus();else items[idx-1].focus();}if(e.key==='Enter'&&document.activeElement===commandInput&&items[0]){e.preventDefault();items[0].click();}});
  document.addEventListener('keydown',function(e){if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();openCommand();}if(e.key==='Escape')closeMenu();});
  var evidence=$$('.ev-card img, .pd-route .panel img[src*="evidence/"]');
  var activeImage=0, lightbox=$('#pd-lightbox'), stage=$('#pd-image-stage');
  function showImage(index){
    activeImage=(index+evidence.length)%evidence.length;
    var source=evidence[activeImage];if(!source)return;
    $('#pd-evidence-image').src=source.src;$('#pd-evidence-image').alt=source.alt;
    $('#pd-evidence-title').textContent=source.alt||'Source evidence';$('#pd-image-original').href=source.src;
    $('#pd-image-count').textContent=(activeImage+1)+' / '+evidence.length;stage.classList.remove('zoom');$('#pd-image-zoom').textContent='Original size';
  }
  evidence.forEach(function(img,index){var card=img.closest('.ev-card')||img;card.setAttribute('tabindex','0');card.setAttribute('role','button');card.setAttribute('aria-label','Enlarge evidence: '+img.alt);function open(){showImage(index);openDialog(lightbox);}card.addEventListener('click',open);card.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();open();}});});
  $('#pd-image-prev').addEventListener('click',function(){showImage(activeImage-1);});$('#pd-image-next').addEventListener('click',function(){showImage(activeImage+1);});
  $('#pd-image-zoom').addEventListener('click',function(){var zoom=stage.classList.toggle('zoom');this.textContent=zoom?'Fit to view':'Original size';});
  lightbox.addEventListener('keydown',function(e){if(e.key==='ArrowRight')showImage(activeImage+1);if(e.key==='ArrowLeft')showImage(activeImage-1);});
  function sourceState(state){
    if(state.name!=='chart-data.json')return;
    var status=$('#pd-status');status.dataset.state=state.mode==='source'?'source':'fallback';
    var date=String(state.updated||'').slice(0,10);
    $('#pd-status-text').textContent=(state.mode==='source'?'Source':'Saved snapshot')+(date?' · '+date:'');
    status.title=(state.mode==='source'?'Connected to the original PhishDestroy feed.':'Original source unavailable. Packaged snapshot is displayed.')+' Source fetch date: '+(date||'not supplied');
    var liveLabel=$('.pd-live-strip-label');if(liveLabel&&state.mode!=='source')liveLabel.innerHTML='<span class="pd-dot"></span>SAVED DATA<br>SNAPSHOT';
  }
  window.addEventListener('pd:source',function(e){sourceState(e.detail);});
  if(window.pdFeedStates&&window.pdFeedStates['chart-data.json'])sourceState(window.pdFeedStates['chart-data.json']);
  else fetch('chart-data.json').then(function(r){return r.json();}).catch(function(){$('#pd-status-text').textContent='Source unavailable';$('#pd-status').dataset.state='fallback';});
  if(window.pdRefreshInlineDataset)window.pdRefreshInlineDataset();
  document.addEventListener('visibilitychange',function(){if(!document.hidden&&window.pdCheckForUpdates)window.pdCheckForUpdates();});
  var backtop=$('#pd-backtop');window.addEventListener('scroll',function(){backtop.hidden=window.scrollY<500;},{passive:true});backtop.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
  // Keep indicators in the source's own fonts, but improve empty-filter feedback.
  function emptyTableMessage(){var info=$('#info'),body=$('#tbody');if(!info||!body||page!=='namesilo-domains')return;if(!body.children.length){var row=document.createElement('tr');var cell=document.createElement('td');cell.colSpan=6;cell.textContent='No matching domains. Try another search or category.';cell.style.cssText='text-align:center;padding:40px;color:var(--tx3)';row.appendChild(cell);body.appendChild(row);}}
  if(page==='namesilo-domains'){$('#q').addEventListener('input',function(){setTimeout(emptyTableMessage,320);});}
})();
