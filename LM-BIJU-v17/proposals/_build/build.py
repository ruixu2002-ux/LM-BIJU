#!/usr/bin/env python3
"""Build step for the LM BIJU demo B prototypes.
- injects self-hosted @font-face rules into demo-b.html
- generates demo-showcase.html (single page) from demo-b.html's shared CSS/JS/home sections
Run from anywhere: python3 proposals/_build/build.py
"""
import re, pathlib
P = pathlib.Path(__file__).resolve().parent.parent
demo = P / 'demo-b.html'
src = demo.read_text(encoding='utf-8')

fonts = (P / 'fonts' / 'fonts.css').read_text(encoding='utf-8').replace('url(', 'url(fonts/')
block = '/*__FONTS__*/\n' + fonts + '/*__FONTS_END__*/'
if '/*__FONTS_END__*/' in src:
    src = re.sub(r'/\*__FONTS__\*/.*?/\*__FONTS_END__\*/', lambda m: block, src, flags=re.S)
else:
    src = src.replace('/*__FONTS__*/', block, 1)
demo.write_text(src, encoding='utf-8')

def between(a, b):
    i = src.index(a) + len(a); j = src.index(b, i); return src[i:j]

css_fonts = between('/*__FONTS__*/', '/*__FONTS_END__*/')
css_core = between('/*__CSS_START__*/', '/*__CSS_END__*/')
home_a = between('<!--__HOME_START__-->', '<!--__HOME_BREAK__-->')
home_b = between('<!--__HOME_RESUME__-->', '<!--__HOME_END__-->')
js_core = between('/*__JS_CORE_START__*/', '/*__JS_CORE_END__*/')
icon_tag = re.search(r'<link rel="icon"[^>]*>', src).group(0)
jsonld = between('<script type="application/ld+json">', '</script>')

def relink(h):
    h = h.replace('href="#registo"', 'href="demo-b.html#/?s=registo"')
    h = h.replace('href="#/', 'href="demo-b.html#/')
    h = h.replace(' data-lights', '')
    return h
home_a, home_b = relink(home_a), relink(home_b)

A = '../_research/demo-b/assets/'
def pic(pfx, ws, alt, sizes):
    s = lambda e: ', '.join(f'{A}{pfx}-{w}.{e} {w}w' for w in ws)
    b = ws[-1]
    return (f'<picture><source type="image/avif" srcset="{s("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{s("webp")}" sizes="{sizes}">'
            f'<img src="{A}{pfx}-{b}.jpg" width="{b}" height="{int(b*1.25)}" alt="{alt}" loading="lazy" decoding="async"></picture>')

PRODUCTS = [
 ('LB-1013','Corrente Cubana — Homem','Aço 316L','aco','legacy/legacy-hero-aco-prod',[480,840,1200],'Corrente cubana em aço 316L sobre fundo preto','28,00 €'),
 ('LB-1001','Anel Pavé Dourado','Banho de ouro 18K','ouro','legacy/legacy-hero-ouro-prod',[480,840],'Anel pavé com banho de ouro 18K sobre pedras brancas','24,90 €'),
 ('LB-1003','Argolas Largas Polidas','Banho de ouro 18K','ouro','legacy/legacy-argolas-pave-prod',[480,840],'Argolas largas polidas com banho de ouro 18K','15,50 €'),
 ('LB-1007','Anéis Zircónia Cor — Série 7','Zircónia','zirconia','legacy/legacy-hero-still-prod',[480,840],'Sete anéis dourados com zircónias de cores diferentes','19,90 €'),
 ('LB-1008','Relógio Bracelete Milanesa','Aço 316L','aco','legacy/legacy-cat-relogios-prod',[480,840],'Relógio com bracelete milanesa em aço sobre carteira de pele','39,00 €'),
 ('LB-1006','Brincos de Pérola Clássicos','Pérola','perola','legacy/legacy-brincos-safira-prod',[480,840,960],'Brincos de argola com pérola pendente sobre tabuleiro branco','9,99 €'),
]
cards = '\n'.join(
 f'''<article class="sc-card"><a class="sc-card__media" href="demo-b.html#/produto/{sku}" data-cursor="Ver" aria-label="{name}">{pic(pfx,ws,alt,"(min-width: 1100px) 30vw, (min-width: 700px) 46vw, 92vw")}</a>
  <h3 class="sc-card__name"><a href="demo-b.html#/produto/{sku}">{name}</a></h3><p class="sc-card__meta"><span class="sc-tag sc-tag--{m}">{mat}</span><span class="mono">{sku}</span></p>
  <p class="sc-card__pvp">PVP recomendado <b>{pvp}</b></p><p class="sc-card__lock"><svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="7" width="10" height="7" rx="1"/><path d="M5 7V5a3 3 0 0 1 6 0v2"/></svg>Preço de revenda para contas validadas</p></article>'''
 for sku,name,mat,m,pfx,ws,alt,pvp in PRODUCTS)

