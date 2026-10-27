const {chromium}=require('playwright');const fs=require('fs');
const base='http://localhost:8765/';
const pages=fs.readFileSync('/home/claude/site8/sitemap.xml','utf8').match(/<loc>[^<]+<\/loc>/g).map(l=>l.replace(/<\/?loc>/g,'').replace(/^https:\/\/[^/]+\//,''));
pages.push('404.html');
(async()=>{const b=await chromium.launch();const out={};const linkSet=new Set();
for(const w of [1440,390]){
 for(const pg of pages){
  const p=await b.newPage({viewport:{width:w,height:900},isMobile:w<500});
  const errs=[];p.on('console',m=>{if(m.type()=='error')errs.push(m.text().slice(0,150))});p.on('pageerror',e=>errs.push('PAGEERR '+e.message.slice(0,150)));
  const bad=[];p.on('response',r=>{if(r.status()>=400&&r.url().startsWith(base))bad.push(r.status()+' '+r.url())});
  await p.route(/fonts\.g|posthog|cdnjs|calendly\.com/,r=>r.abort());
  await p.goto(base+(pg||'index.html'),{waitUntil:'load'});await p.waitForTimeout(600);
  // scroll through to trigger lazy
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}});
  await p.waitForTimeout(400);
  const r=await p.evaluate(()=>{
   const o={};o.overflow=document.documentElement.scrollWidth-innerWidth;
   o.wide=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>innerWidth+2&&getComputedStyle(e).position!='fixed'&&!e.closest('.ticker,.marquee,[class*=track],.rev-track,.reviews-track,#stage')}).slice(0,5).map(e=>e.tagName+'.'+e.className.toString().slice(0,40)+' r='+Math.round(e.getBoundingClientRect().right));
   o.title=document.title;o.tlen=document.title.length;
   const d=document.querySelector('meta[name=description]');o.dlen=d?d.content.length:0;
   o.canon=(document.querySelector('link[rel=canonical]')||{}).href;
   o.h1=document.querySelectorAll('h1').length;
   o.noalt=[...document.images].filter(i=>!i.hasAttribute('alt')).map(i=>i.src.slice(-40));
   o.brokenimg=[...document.images].filter(i=>i.complete&&i.naturalWidth==0&&i.currentSrc).map(i=>i.currentSrc.slice(-50));
   o.ld=[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>{try{const j=JSON.parse(s.textContent);return (j['@type']||(j['@graph']||[]).map(x=>x['@type']).join('+'))}catch(e){return 'INVALID JSON'}});
   o.links=[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'));
   o.emptylinks=[...document.querySelectorAll('a')].filter(a=>!a.textContent.trim()&&!a.querySelector('img,svg')&&!a.getAttribute('aria-label')).length;
   o.blanknoopener=[...document.querySelectorAll('a[target=_blank]')].filter(a=>!(a.rel||'').includes('noopener')).length;
   o.smalltap=innerWidth<500?[...document.querySelectorAll('a,button')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&r.height<24&&!e.closest('p,li,footer')}).slice(0,6).map(e=>e.textContent.trim().slice(0,25)+':'+Math.round(e.getBoundingClientRect().height)):[];
   o.hidden_reveal=[...document.querySelectorAll('.reveal')].filter(e=>getComputedStyle(e).opacity<0.1).length;
   return o});
  r.errs=errs;r.bad=bad;r.links.forEach(l=>linkSet.add((pg.includes('/')&&!pg.startsWith('blog/')?'':'')+l));delete r.links;
  out[w+' '+(pg||'index.html')]=r;await p.close();
 }}
fs.writeFileSync('/home/claude/audit/out.json',JSON.stringify(out,null,1));
fs.writeFileSync('/home/claude/audit/links.json',JSON.stringify([...linkSet],null,1));
await b.close();})();
