const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
window.story = { p:0, target:0, bars:1, burst:0, hidden:false };
const story = window.story;
/* menu: mobile toggle, current page, scroll progress */
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
/* single-row review carousel: slow, readable, smooth on phones */
(function(){
  document.querySelectorAll('.carousel').forEach(c=>{
    const run=c.querySelector('.run'); if(!run) return;
    run.innerHTML+=run.innerHTML;
    const n=run.children.length/2; run.style.setProperty('--dur',(n*11)+'s');
    const btn=c.parentElement.querySelector('[data-toggle]');
    if(btn) btn.addEventListener('click',()=>{ const p=c.classList.toggle('paused'); btn.textContent=p?'Play':'Pause'; });
  });
})();
/* booking card preview: viewer's own time zone, next five weekdays, slots open Calendly on that date */
(function(){
  const CAL='https://calendly.com/learnwithasimshah/1-1-meeting-with-one-of-the-top-email-marketers';
  const dWrap=document.getElementById('bcDays'), sWrap=document.getElementById('bcSlots'), tzEl=document.getElementById('bcTz'); if(!dWrap) return;
  let tz='', tzName='';
  try{ tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''; }catch(e){}
  try{ tzName=(new Intl.DateTimeFormat('en-US',{timeZoneName:'long'}).formatToParts(new Date()).find(p=>p.type==='timeZoneName')||{}).value||''; }catch(e){}
  const city=tz.includes('/')?tz.split('/').pop().replace(/_/g,' '):'';
  if(tzEl) tzEl.textContent='🌎 Times shown in your time zone: '+(tzName||tz||'local time')+(city&&tzName?' ('+city+')':'');
  const days=[]; const d=new Date(); while(days.length<5){ d.setDate(d.getDate()+1); if(d.getDay()%6) days.push(new Date(d)); }
  const iso=x=>x.getFullYear()+'-'+String(x.getMonth()+1).padStart(2,'0')+'-'+String(x.getDate()).padStart(2,'0');
  const link=x=>CAL+'?month='+iso(x).slice(0,7)+'&date='+iso(x);
  const slots=[['10:00 AM','11:30 AM','1:00 PM','3:30 PM'],['9:30 AM','12:00 PM','2:00 PM','4:30 PM'],['10:30 AM','1:30 PM','3:00 PM','5:00 PM']];
  function draw(k){ dWrap.innerHTML=days.map((x,i)=>`<button type="button" class="${i===k?'on':''}" data-i="${i}">${x.toLocaleDateString('en-US',{weekday:'short'})}<small>${x.toLocaleDateString('en-US',{month:'short',day:'numeric'})}</small></button>`).join('');
    sWrap.innerHTML=slots[k%3].map(t=>`<a href="${link(days[k])}" target="_blank" rel="noopener">${t}</a>`).join('');
    dWrap.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>draw(+b.dataset.i))); }
  draw(0);
})();

/* calculator, also scales the 3D bars */
(function(){
  if(!document.getElementById('calls')) return;
  const $=id=>document.getElementById(id), fmt=n=>'$'+Math.round(n).toLocaleString('en-US');
  function upd(){ const c=+$('calls').value, r=+$('close').value, d=+$('deal').value;
    $('callsV').textContent=c; $('closeV').textContent=r+'%'; $('dealV').textContent=fmt(d);
    const wins=c*r/100, rev=wins*d, w=Math.round(wins*10)/10;
    $('rev').textContent=fmt(rev);
    $('revY').textContent=`${w} new client${w===1?'':'s'} a month. ${fmt(rev*12)} in new monthly billing after a year.`;
    story.bars=Math.max(.35,Math.min(1.7,Math.sqrt(rev/12000))); }
  ['calls','close','deal'].forEach(id=>$(id).addEventListener('input',upd)); upd();
})();

/* case studies: images, straighten on scroll, lightbox, count-ups */
(function(){
  document.querySelectorAll('img[data-img]').forEach(im=>{ im.loading='lazy'; im.src='assets/img/'+im.dataset.img+'.jpg'; });
  const frames=[...document.querySelectorAll('.study .frame')];
  function tilt(){ if(reduce) return; frames.forEach((f,k)=>{ const r=f.getBoundingClientRect(), c=(r.top+r.height/2)/innerHeight - .5, a=Math.max(-1,Math.min(1,c*1.6));
    const side=k%2?-1:1; f.style.transform=`rotateX(${a*14}deg) rotateY(${side*Math.abs(a)*12}deg) scale(${1-Math.abs(a)*.08})`; }); }
  addEventListener('scroll',tilt,{passive:true}); addEventListener('resize',tilt); tilt();
  const lb=document.getElementById('lb'), li=document.getElementById('lbImg'), lc=document.getElementById('lbCap');
  if(lb){
  const open=el=>{ li.src='assets/img/'+el.dataset.zoom+'.jpg'; li.alt=el.dataset.cap; lc.textContent=el.dataset.cap; lb.classList.add('on'); document.getElementById('lbX').focus(); };
  document.querySelectorAll('[data-zoom]').forEach(el=>{ el.addEventListener('click',()=>open(el)); el.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); open(el);} }); });
  const close=()=>lb.classList.remove('on');
  lb.addEventListener('click',e=>{ if(e.target===lb||e.target.id==='lbX') close(); }); addEventListener('keydown',e=>{ if(e.key==='Escape') close(); });
  }
  if(!reduce && 'IntersectionObserver' in window){
    const io=new IntersectionObserver(es=>es.forEach(en=>{ if(!en.isIntersecting) return; io.unobserve(en.target);
      const el=en.target, end=+el.dataset.to, t0=performance.now();
      (function tk(now){ const p=Math.min(1,(now-t0)/1600), v=Math.round(end*(1-Math.pow(1-p,4))); el.textContent=v.toLocaleString('en-US'); if(p<1) requestAnimationFrame(tk); })(t0); }),{threshold:.6});
    document.querySelectorAll('[data-to]').forEach(el=>{ if(el.getBoundingClientRect().top>innerHeight) io.observe(el); });
  }
})();

/* reveal below the fold */
if(!reduce && 'IntersectionObserver' in window){
  const io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.remove('pre'); io.unobserve(e.target);} }),{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>{ if(el.getBoundingClientRect().top>innerHeight){ el.classList.add('pre'); io.observe(el);} });
}