showcase_sections = f'''
  <section class="sc-sel sec" id="selecao" aria-labelledby="sel-t">
    <div class="wrap">
      <div class="sc-head"><div><p class="eyebrow">Seleção</p><h2 class="display" id="sel-t">Peças que <em>rodam.</em></h2></div>
      <p class="lead">Fotografias de produto próprias. O preço de venda ao público aparece a todos; o preço de revenda, só a contas profissionais validadas.</p></div>
      <div class="sc-grid">{cards}</div>
      <p style="margin-top:40px"><a class="btn" href="demo-b.html#/catalogo">Ver o catálogo completo <span class="arrow" aria-hidden="true">→</span></a></p>
    </div>
  </section>

  <section class="sc-b2b sec" aria-labelledby="b2b-t">
    <div class="wrap sc-b2b__in">
      <div>
        <p class="eyebrow">Feito para comprar por grosso</p>
        <h2 class="display" id="b2b-t">Um catálogo<br><em>que trabalha.</em></h2>
        <ol class="sc-feat">
          <li><span class="mono">01</span><div><b>Conta com NIF</b><p>Registo com validação do NIF português. A conta abre os preços de revenda da sua empresa.</p></div></li>
          <li><span class="mono">02</span><div><b>Mínimos por referência</b><p>Cada peça tem o seu mínimo e múltiplo. As quantidades ajustam-se sozinhas.</p></div></li>
          <li><span class="mono">03</span><div><b>Escalões com margem à vista</b><p>Quanto mais encomenda, melhor o preço — com a margem sobre o PVP calculada linha a linha.</p></div></li>
          <li><span class="mono">04</span><div><b>Pedido de proposta</b><p>Cole uma lista de referências ou importe um CSV. Recebe o pedido numerado e o ficheiro para arquivo.</p></div></li>
        </ol>
      </div>
      <div class="sc-tier" aria-labelledby="tier-t">
        <p class="eyebrow" id="tier-t">Exemplo · LB-1003 Argolas Largas Polidas</p>
        <p class="sc-tier__pvp">PVP recomendado <b>15,50 €</b> · mínimo 6 · múltiplos de 6</p>
        <label class="sc-tier__q" for="sc-qty">Quantidade<input id="sc-qty" type="number" inputmode="numeric" min="6" step="6" value="24"></label>
        <table class="sc-tiers"><caption class="sr-only">Escalões de preço de revenda (exemplo)</caption><thead><tr><th scope="col">Quantidade</th><th scope="col">Preço / un. sem IVA</th><th scope="col">Margem</th></tr></thead>
          <tbody><tr data-min="6"><td>6–23</td><td>5,25 €</td><td>×2,4</td></tr><tr data-min="24"><td>24–95</td><td>4,85 €</td><td>×2,6</td></tr><tr data-min="96"><td>96+</td><td>4,45 €</td><td>×2,8</td></tr></tbody></table>
        <p class="mono" id="sc-total" aria-live="polite"></p>
        <p class="note">Valores de exemplo. No site final, os preços são calculados no servidor para cada conta.</p>
      </div>
    </div>
  </section>
'''

