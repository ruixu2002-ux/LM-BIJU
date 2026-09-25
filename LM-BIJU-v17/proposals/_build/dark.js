/* LM BIJU v3 · DARK motion: M01 title · M02 parallax + scrub · M03 reveal · M04 loader · M05 counters · M06 glow · M07 chapter Nº · M08 cursor · M09 push-in · M10 transitions */
(()=>{'use strict';
const {$,$$,reduced,hooks}=window.LMB;const html=document.documentElement;
const fine=matchMedia('(hover: hover) and (pointer: fine)').matches;
const desk=()=>matchMedia('(min-width: 1024px)').matches&&!matchMedia('(max-aspect-ratio: 4/5)').matches;
const ss={get(k){try{return sessionStorage.getItem(k)}catch(e){return null}},set(k,v){try{sessionStorage.setItem(k,v)}catch(e){}}};

/* header solid after hero */
{let tk=false;const f=()=>{tk=false;html.classList.toggle('hdr-solid',scrollY>innerHeight*.55)};addEventListener('scroll',()=>{if(!tk){tk=true;requestAnimationFrame(f)}},{passive:true});f()}

/* M04 loader — 1.5 s, once per tab, skipped on deep links and reduced motion */
const loaderDone=new Promise(res=>{const el=$('#loader');
  if(!el||html.classList.contains('noload')||reduced()||(location.hash&&!/^#(inicio)?$/.test(location.hash))||ss.get('lmb-loader')){el&&el.remove();res();return}
  ss.set('lmb-loader','1');let ended=false;const end=()=>{if(ended)return;ended=true;el.classList.add('done');setTimeout(()=>el.remove(),520);res()};
  setTimeout(end,1500);el.addEventListener('click',end);addEventListener('keydown',end,{once:true})});
loaderDone.then(()=>requestAnimationFrame(()=>html.classList.add('hero-in')));   // M01

/* M03 mask reveal (all views) */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -4% 0px'});
$$('[data-reveal]').forEach(el=>io.observe(el));
hooks.pdp=box=>$$('[data-reveal]',box).forEach(el=>io.observe(el));

/* M05 counters */
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;cio.unobserve(e.target);const el=e.target,to=+el.dataset.count;if(reduced()){el.textContent=to;return}
  const t0=performance.now(),d=1400;const step=t=>{const k=Math.min(1,(t-t0)/d);el.textContent=Math.round(to*(1-Math.pow(1-k,3)));if(k<1)requestAnimationFrame(step)};el.textContent='0';requestAnimationFrame(step)}),{threshold:.6});
$$('[data-count]').forEach(el=>cio.observe(el));

/* M08 cursor + M09 push-in + M06 glow */
if(fine&&!reduced()){html.classList.add('has-cursor','cursor-hidden');
  const dot=$('.cur-dot'),ring=$('.cur-ring'),lab=$('span',ring);let mx=-100,my=-100,rx=-100,ry=-100;
  addEventListener('pointermove',e=>{if(e.pointerType!=='mouse'){html.classList.add('cursor-hidden');return}if(mx<0){rx=e.clientX;ry=e.clientY}mx=e.clientX;my=e.clientY;html.classList.remove('cursor-hidden')},{passive:true});
  addEventListener('keydown',e=>{if(e.key==='Tab')html.classList.add('cursor-hidden')});
  document.addEventListener('pointerover',e=>{const t=e.target.closest('[data-cursor]');ring.classList.toggle('is-hover',!!t);if(t)lab.textContent=t.dataset.cursor});
  (function loop(){rx+=(mx-rx)*.2;ry+=(my-ry)*.2;dot.style.transform=`translate(${mx}px,${my}px)`;ring.style.transform=`translate(${rx}px,${ry}px)`;requestAnimationFrame(loop)})();
  const glow=$('.hero__glow'),hero=$('[data-hero]');
  if(hero&&glow)hero.addEventListener('pointermove',e=>{const r=hero.getBoundingClientRect();glow.style.transform=`translate(${e.clientX-r.left}px,${e.clientY-r.top}px)`},{passive:true});}
else{$$('.cur').forEach(c=>c.remove())}

/* hero slideshow: 4 frames × 5 s, mask + slight 3D, pausable */
const Hero=(()=>{const root=$('[data-hero]');if(!root)return{start(){},stop(){}};
  const all=$$('.hero__slide',root),sub=$('[data-hero-sub]',root),cap=$('[data-hero-cap]',root),link=$('[data-hero-link]',root),ai=$('[data-hero-ai]',root),iEl=$('[data-hero-i]',root),nEl=$('[data-hero-n]',root),dots=$('.hero__dots',root),pb=$('[data-hero-pause]',root);
  const pool=()=>{const mob=!desk();return all.filter(s=>mob?s.dataset.kind==='v':!('mobile' in s.dataset))};
  let list=pool(),i=0,timer=null,paused=false,visible=true;
  function paintDots(){dots.innerHTML=list.map((s,k)=>`<button type="button" aria-label="Fotografia ${k+1} de ${list.length}" aria-pressed="${k===i}"></button>`).join('');nEl.textContent=String(list.length).padStart(2,'0')}
  function show(k,manual){const prev=list[i];i=(k+list.length)%list.length;const s=list[i];if(s===prev&&!manual)return;
    all.forEach(x=>{if(x!==s&&x!==prev)x.classList.remove('is-active','is-entering')});
    if(!reduced()){s.classList.add('is-entering');setTimeout(()=>{s.classList.add('is-active');s.classList.remove('is-entering');prev&&prev!==s&&prev.classList.remove('is-active')},1400)}else{s.classList.add('is-active');prev&&prev!==s&&prev.classList.remove('is-active')}
    sub.classList.add('swap');setTimeout(()=>{sub.textContent=s.dataset.sub;sub.classList.remove('swap')},240);
    cap.textContent=s.dataset.cap;link.hidden=!s.dataset.sku;if(s.dataset.sku)link.setAttribute('href','#produto/'+s.dataset.sku);ai.hidden=s.dataset.ai!=='1';
    iEl.textContent=String(i+1).padStart(2,'0');$$('button',dots).forEach((b,n)=>b.setAttribute('aria-pressed',String(n===i)))}
  function tick(){clearTimeout(timer);if(paused||!visible||reduced())return;timer=setTimeout(()=>{show(i+1);tick()},5000)}
  dots.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;show($$('button',dots).indexOf(b),true);tick()});
  pb.addEventListener('click',()=>{paused=!paused;pb.setAttribute('aria-pressed',String(paused));pb.textContent=paused?'Retomar':'Pausar';tick()});
  if(reduced()){pb.hidden=true}
  new IntersectionObserver(es=>{visible=es[0].isIntersecting;tick()}).observe(root);
  addEventListener('resize',()=>{const n=pool();if(n.length!==list.length){list=n;i=0;all.forEach(x=>x.classList.remove('is-active','is-entering'));list[0].classList.add('is-active');paintDots();show(0,true)}});
  // initial: make sure the first slide of the pool is active (mobile pool differs)
  if(!list.includes(all.find(s=>s.classList.contains('is-active')))){all.forEach(x=>x.classList.remove('is-active'));list[0].classList.add('is-active')}
  paintDots();
  return{start(){loaderDone.then(tick)},stop(){clearTimeout(timer)}}})();

