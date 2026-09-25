/* LM BIJU v3 · LIGHT motion (4 only): L1 fade-in · L2 mask reveal · L3 hover lift (CSS) · L4 page transition (View Transitions in app.js). No libraries. */
(()=>{'use strict';
const {$,$$,reduced,hooks,D}=window.LMB;

/* L1 + L2 */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -10% 0px'});
function arm(root){$$('.head,.tile,.card,.art,.num,.faq-g,.guar>div,.steps3 li,.cust',root).forEach(el=>{if(!el.closest('[data-reveal]')&&!el.hasAttribute('data-fade')&&!el.closest('.lhero')){el.setAttribute('data-fade','');io.observe(el)}});
  $$('[data-reveal]',root).forEach(el=>io.observe(el))}
arm(document);
hooks.pdp=box=>arm(box);
hooks.route.push(()=>{$$('.view.is-active [data-fade]:not(.in),.view.is-active [data-reveal]:not(.in)').forEach(el=>io.observe(el))});

/* hero slideshow — mask reveal every 5 s, pausable, off with reduced motion */
(()=>{const root=$('[data-lhero]');if(!root)return;const sl=$$('.lhero__slide',root),dots=$('.lhero__dots',root),pb=$('[data-lh-pause]',root),sku=$('[data-lh-sku]',root),nm=$('[data-lh-name]',root),ln=$('[data-lh-link]',root);
  let i=0,t=null,paused=false,vis=true;
  dots.innerHTML=sl.map((s,k)=>`<button type="button" aria-label="Fotografia ${k+1} de ${sl.length}: ${s.dataset.name}" aria-pressed="${k===0}"></button>`).join('');
  function show(k){const prev=sl[i];i=(k+sl.length)%sl.length;const s=sl[i];if(s===prev)return;
    if(!reduced()){s.classList.add('is-entering');setTimeout(()=>{s.classList.add('is-active');s.classList.remove('is-entering');prev.classList.remove('is-active')},900)}else{s.classList.add('is-active');prev.classList.remove('is-active')}
    sku.textContent=s.dataset.sku;nm.textContent=s.dataset.name;ln.setAttribute('href','#produto/'+s.dataset.sku);$$('button',dots).forEach((b,n)=>b.setAttribute('aria-pressed',String(n===i)))}
  const tick=()=>{clearTimeout(t);if(paused||!vis||reduced())return;t=setTimeout(()=>{show(i+1);tick()},5000)};
  dots.addEventListener('click',e=>{const b=e.target.closest('button');if(b){show($$('button',dots).indexOf(b));tick()}});
  pb.addEventListener('click',()=>{paused=!paused;pb.setAttribute('aria-pressed',String(paused));pb.textContent=paused?'Retomar':'Pausar';tick()});
  if(reduced())pb.hidden=true;
  new IntersectionObserver(es=>{vis=es[0].isIntersecting;tick()}).observe(root);
  hooks.route.push(r=>{if(r.view==='inicio')tick();else clearTimeout(t)})})();

/* 48 frames — user-driven slider (no scroll animation) */
(()=>{const r=$('#lf-range'),img=$('[data-lf-img]'),n=$('[data-lf-n]');if(!r||!img)return;let ext=null;const cache=[];
  const src=k=>`${D.base}video/frame-${String(k).padStart(3,'0')}-${ext==='avif'?'1080.avif':'720.jpg'}`;
  const probe=new Image();probe.onload=()=>{ext='avif';warm()};probe.onerror=()=>{ext='jpg';warm()};
  function warm(){for(let k=1;k<=48;k++){const im=new Image();im.decoding='async';im.src=src(k);cache[k]=im}}
  new IntersectionObserver((es,o)=>{if(es[0].isIntersecting){o.disconnect();probe.src=`${D.base}video/frame-001-1080.avif`}},{rootMargin:'600px 0px'}).observe(img);
  r.addEventListener('input',()=>{const k=+r.value;n.textContent=k;img.alt=`Colar com pendente em zircónia ao pescoço, fotograma ${k} de 48`;img.src=ext?src(k):img.src.replace(/frame-\d{3}/,'frame-'+String(k).padStart(3,'0'))})})();

window.LMB.route();
})();