showcase_css = '''
.sc-hdr{position:fixed;inset:0 0 auto;height:var(--hdr);z-index:60;display:flex;align-items:center;gap:24px;padding:0 var(--gutter);background:linear-gradient(rgba(20,18,15,.72),rgba(20,18,15,0))}
.sc-hdr nav{margin-left:auto;display:flex;gap:24px;align-items:center}
.sc-hdr nav a{font:500 14px/1 var(--f-ui);text-decoration:none;color:var(--stone-300);padding:14px 0}
.sc-hdr nav a:hover{color:var(--paper)}
.sc-hdr nav .btn{color:var(--ink-950);padding:0 18px;min-height:40px}
.sc-head{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:32px;align-items:end;margin-bottom:48px}
@media (max-width:899px){.sc-head{grid-template-columns:1fr}}
.sc-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:48px 24px}
@media (max-width:1099px){.sc-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:699px){.sc-grid{grid-template-columns:1fr}}
.sc-card__media{display:block;aspect-ratio:4/5;overflow:hidden;background:var(--ink-900);border:1px solid var(--ink-800)}
.sc-card__media img{width:100%;height:100%;object-fit:cover;transition:transform var(--t4) var(--ease-out)}
.sc-card__media:hover img,.sc-card__media:focus-visible img{transform:scale(1.06)}
.sc-card__name{font:500 17px/1.3 var(--f-ui);margin-top:16px}
.sc-card__name a{text-decoration:none}
.sc-card__meta{display:flex;gap:12px;align-items:center;margin-top:8px;color:var(--stone-400)}
.sc-tag{font:500 12px/1 var(--f-ui);padding:5px 8px;border:1px solid currentColor}
.sc-tag--ouro{color:var(--gold-300)}.sc-tag--aco{color:#C9CCD0}.sc-tag--zirconia,.sc-tag--perola{color:var(--stone-300)}
.sc-card__pvp{margin-top:8px;color:var(--stone-300);font-size:14px}.sc-card__pvp b{color:var(--paper);font-weight:500}
.sc-card__lock{display:flex;gap:8px;align-items:center;margin-top:10px;padding-top:10px;border-top:1px solid var(--ink-800);font-size:14px;color:var(--stone-300)}
.sc-card__lock svg{width:14px;height:14px;stroke:var(--gold-decor);fill:none;stroke-width:1.6}
.sc-b2b{border-top:1px solid var(--ink-800)}
.sc-b2b__in{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,5fr);gap:clamp(32px,6vw,112px);align-items:start}
@media (max-width:999px){.sc-b2b__in{grid-template-columns:1fr}}
.sc-feat{margin-top:36px;border-top:1px solid var(--ink-800)}
.sc-feat li{display:grid;grid-template-columns:48px 1fr;gap:16px;padding:22px 0;border-bottom:1px solid var(--ink-800)}
.sc-feat .mono{color:var(--gold-decor);padding-top:4px}
.sc-feat b{font:400 24px/1.2 var(--f-display);display:block;margin-bottom:6px}
.sc-feat p{color:var(--stone-300)}
.sc-tier{border:1px solid var(--ink-800);background:var(--ink-900);padding:28px;position:sticky;top:96px}
.sc-tier__pvp{margin:12px 0 18px;color:var(--stone-300)}.sc-tier__pvp b{color:var(--paper);font-weight:500}
.sc-tier__q{display:grid;gap:6px;font:500 14px/1.3 var(--f-ui);max-width:160px}
.sc-tier__q input{min-height:48px;padding:0 12px;background:transparent;border:1px solid #8A8278;color:var(--paper);font-variant-numeric:tabular-nums}
.sc-tiers{width:100%;border-collapse:collapse;margin:18px 0 12px;font-size:15px}
.sc-tiers th{font:500 12px/1 var(--f-ui);letter-spacing:.08em;text-transform:uppercase;color:var(--stone-400);text-align:left;padding:10px 12px;border-bottom:1px solid var(--ink-800)}
.sc-tiers td{padding:14px 12px;border-bottom:1px solid var(--ink-800);font-variant-numeric:tabular-nums;transition:background var(--t2) var(--ease-ui)}
.sc-tiers tr.on td{background:var(--ink-800)}
.sc-tiers tr.on td:first-child{box-shadow:inset 2px 0 0 var(--gold-decor)}
#sc-total{color:var(--stone-300);min-height:1.5em}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:1ms!important;animation-iteration-count:1!important;transition-duration:1ms!important;scroll-behavior:auto!important}.slide.is-active img{animation:none}.hero__glow,.hero__hint i::after{display:none}}
'''

showcase_js = '''
/* showcase: mini tier widget (MOQ + escalões) */
(()=>{const q=$('#sc-qty');if(!q)return;const rows=$$('.sc-tiers tbody tr');const price={6:5.25,24:4.85,96:4.45};const eur=new Intl.NumberFormat('pt-PT',{style:'currency',currency:'EUR'});
  const upd=()=>{let v=parseInt(q.value,10);if(!Number.isFinite(v)||v<6)v=6;v=Math.ceil(v/6)*6;if(String(v)!==q.value)q.value=v;let t=6;rows.forEach(r=>{if(v>=+r.dataset.min)t=+r.dataset.min});rows.forEach(r=>r.classList.toggle('on',+r.dataset.min===t));$('#sc-total').textContent=`${v} × ${eur.format(price[t])} = ${eur.format(v*price[t])} sem IVA`};
  q.addEventListener('change',upd);upd()})();
Hero.start();Scrub.enter();homeMotion();
'''