/* scroll-scrub (48 frames) — desktop; mobile = muted loop video; reduced = poster */
const Scrub=(()=>{const sec=$('#gesto');if(!sec)return{};const cv=$('canvas',sec),ctx=cv.getContext('2d'),cap=$('[data-gcap]',sec),prog=$('[data-gprog]',sec),cta=$('.gesto__cta',sec),N=48;
  const CAPS=['A luz corre pelo fio.','Pendente em zircónia.','Banho de ouro 18K.','Como o cliente o vê.'];
  const frames=[];let ext='avif',loaded=false,cur=-1,lastCap=0;
  const src=k=>`${window.LMB.D.base}video/frame-${String(k+1).padStart(3,'0')}-${ext==='avif'?'1080.avif':'720.jpg'}`;
  function load(){if(loaded)return;loaded=true;const probe=new Image();probe.onload=()=>go();probe.onerror=()=>{ext='jpg';go()};probe.src=src(0);
    function go(){for(let k=0;k<N;k++){const im=new Image();im.decoding='async';im.src=src(k);frames[k]=im;if(k===0)im.onload=()=>draw(0,true)}}}
  function draw(k,force){k=Math.max(0,Math.min(N-1,k));if(k===cur&&!force)return;const im=frames[k];if(!im||!im.complete||!im.naturalWidth){return}cur=k;
    const cw=cv.width,chh=cv.height,r=Math.max(cw/im.naturalWidth,chh/im.naturalHeight),w=im.naturalWidth*r,h=im.naturalHeight*r;ctx.drawImage(im,(cw-w)/2,(chh-h)/2,w,h)}
  function setCap(k){if(k===lastCap)return;lastCap=k;cap.parentElement.classList.add('swap');setTimeout(()=>{cap.textContent=CAPS[k];cap.parentElement.classList.remove('swap')},240)}
  function progress(p){draw(Math.round(p*(N-1)));prog.style.transform=`scaleX(${p})`;setCap(Math.min(3,Math.floor(p*4)));cta.classList.toggle('show',p>=.5)}
  let video=null;
  function mobileVideo(){if(video||reduced())return;const pv=$('.gesto__poster',sec);video=document.createElement('video');video.muted=true;video.loop=true;video.playsInline=true;video.setAttribute('playsinline','');video.preload='none';
    video.poster=`${window.LMB.D.base}video/video-poster-540.jpg`;video.src=`${window.LMB.D.base}video/video-mobile-540.mp4`;video.setAttribute('aria-hidden','true');pv.after(video);
    new IntersectionObserver(es=>{es[0].isIntersecting?video.play().catch(()=>{}):video.pause()},{threshold:.3}).observe(video)}
  const near=new IntersectionObserver(es=>{if(es[0].isIntersecting){near.disconnect();if(desk()&&!reduced())load();else mobileVideo()}},{rootMargin:'800px 0px'});near.observe(sec);
  return{sec,progress,load,mobileVideo}})();

