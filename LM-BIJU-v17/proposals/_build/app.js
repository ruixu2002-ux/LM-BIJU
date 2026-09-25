/* LM BIJU v3 · shared app (dark + light): router, catalogue, PDP, RFQ, forms, search, account */
(()=>{'use strict';
const D=JSON.parse(document.getElementById('lmb-data').textContent);
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const html=document.documentElement;
const reduced=()=>matchMedia('(prefers-reduced-motion: reduce)').matches;
const store={get(k,d){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const ss={get(k){try{return sessionStorage.getItem(k)}catch(e){return null}},set(k,v){try{sessionStorage.setItem(k,v)}catch(e){}},del(k){try{sessionStorage.removeItem(k)}catch(e){}}};
const eur=new Intl.NumberFormat('pt-PT',{style:'currency',currency:'EUR'});
const x1=new Intl.NumberFormat('pt-PT',{maximumFractionDigits:1});
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const live=t=>{const l=$('#live');l.textContent='';setTimeout(()=>{l.textContent=t},40)};
const BY=Object.fromEntries(D.products.map(p=>[p.sku,p]));
const mailto=(s,b)=>`mailto:${D.email}?subject=${encodeURIComponent(s)}&body=${encodeURIComponent(b)}`;
const LMB=window.LMB={D,$,$$,reduced,hooks:{route:[],leave:[]},live};
const lockSvg='<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="7" width="10" height="7" rx="1"/><path d="M5 7V5a3 3 0 0 1 6 0v2"/></svg>';

function pic(id,{alt='',sizes='100vw',eager=false}={}){const a=D.img[id];if(!a)return'';const set=e=>a.w.map(w=>`${D.base}${a.p}-${w}.${e} ${w}w`).join(', ');
  return `<picture><source type="image/avif" srcset="${set('avif')}" sizes="${sizes}"><source type="image/webp" srcset="${set('webp')}" sizes="${sizes}"><img src="${D.base}${a.p}-${a.jw}.jpg" width="${a.jw}" height="${Math.round(a.jw*a.r)}" alt="${esc(alt)}"${eager?' fetchpriority="high"':' loading="lazy"'} decoding="async"></picture>`}
LMB.pic=pic;

/* ---------- validation helpers ---------- */
function nifValid(v){const d=String(v).replace(/\s/g,'');if(!/^\d{9}$/.test(d))return false;
  if(!(['1','2','3','5','6','8','9'].includes(d[0])||['45','70','71','72','74','75','77','79','90','91','98','99'].includes(d.slice(0,2))))return false;
  let s=0;for(let i=0;i<8;i++)s+=+d[i]*(9-i);const r=s%11;return (r<2?0:11-r)===+d[8]}
const emailOk=v=>/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(String(v).trim());
function bindNif(input,msg){if(!input)return;input.addEventListener('input',()=>{const v=input.value.replace(/\D/g,'');if(v.length<9){msg.textContent='';msg.className='msg';input.removeAttribute('aria-invalid');return}
  const ok=nifValid(v);msg.textContent=ok?'NIF válido.':'NIF inválido: verifique os 9 dígitos.';msg.className='msg '+(ok?'ok':'err');input.setAttribute('aria-invalid',ok?'false':'true')})}
const fixQty=(p,q)=>{q=parseInt(q,10);if(!Number.isFinite(q)||q<p.moq)q=p.moq;return Math.ceil(q/p.moq)*p.moq};
const tierFor=(p,q)=>{let t=p.tiers[0];for(const r of p.tiers)if(q>=r[0])t=r;return t};
const margin=(p,price)=>(p.pvp/1.23)/price;

/* ---------- state ---------- */
const S={session:(()=>{try{return JSON.parse(ss.get('lmb-session'))}catch(e){return null}})(),rfq:store.get('lmb-rfq',[]).filter(l=>BY[l.sku]),sent:null};
function saveRFQ(){store.set('lmb-rfq',S.rfq);$$('[data-rfq-count]').forEach(e=>{e.textContent=S.rfq.length});if(cur&&cur.view==='pedido')steps()}
function addRFQ(sku,qty){const p=BY[sku];if(!p)return;qty=fixQty(p,qty);const l=S.rfq.find(x=>x.sku===sku);if(l)l.qty=fixQty(p,l.qty+qty);else S.rfq.push({sku,qty});S.sent=null;saveRFQ();live(`${p.name}: ${qty} unidades adicionadas ao pedido de proposta.`);return qty}
function setSession(v,quiet){S.session=v;if(v)ss.set('lmb-session',JSON.stringify(v));else ss.del('lmb-session');html.classList.toggle('session',!!v);
  $$('[data-acc-link]').forEach(a=>{a.textContent=v?'A minha conta':'Entrar';a.setAttribute('href',v?'#conta':'#entrar')});
  $$('[data-company]').forEach(e=>{e.textContent=v?v.company:''});
  if(!quiet){live(v?'Sessão iniciada na conta de demonstração: preços de revenda de exemplo visíveis.':'Sessão terminada.');if(cur&&cur.view==='produto')renderPDP(cur.arg);if(cur&&cur.view==='conta')renderAccount()}}
LMB.S=S;LMB.addRFQ=addRFQ;

/* ---------- router ---------- */
const VIEWS=new Set($$('[data-view]').map(v=>v.dataset.view));
const CATVIEW=new Set(Object.keys(D.cats));
function parse(){const h=decodeURIComponent(location.hash.slice(1));const i=h.indexOf('?');const path=i<0?h:h.slice(0,i),qs=i<0?'':h.slice(i+1);
  const [name,arg]=path.split('/');const q=Object.fromEntries(new URLSearchParams(qs));return {view:VIEWS.has(name)?name:'inicio',arg:arg||'',q,has:!!name}}
let cur=null,first=true,lightsReq=null;
function navCurrent(view){const key=CATVIEW.has(view)||view==='produto'?'colecoes':view.startsWith('jornal')?'jornal':view;
  $$('.nav a[href^="#"],.drawer nav a[href^="#"]').forEach(a=>{const h=a.getAttribute('href').slice(1);if(h===key)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')})}
function apply(r){const prev=cur;cur=r;
  const changed=!prev||prev.view!==r.view||(r.view==='produto'&&prev.arg!==r.arg);
  if(changed){LMB.hooks.leave.forEach(f=>f(prev,r));
    $$('.view.is-active').forEach(v=>v.classList.remove('is-active'));
    const v=$(`[data-view="${r.view}"]`);
    if(r.view==='produto')renderPDP(r.arg);
    if(r.view==='conta')renderAccount();
    if(r.view==='pedido')renderRFQ();
    v.hidden=false;v.classList.add('is-active');html.dataset.route=r.view;
    if(r.view!=='produto')document.title=v.dataset.title||'LM BIJU';
    navCurrent(r.view);closeMenus();
    if(!first){window.scrollTo(0,0);const f=$('[data-focus]',v)||$('h1',v);if(f){if(!f.hasAttribute('tabindex'))f.setAttribute('tabindex','-1');f.focus({preventScroll:true})}}}
  if(r.view==='colecoes')applyFilters(r.q,changed);
  if(changed)LMB.hooks.route.forEach(f=>f(r,prev,first));
  first=false}
function route(){const r=parse();
  const will=cur&&(cur.view!==r.view||(r.view==='produto'&&cur.arg!==r.arg));
  if(will&&document.startViewTransition&&!reduced()){
    if(lightsReq){html.style.setProperty('--vt-x',lightsReq.x+'px');html.style.setProperty('--vt-y',lightsReq.y+'px');html.classList.add('vt-lights')}
    const t=document.startViewTransition(()=>apply(r));t.finished.finally(()=>{html.classList.remove('vt-lights')})}
  else apply(r);lightsReq=null}
addEventListener('hashchange',route);
document.addEventListener('click',e=>{const a=e.target.closest('a[data-lights]');if(a)lightsReq={x:e.clientX||innerWidth/2,y:e.clientY||innerHeight/2}});
LMB.route=route;LMB.cur=()=>cur;

/* ---------- header: mega menu, drawer, search ---------- */
const mega=$('#mega'),megaBtn=$('[data-mega]');
function setMega(open){if(!mega)return;mega.classList.toggle('is-open',open);megaBtn.setAttribute('aria-expanded',String(open))}
if(megaBtn){let hoverAt=0;megaBtn.addEventListener('click',()=>setMega(Date.now()-hoverAt<600?true:!mega.classList.contains('is-open')));
  const li=megaBtn.closest('li');let tm;
  if(matchMedia('(hover: hover)').matches){[li,mega].forEach(el=>{el.addEventListener('mouseenter',()=>{clearTimeout(tm);if(!mega.classList.contains('is-open'))hoverAt=Date.now();setMega(true)});el.addEventListener('mouseleave',()=>{tm=setTimeout(()=>setMega(false),160)})})}
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&mega.classList.contains('is-open')){setMega(false);megaBtn.focus()}});
  document.addEventListener('focusin',e=>{if(mega.classList.contains('is-open')&&!mega.contains(e.target)&&!li.contains(e.target))setMega(false)})}
const drawer=$('#drawer');
$$('[data-drawer-open]').forEach(b=>b.addEventListener('click',()=>{drawer.showModal();b.setAttribute('aria-expanded','true')}));
$$('[data-drawer-close]').forEach(b=>b.addEventListener('click',()=>drawer.close()));
drawer&&drawer.addEventListener('close',()=>$$('[data-drawer-open]').forEach(b=>b.setAttribute('aria-expanded','false')));
function closeMenus(){setMega(false);if(drawer&&drawer.open)drawer.close();const s=$('#search');if(s&&s.open)s.close()}
const sd=$('#search'),si=$('#search-q'),sr=$('#search-res');
$$('[data-search]').forEach(b=>b.addEventListener('click',()=>{sd.showModal();si.value='';searchRender('');si.focus()}));
$('[data-search-close]').addEventListener('click',()=>sd.close());
sd.addEventListener('click',e=>{if(e.target===sd)sd.close()});
const norm=s=>String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');
function searchRender(q){q=norm(q.trim());let list=D.products;
  if(q){list=D.products.map(p=>{const hay=norm([p.sku,p.name,D.fam[p.fam]||'',p.mats.map(m=>D.mat[m]).join(' ')].join(' '));let sc=0;if(norm(p.sku)===q||norm(p.sku).endsWith(q))sc=10;else if(hay.includes(q))sc=5;else if(q.split(/\s+/).every(w=>hay.includes(w)))sc=3;return [sc,p]}).filter(x=>x[0]>0).sort((a,b)=>b[0]-a[0]).map(x=>x[1])}
  const cats=q?Object.entries(D.cats).filter(([k,c])=>norm(c.title).includes(q)):[];
  sr.innerHTML=cats.map(([k,c])=>`<li><a href="#${k}"><span></span><span><b>${esc(c.title)}</b><br><small>Família · ${c.n} referências</small></span><small>Ver</small></a></li>`).join('')+
    list.slice(0,8).map(p=>`<li><a href="#produto/${p.sku}">${pic(p.img,{alt:'',sizes:'56px'})}<span><b>${esc(p.name)}</b><br><small>${p.sku} · ${esc(p.mats.map(m=>D.mat[m]).join(', ')||D.fam[p.fam])}</small></span><small>${eur.format(p.pvp)}</small></a></li>`).join('')||`<li class="muted" style="padding:8px">Sem resultados para “${esc(q)}”. Experimente uma referência (ex.: LB-1003) ou uma família.</li>`;
  $('#search-count').textContent=q?`${list.length+cats.length} resultados`:''}
si.addEventListener('input',()=>searchRender(si.value));
si.addEventListener('keydown',e=>{if(e.key==='Enter'){const a=$('a',sr);if(a){e.preventDefault();location.hash=a.getAttribute('href');sd.close()}}});
sr.addEventListener('click',e=>{if(e.target.closest('a'))sd.close()});

/* ---------- catalogue: filters on #colecoes ---------- */
const F={fam:'',mat:'',aud:'',occ:'',band:'',style:'',sort:'',view:store.get('lmb-view','grid')};
const grid=$('#todas-grid');
const KEYS=['fam','mat','aud','occ','band','style','sort'];
function cardMatch(c){const has=(k,v)=>!v||(c.dataset[k]||'').split(' ').includes(v);
  return (!F.fam||c.dataset.fam===F.fam||has('cats',F.fam))&&has('mat',F.mat)&&has('aud',F.aud)&&has('occ',F.occ)&&has('band',F.band)&&has('style',F.style)}
function sortCards(box,sort){const cs=$$('.card',box);const k={'pvp-asc':(a,b)=>a.dataset.pvp-b.dataset.pvp,'pvp-desc':(a,b)=>b.dataset.pvp-a.dataset.pvp,'nome':(a,b)=>a.dataset.name.localeCompare(b.dataset.name,'pt'),'ref':(a,b)=>a.dataset.sku.localeCompare(b.dataset.sku)}[sort]||((a,b)=>a.dataset.order-b.dataset.order);cs.sort(k).forEach(c=>box.append(c))}
function applyFilters(q,entered){if(!grid)return;KEYS.forEach(k=>{F[k]=q[k]||''});if(q.view)F.view=q.view;
  KEYS.forEach(k=>{const s=$('#f-'+k);if(s)s.value=F[k]});
  let n=0;$$('.card',grid).forEach(c=>{const ok=cardMatch(c);c.hidden=!ok;if(ok)n++});sortCards(grid,F.sort);
  grid.classList.toggle('is-list',F.view==='list');$$('#todas .viewtog button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.v===F.view)));
  $('#f-count').textContent=`${n} ${n===1?'referência':'referências'}`;$('#f-empty').hidden=n>0;
  const active=KEYS.filter(k=>k!=='sort'&&F[k]).length;$('#f-clear').hidden=!active&&!F.sort;
  if(entered&&KEYS.some(k=>q[k]))requestAnimationFrame(()=>$('#todas').scrollIntoView({block:'start'}))}
function writeFilters(){const p=new URLSearchParams();KEYS.forEach(k=>{if(F[k])p.set(k,F[k])});if(F.view==='list')p.set('view','list');
  const qs=p.toString();history.replaceState(null,'','#colecoes'+(qs?'?'+qs:''));cur=parse();applyFilters(cur.q,false)}
KEYS.forEach(k=>{const s=$('#f-'+k);if(s)s.addEventListener('change',()=>{F[k]=s.value;writeFilters()})});
$$('#todas .viewtog button').forEach(b=>b.addEventListener('click',()=>{F.view=b.dataset.v;store.set('lmb-view',F.view);writeFilters()}));
$('#f-clear')&&$('#f-clear').addEventListener('click',()=>{KEYS.forEach(k=>{F[k]=''});writeFilters();live('Filtros limpos.')});
/* category pages: material chips */
$$('[data-catfilter]').forEach(box=>{const g=$('.cards',box.closest('.view'));box.addEventListener('click',e=>{const b=e.target.closest('button[data-m]');if(!b)return;
  $$('button',box).forEach(x=>x.setAttribute('aria-pressed',String(x===b)));let n=0;$$('.card',g).forEach(c=>{const ok=!b.dataset.m||(c.dataset.mat||'').split(' ').includes(b.dataset.m);c.hidden=!ok;if(ok)n++});
  const cnt=$('[data-catcount]',box.closest('.view'));if(cnt)cnt.textContent=`${n} ${n===1?'referência':'referências'}`;live(`${n} referências.`)})});

/* ---------- add to RFQ (cards) ---------- */
document.addEventListener('submit',e=>{const f=e.target.closest('form[data-add]');if(!f)return;e.preventDefault();const inp=$('input',f);const q=addRFQ(f.dataset.add,inp.value);inp.value=q;
  const b=$('button',f);const t=b.textContent;b.textContent='Adicionado';b.disabled=true;setTimeout(()=>{b.textContent=t;b.disabled=false},1400)});
document.addEventListener('change',e=>{const i=e.target.closest('form[data-add] input');if(i){const p=BY[i.closest('form').dataset.add];i.value=fixQty(p,i.value)}});

/* ---------- PDP ---------- */
function relatedFor(p){const pool=D.products.filter(x=>x.sku!==p.sku);const sc=x=>(x.cats.some(c=>p.cats.includes(c))?2:0)+(x.mats.some(m=>p.mats.includes(m))?1:0)-(x.temp?.5:0);
  return pool.map(x=>[sc(x),x]).sort((a,b)=>b[0]-a[0]).slice(0,3).map(x=>x[1])}
let cloneN=0;
function cloneCard(sku,level){const c=$(`#todas-grid .card[data-sku="${sku}"]`);if(!c)return null;const n=c.cloneNode(true);n.hidden=false;const sfx='-c'+(++cloneN);
  $$('[id]',n).forEach(x=>{x.id+=sfx});$$('label[for]',n).forEach(x=>{x.htmlFor+=sfx});
  if(level){const h=$('.card__name',n);if(h&&h.tagName.toLowerCase()!==level){const m=document.createElement(level);m.className=h.className;m.innerHTML=h.innerHTML;h.replaceWith(m)}}return n}
/* category + favourites grids are filled from the master cards in #todas-grid */
$$('[data-skus]').forEach(g=>{g.dataset.skus.split(' ').forEach(s=>{const c=cloneCard(s,g.dataset.level);if(c)g.append(c)})});
function tierRows(p,q){const t=tierFor(p,q);return p.tiers.map(r=>`<tr${r===t?' class="on"':''}><td>${r[0]}+ un.${r===t?' <span class="sr-only">(escalão atual)</span>':''}</td><td>${eur.format(r[1])}</td><td>×${x1.format(margin(p,r[1]))}</td></tr>`).join('')}
function renderPDP(sku){const p=BY[sku];const box=$('#pdp');
  if(!p){box.innerHTML=`<div class="wrap page-hd"><h1 class="h1" data-focus tabindex="-1">Referência não encontrada</h1><p class="lede">A referência “${esc(sku)}” não existe nesta demonstração.</p><p><a class="btn" href="#colecoes">Ver coleções</a></p></div>`;document.title='Referência não encontrada — LM BIJU';return}
  const cat=p.cats[0],ct=D.cats[cat]?D.cats[cat].title:D.fam[p.fam];const mats=p.mats.map(m=>D.mat[m]);
  const sub=[mats.join(' · ')||p.specs[0][1],p.size,'Ficha técnica a pedido'].filter(Boolean).join(' · ');
  const q0=p.moq;
  const buy=S.session?`<div class="box"><p><b>Preço de revenda</b> <span class="muted">(exemplo, sem IVA)</span></p>
      <table class="tiers"><caption class="sr-only">Escalões de preço de revenda para ${esc(p.name)}</caption><thead><tr><th scope="col">Quantidade</th><th scope="col">Preço / un.</th><th scope="col">Margem sobre PVP</th></tr></thead><tbody id="pdp-tiers">${tierRows(p,q0)}</tbody></table>
      <div class="addrow"><label class="sr-only" for="pdp-qty">Quantidade (mínimo ${p.moq}, múltiplos de ${p.moq})</label><input class="qty" id="pdp-qty" type="number" inputmode="numeric" min="${p.moq}" step="${p.moq}" value="${q0}"><button class="btn" id="pdp-add" type="button">Adicionar ao pedido</button></div>
      <p class="small muted" id="pdp-total" aria-live="polite"></p></div>`
    :`<div class="box"><p class="lock-t">${lockSvg.replace('<svg','<svg style="display:inline;width:14px;height:14px;stroke:currentColor;fill:none;vertical-align:-2px"')} <b>Preço de revenda, escalões e stock</b> aparecem para contas profissionais validadas.</p>
      <div class="btns"><a class="btn btn--sm" href="#entrar">Criar conta profissional</a><button class="btn btn--sm btn--ghost" type="button" data-demo-login>Entrar com a conta de demonstração</button></div>
      <p class="small muted">Pode pedir proposta sem conta:</p>
      <div class="addrow"><label class="sr-only" for="pdp-qty">Quantidade (mínimo ${p.moq}, múltiplos de ${p.moq})</label><input class="qty" id="pdp-qty" type="number" inputmode="numeric" min="${p.moq}" step="${p.moq}" value="${q0}"><button class="btn btn--ghost" id="pdp-add" type="button">Adicionar ao pedido</button></div></div>`;
  const rel=relatedFor(p);
  box.innerHTML=`<div class="wrap" style="padding-top:clamp(24px,4vw,48px)">
   <nav class="crumbs" aria-label="Caminho"><ol><li><a href="#inicio">Início</a></li><li><a href="#colecoes">Coleções</a></li><li><a href="#${cat}">${esc(ct)}</a></li><li aria-current="page">${esc(p.name)}</li></ol></nav>
   <div class="pdp" style="margin-top:24px">
    <div class="pdp__media"><button class="pdp__main" type="button" data-lightbox aria-label="Ampliar fotografia de ${esc(p.name)}">${pic(p.img,{alt:p.alt,sizes:'(min-width: 900px) 55vw, 100vw',eager:true})}
      ${p.temp?'<span class="card__badges"><span class="badge badge--temp">Foto temporária</span></span>':''}</button>
      ${p.temp?'<p class="temp-note">Esta referência ainda não tem fotografia própria. A imagem mostra uma peça semelhante e será substituída pela fotografia de produto.</p>':'<p class="small muted">Clique na fotografia para ampliar.</p>'}</div>
    <div class="pdp__info">
     <p class="idx">${esc(D.fam[p.fam])}${mats.length?' · '+esc(mats[0]):''}</p>
     <h1 class="h2" data-focus tabindex="-1">${esc(p.name)}</h1>
     <p class="pdp__sub">${esc(sub)}</p>
     <p class="pdp__ref">REF ${p.sku} <button type="button" data-copy="${p.sku}">Copiar referência</button></p>
     <p class="pdp__pvp">PVP recomendado <b>${eur.format(p.pvp)}</b> com IVA · mínimo ${p.moq} un. · múltiplos de ${p.moq}</p>
     ${buy}
     <p>${esc(p.desc)}</p>
     <div class="acc">
      <details open><summary>Especificações</summary><div class="acc__b"><dl>${p.specs.map(s=>`<dt>${esc(s[0])}</dt><dd>${esc(s[1])}</dd>`).join('')}<dt>Referência</dt><dd class="tnum">${p.sku}</dd><dt>Mínimo</dt><dd>${p.moq} un., múltiplos de ${p.moq}</dd></dl></div></details>
      ${p.mats.length?`<details><summary>Material e cuidados</summary><div class="acc__b">${p.mats.map(m=>`<p><b>${esc(D.mat[m])}.</b> ${esc(D.matinfo[m])}</p>`).join('')}</div></details>`:''}
      <details><summary>Ficha técnica e conformidade</summary><div class="acc__b"><p>A ficha técnica de cada referência — composição, medidas e documentação de conformidade — é enviada a pedido.</p><p><a class="link" href="${mailto('Ficha técnica '+p.sku,'Olá,\n\nPedimos a ficha técnica da referência '+p.sku+' — '+p.name+'.\n\nObrigado.')}">Pedir ficha técnica por e-mail</a></p></div></details>
      <details><summary>Envio e faturação</summary><div class="acc__b"><p>Enviado de Vila do Conde, a partir de stock próprio. Prazo indicado em cada proposta. Fatura com IVA; pagamento por MB Way, Multibanco, transferência, cartão ou PayPal.</p></div></details>
     </div>
    </div>
   </div>
   <section class="sec" aria-labelledby="rel-t"><div class="head"><p class="idx">Da mesma família</p><h2 class="h2" id="rel-t">Também para a sua montra</h2></div><div class="cards cards--3" id="pdp-rel"></div></section>
  </div>`;
  const rb=$('#pdp-rel');rel.forEach(x=>{const c=cloneCard(x.sku,'h3');if(c)rb.append(c)});
  document.title=`${p.name} (${p.sku}) — LM BIJU`;
  const qi=$('#pdp-qty');const upd=()=>{const q=fixQty(p,qi.value);if(S.session){$('#pdp-tiers').innerHTML=tierRows(p,q);const t=tierFor(p,q);$('#pdp-total').textContent=`${q} × ${eur.format(t[1])} = ${eur.format(q*t[1])} sem IVA (exemplo)`}};
  qi.addEventListener('input',upd);qi.addEventListener('change',()=>{qi.value=fixQty(p,qi.value);upd()});upd();
  $('#pdp-add').addEventListener('click',()=>{qi.value=fixQty(p,qi.value);addRFQ(p.sku,qi.value);const b=$('#pdp-add');b.textContent='Adicionado ao pedido';setTimeout(()=>{b.textContent='Adicionar ao pedido'},1600)});
  LMB.hooks.pdp&&LMB.hooks.pdp(box)}
document.addEventListener('click',e=>{
  const c=e.target.closest('[data-copy]');if(c){const v=c.dataset.copy;(navigator.clipboard?navigator.clipboard.writeText(v):Promise.reject()).then(()=>live(`Referência ${v} copiada.`),()=>live(`Referência ${v}.`));return}
  const l=e.target.closest('[data-demo-login]');if(l){setSession({company:D.account.company,email:'demo@exemplo.pt'});return}
  const lb=e.target.closest('[data-lightbox]');if(lb){const d=$('#lightbox');$('.lightbox__img',d).innerHTML=lb.querySelector('picture').outerHTML.replace(/ sizes="[^"]*"/g,' sizes="100vw"');d.showModal();return}
  const lo=e.target.closest('[data-logout]');if(lo){setSession(null);location.hash='#inicio';return}
  const ro=e.target.closest('[data-reorder]');if(ro){ro.dataset.reorder.split(',').forEach(s=>addRFQ(s,BY[s].moq));location.hash='#pedido';return}});
$('.lightbox__x').addEventListener('click',()=>$('#lightbox').close());
$('#lightbox').addEventListener('click',e=>{if(e.target.id==='lightbox')e.target.close()});

/* ---------- RFQ ---------- */
function steps(){const st=$$('#rfq-steps li');if(!st.length)return;const n=S.rfq.length;const f=$('#f-rfq');const ready=f&&f.empresa.value.trim()&&emailOk(f.email.value)&&f.consent.checked;
  const i=S.sent?3:!n?0:ready?2:1;st.forEach((li,k)=>{li.classList.toggle('done',k<i);if(k===i)li.setAttribute('aria-current','step');else li.removeAttribute('aria-current')})}
function renderRFQ(){const tb=$('#rfq-lines');if(!tb)return;$('#rfq-empty').hidden=S.rfq.length>0;$('#rfq-table').hidden=!S.rfq.length;
  tb.innerHTML=S.rfq.map(l=>{const p=BY[l.sku];return `<tr><td class="tnum">${p.sku}</td><td><a href="#produto/${p.sku}">${esc(p.name)}</a></td><td class="tnum">${p.moq}</td><td><label class="sr-only" for="rq-${p.sku}">Quantidade de ${esc(p.name)}</label><input class="qty" id="rq-${p.sku}" data-sku="${p.sku}" type="number" inputmode="numeric" min="${p.moq}" step="${p.moq}" value="${l.qty}"></td><td class="ok-c">${l.qty%p.moq===0&&l.qty>=p.moq?'OK':'Ajustado'}</td><td><button class="rm" type="button" data-rm="${p.sku}">Remover<span class="sr-only"> ${esc(p.name)}</span></button></td></tr>`}).join('');
  $('#rfq-sum').textContent=S.rfq.length?`${S.rfq.length} ${S.rfq.length===1?'linha':'linhas'} · ${S.rfq.reduce((a,l)=>a+l.qty,0)} unidades`:'';steps()}
const rfqBox=$('#pedido');
if(rfqBox){rfqBox.addEventListener('change',e=>{const i=e.target.closest('input[data-sku]');if(i){const l=S.rfq.find(x=>x.sku===i.dataset.sku);l.qty=fixQty(BY[l.sku],i.value);saveRFQ();renderRFQ();live(`${BY[l.sku].name}: ${l.qty} unidades.`)}});
  rfqBox.addEventListener('click',e=>{const b=e.target.closest('[data-rm]');if(b){const p=BY[b.dataset.rm];S.rfq=S.rfq.filter(x=>x.sku!==b.dataset.rm);saveRFQ();renderRFQ();live(`${p.name} removido do pedido.`);($('#rfq-lines input')||$('#rfq-paste')).focus()}});
  const ingest=txt=>{let ok=0,bad=[];txt.split(/\r?\n/).map(s=>s.trim()).filter(Boolean).forEach(line=>{const m=line.match(/(LB-\d{4})\s*[;,\t ]\s*(\d+)?/i);if(m&&BY[m[1].toUpperCase()]){addRFQ(m[1].toUpperCase(),m[2]||0);ok++}else if(!/^ref/i.test(line))bad.push(line)});
    renderRFQ();const msg=$('#rfq-paste-msg');msg.className='msg '+(bad.length?'err':'ok');msg.textContent=`${ok} ${ok===1?'linha adicionada':'linhas adicionadas'}${bad.length?` · não reconhecidas: ${bad.slice(0,3).join(', ')}`:''}.`};
  $('#rfq-paste-add').addEventListener('click',()=>{ingest($('#rfq-paste').value);$('#rfq-paste').value=''});
  $('#rfq-csv').addEventListener('change',e=>{const f=e.target.files[0];if(!f)return;const r=new FileReader();r.onload=()=>ingest(String(r.result));r.readAsText(f);e.target.value=''});
  let refName='';$('#rfq-ref').addEventListener('change',e=>{const f=e.target.files[0];const box=$('#rfq-ref-prev');$('#rfq-ref-name').textContent=f?f.name:'Nenhuma imagem escolhida';if(!f){box.hidden=true;refName='';return}
    refName=f.name;box.hidden=false;box.innerHTML=`<img src="${URL.createObjectURL(f)}" alt="Pré-visualização da imagem de referência"><span>${esc(f.name)} · fica no seu dispositivo; anexe-a ao e-mail.</span>`});
  bindNif($('#rfq-nif'),$('#rfq-nif-msg'));
  const f=$('#f-rfq');f.addEventListener('input',steps);f.addEventListener('change',steps);
  f.addEventListener('submit',e=>{e.preventDefault();const msg=$('#rfq-msg');const errs=[];if(!S.rfq.length)errs.push('pelo menos uma referência');if(!f.empresa.value.trim())errs.push('empresa');
    if(f.nif.value.trim()&&!nifValid(f.nif.value))errs.push('NIF válido');if(!emailOk(f.email.value))errs.push('e-mail');if(!f.consent.checked)errs.push('consentimento');
    if(errs.length){msg.className='msg err';msg.textContent='Falta: '+errs.join(', ')+'.';return}
    const d=new Date(),id=`RFQ-${d.getFullYear()}${String(d.getMonth()+1).padStart(2,'0')}${String(d.getDate()).padStart(2,'0')}-${String(Math.floor(Math.random()*9000)+1000)}`;
    const rows=[['Referência','Produto','Quantidade','PVP recomendado (€)'],...S.rfq.map(l=>[l.sku,BY[l.sku].name,l.qty,BY[l.sku].pvp.toFixed(2).replace('.',',')])];
    const csv='﻿'+rows.map(r=>r.map(c=>`"${String(c).replace(/"/g,'""')}"`).join(';')).join('\r\n');
    const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));a.download=id+'.csv';document.body.append(a);a.click();a.remove();
    const body=`Pedido de proposta ${id}\n\nEmpresa: ${f.empresa.value}\nNIF: ${f.nif.value||'—'}\nE-mail: ${f.email.value}\n\n${S.rfq.map(l=>`${l.sku} · ${BY[l.sku].name} · ${l.qty} un.`).join('\n')}\n\nObservações: ${f.notas.value||'—'}${refName?`\nImagem de referência: ${refName} (em anexo)`:''}\n\nO ficheiro ${id}.csv foi descarregado com as mesmas linhas.`;
    const href=mailto(`Pedido de proposta ${id} — ${f.empresa.value}`,body);S.sent=id;steps();
    const r=$('#rfq-result');r.hidden=false;r.innerHTML=`<p class="idx idx--plain">Pedido preparado</p><h3 class="h3">${id}</h3><p>Descarregámos o ficheiro <b>${id}.csv</b> e abrimos o e-mail para a equipa comercial no seu programa de correio. Basta enviar.</p><p>Se o e-mail não abriu, <a class="link" href="${href}">abra-o aqui</a>.</p>`;r.focus();msg.textContent='';location.href=href})}

/* ---------- forms: register, login, contact, visit ---------- */
function mailForm(f,resultSel,subject,build,check){f.addEventListener('submit',e=>{e.preventDefault();const msg=$('.msg[data-for="'+f.id+'"]');const errs=check(f);
  if(errs.length){msg.className='msg err';msg.textContent='Falta: '+errs.join(', ')+'.';const bad=f.querySelector('[aria-invalid="true"],:invalid');bad&&bad.focus();return}
  const href=mailto(subject(f),build(f));const r=$(resultSel);r.hidden=false;
  r.innerHTML=`<p class="idx idx--plain">Pedido preparado</p><p>Abrimos o e-mail para a equipa comercial no seu programa de correio. Basta enviar — respondemos a partir de ${esc(D.email)}.</p><p>Se não abriu, <a class="link" href="${href}">abra-o aqui</a>.</p>`;msg.textContent='';r.focus();location.href=href})}
const fr=$('#f-reg');if(fr){bindNif($('#reg-nif'),$('#reg-nif-msg'));
  mailForm(fr,'#reg-result',f=>'Pedido de conta profissional — '+f.empresa.value,f=>`Pedido de conta profissional\n\nEmpresa: ${f.empresa.value}\nNIF: ${f.nif.value}\nTipo de negócio: ${f.tipo.value}\nE-mail: ${f.email.value}\nTelefone: ${f.tel.value||'—'}\n`,
    f=>{const e=[];if(!f.empresa.value.trim())e.push('empresa');if(!nifValid(f.nif.value))e.push('NIF válido');if(!f.tipo.value)e.push('tipo de negócio');if(!emailOk(f.email.value))e.push('e-mail');if(!f.consent.checked)e.push('consentimento');return e})}
const fc=$('#f-contact');if(fc)mailForm(fc,'#contact-result',f=>`${f.assunto.value} — ${f.nome.value}`,f=>`${f.mensagem.value}\n\n${f.nome.value}${f.empresa.value?' · '+f.empresa.value:''}\n${f.email.value}`,
  f=>{const e=[];if(!f.nome.value.trim())e.push('nome');if(!emailOk(f.email.value))e.push('e-mail');if(!f.mensagem.value.trim())e.push('mensagem');if(!f.consent.checked)e.push('consentimento');return e});
const fv=$('#f-visit');if(fv){const di=fv.data;const t=new Date();t.setDate(t.getDate()+1);di.min=t.toISOString().slice(0,10);
  mailForm(fv,'#visit-result',f=>'Marcação de visita ao showroom — '+f.nome.value,f=>`Marcação de visita ao showroom\n\nNome: ${f.nome.value}\nEmpresa: ${f.empresa.value||'—'}\nE-mail: ${f.email.value}\nData preferida: ${f.data.value}\nPeríodo: ${f.periodo.value}\nFamílias de interesse: ${$$('input[name="fam"]:checked',f).map(x=>x.value).join(', ')||'—'}\nNotas: ${f.notas.value||'—'}\n`,
    f=>{const e=[];if(!f.nome.value.trim())e.push('nome');if(!emailOk(f.email.value))e.push('e-mail');if(!f.data.value)e.push('data');else{const d=new Date(f.data.value+'T12:00'),w=d.getDay();if(w===0||w===6)e.push('um dia útil (segunda a sexta)')}if(!f.consent.checked)e.push('consentimento');return e})}
const fl=$('#f-login');if(fl){fl.addEventListener('submit',e=>{e.preventDefault();const msg=$('.msg[data-for="f-login"]');if(!emailOk(fl.email.value)||fl.pass.value.length<4){msg.className='msg err';msg.textContent='Indique um e-mail válido e uma palavra-passe com pelo menos 4 caracteres.';return}
  setSession({company:D.account.company,email:fl.email.value.trim()});location.hash='#conta'});
  $('#login-demo').addEventListener('click',()=>{fl.email.value='demo@exemplo.pt';fl.pass.value='demo2026';fl.requestSubmit()})}

/* ---------- account ---------- */
function renderAccount(){const box=$('#acc-rfq');if(!box)return;
  box.innerHTML=S.rfq.length?`<ul class="ticks">${S.rfq.map(l=>`<li>${l.sku} · ${esc(BY[l.sku].name)} · ${l.qty} un.</li>`).join('')}</ul><p style="margin-top:16px"><a class="btn btn--sm" href="#pedido">Continuar o pedido</a></p>`:'<p class="muted">Ainda não tem linhas no pedido de proposta.</p>';
  $$('[data-company]').forEach(e=>{e.textContent=S.session?S.session.company:''});$$('[data-acc-email]').forEach(e=>{e.textContent=S.session?S.session.email:''})}

/* ---------- tabs ---------- */
$$('[role="tablist"]').forEach(tl=>{const tabs=$$('[role="tab"]',tl);const sel=(t,focus)=>{tabs.forEach(x=>{const on=x===t;x.setAttribute('aria-selected',String(on));x.tabIndex=on?0:-1;$('#'+x.getAttribute('aria-controls')).hidden=!on});focus&&t.focus()};
  tabs.forEach((t,i)=>{t.addEventListener('click',()=>sel(t));t.addEventListener('keydown',e=>{const k={ArrowRight:1,ArrowLeft:-1}[e.key];if(k){e.preventDefault();sel(tabs[(i+k+tabs.length)%tabs.length],true)}})})});

/* ---------- boot ---------- */
if(S.session)setSession(S.session,true);saveRFQ();
if('scrollRestoration' in history)history.scrollRestoration='manual';
/* first route() is called by the theme script, after it registers its hooks */
})();