page = f'''<!DOCTYPE html>
<html lang="pt-PT" data-theme="dark" data-view="inicio">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>LM BIJU — Apresentação</title>
<meta name="description" content="LM BIJU, grossista de bijuteria em Vila do Conde: aço 316L, banho de ouro 18K, pérola e zircónia. Apresentação numa só página.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#14120F">
<meta property="og:type" content="website">
<meta property="og:title" content="LM BIJU — Bijuteria por grosso, à luz certa">
<meta property="og:description" content="Aço 316L, banho de ouro 18K, pérola e zircónia para lojas físicas, montras e lojas online.">
<meta property="og:image" content="../_research/demo-b/assets/mj/mj-g3-2-hero-1680.jpg">
<meta name="twitter:card" content="summary_large_image">
{icon_tag}
<link rel="preload" as="font" type="font/woff2" href="fonts/Fraunces-normal-latin.woff2" crossorigin>
<link rel="preload" as="image" type="image/avif" fetchpriority="high" imagesrcset="../_research/demo-b/assets/legacy/legacy-hero-aco-hero-600.avif 600w, ../_research/demo-b/assets/legacy/legacy-hero-aco-hero-900.avif 900w, ../_research/demo-b/assets/legacy/legacy-hero-aco-hero-1200.avif 1200w" imagesizes="(max-aspect-ratio: 4/5) 100vw, 67vh">
<script type="application/ld+json">{jsonld}</script>
<style>
{css_fonts}
/* Gerado por _build/build.py a partir de demo-b.html — não editar à mão */
{css_core}
{showcase_css}
</style>
</head>
<body>
<a class="skip" href="#main">Saltar para o conteúdo</a>
<div class="loader" id="loader" aria-hidden="true"><div class="loader__in"><p class="loader__brand">LM <em>Biju</em></p><div class="loader__line"></div><p class="loader__tag">Bijuteria por grosso · Vila do Conde</p></div></div>
<header class="sc-hdr">
  <a class="brand" href="#hero" aria-label="LM BIJU — topo">LM <em>Biju</em></a>
  <nav aria-label="Principal"><a href="#materia">Matéria</a><a href="#selecao">Seleção</a><a href="#empresa">Showroom</a><a class="btn" href="demo-b.html#/catalogo">Catálogo</a></nav>
</header>
<main id="main" tabindex="-1">
{home_a}
{showcase_sections}
{home_b}
</main>
<footer class="ftr">
  <div><b>LM BIJU, Lda.</b>Zona Industrial da Varziela<br>Vila do Conde · Portugal</div>
  <div><b>Área profissional</b><a href="demo-b.html#/?s=registo">Criar conta</a><br><a href="demo-b.html#/pedido">Pedido de proposta</a><br><a href="demo-b.html#/catalogo">Catálogo</a></div>
  <div><b>Contacto comercial</b><a href="mailto:geral@lmbiju.pt">geral@lmbiju.pt</a><br>WhatsApp +351 000 000 000</div>
  <div class="ftr__legal"><a href="https://www.livroreclamacoes.pt" target="_blank" rel="noopener">Livro de Reclamações <span class="sr-only">(abre noutra janela)</span></a><span>Imagens marcadas "Imagem ilustrativa gerada por IA" são ilustrativas e não representam referências do catálogo.</span><span>© LM BIJU · Demonstração de design</span></div>
</footer>
<div class="cur cur-dot" aria-hidden="true"></div>
<div class="cur cur-ring" aria-hidden="true"><span>Ver</span></div>
<div class="sr-only" aria-live="polite" id="live"></div>
<script src="vendor/gsap.min.js" defer></script>
<script src="vendor/ScrollTrigger.min.js" defer></script>
<script src="vendor/lenis.min.js" defer></script>
<script>
document.addEventListener('DOMContentLoaded',()=>{{'use strict';
{js_core}
{showcase_js}
}});
</script>
</body>
</html>
'''
(P / 'demo-showcase.html').write_text(page, encoding='utf-8')
print('demo-b.html', len(src)//1024, 'KB · demo-showcase.html', len(page)//1024, 'KB')