/* GSAP-driven parts (after deferred vendor scripts) */
let ctx=null,lenis=null;
function homeOn(){if(!window.gsap||!window.ScrollTrigger||reduced())return;const gsap=window.gsap;gsap.registerPlugin(window.ScrollTrigger);
  ctx&&ctx.revert();ctx=gsap.context(()=>{
    // M02 parallax
    $$('.view.is-active [data-parallax]').forEach(el=>{const img=$('img',el);if(!img)return;gsap.fromTo(img,{yPercent:-6,scale:1.12},{yPercent:6,scale:1.12,ease:'none',scrollTrigger:{trigger:el.closest('section,article')||el,start:'top bottom',end:'bottom top',scrub:true}})});
    if(desk()){
      // M07 chapters pinned, Nº slides in from the left
      const wrap=$('.chapters'),ch=$$('.chapter',wrap),idx=$$('.chapter-index li',wrap);
      if(wrap&&ch.length){wrap.classList.add('is-pinned');ch.forEach((c,k)=>{c.style.zIndex=k+1});idx[0]&&idx[0].classList.add('on');
        gsap.set(ch.slice(1),{clipPath:'inset(100% 0 0 0)'});gsap.set($$('.chapter__no',wrap).slice(1),{xPercent:-60,autoAlpha:0});gsap.set($$('.chapter__body',wrap).slice(1),{autoAlpha:0,y:40});
        gsap.from($('.chapter__no',ch[0]),{xPercent:-50,autoAlpha:0,duration:.9,ease:'expo.out',scrollTrigger:{trigger:wrap,start:'top 60%',once:true}});
        const tl=gsap.timeline({scrollTrigger:{trigger:wrap,start:'top top',end:()=>'+='+innerHeight*(ch.length-1)*1.1,pin:true,scrub:.6,anticipatePin:1,
          onUpdate:s=>{const k=Math.min(ch.length-1,Math.round(s.progress*(ch.length-1)));idx.forEach((l,n)=>l.classList.toggle('on',n===k))}}});
        for(let k=1;k<ch.length;k++){tl.to(ch[k],{clipPath:'inset(0% 0 0 0)',duration:1,ease:'none'},k-1)
          .to($('.chapter__no',ch[k]),{xPercent:0,autoAlpha:1,duration:.35,ease:'expo.out'},k-.35)
          .to($('.chapter__body',ch[k]),{autoAlpha:1,y:0,duration:.35},k-.3)}}
      // scrub
      if(Scrub.sec){Scrub.sec.classList.add('is-scrub');Scrub.load();
        window.ScrollTrigger.create({trigger:Scrub.sec,start:'top top',end:'+=220%',pin:$('.gesto__pin',Scrub.sec),scrub:true,onUpdate:s=>Scrub.progress(s.progress)});}
    }else{
      $$('.chapter__no').forEach(n=>gsap.from(n,{xPercent:-40,autoAlpha:0,duration:.9,ease:'expo.out',scrollTrigger:{trigger:n,start:'top 85%',once:true}}));
    }
  });
  requestAnimationFrame(()=>window.ScrollTrigger.refresh())}
