const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
window.story = { p:0, target:0, bars:1, burst:0, hidden:false };
const story = window.story;
const CAL = 'https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers';

/* menu, current page, scroll progress */
(function(){
  const menu=document.getElementById('menu'), bur=document.getElementById('burger'), prog=document.getElementById('prog');
  const set=o=>{ menu.classList.toggle('open',o); bur.setAttribute('aria-expanded',o); bur.setAttribute('aria-label',o?'Close menu':'Open menu'); };
  bur.addEventListener('click',()=>set(!menu.classList.contains('open')));
  menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>set(false)));
  addEventListener('keydown',e=>{ if(e.key==='Escape') set(false); });
  const page=document.body.dataset.page; menu.querySelectorAll('a[data-p]').forEach(a=>a.classList.toggle('on',a.dataset.p===page));
  const upd=()=>{ const h=document.documentElement.scrollHeight-innerHeight; if(prog) prog.style.setProperty('--p',(h>0?scrollY/h*100:0)+'%'); };
  addEventListener('scroll',upd,{passive:true}); upd();
})();

/* review carousel: one slow row */
(function(){
  document.querySelectorAll('.carousel').forEach(c=>{
    const run=c.querySelector('.run'); if(!run) return;
    const n=run.children.length; run.innerHTML+=run.innerHTML; run.style.setProperty('--dur',(n*12)+'s');
    const btn=document.querySelector('[data-toggle]');
    if(btn) btn.addEventListener('click',()=>{ const p=c.classList.toggle('paused'); btn.textContent=p?'Play reviews':'Pause reviews'; });
  });
})();

/* booking widget in the viewer's own time zone */
(function(){
  document.querySelectorAll('.bookcard').forEach(card=>{
    const dWrap=card.querySelector('.bc-days'), sWrap=card.querySelector('.bc-slots'), tzEl=card.querySelector('.bc-tz'); if(!dWrap) return;
    let tz='', tzName='';
    try{ tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''; }catch(e){}
    try{ tzName=(new Intl.DateTimeFormat('en-US',{timeZoneName:'long'}).formatToParts(new Date()).find(p=>p.type==='timeZoneName')||{}).value||''; }catch(e){}
    const city=tz.includes('/')?tz.split('/').pop().replace(/_/g,' '):'';
    if(tzEl) tzEl.textContent='🌎 Times shown in your time zone: '+(tzName||tz||'local time')+(city&&tzName?' ('+city+')':'');
    const days=[]; const d=new Date(); while(days.length<5){ d.setDate(d.getDate()+1); if(d.getDay()%6) days.push(new Date(d)); }
    const iso=x=>x.getFullYear()+'-'+String(x.getMonth()+1).padStart(2,'0')+'-'+String(x.getDate()).padStart(2,'0');
    const link=x=>CAL+'?month='+iso(x).slice(0,7)+'&date='+iso(x);
    const slots=[['10:00 AM','11:30 AM','1:00 PM','3:30 PM'],['9:30 AM','12:00 PM','2:00 PM','4:30 PM'],['10:30 AM','1:30 PM','3:00 PM','5:00 PM']];
    function draw(k){
      dWrap.innerHTML=days.map((x,i)=>`<button type="button" class="${i===k?'on':''}" data-i="${i}">${x.toLocaleDateString('en-US',{weekday:'short'})}<small>${x.toLocaleDateString('en-US',{month:'short',day:'numeric'})}</small></button>`).join('');
      sWrap.innerHTML=slots[k%3].map(t=>`<a href="${link(days[k])}" target="_blank" rel="noopener">${t}</a>`).join('');
      dWrap.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>draw(+b.dataset.i)));
    }
    draw(0);
  });
})();

/* revenue calculator */
(function(){
  const $=id=>document.getElementById(id); if(!$('calls')) return;
  const fmt=n=>'$'+Math.round(n).toLocaleString('en-US');
  function upd(){ const c=+$('calls').value, r=+$('close').value, d=+$('deal').value;
    $('callsV').textContent=c; $('closeV').textContent=r+'%'; $('dealV').textContent=fmt(d);
    const wins=c*r/100, rev=wins*d, w=Math.round(wins*10)/10;
    $('rev').textContent=fmt(rev);
    $('revY').textContent=`${w} new client${w===1?'':'s'} a month. ${fmt(rev*12)} in new revenue over a year.`; }
  ['calls','close','deal'].forEach(id=>$(id).addEventListener('input',upd)); upd();
})();

/* screenshot lightbox */
(function(){
  const lb=document.getElementById('lb'); if(!lb) return;
  const li=lb.querySelector('img'), lc=lb.querySelector('p');
  const open=el=>{ const im=el.querySelector('img'); li.src=im.src; li.alt=im.alt; lc.textContent=im.alt; lb.classList.add('on'); lb.querySelector('button').focus(); };
  document.querySelectorAll('.shot').forEach(el=>{ el.addEventListener('click',e=>{ e.preventDefault(); e.stopPropagation(); open(el); }); el.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); open(el);} }); });
  const close=()=>lb.classList.remove('on');
  lb.addEventListener('click',e=>{ if(e.target===lb||e.target.tagName==='BUTTON') close(); });
  addEventListener('keydown',e=>{ if(e.key==='Escape') close(); });
})();

/* count-up numbers and gentle reveal (content stays visible without JS) */
(function(){
  if(reduce || !('IntersectionObserver' in window)) return;
  const io=new IntersectionObserver(es=>es.forEach(en=>{ if(!en.isIntersecting) return; io.unobserve(en.target);
    const el=en.target;
    if(el.dataset.to){ const end=+el.dataset.to, suf=el.dataset.suf||'', t0=performance.now();
      (function tk(now){ const p=Math.min(1,(now-t0)/1500), v=Math.round(end*(1-Math.pow(1-p,4))); el.textContent=v.toLocaleString('en-US')+suf; if(p<1) requestAnimationFrame(tk); })(t0); }
    else el.classList.remove('pre'); }),{threshold:.15});
  document.querySelectorAll('[data-to]').forEach(el=>{ if(el.getBoundingClientRect().top>innerHeight) io.observe(el); });
  document.querySelectorAll('.reveal').forEach(el=>{ if(el.getBoundingClientRect().top>innerHeight){ el.classList.add('pre'); io.observe(el);} });
})();

/* hero: count the headline number up on page open */
(function(){
  const el=document.querySelector('.hero-h [data-count]'); if(!el||reduce) return;
  const end=+el.dataset.count, t0=performance.now()+150; el.textContent='0';
  const tk=now=>{ const p=Math.max(0,Math.min(1,(now-t0)/1100)); el.textContent=Math.round(end*(1-Math.pow(1-p,3))); if(p<1) requestAnimationFrame(tk); };
  requestAnimationFrame(tk);
  setTimeout(()=>{ el.textContent=end; },2000);
})();

/* phone: sticky menu shadow + tap-outside-to-close (styles only apply on phones) */
(function(){
  const nav=document.querySelector('nav'), menu=document.getElementById('menu'), bur=document.getElementById('burger'); if(!nav||!menu||!bur) return;
  const dim=document.createElement('div'); dim.className='menu-dim'; document.body.appendChild(dim);
  const sync=()=>{ const o=menu.classList.contains('open'); dim.classList.toggle('on',o); };
  new MutationObserver(sync).observe(menu,{attributes:true,attributeFilter:['class']});
  dim.addEventListener('click',()=>bur.click());
  const sc=()=>nav.classList.toggle('scrolled',scrollY>8); addEventListener('scroll',sc,{passive:true}); sc();
})();
