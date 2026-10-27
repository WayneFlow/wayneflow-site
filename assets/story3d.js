/* ================= 3D envelope story ================= */
(function(){
  const cv=document.getElementById('stage');
  if(!window.THREE) return;
  let R; try{ R=new THREE.WebGLRenderer({canvas:cv,antialias:true,alpha:true}); }catch(e){ return; }
  R.setPixelRatio(Math.min(devicePixelRatio,2));
  const scene=new THREE.Scene(), cam=new THREE.PerspectiveCamera(42,1,.1,200);
  const mobile=()=>innerWidth<860;
  const N = innerWidth<860 ? 320 : 640, RN = 40;

  // envelope texture
  const tc=document.createElement('canvas'); tc.width=256; tc.height=168; const g=tc.getContext('2d');
  g.fillStyle='#ffffff'; g.strokeStyle='rgba(11,26,58,.25)'; g.lineWidth=5; g.beginPath(); g.roundRect ? g.roundRect(4,4,248,160,16) : g.rect(4,4,248,160); g.fill(); g.stroke();
  g.strokeStyle='rgba(0,0,0,.28)'; g.lineWidth=7; g.lineJoin='round';
  g.beginPath(); g.moveTo(12,14); g.lineTo(128,96); g.lineTo(244,14); g.stroke();
  g.lineWidth=4; g.strokeStyle='rgba(0,0,0,.14)'; g.beginPath(); g.moveTo(12,160); g.lineTo(100,84); g.moveTo(244,160); g.lineTo(156,84); g.stroke();
  const tex=new THREE.CanvasTexture(tc);
  const geo=new THREE.PlaneGeometry(.8,.525);
  const mat=new THREE.MeshBasicMaterial({map:tex,side:THREE.DoubleSide,transparent:true});
  const mesh=new THREE.InstancedMesh(geo,mat,N);
  mesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  mesh.instanceColor=new THREE.InstancedBufferAttribute(new Float32Array(N*3),3);
  const world=new THREE.Group(); world.add(mesh); scene.add(world);

  // star dust
  const SD=900, sp=new Float32Array(SD*3);
  for(let i=0;i<SD;i++){ sp[i*3]=(Math.random()-.5)*60; sp[i*3+1]=(Math.random()-.5)*40; sp[i*3+2]=-10-Math.random()*40; }
  const sg=new THREE.BufferGeometry(); sg.setAttribute('position',new THREE.BufferAttribute(sp,3));
  scene.add(new THREE.Points(sg,new THREE.PointsMaterial({color:0x9FB4D8,size:.06,transparent:true,opacity:.7})));

  // globe orbit rings and glow
  const orb=new THREE.Group(); const orbMats=[];
  [[3.9,.016,.9,.35],[4.5,.008,-.5,.8]].forEach(([rad,th,tx,tz])=>{ const m=new THREE.MeshBasicMaterial({color:0x1F6BFF,transparent:true,opacity:0}); const t=new THREE.Mesh(new THREE.TorusGeometry(rad,th,8,140),m); t.rotation.set(Math.PI/2+tx,0,tz); orb.add(t); orbMats.push(m); });
  const gc=document.createElement('canvas'); gc.width=gc.height=128; const gx2=gc.getContext('2d'), grd=gx2.createRadialGradient(64,64,0,64,64,64);
  grd.addColorStop(0,'rgba(31,107,255,.22)'); grd.addColorStop(.5,'rgba(25,180,234,.08)'); grd.addColorStop(1,'rgba(25,180,234,0)'); gx2.fillStyle=grd; gx2.fillRect(0,0,128,128);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(gc),transparent:true,depthWrite:false})); glow.scale.set(13,13,1); orb.add(glow);
  scene.add(orb);
  // the four gates
  const gates=new THREE.Group(); const gateMats=[];
  for(let k=0;k<4;k++){ const m=new THREE.MeshBasicMaterial({color:0x1F6BFF,transparent:true,opacity:0});
    const t=new THREE.Mesh(new THREE.TorusGeometry(mobile()?1.9:1.45,.035,10,90),m); t.position.x=mobile()?(-6+k*4):(0.2+k*2.3); t.rotation.y=Math.PI/2; gates.add(t); gateMats.push(m);
    const m2=new THREE.MeshBasicMaterial({color:0x1F6BFF,transparent:true,opacity:0}); const h=new THREE.Mesh(new THREE.TorusGeometry(mobile()?2.3:1.8,.01,6,90),m2); h.position.copy(t.position); h.rotation.y=Math.PI/2; gates.add(h); gateMats.push(m2); }
  world.add(gates);

  // calendar frame
  const calMat=new THREE.LineBasicMaterial({color:0x1F6BFF,transparent:true,opacity:0});
  const cpts=[]; const cw=5, ch=8, sx=1.0, sy=.68;
  for(let c=0;c<=cw;c++){ cpts.push(-cw*sx/2+c*sx,-ch*sy/2,0, -cw*sx/2+c*sx,ch*sy/2,0); }
  for(let r=0;r<=ch;r++){ cpts.push(-cw*sx/2,-ch*sy/2+r*sy,0, cw*sx/2,-ch*sy/2+r*sy,0); }
  const cg=new THREE.BufferGeometry(); cg.setAttribute('position',new THREE.Float32BufferAttribute(cpts,3));
  const cal=new THREE.LineSegments(cg,calMat); world.add(cal);

  // floor for bars
  const floorMat=new THREE.LineBasicMaterial({color:0x1F6BFF,transparent:true,opacity:0});
  const fpts=[]; for(let k=-8;k<=8;k++){ fpts.push(k*.6,0,-3, k*.6,0,3); } for(let k=-5;k<=5;k++){ fpts.push(-4.8,0,k*.6, 4.8,0,k*.6); }
  const fg=new THREE.BufferGeometry(); fg.setAttribute('position',new THREE.Float32BufferAttribute(fpts,3));
  const floor=new THREE.LineSegments(fg,floorMat); world.add(floor);

  const rnd=Array.from({length:N},()=>[Math.random(),Math.random(),Math.random(),Math.random(),Math.random(),Math.random()]);
  const isR=i=>i<RN;
  const C={ ice:new THREE.Color(0x2A4C8F), blue:new THREE.Color(0x3D86FF), dim:new THREE.Color(0xC4D3EE), grey:new THREE.Color(0xA9B6CF), lime:new THREE.Color(0x8CCB16), gone:new THREE.Color(0xF4F7FC) };
  const HW=()=>Math.tan(21*Math.PI/180)*cam.position.z*cam.aspect, RX=()=>Math.max(3.2,Math.min(HW()*0.5,6)), KS=()=>Math.max(1,Math.min(HW()/8.6,1.25));
  const barH=[2,4,5,7,9,13]; const barOf=[]; { let i=0; barH.forEach((h,b)=>{ for(let l=0;l<h;l++) barOf[i++]=[b,l]; }); }

  // each formation returns position, rotation(x,y,z), scale, color for instance i at time t
  function F(k,i,t,o){
    const r=rnd[i], cx=mobile()?0:RX(), cy=mobile()?2.6:0;
    switch(k){
      case 0: { // a globe of envelopes, kept clear of the headline
        const gx=mobile()?0:RX(), gy=mobile()?-4.7:-.2, GR=mobile()?1.9:2.6*KS();
        const yy=1-2*(i+.5)/N, rr=Math.sqrt(1-yy*yy), ph=i*2.39996+t*.22;
        let nx=Math.cos(ph)*rr, nz=Math.sin(ph)*rr, ny=yy;
        const pop=isR(i)?1+.32*Math.max(0,Math.sin(t*1.3+r[0]*6.28)):1;
        o.x=gx+nx*GR*pop; o.y=gy+ny*GR*pop; o.z=nz*GR*pop;
        o.rx=-Math.asin(ny); o.ry=Math.atan2(nx,nz); o.rz=0; o.s=mobile()?.42:.5*KS(); o.c=isR(i)?C.lime:(r[4]>.55?C.ice:C.blue); return; }
      case 1: { // chaos: spray and pray
        o.x=mobile()?(r[0]-.5)*24:(-1+r[0]*12); o.y=((r[1]-.5)*16 - t*(.4+r[2]*.6)) % 8; if(o.y<-8) o.y+=16; o.z=(r[2]-.7)*14;
        o.rx=r[3]*6+t*r[4]; o.ry=r[4]*6+t*.5; o.rz=r[5]*6; o.s=.6+r[5]*.5; o.c=C.grey; return; }
      case 2: { // the machine: a clean stream through four gates
        const u=(r[0]+t*.035)%1, x=mobile()?(-10+u*20):(RX()-7.8+u*12.5), ang=r[1]*Math.PI*2+u*14, rad=mobile()?(.25+r[2]*.95):(.2+r[2]*.75);
        o.x=x+(mobile()?0:1.5); o.y=Math.sin(x*.35)*.5+Math.cos(ang)*rad+(mobile()?2.4:0); o.z=Math.sin(ang)*rad;
        o.rx=0; o.ry=-.35; o.rz=Math.cos(x*.35)*.18; o.s=.55; o.c=r[3]>.4?C.blue:C.ice; return; }
      case 3: { // replies: the few come back toward you
        if(isR(i)){ const a=r[0]*Math.PI*2+t*.4, b=r[1]*Math.PI, rad=1.1+r[2]*1.1;
          o.x=cx+Math.cos(a)*Math.sin(b)*rad; o.y=cy+Math.cos(b)*rad*.8; o.z=3+Math.sin(a)*Math.sin(b)*rad;
          o.rx=Math.sin(t+r[3]*6)*.4; o.ry=Math.cos(t*.8+r[4]*6)*.6; o.rz=0; o.s=.95; o.c=C.lime; return; }
        F(2,i,t,o); o.z-=4; o.s=.45; o.c=C.dim; return; }
      case 4: { // calendar
        if(isR(i)){ const col=i%5, row=Math.floor(i/5);
          const ks=mobile()?1:.82*KS(); o.x=cx+(-2+col*1.0)*ks; o.y=cy+(2.38-row*.68)*ks; o.z=mobile()?1.2:.2; o.rx=0; o.ry=0; o.rz=0; o.s=.95*ks; o.c=C.lime; return; }
        F(2,i,t,o); o.z-=14; o.s=.35; o.c=C.dim; return; }
      case 5: { // revenue bars
        if(isR(i)){ const [b,l]=barOf[i];
          o.x=cx+(-2.6+b*1.05)*(mobile()?1:KS()); o.y=(mobile()?.6:-2.6)+l*.36*story.bars; o.z=.6; o.rx=-Math.PI/2+.0; o.ry=0; o.rz=0; o.s=.95; o.c=C.lime;
          o.rx=-.25; return; }
        o.x=(r[0]-.5)*30; o.y=-12; o.z=-20; o.rx=0; o.ry=0; o.rz=0; o.s=0; o.c=C.gone; return; }
    }
  }
  const ease=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
  const A={},B={}, m4=new THREE.Matrix4(), q=new THREE.Quaternion(), e=new THREE.Euler(0,0,0,'YXZ'), v=new THREE.Vector3(), sc=new THREE.Vector3(), col=new THREE.Color();
  let mx=0,my=0,time=0,last=performance.now();
  addEventListener('pointermove',ev=>{ mx=ev.clientX/innerWidth-.5; my=ev.clientY/innerHeight-.5; });
  function size(){ const w=innerWidth,h=innerHeight; R.setSize(w,h,false); cam.aspect=w/h; cam.updateProjectionMatrix(); cam.position.set(0,0,mobile()?19:14); }
  size(); addEventListener('resize',size);
  const win=(p,c,w)=>Math.max(0,1-Math.abs(p-c)/w);
  (function frame(now){
    requestAnimationFrame(frame);
    if(story.hidden){ last=now; return; }
    const dt=Math.min((now-last)/1000,.05); last=now; if(!reduce) time+=dt;
    story.p += (story.target-story.p)*(reduce?1:Math.min(1,dt*3.2));
    story.burst *= Math.pow(.15,dt);
    const p=Math.min(5,Math.max(0,story.p)), k=Math.min(4,Math.floor(p)), f=p-k;
    for(let i=0;i<N;i++){
      const d=rnd[i][5]*.35, ti=ease(Math.min(1,Math.max(0,(f-d)/(1-.35))));
      F(k,i,time,A); F(k+1,i,time,B);
      const bx=story.burst*(A.x-(mobile()?0:RX()))*1.6, by=story.burst*(A.y-(mobile()?-4.7:-.2))*1.6;
      v.set(A.x+(B.x-A.x)*ti+bx*(1-ti), A.y+(B.y-A.y)*ti+by*(1-ti), A.z+(B.z-A.z)*ti);
      e.set(A.rx+(B.rx-A.rx)*ti, A.ry+(B.ry-A.ry)*ti, A.rz+(B.rz-A.rz)*ti); q.setFromEuler(e);
      const s=A.s+(B.s-A.s)*ti; sc.set(s,s,s);
      m4.compose(v,q,sc); mesh.setMatrixAt(i,m4);
      col.copy(A.c).lerp(B.c,ti); mesh.setColorAt(i,col);
    }
    mesh.instanceMatrix.needsUpdate=true; mesh.instanceColor.needsUpdate=true;
    const gw=Math.max(win(p,2,.9),win(p,2.4,.9)*.6);
    gateMats.forEach((m,j)=>{ m.opacity=gw*(j%2?.25:.9); });
    gates.position.set(mobile()?0:RX()-3.8, mobile()?2.4:0, 0); gates.children.forEach((g2,j)=>{ g2.rotation.x=time*(j%2?-.6:.4); });
    const ow=Math.max(0,1-p*1.4); orbMats.forEach(m=>m.opacity=ow*.7); glow.material.opacity=ow;
    orb.position.set(mobile()?0:RX(), mobile()?-4.7:-.2, -.5); orb.scale.setScalar(mobile()?.62:.83*KS()); orb.rotation.y=time*.15; orb.children[0].rotation.z=time*.3; orb.children[1].rotation.z=-time*.2;
    calMat.opacity=win(p,4,.8)*.55; cal.position.set(mobile()?0:RX(), (mobile()?2.6:0)+.04, mobile()?1.15:.15); cal.scale.setScalar(mobile()?1:.82*KS());
    floorMat.opacity=win(p,5,1)*.35; floor.position.set(mobile()?0:RX()-.1, mobile()?.3:-2.9, 0);
    world.rotation.y=mx*.25 + (p>4.5?(p-4.5)*.5*-.5:0); world.rotation.x=my*.15 + (p>4.5?(p-4.5)*.25:0);
    R.render(scene,cam);
  })(last);
})();

/* scroll: drive the story and the nav */
(function(){
  const scns=[...document.querySelectorAll('.scn')], labels=[...document.querySelectorAll('[data-label]')];
  const where=document.getElementById('where'), prog=document.getElementById('prog'), stage=document.getElementById('stage'), storyEl=document.getElementById('story');
  function upd(){
    let t=0; for(let i=1;i<scns.length;i++){ const r=scns[i].getBoundingClientRect(); t+=Math.min(1,Math.max(0,(innerHeight*.75-r.top)/(innerHeight*.55))); }
    story.target=t*5/Math.max(1,scns.length-1);
    const sr=storyEl.getBoundingClientRect(); const gone = sr.bottom < innerHeight*.15; stage.style.opacity = sr.bottom < innerHeight*.5 ? 0 : 1; story.hidden = gone;
    
    
  }
  addEventListener('scroll',upd,{passive:true}); addEventListener('resize',upd); upd();
  const sb=document.getElementById('sendBtn'); if(sb) sb.addEventListener('click',()=>{ story.burst=1; setTimeout(()=>scns[1].scrollIntoView({behavior:reduce?'auto':'smooth',block:'center'}),reduce?0:250); });
})();