function homeOff(){if(ctx){ctx.revert();ctx=null}const w=$('.chapters');if(w){w.classList.remove('is-pinned');$$('.chapter',w).forEach(c=>{c.style.zIndex=''})}Scrub.sec&&Scrub.sec.classList.remove('is-scrub');Hero.stop()}
function lenisOn(){if(lenis||!window.Lenis||!fine||reduced())return;lenis=new window.Lenis({lerp:.12,wheelMultiplier:1});
  if(window.gsap){lenis.on('scroll',()=>window.ScrollTrigger&&window.ScrollTrigger.update());window.gsap.ticker.add(t=>lenis.raf(t*1000));window.gsap.ticker.lagSmoothing(0)}
  else{const raf=t=>{lenis.raf(t);requestAnimationFrame(raf)};requestAnimationFrame(raf)}
  $$('dialog').forEach(d=>{new MutationObserver(()=>{d.open?lenis.stop():lenis.start()}).observe(d,{attributes:true,attributeFilter:['open']})})}

hooks.leave.push((prev,r)=>{if(prev&&prev.view==='inicio')homeOff()});
hooks.route.push((r,prev,first)=>{if(lenis)lenis.scrollTo(0,{immediate:true});
  if(r.view==='inicio'){if(window.gsap&&window.ScrollTrigger)homeOn();Hero.start()}
  else if(window.ScrollTrigger)requestAnimationFrame(()=>window.ScrollTrigger.refresh());
  $$('.view.is-active [data-reveal]:not(.in)').forEach(el=>io.observe(el))});
const boot=()=>{lenisOn();const c=window.LMB.cur();if(c&&c.view==='inicio')homeOn()};
/* vendor libraries load after the page (they only drive scroll effects), so they never compete with the first screen */
const loadJs=src=>new Promise((res,rej)=>{const s=document.createElement('script');s.src=src;s.onload=res;s.onerror=rej;document.head.append(s)});
const V=window.LMB.D.base+'vendor/';
const afterLoad=()=>{if(reduced()){return}
  loadJs(V+'gsap.min.js').then(()=>loadJs(V+'ScrollTrigger.min.js')).then(()=>fine?loadJs(V+'lenis.min.js').catch(()=>{}):null).then(boot)
    .catch(()=>{if(Scrub.sec)Scrub.mobileVideo()})};   // offline/blocked: mobile-style fallbacks
if(document.readyState==='complete')afterLoad();else addEventListener('load',afterLoad);
window.LMB.route();
})();
