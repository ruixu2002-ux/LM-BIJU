#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LM BIJU demo v3 — generator.

Writes proposals/demo-dark.html, demo-light.html, demo-showcase-dark.html, demo-showcase-light.html,
records where every image is used (assets/manifest.json → usedIn) and writes assets/preview.html.
Run: python3 proposals/_build/site.py
"""
import json, pathlib, re, html as H, sys
B = pathlib.Path(__file__).resolve().parent
PD = B.parent
sys.path.insert(0, str(B))
from content import *  # noqa

MAN = json.loads((PD / 'assets/manifest.json').read_text(encoding='utf-8'))
A = {a['id']: a for a in MAN['assets']}
BASE = 'assets/'
USED = set()
esc = lambda s: H.escape(str(s), quote=True)
def eur(x): return f'{x:.2f}'.replace('.', ',') + ' €'


# ---------------------------------------------------------------- images
def pic(id, alt, sizes='100vw', eager=False, extra='', maxw=None):
    a = A[id]; USED.add(id); path = 'img/' + id
    ws = [w for w in a['widths'] if not maxw or w <= maxw] or a['widths'][:1]
    s = lambda e: ', '.join(f'{BASE}{path}-{w}.{e} {w}w' for w in ws)
    j = next(v for v in a['variants'] if v['format'] == 'jpg')
    ld = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return (f'<picture><source type="image/avif" srcset="{s("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{s("webp")}" sizes="{sizes}">'
            f'<img src="{BASE}{path}-{a["jpg"]}.jpg" width="{j["width"]}" height="{j["height"]}" alt="{esc(alt)}"{ld} decoding="async"{extra}></picture>')


def fig(id, alt, sizes='100vw', cls='', eager=False, cap=None, attrs=''):
    ai = '<span class="ai">Imagem ilustrativa gerada por IA</span>' if A[id]['ai'] else ''
    c = f'<figcaption class="cap">{cap}</figcaption>' if cap else ''
    return f'<figure class="fig {cls}"{attrs}>{pic(id, alt, sizes, eager)}{ai}{c}</figure>'


def img_js(ids):
    out = {}
    for id in ids:
        a = A[id]; j = next(v for v in a['variants'] if v['format'] == 'jpg')
        out[id] = dict(p='img/' + id, w=a['widths'], jw=a['jpg'], r=round(j['height'] / j['width'], 4))
    return out


def poster(alt, sizes='(min-width: 1024px) 34vw, 100vw', cls='', eager=False):
    ld = '' if eager else ' loading="lazy"'
    return (f'<picture class="{cls}"><source type="image/avif" srcset="{BASE}video/video-poster-540.avif 540w, {BASE}video/video-poster-1080.avif 1080w" sizes="{sizes}">'
            f'<img src="{BASE}video/video-poster-1080.jpg" width="1080" height="1920" alt="{esc(alt)}"{ld} decoding="async"></picture>')


# ---------------------------------------------------------------- components
LOCK = '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="7" width="10" height="7" rx="1"/><path d="M5 7V5a3 3 0 0 1 6 0v2"/></svg>'
ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'
ORDER = {p['sku']: i for i, p in enumerate(P)}
TI = ' tabindex="-1"'


def card(p, h='h3', ctx='x', sizes='(min-width: 1024px) 23vw, (min-width: 768px) 31vw, 46vw'):
    mats = ' · '.join(MAT[m] for m in p['mats']) or p['specs'][0][1]
    low = tiers(p)[-1][1]
    badges = (f'<span class="badge">{esc(p["badge"])}</span>' if p['badge'] else '') + ('<span class="badge badge--temp">Foto temporária</span>' if p['temp'] else '')
    iid = f'q-{ctx}-{p["sku"]}'
    return (f'<article class="card" data-sku="{p["sku"]}" data-name="{esc(p["name"])}" data-fam="{p["fam"]}" data-cats="{" ".join(p["cats"])}" '
            f'data-mat="{" ".join(p["mats"])}" data-aud="{" ".join(p["aud"])}" data-occ="{" ".join(p["occ"])}" data-band="{p["band"]}" data-style="{p["style"]}" '
            f'data-pvp="{p["pvp"]:.2f}" data-order="{ORDER[p["sku"]]}">'
            f'<div class="card__media"><a href="#produto/{p["sku"]}" tabindex="-1" aria-hidden="true" data-cursor="Ver">{pic(p["img"], p["alt"], sizes, maxw=800)}</a>'
            + (f'<div class="card__badges">{badges}</div>' if badges else '') + '</div>'
            f'<div class="card__body"><{h} class="card__name"><a href="#produto/{p["sku"]}">{esc(p["name"])}</a></{h}>'
            f'<p class="card__meta"><span>{esc(mats)}</span><span class="sku">{p["sku"]}</span></p>'
            f'<p class="card__price"><span>PVP <b class="price">{eur(p["pvp"])}</b></span>'
            f'<span class="lock">Revenda com conta</span><span class="pro price">Revenda desde {eur(low)} · mín. {p["moq"]}</span></p></div>'
            f'<form class="card__add" data-add="{p["sku"]}" action="#pedido"><label class="sr-only" for="{iid}">Quantidade de {esc(p["name"])} (mínimo {p["moq"]})</label>'
            f'<input id="{iid}" type="number" inputmode="numeric" min="{p["moq"]}" step="{p["moq"]}" value="{p["moq"]}"><button type="submit">+ Pedido</button></form></article>')


def nojs_list(items):
    li = ''.join(f'<li>{esc(p["name"])} · <span class="tnum">{p["sku"]}</span> · PVP {eur(p["pvp"])}</li>' for p in items)
    return f'<div class="nojs"><ul class="ticks">{li}</ul><p class="small muted" style="margin-top:12px">Fotografias e pedido de proposta em <a class="link" href="#todas">Todas as peças</a>.</p></div>'


def crumbs(*items):
    li = ''.join(f'<li><a href="{h}">{esc(t)}</a></li>' if h else f'<li aria-current="page">{esc(t)}</li>' for t, h in items)
    return f'<nav class="crumbs" aria-label="Caminho"><ol>{li}</ol></nav>'


def head_block(idx, title, lede=None, tid=None, split=False, level='h2', cls='h2'):
    t = f'<{level} class="{cls}"{f" id={chr(34)}{tid}{chr(34)}" if tid else ""}>{title}</{level}>'
    l = f'<p class="lede">{lede}</p>' if lede else ''
    if split:
        return f'<div class="head head--split"><div class="head"><p class="idx">{idx}</p>{t}</div>{l}</div>'
    return f'<div class="head"><p class="idx">{idx}</p>{t}{l}</div>'


def count_cat(k): return sum(1 for p in P if k in p['cats'])


def view(id, title, body, cls='', hidden=False):
    return f'<section class="view {cls}" id="{id}" data-view="{id}" data-title="{esc(title)}"{" hidden" if hidden else ""}>{body}</section>'


def consent(fid, text):
    return f'<label class="check"><input type="checkbox" name="consent" id="{fid}-consent"><span>{text}</span></label>'


# ---------------------------------------------------------------- shared chrome
def header(theme, showcase=False, pre=''):
    fam_links = ''.join(f'<li><a href="{pre}#{k}">{v}</a></li>' for k, v in FAM.items())
    mat_links = ''.join(f'<li><a href="{pre}#colecoes?mat={k}">{v}</a></li>' for k, v in MAT.items())
    aud_links = ''.join(f'<li><a href="{pre}#colecoes?aud={k}">{v}</a></li>' for k, v in AUD.items())
    occ_links = ''.join(f'<li><a href="{pre}#colecoes?occ={k}">{v}</a></li>' for k, v in OCC.items())
    chev = '<svg viewBox="0 0 10 10" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M1 3l4 4 4-4"/></svg>'
    search = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4.2-4.2"/></svg>'
    logo = '<span class="logo__a">LM</span> <span>Biju</span>' if theme == 'dark' else 'LM <span>BIJU</span>'
    return f'''<header class="hdr" id="hdr"><div class="wrap hdr__in">
<a class="logo" href="{pre}#inicio" aria-label="LM BIJU — início">{logo}</a>
<nav class="nav" aria-label="Principal"><ul>
<li class="nav__mega"><a href="{pre}#colecoes">Coleções</a><button class="nav__btn" type="button" data-mega aria-expanded="false" aria-controls="mega" aria-label="Abrir menu de coleções">{chev}</button></li>
<li><a href="{pre}#empresa">Empresa</a></li><li><a href="{pre}#showroom">Showroom</a></li><li><a href="{pre}#jornal">Jornal</a></li><li><a href="{pre}#faq">FAQ</a></li><li><a href="{pre}#contactos">Contactos</a></li></ul></nav>
<div class="tools">
<button class="icon-btn" type="button" data-search aria-label="Pesquisar peças ou referências" aria-haspopup="dialog">{search}</button>
<a class="acc-link" href="{pre}#entrar" data-acc-link>Entrar</a>
<a class="rfq-pill" href="{pre}#pedido">Pedido <b data-rfq-count aria-label="linhas">0</b></a>
<button class="menu-btn" type="button" data-drawer-open aria-expanded="false" aria-controls="drawer">Menu</button>
</div></div>
<div class="mega" id="mega"><div class="wrap mega__g">
<div><h2>Família</h2><ul>{fam_links}</ul></div><div><h2>Material</h2><ul>{mat_links}</ul></div>
<div><h2>Para quem</h2><ul>{aud_links}</ul><h2 style="margin-top:24px">Ocasião</h2><ul>{occ_links}</ul></div>
<div><h2>Área profissional</h2><ul><li><a href="{pre}#colecoes">Todas as peças</a></li><li><a href="{pre}#pedido">Pedido de proposta</a></li><li><a href="{pre}#entrar">Criar conta</a></li><li><a href="{pre}#faq">Como comprar</a></li></ul></div>
<a class="mega__fig" href="{pre}#loja">{fig('mj/mj-g7-2-s', 'Tabuleiros de veludo com brincos e expositor metálico', '(min-width: 1024px) 26vw, 1px')}<span class="mega__cap">Loja &amp; montra <span aria-hidden="true">→</span></span></a>
</div></div></header>
<dialog class="drawer" id="drawer" aria-label="Menu"><div class="drawer__in">
<div class="drawer__top"><a class="logo" href="{pre}#inicio">{logo}</a><button class="btn btn--sm btn--ghost" type="button" data-drawer-close>Fechar</button></div>
<nav aria-label="Menu móvel"><ul><li><a href="{pre}#colecoes">Coleções</a></li><li class="sub"><ul>{fam_links}</ul></li><li><a href="{pre}#empresa">Empresa</a></li><li><a href="{pre}#showroom">Showroom</a></li><li><a href="{pre}#jornal">Jornal</a></li><li><a href="{pre}#faq">FAQ</a></li><li><a href="{pre}#contactos">Contactos</a></li><li><a href="{pre}#entrar" data-acc-link>Entrar</a></li><li><a href="{pre}#pedido">Pedido de proposta</a></li></ul></nav>
</div></dialog>
<dialog class="search" id="search" aria-labelledby="search-l"><div class="search__in">
<div class="search__bar"><label class="sr-only" for="search-q" id="search-l">Pesquisar peças, referências ou famílias</label>{search.replace('<svg', '<svg style="width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.6"')}
<input id="search-q" type="search" placeholder="Pesquisar: argolas, aço, LB-1003…" autocomplete="off"><button class="btn btn--sm btn--ghost" type="button" data-search-close>Fechar</button></div>
<p class="small muted" id="search-count" aria-live="polite" style="margin-top:10px"></p><ul class="search__res" id="search-res"></ul></div></dialog>'''


def footer(pre=''):
    fam = ''.join(f'<li><a href="{pre}#{k}">{v}</a></li>' for k, v in FAM.items())
    return f'''<footer class="ftr"><div class="wrap">
<div class="ftr__g">
<div><h2>LM BIJU, Lda.</h2><p>{esc(ADDRESS)}</p><p style="margin-top:12px"><a href="mailto:{EMAIL}">{EMAIL}</a><br>WhatsApp {WHATSAPP}</p><p style="margin-top:12px">Venda exclusiva a profissionais.</p></div>
<div><h2>Coleções</h2><ul>{fam}</ul></div>
<div><h2>Área profissional</h2><ul><li><a href="{pre}#entrar">Entrar</a></li><li><a href="{pre}#entrar">Criar conta</a></li><li><a href="{pre}#pedido">Pedido de proposta</a></li><li><a href="{pre}#conta">A minha conta</a></li></ul></div>
<div><h2>Informação</h2><ul><li><a href="{pre}#empresa">Empresa</a></li><li><a href="{pre}#showroom">Showroom</a></li><li><a href="{pre}#jornal">Jornal</a></li><li><a href="{pre}#faq">Perguntas frequentes</a></li><li><a href="{pre}#contactos">Contactos</a></li><li><a href="{LIVRO}" rel="noopener" target="_blank">Livro de Reclamações<span class="sr-only"> (abre numa nova janela)</span></a></li></ul></div>
</div>
<div class="ftr__legal"><span>© LM BIJU · Demonstração de design</span><span>Pagamentos: MB Way · Multibanco · Transferência · Cartão · PayPal</span><span>Imagens marcadas “Imagem ilustrativa gerada por IA” são ilustrativas e não representam referências do catálogo.</span></div>
</div></footer>'''


# ---------------------------------------------------------------- shared pages
def v_colecoes():
    fam_img = {'aneis': 'legacy/hero-ouro-p', 'brincos': 'legacy/argolas-pave-p', 'colares': 'legacy/colar-topazio-p', 'pulseiras': 'legacy/pulseira-rosa-p',
               'relogios': 'legacy/cat-relogios-p', 'homem': 'legacy/cat-homem-p', 'loja': 'legacy/cat-loja-p'}
    tiles = ''.join(f'<a class="tile" href="#{k}">{fig(fam_img[k], "", "(min-width: 1024px) 23vw, 46vw", "fig--45")}<span class="tile__t">{v} <small>{count_cat(k)}</small></span></a>' for k, v in FAM.items())
    mats = ''.join(f'<a class="tile" href="#colecoes?mat={k}">{fig(i, "", "(min-width: 1024px) 18vw, 46vw", "fig--45")}<span class="tile__t">{MAT[k]} <small>{sum(1 for p in P if k in p["mats"])}</small></span><p>{l}</p></a>' for k, i, l in MAT_TILES)
    auds = ''.join(f'<a class="tile" href="#colecoes?aud={k}">{fig(i, "", "(min-width: 1024px) 30vw, 46vw", "fig--45")}<span class="tile__t">{AUD[k]} <small>{sum(1 for p in P if k in p["aud"])}</small></span><p>{l}</p></a>' for k, i, l in AUD_TILES)
    chip = lambda k, d: ''.join(f'<a class="chip" href="#colecoes?{k}={a}">{b}</a>' for a, b in d.items())
    opt = lambda d: ''.join(f'<option value="{a}">{b}</option>' for a, b in d.items())
    sel = lambda k, lab, d, all_='Todos': f'<label class="sel"><span>{lab}</span><select id="f-{k}"><option value="">{all_}</option>{opt(d)}</select></label>'
    cards = ''.join(card(p, 'h3', 'all') for p in P)
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Coleções", None))}
<p class="idx">Catálogo profissional</p><h1 class="h1" data-focus>Coleções</h1>
<p class="lede">Banho de ouro 18K, aço 316L, pérola e zircónia, organizados por família, material, para quem e ocasião. O catálogo completo tem 956 referências; nesta demonstração mostramos {len(P)}.</p></div>
<div class="wrap">{fig("mj/mj-g3-2-w", "Corrente dourada pousada sobre pedra de basalto escura", "(min-width: 1440px) 1344px, 100vw", "fig--219", attrs=" data-reveal")}</div>
<section class="sec wrap" aria-labelledby="c-fam">{head_block("01 — Por família", "Sete famílias, <em>um só fornecedor.</em>", "Da peça à montra: anéis, brincos, colares, pulseiras, relógios, linha homem, e expositores e embalagem na mesma encomenda.", "c-fam", True)}
<div class="tiles tiles--7">{tiles}</div></section>
<section class="sec wrap" aria-labelledby="c-mat">{head_block("02 — Por material", "Cinco materiais, <em>uma regra:</em> durar na montra.", None, "c-mat")}<div class="tiles tiles--5">{mats}</div></section>
<section class="sec wrap" aria-labelledby="c-aud">{head_block("03 — Para quem e para quando", "Para quem compra, <em>e para quando.</em>", None, "c-aud")}<div class="tiles tiles--3">{auds}</div>
<div class="facets"><div><h3 class="small">Ocasião</h3><div class="chips">{chip("occ", OCC)}</div></div><div><h3 class="small">Estilo</h3><div class="chips">{chip("style", STYLE)}</div></div><div><h3 class="small">Preço (PVP)</h3><div class="chips">{chip("band", PRICE)}</div></div></div></section>
<section class="sec wrap" id="todas" aria-labelledby="c-all">{head_block("04 — Todas as peças", "Todas as peças", "PVP recomendado com IVA em todas as fichas. Preço de revenda, mínimos e escalões para contas validadas.", "c-all", True)}
<div class="filters" role="group" aria-label="Filtrar e ordenar" data-js-only>
{sel("fam", "Família", FAM_FILTER, "Todas")}{sel("mat", "Material", MAT)}{sel("aud", "Para quem", AUD)}{sel("occ", "Ocasião", OCC, "Todas")}{sel("band", "Preço", PRICE)}{sel("style", "Estilo", STYLE)}
<label class="sel"><span>Ordenar</span><select id="f-sort"><option value="">Destaques</option><option value="pvp-asc">PVP: mais baixo</option><option value="pvp-desc">PVP: mais alto</option><option value="nome">Nome A–Z</option><option value="ref">Referência</option></select></label>
<div class="viewtog" role="group" aria-label="Vista"><button type="button" data-v="grid" aria-pressed="true"><svg viewBox="0 0 14 14" aria-hidden="true"><rect width="6" height="6"/><rect x="8" width="6" height="6"/><rect y="8" width="6" height="6"/><rect x="8" y="8" width="6" height="6"/></svg>Grelha</button><button type="button" data-v="list" aria-pressed="false"><svg viewBox="0 0 14 14" aria-hidden="true"><rect y="1" width="14" height="2"/><rect y="6" width="14" height="2"/><rect y="11" width="14" height="2"/></svg>Lista</button></div>
<button class="chip" type="button" id="f-clear" hidden>Limpar filtros</button><span class="count" id="f-count" aria-live="polite">{len(P)} referências</span></div>
<div class="cards" id="todas-grid">{cards}</div><p class="empty" id="f-empty" hidden>Nenhuma peça com estes filtros. <button class="link" type="button" onclick="document.getElementById('f-clear').click()" style="background:none;border:0;padding:0">Limpar filtros</button></p></section>'''
    return view('colecoes', 'Coleções — LM BIJU', body)


def v_cat(k):
    c = CATS[k]; items = [p for p in P if k in p['cats']]
    mats = [m for m in MAT if any(m in p['mats'] for p in items)]
    chips = ''.join(f'<button class="chip" type="button" data-m="{m}" aria-pressed="false">{MAT[m]}</button>' for m in mats)
    chips = f'<div class="chips" data-catfilter data-js-only role="group" aria-label="Filtrar por material"><button class="chip" type="button" data-m="" aria-pressed="true">Todos</button>{chips}</div>' if len(mats) > 1 else ''
    i0, i1 = c['imgs']
    other = ''.join(f'<a class="chip" href="#{o}">{FAM[o]}</a>' for o in FAM if o != k)
    body = f'''<div class="wrap cat-hd">{crumbs(("Início", "#inicio"), ("Coleções", "#colecoes"), (c["title"], None))}
<div class="cat-hd__g"><div class="cat-hd__t"><p class="idx">Família</p><h1 class="h1" data-focus>{c["title"]}</h1><p class="lede">{c["lede"]}</p>
<p class="small muted" data-catcount>{len(items)} {"referência" if len(items) == 1 else "referências"} nesta demonstração</p>{chips}</div>
<div class="cat-hd__m">{fig(i0, "", "(min-width: 900px) 30vw, 60vw", "cat-hd__a", attrs=" data-reveal")}{fig(i1, "", "(min-width: 900px) 22vw, 40vw", "cat-hd__b", attrs=" data-reveal")}</div></div></div>
<div class="wrap sec--tight"><div class="cards" data-skus="{" ".join(p["sku"] for p in items)}" data-level="h2"></div>{nojs_list(items)}</div>
<nav class="wrap sec--tight cat-next" aria-label="Outras famílias"><p class="idx">Outras famílias</p><div class="chips">{other}</div></nav>'''
    return view(k, f'{c["title"]} — LM BIJU', body, 'cat')


def v_empresa(theme):
    nums = ''.join(f'<div class="num"><b data-count="{n}">{n}</b><span>{esc(l)}</span><small>{esc(s)}</small></div>' for n, l, s in NUMBERS)
    cust = ''.join(f'<article class="cust">{fig(c["img"], c["alt"], "(min-width: 900px) 30vw, 100vw", "fig--32")}<h3 class="h3">{c["tab"]}</h3><p class="muted">{c["text"]}</p></article>' for c in CUSTOMERS)
    steps = ''.join(f'<li><b>{n}</b><h3 class="h3">{t}</h3><p class="muted">{d}</p></li>' for n, t, d in STEPS)
    guar = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in GUARANTEES)
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Empresa", None))}<p class="idx">Empresa</p>
<h1 class="h1" data-focus>Um fornecedor, <em>não um catálogo anónimo.</em></h1>
<p class="lede">Grossistas de bijuteria com showroom físico, equipa comercial e regras claras. Aqui explicamos quem somos, como se compra por grosso e que garantias tem ao fazê-lo.</p></div>
<section class="wrap split" aria-label="Quem somos">{fig("legacy/anel-solitario-v", "Duas mãos com anéis finos dourados sobre fundo terracota", "(min-width: 900px) 42vw, 100vw", "split__m", attrs=" data-reveal")}
<div class="split__t"><p class="idx">Quem somos</p><h2 class="h2">Da Varziela para as lojas de todo o país.</h2>
<p class="lede">Trabalhamos a partir da Zona Industrial da Varziela, em Vila do Conde, com stock próprio e um showroom onde se vê cada família antes de encomendar.</p>
<p class="muted">Vendemos só a profissionais — lojas físicas, revendedores online e quem está a começar — e o catálogo é fechado ao público para proteger as margens de quem já compra connosco.</p>
<div class="btns"><a class="btn" href="#entrar">Criar conta profissional</a><a class="btn btn--ghost" href="#showroom">Marcar visita</a></div></div></section>
<section class="sec wrap" aria-labelledby="e-num">{head_block("Em números", "956 referências, <em>três linhas.</em>", "Contagem do catálogo por linha, tal como aparece no site atual.", "e-num", True)}<div class="nums">{nums}</div></section>
<section class="sec wrap" aria-labelledby="e-cust">{head_block("Para quem vendemos", "Três tipos de cliente, <em>uma conta.</em>", None, "e-cust")}<div class="custs">{cust}</div></section>
<section class="sec wrap" aria-labelledby="e-steps">{head_block("Comprar por grosso", "Três passos até ao preço por grosso.", "O catálogo é fechado ao público para proteger as margens de quem já compra connosco.", "e-steps", True)}<ol class="steps3">{steps}</ol></section>
<section class="sec wrap" aria-labelledby="e-g">{head_block("Garantias", "Comprar por grosso, <em>com chão firme.</em>", None, "e-g")}<div class="guar">{guar}</div></section>
<section class="wrap sec--tight duo" aria-label="Loja e montra">{fig("mj/mj-g7-0-s", "Expositor em T dourado sobre base de pedra com tabuleiros de veludo", "(min-width: 900px) 48vw, 100vw", "fig--32", attrs=" data-reveal")}{fig("mj/mj-g6-1-s", "Caixa rígida preta com pulseira sobre cetim", "(min-width: 900px) 48vw, 100vw", "fig--32", attrs=" data-reveal")}</section>'''
    return view('empresa', 'Empresa — LM BIJU', body)


def v_showroom():
    fams = ''.join(f'<label class="check"><input type="checkbox" name="fam" value="{v}"><span>{v}</span></label>' for v in FAM.values())
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Showroom", None))}<p class="idx">Showroom</p>
<h1 class="h1" data-focus>Varziela, <em>Vila do Conde.</em></h1>
<p class="lede">Um espaço de exposição dedicado a bijuteria e acessórios. Visite com marcação — preparamos as famílias que lhe interessam antes de chegar.</p></div>
<div class="wrap">{fig("mj/mj-g1-1-w", "Montra com bustos de veludo e colares, vista da rua ao anoitecer", "(min-width: 1440px) 1344px, 100vw", "fig--219", cap="Ambiente ilustrativo. As fotografias do showroom real entram na versão final.", attrs=" data-reveal")}</div>
<section class="sec wrap g2" aria-labelledby="s-info"><div><p class="idx">Visitas</p><h2 class="h2" id="s-info">Com marcação, <em>em dias úteis.</em></h2>
<dl class="facts" style="margin-top:32px"><dt>Morada</dt><dd>{esc(ADDRESS)}</dd><dt>Horário</dt><dd>{HOURS}</dd><dt>Visitas</dt><dd>Com marcação prévia</dd><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></dl>
<p style="margin-top:28px"><a class="btn btn--ghost" href="{MAPS}" rel="noopener" target="_blank">Abrir no mapa<span class="sr-only"> (abre numa nova janela)</span></a></p></div>
<form class="form box" id="f-visit" action="mailto:{EMAIL}" method="post" enctype="text/plain" novalidate aria-labelledby="visit-t"><h3 class="h3" id="visit-t">Marcar visita</h3>
<div class="row2"><div class="field"><label for="v-nome">Nome</label><input id="v-nome" name="nome" autocomplete="name" required></div><div class="field"><label for="v-emp">Empresa <span class="muted">(opcional)</span></label><input id="v-emp" name="empresa" autocomplete="organization"></div></div>
<div class="field"><label for="v-email">E-mail</label><input id="v-email" name="email" type="email" autocomplete="email" required></div>
<div class="row2"><div class="field"><label for="v-data">Data preferida</label><input id="v-data" name="data" type="date" required><span class="hint">Segunda a sexta.</span></div>
<div class="field"><label for="v-per">Período</label><select id="v-per" name="periodo"><option>Manhã (09h00 – 13h00)</option><option>Tarde (14h00 – 18h30)</option></select></div></div>
<fieldset class="field"><legend>Famílias de interesse</legend><div class="checks">{fams}</div></fieldset>
<div class="field"><label for="v-notas">Notas <span class="muted">(opcional)</span></label><textarea id="v-notas" name="notas"></textarea></div>
{consent("v", "Aceito que a LM BIJU use estes dados para responder a este pedido.")}
<button class="btn" type="submit">Pedir marcação</button><p class="msg" data-for="f-visit" role="alert"></p>
<p class="demo-note">Ao enviar, preparamos o e-mail para a equipa comercial no seu programa de correio.</p></form>
<div class="result" id="visit-result" hidden tabindex="-1"></div></section>
<section class="wrap sec--tight trio3" aria-label="Ambientes">{fig("mj/mj-g7-2-s", "Tabuleiros de veludo preto com brincos e bloco de pedra", "(min-width: 900px) 32vw, 100vw", "fig--32", attrs=" data-reveal")}{fig("mj/mj-g1-0-s", "Rua histórica com montra iluminada ao anoitecer", "(min-width: 900px) 32vw, 100vw", "fig--32", attrs=" data-reveal")}{fig("mj/mj-g7-1-t", "Tabuleiros de veludo com brincos iluminados de cima", "(min-width: 900px) 32vw, 100vw", "fig--45", attrs=" data-reveal")}</section>'''
    return view('showroom', 'Showroom — LM BIJU', body)


def v_pedido():
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Pedido de proposta", None))}<p class="idx">Pedido de proposta</p>
<h1 class="h1" data-focus>Pedido de proposta</h1><p class="lede">Junte referências e quantidades. Validamos os mínimos linha a linha e respondemos com preço e prazo.</p></div>
<div class="wrap" style="padding-bottom:var(--sec)"><ol class="steps" id="rfq-steps" aria-label="Progresso do pedido"><li aria-current="step">Produtos</li><li>Os seus dados</li><li>Confirmar</li><li>Enviado</li></ol>
<div class="rfq"><div>
<p id="rfq-empty" class="empty" style="padding-top:0">Ainda não há linhas. Adicione peças a partir das <a class="link" href="#colecoes">coleções</a>, cole uma lista ou importe um ficheiro CSV.</p>
<table class="lines" id="rfq-table" hidden><caption class="sr-only">Linhas do pedido</caption><thead><tr><th scope="col">Referência</th><th scope="col">Produto</th><th scope="col">Mín.</th><th scope="col">Quantidade</th><th scope="col">Estado</th><th scope="col"><span class="sr-only">Ações</span></th></tr></thead><tbody id="rfq-lines"></tbody></table>
<p id="rfq-sum" class="small muted" aria-live="polite" style="margin-top:10px"></p>
<div class="box" style="margin-top:32px" data-js-only><div class="field"><label for="rfq-paste">Colar lista de referências</label><p class="hint" id="rfq-paste-h">Uma linha por referência: <span class="tnum">LB-1003;24</span></p><textarea id="rfq-paste" aria-describedby="rfq-paste-h" spellcheck="false"></textarea></div>
<div class="btns"><button class="btn btn--sm" type="button" id="rfq-paste-add">Adicionar linhas</button><span class="filepick"><input id="rfq-csv" type="file" accept=".csv,text/csv,text/plain" aria-label="Importar ficheiro CSV"><span class="btn btn--sm btn--ghost" aria-hidden="true">Importar CSV</span></span><a class="link" href="#colecoes">Continuar nas coleções</a></div>
<p class="msg" id="rfq-paste-msg" aria-live="polite"></p></div></div>
<div><form class="form box" id="f-rfq" action="mailto:{EMAIL}" method="post" enctype="text/plain" novalidate aria-labelledby="rfq-ft"><h2 class="h3" id="rfq-ft">Os seus dados</h2>
<div class="field"><label for="rfq-emp">Empresa</label><input id="rfq-emp" name="empresa" autocomplete="organization" required></div>
<div class="field"><label for="rfq-nif">NIF <span class="muted">(opcional)</span></label><input id="rfq-nif" name="nif" inputmode="numeric" maxlength="9" autocomplete="off" aria-describedby="rfq-nif-msg"><p class="msg" id="rfq-nif-msg" aria-live="polite"></p></div>
<div class="field"><label for="rfq-email">E-mail</label><input id="rfq-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="rfq-notas">Observações <span class="muted">(opcional)</span></label><textarea id="rfq-notas" name="notas"></textarea></div>
<div class="field"><span class="lab" id="rfq-ref-l"><b class="small">Imagem de referência</b> <span class="muted small">(opcional)</span></span><p class="hint" id="rfq-ref-h">Por exemplo, uma peça que um cliente pediu. A imagem fica apenas no seu dispositivo: anexe-a ao e-mail.</p>
<span class="filepick"><input id="rfq-ref" type="file" accept="image/*" aria-labelledby="rfq-ref-l" aria-describedby="rfq-ref-h rfq-ref-name"><span class="btn btn--sm btn--ghost" aria-hidden="true">Escolher imagem</span><span class="small muted" id="rfq-ref-name">Nenhuma imagem escolhida</span></span><div class="refprev" id="rfq-ref-prev" hidden></div></div>
{consent("rfq", "Aceito que a LM BIJU use estes dados para responder a este pedido.")}
<button class="btn btn--block" type="submit">Enviar pedido de proposta</button><p class="msg" id="rfq-msg" role="alert"></p>
<p class="demo-note">Ao enviar, descarregamos o ficheiro CSV do pedido e preparamos o e-mail para a equipa comercial, com o número do pedido.</p></form>
<div class="result" id="rfq-result" hidden tabindex="-1" style="margin-top:20px"></div></div></div></div>'''
    return view('pedido', 'Pedido de proposta — LM BIJU', body)


def v_entrar():
    tipos = ''.join(f'<option>{t}</option>' for t in ['Loja física', 'Revendedor online', 'Novo negócio', 'Outro'])
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Entrar", None))}<p class="idx">Área profissional</p>
<h1 class="h1" data-focus>Entrar ou criar conta</h1><p class="lede">Os preços de revenda só aparecem para contas validadas. Pedimos o NIF para confirmar a atividade comercial e respondemos por e-mail — em regra, num dia útil.</p>
<ul class="ticks"><li>Preço de revenda e escalões por quantidade</li><li>Mínimos e múltiplos em cada referência</li><li>Pedido de proposta com exportação CSV</li></ul></div>
<div class="wrap auth" style="padding-bottom:var(--sec)">
<form class="form box" id="f-login" novalidate aria-labelledby="login-t" data-js-only><h2 class="h3" id="login-t">Já tenho conta</h2>
<p class="demo-note">Demonstração: qualquer e-mail válido abre a conta de exemplo, sem verificação.</p>
<div class="field"><label for="l-email">E-mail</label><input id="l-email" name="email" type="email" autocomplete="username" required></div>
<div class="field"><label for="l-pass">Palavra-passe</label><input id="l-pass" name="pass" type="password" autocomplete="current-password" required></div>
<button class="btn btn--block" type="submit">Entrar</button><button class="btn btn--block btn--ghost" type="button" id="login-demo">Entrar com a conta de demonstração</button>
<p class="msg" data-for="f-login" role="alert"></p></form>
<form class="form box" id="f-reg" action="mailto:{EMAIL}" method="post" enctype="text/plain" novalidate aria-labelledby="reg-t"><h2 class="h3" id="reg-t">Criar conta profissional</h2>
<div class="field"><label for="reg-emp">Empresa</label><input id="reg-emp" name="empresa" autocomplete="organization" required></div>
<div class="row2"><div class="field"><label for="reg-nif">NIF</label><input id="reg-nif" name="nif" inputmode="numeric" maxlength="9" autocomplete="off" required aria-describedby="reg-nif-msg"><p class="msg" id="reg-nif-msg" aria-live="polite"></p></div>
<div class="field"><label for="reg-tipo">Tipo de negócio</label><select id="reg-tipo" name="tipo" required><option value="">Escolher…</option>{tipos}</select></div></div>
<div class="row2"><div class="field"><label for="reg-email">E-mail profissional</label><input id="reg-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="reg-tel">Telefone <span class="muted">(opcional)</span></label><input id="reg-tel" name="tel" type="tel" autocomplete="tel"></div></div>
{consent("reg", "Aceito que a LM BIJU use estes dados para validar a conta, conforme a Política de Privacidade.")}
<button class="btn btn--block" type="submit">Pedir acesso profissional</button><p class="msg" data-for="f-reg" role="alert"></p>
<p class="demo-note">O pedido segue por e-mail para a equipa comercial. Na versão final fica registado no sistema e a confirmação chega por e-mail.</p>
<div class="result" id="reg-result" hidden tabindex="-1"></div></form>
{fig("mj/mj-g3-1-t", "Corrente de elos alongados dourada sobre pedra escura", "(min-width: 1100px) 22vw, 1px", "auth__img fig--45")}
</div>'''
    return view('entrar', 'Entrar — LM BIJU', body)


def v_conta():
    d = ACCOUNT_DEMO
    rows = ''.join(f'<tr><td>{n}</td><td>{s}</td><td>{u}</td><td>{eur(t)}</td></tr>' for n, s, u, t in d['orders'])
    fav = ''
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("A minha conta", None))}<p class="idx">Área profissional</p><h1 class="h1" data-focus>A minha conta</h1>
<div class="acc-guest"><p class="lede">Inicie sessão para ver encomendas, pedidos de proposta e preços de revenda.</p><div class="btns" style="margin-top:20px"><a class="btn" href="#entrar">Entrar</a><button class="btn btn--ghost" type="button" data-demo-login data-js-only>Entrar com a conta de demonstração</button></div></div>
<p class="lede acc-private"><b data-company></b> · <span data-acc-email></span></p></div>
<div class="acc-private wrap" style="padding-bottom:var(--sec)"><p class="demo-note" style="margin-bottom:24px">Dados de exemplo nesta demonstração.</p>
<div class="acc-grid"><div class="box"><h2 class="h3">Conta</h2><dl class="facts small"><dt>Estado</dt><dd>Validada</dd><dt>NIF</dt><dd class="tnum">{d["nif"]}</dd><dt>Preços</dt><dd>Revenda com escalões</dd></dl></div>
<div class="box"><h2 class="h3">Pedido em curso</h2><div id="acc-rfq"></div></div>
<div class="box"><h2 class="h3">Documentos</h2><p class="muted">Faturas, guias e fichas técnicas ficam disponíveis aqui na versão final.</p><p><a class="link" href="#contactos">Pedir segunda via</a></p></div></div>
<section class="sec--tight" aria-labelledby="acc-ord"><h2 class="h2" id="acc-ord" style="margin-bottom:20px">Encomendas recentes</h2>
<table class="ordtbl"><caption class="sr-only">Encomendas recentes (exemplo)</caption><thead><tr><th scope="col">Encomenda</th><th scope="col">Estado</th><th scope="col">Unidades</th><th scope="col">Total s/ IVA</th></tr></thead><tbody>{rows}</tbody></table>
<p style="margin-top:20px"><button class="btn btn--ghost" type="button" data-reorder="{",".join(d["favourites"])}">Repetir as peças que mais encomenda</button></p></section>
<section class="sec--tight" aria-labelledby="acc-fav"><h2 class="h2" id="acc-fav" style="margin-bottom:24px">Peças que mais encomenda</h2><div class="cards" data-skus="{" ".join(d["favourites"])}" data-level="h3"></div></section>
<div class="duo acc-duo">{fig("mj/mj-g6-0-t", "Caixa rígida preta aberta com interior de cetim e pulseira", "(min-width: 900px) 30vw, 100vw", "fig--45")}<div class="box" style="align-self:start"><h2 class="h3">Embalagem para as suas encomendas</h2><p class="muted">Caixas, sacos e cartões podem juntar-se a qualquer pedido.</p><p><a class="link" href="#loja">Ver loja &amp; montra</a></p></div></div>
<p style="margin-top:40px"><button class="btn btn--ghost" type="button" data-logout>Terminar sessão</button></p></div>'''
    return view('conta', 'A minha conta — LM BIJU', body)


def v_contactos():
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Contactos", None))}<p class="idx">Contactos</p>
<h1 class="h1" data-focus>Fale com a <em>equipa comercial.</em></h1><p class="lede">Respondemos por e-mail em dias úteis. Para visitas ao showroom, marque a hora antes de vir.</p></div>
<div class="wrap g2" style="padding-bottom:var(--sec)"><div>
<dl class="facts"><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd><dt>WhatsApp</dt><dd class="tnum">{WHATSAPP}</dd><dt>Morada</dt><dd>{esc(ADDRESS)}</dd><dt>Horário</dt><dd>{HOURS}</dd></dl>
<p style="margin-top:24px" class="btns"><a class="btn btn--ghost" href="#showroom">Marcar visita ao showroom</a><a class="link" href="#faq">Perguntas frequentes</a></p>
{fig("mj/mj-g1-3-s", "Rua de pedra molhada ao anoitecer com montras iluminadas", "(min-width: 900px) 44vw, 100vw", "fig--32", attrs=' data-reveal style="margin-top:40px"')}</div>
<div><form class="form box" id="f-contact" action="mailto:{EMAIL}" method="post" enctype="text/plain" novalidate aria-labelledby="ct-t"><h2 class="h3" id="ct-t">Escreva-nos</h2>
<div class="row2"><div class="field"><label for="c-nome">Nome</label><input id="c-nome" name="nome" autocomplete="name" required></div><div class="field"><label for="c-emp">Empresa <span class="muted">(opcional)</span></label><input id="c-emp" name="empresa" autocomplete="organization"></div></div>
<div class="field"><label for="c-email">E-mail</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="c-ass">Assunto</label><select id="c-ass" name="assunto"><option>Conta profissional</option><option>Pedido de proposta</option><option>Visita ao showroom</option><option>Outro assunto</option></select></div>
<div class="field"><label for="c-msg">Mensagem</label><textarea id="c-msg" name="mensagem" required></textarea></div>
{consent("c", "Aceito que a LM BIJU use estes dados para responder a esta mensagem.")}
<button class="btn" type="submit">Enviar mensagem</button><p class="msg" data-for="f-contact" role="alert"></p><p class="demo-note">Ao enviar, preparamos o e-mail no seu programa de correio.</p></form>
<div class="result" id="contact-result" hidden tabindex="-1" style="margin-top:20px"></div></div></div>'''
    return view('contactos', 'Contactos — LM BIJU', body)


def art_card(a, h='h3', sizes='(min-width: 768px) 44vw, 100vw'):
    return f'<a class="art" href="#{a["id"]}">{fig(a["cover"], a["cover_alt"], sizes, "fig--32")}<span class="meta"><span>{a["tag"]}</span><span>{a["read"]} de leitura</span></span><{h}>{a["title"]}</{h}><p>{a["lede"]}</p></a>'


def v_jornal():
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Jornal", None))}<p class="idx">Jornal</p>
<h1 class="h1" data-focus>Jornal</h1><p class="lede">Notas práticas para quem vende bijuteria: materiais, montra, embalagem e o que dizer ao cliente.</p></div>
<div class="wrap" style="padding-bottom:var(--sec)"><div class="art-list">{"".join(art_card(a, "h2") for a in ARTICLES)}</div></div>'''
    return view('jornal', 'Jornal — LM BIJU', body)


def v_article(a):
    parts = []
    for b in a['body']:
        if b[0] == 'p': parts.append(f'<p>{b[1]}</p>')
        elif b[0] == 'h': parts.append(f'<h2>{b[1]}</h2>')
        elif b[0] in ('ul', 'ol'): parts.append(f'<{b[0]}>' + ''.join(f'<li>{x}</li>' for x in b[1]) + f'</{b[0]}>')
        elif b[0] == 'img':
            cap = b[3]
            parts.append(fig(b[1], b[2], '(min-width: 900px) 680px, 100vw', 'fig--32' if not b[1].endswith('-t') and not b[1].endswith('-p') else 'fig--45 fig--narrow', cap=cap, attrs=' data-reveal'))
    others = ''.join(art_card(o, 'h3', '(min-width: 768px) 30vw, 100vw') for o in ARTICLES if o['id'] != a['id'])
    body = f'''<article class="wrap article"><div class="page-hd" style="padding-bottom:0">{crumbs(("Início", "#inicio"), ("Jornal", "#jornal"), (a["title"], None))}
<p class="idx">{a["tag"]} · {a["read"]} de leitura</p><h1 class="h1" data-focus>{a["title"]}</h1><p class="lede">{a["lede"]}</p></div>
{fig(a["cover"], a["cover_alt"], "(min-width: 1440px) 1344px, 100vw", "article__cover fig--219", eager=False)}
<div class="prose">{"".join(parts)}</div>
<p class="btns"><a class="btn" href="#colecoes">Ver coleções</a><a class="link" href="#jornal">Todos os artigos</a></p></article>
<section class="wrap sec--tight" aria-labelledby="more-{a["id"]}"><h2 class="idx" id="more-{a["id"]}" style="margin-bottom:24px">Continuar a ler</h2><div class="art-list art-list--3">{others}</div></section>'''
    return view(a['id'], f'{a["title"]} — Jornal LM BIJU', body, 'jv')


def v_faq():
    groups = ''
    for i, (g, qs) in enumerate(FAQ):
        items = ''.join(f'<details><summary>{q}</summary><div class="acc__b"><p>{a}</p></div></details>' for q, a in qs)
        groups += f'<section class="faq-g" aria-labelledby="faq-{i}"><h2 class="h3" id="faq-{i}">{g}</h2><div class="acc">{items}</div></section>'
    body = f'''<div class="wrap page-hd">{crumbs(("Início", "#inicio"), ("Perguntas frequentes", None))}<p class="idx">Ajuda</p>
<h1 class="h1" data-focus>Perguntas frequentes</h1><p class="lede">Conta, preços, mínimos, pagamento, envio e showroom. Se a sua pergunta não estiver aqui, <a class="link" href="#contactos">escreva-nos</a>.</p></div>
<div class="wrap" style="padding-bottom:var(--sec)">{groups}</div>'''
    return view('faq', 'Perguntas frequentes — LM BIJU', body)


def v_produto():
    return f'<section class="view" id="produto" data-view="produto" data-title="Produto — LM BIJU" hidden><div id="pdp"></div></section>'


# ---------------------------------------------------------------- theme homes
def home_dark():
    slides = ''
    for i, h in enumerate(HERO):
        sizes = '(max-aspect-ratio: 4/5) 100vw, (min-width: 1024px) 60vw, 100vw' if h['kind'] == 'v' else '100vw'
        slides += (f'<figure class="hero__slide hero__slide--{h["kind"]}{" is-active" if i == 0 else ""}" data-kind="{h["kind"]}" data-sub="{esc(h["sub"])}" data-cap="{esc(h["cap"])}" data-sku="{h["sku"] or ""}" data-ai="{1 if h.get("ai") else 0}">'
                   f'{pic(h["img"], "", sizes, eager=(i == 0))}</figure>')
    slides += f'<figure class="hero__slide hero__slide--v" data-kind="v" data-mobile data-sub="Anéis finos para usar todos os dias: banho de ouro 18K, aros ajustáveis." data-cap="Nº 05 · Anéis finos · Na pele" data-sku="" data-ai="0">{pic("legacy/anel-solitario-v", "", "100vw")}</figure>'
    fam_img = {'aneis': 'legacy/cat-aneis-p', 'brincos': 'legacy/cat-brincos-p', 'colares': 'legacy/colar-topazio-p', 'pulseiras': 'legacy/pulseira-rosa-p',
               'relogios': 'legacy/cat-relogios-p', 'homem': 'legacy/cat-homem-p', 'loja': 'legacy/cat-loja-p'}
    fams = ''.join(f'<a class="ftile" href="#{k}" data-cursor="Abrir">{fig(fam_img[k], "", "(min-width: 1024px) 24vw, 50vw", "fig--45")}<span class="ftile__t"><span>{v}</span><small>{count_cat(k)} ref.</small></span></a>' for k, v in FAM.items())
    chaps = ''
    for c in CHAPTERS:
        data = ''.join(f'<li>{d}</li>' for d in c['data'])
        chaps += (f'<article class="chapter" aria-labelledby="ch{c["no"]}-t">{fig(c["img"], c["alt"], "100vw", "chapter__media", attrs=" data-parallax")}'
                  f'<p class="chapter__no" aria-hidden="true">Nº {c["no"]} <small>{c["key"]}</small></p>'
                  f'<div class="chapter__body wrap"><p class="idx">Capítulo {c["no"]} · {c["key"]}</p><h3 class="chapter__t" id="ch{c["no"]}-t">{c["title"]} <em>{c["em"]}</em></h3><p class="chapter__p">{c["text"]}</p>'
                  f'<ul class="chapter__data">{data}</ul><a class="link arrow" href="{c["link"][0]}">{c["link"][1]}</a></div></article>')
    feats = ''.join(card(BY[s], 'h3', 'home') for s in FEATURED)
    tabs = ''.join(f'<button role="tab" id="tab-{c["id"]}" aria-controls="pan-{c["id"]}" aria-selected="{"true" if i == 0 else "false"}"{"" if i == 0 else TI}>{c["tab"]}</button>' for i, c in enumerate(CUSTOMERS))
    pans = ''.join(f'<div class="panel" role="tabpanel" id="pan-{c["id"]}" aria-labelledby="tab-{c["id"]}"{"" if i == 0 else " hidden"}>{fig(c["img"], c["alt"], "(min-width: 768px) 46vw, 100vw", "fig--32")}'
                   f'<div><h3 class="h3">{c["title"]}</h3><p class="muted" style="margin-top:12px">{c["text"]}</p><ul class="ticks">{"".join(f"<li>{x}</li>" for x in c["points"])}</ul></div></div>' for i, c in enumerate(CUSTOMERS))
    nums = ''.join(f'<div class="num"><b data-count="{n}">{n}</b><span>{esc(l)}</span><small>{esc(s)}</small></div>' for n, l, s in NUMBERS)
    arts = ''.join(art_card(a) for a in ARTICLES[:3])
    body = f'''<section class="hero" aria-labelledby="hero-t" data-hero>
<div class="hero__media">{slides}</div><div class="hero__shade" aria-hidden="true"></div><div class="hero__glow" aria-hidden="true"></div>
<div class="hero__body wrap"><p class="idx">Grossista · Varziela, Vila do Conde</p>
<h1 class="hero__t" id="hero-t" data-focus><span class="ln"><span>Peças que pedem</span></span> <span class="ln"><span><em>a luz certa.</em></span></span></h1>
<p class="hero__sub" data-hero-sub>{esc(HERO[0]["sub"])}</p>
<div class="btns"><a class="btn" href="#colecoes" data-lights>Ver coleções {ARROW}</a><a class="btn btn--ghost" href="#entrar">Criar conta profissional</a></div></div>
<div class="hero__bar wrap"><p class="hero__count tnum" aria-hidden="true"><span data-hero-i>01</span> / <span data-hero-n>04</span></p>
<div class="hero__dots" data-js-only role="group" aria-label="Fotografias em destaque"></div>
<button class="hero__pause" type="button" data-hero-pause aria-pressed="false" data-js-only>Pausar</button>
<p class="hero__cap"><span data-hero-cap>{esc(HERO[0]["cap"])}</span> <a class="link" data-hero-link href="#produto/{HERO[0]["sku"]}">Ver peça</a> <span class="ai hero__ai" data-hero-ai hidden>Imagem ilustrativa gerada por IA</span></p></div>
<p class="hero__hint" aria-hidden="true">Deslize</p></section>

<section class="sec wrap" aria-labelledby="h-fam">{head_block("01 — Coleções", "Sete famílias, <em>um só fornecedor.</em>", "Anéis, brincos, colares, pulseiras, relógios, linha homem e tudo o que a montra precisa — na mesma encomenda.", "h-fam", True)}
<div class="fams">{fams}</div></section>

<section class="materia" id="materia" aria-labelledby="h-mat"><div class="wrap">{head_block("02 — Matéria", "Quatro passos <em>antes do balcão.</em>", "O que separa uma peça que roda de uma que fica na gaveta: a liga, o banho, o conforto na pele e a forma como chega à montra.", "h-mat", True)}</div>
<div class="chapters">{chaps}<ol class="chapter-index" aria-hidden="true">{"".join(f"<li>{c['no']} {c['key']}</li>" for c in CHAPTERS)}</ol></div></section>

<section class="gesto" id="gesto" aria-labelledby="h-gesto"><div class="gesto__pin wrap">
<div class="gesto__text"><p class="idx">03 — Filmagem própria</p><h2 class="h2" id="h-gesto">Um fio fino, <em>visto de perto.</em></h2>
<p class="gesto__cap" aria-live="off"><span data-gcap>A luz corre pelo fio.</span></p><div class="gesto__prog" aria-hidden="true"><i data-gprog></i></div>
<a class="btn btn--ghost gesto__cta" href="#colares">Ver a coleção completa {ARROW}</a></div>
<div class="gesto__stage"><canvas width="1080" height="1920" aria-hidden="true"></canvas>{poster("Colar com pendente em zircónia usado ao pescoço", cls="gesto__poster")}</div>
<ul class="gesto__facts"><li>Colar com pendente em zircónia</li><li>Banho de ouro 18K</li><li>48 fotogramas · filmagem própria</li></ul></div></section>

<section class="sec wrap" aria-labelledby="h-sel">{head_block("04 — Seleção", "Peças que <em>rodam.</em>", "PVP recomendado em todas as fichas. Com conta validada vê o preço de revenda e os escalões.", "h-sel", True)}
<div class="cards">{feats}</div><p style="margin-top:40px"><a class="btn btn--ghost" href="#colecoes">Ver todas as peças {ARROW}</a></p></section>

<section class="montra" aria-labelledby="h-montra"><div class="montra__band">{fig("mj/mj-g1-1-w", "Montra com bustos de veludo e colares, vista da rua ao anoitecer", "100vw", "montra__img", attrs=" data-parallax")}
<div class="montra__t wrap"><p class="idx">05 — Para a sua montra</p><h2 class="h2" id="h-montra">A peça vende-se <em>pela montra.</em></h2><p class="lede">Bustos, tabuleiros, expositores e embalagem na mesma fatura que as peças.</p><a class="link arrow" href="#loja">Ver loja &amp; montra</a></div></div>
<div class="trio wrap"><figure class="t1">{fig("mj/mj-g7-2-s", "Tabuleiros de veludo preto com brincos e bloco de pedra", "(min-width: 900px) 56vw, 100vw", "fig--32", attrs=" data-reveal")}<figcaption class="cap"><b>Tabuleiros e expositores</b> — veludo, metal e pedra para balcão e montra.</figcaption></figure>
<figure class="t2">{fig("legacy/cat-loja-l", "Taça de madeira com pulseiras e anéis dourados sobre fundo claro", "(min-width: 900px) 34vw, 100vw", "fig--32", attrs=" data-reveal")}<figcaption class="cap"><b>Taça de madeira</b> · LB-2001. Para expor anéis e pulseiras ao balcão.</figcaption></figure>
<figure class="t3">{fig("mj/mj-g6-0-s", "Caixa rígida preta aberta com interior de cetim e pulseira", "(min-width: 900px) 46vw, 100vw", "fig--32", attrs=" data-reveal")}<figcaption class="cap"><b>Embalagem de oferta</b> — caixas e cartões para fechar a venda ao balcão.</figcaption></figure></div></section>

<section class="sec wrap" aria-labelledby="h-cli">{head_block("06 — Para quem vendemos", "Uma conta, <em>o seu tipo de loja.</em>", None, "h-cli")}
<div class="tabs" role="tablist" aria-label="Tipo de negócio">{tabs}</div>{pans}
<p class="btns" style="margin-top:40px"><a class="btn" href="#entrar">Criar conta profissional</a><a class="link" href="#empresa">Como funciona</a></p></section>

<section class="sec wrap showroom-t" aria-labelledby="h-show"><div class="showroom-t__g">
{fig("legacy/hero-aco-v", "Corrente cubana em aço 316L sobre fundo preto", "(min-width: 900px) 40vw, 100vw", "showroom-t__img", attrs=" data-reveal")}
<div><p class="idx">07 — Showroom</p><h2 class="h2" id="h-show">Varziela, <em>Vila do Conde.</em></h2><p class="lede">Visite com marcação: preparamos as famílias que lhe interessam antes de chegar.</p>
<div class="nums nums--2">{nums}</div><p class="small muted" style="margin-top:12px">Referências por linha no catálogo atual.</p>
<dl class="facts" style="margin-top:28px"><dt>Morada</dt><dd>{esc(ADDRESS)}</dd><dt>Horário</dt><dd>{HOURS}</dd></dl>
<p class="btns" style="margin-top:28px"><a class="btn btn--ghost" href="#showroom">Marcar visita</a></p></div></div></section>

<section class="sec wrap" aria-labelledby="h-jor">{head_block("08 — Jornal", "Para quem vende, <em>não só para quem compra.</em>", None, "h-jor")}<div class="art-list art-list--3">{arts}</div></section>

<section class="final" aria-labelledby="h-final">{fig("mj/mj-g2-3-s", "", "100vw", "final__bg", attrs=" data-parallax")}
<div class="final__t wrap"><p class="idx">Próximo passo</p><h2 class="final__h" id="h-final">Pronto para ver <em>os preços?</em></h2>
<p class="lede">Crie a conta profissional com o NIF da sua empresa. Validamos a atividade e abrimos o catálogo com os seus preços de revenda.</p>
<div class="btns"><a class="btn btn--xl" href="#entrar">Criar conta profissional</a><a class="btn btn--xl btn--ghost" href="#contactos">Falar com a equipa</a></div></div></section>'''
    return view('inicio', 'LM BIJU — Bijuteria por grosso · Vila do Conde', body, 'home')


def home_light():
    slides = ''.join(f'<figure class="lhero__slide{" is-active" if i == 0 else ""}" data-sku="{h["sku"]}" data-name="{esc(BY[h["sku"]]["name"])}">{pic(h["img"], BY[h["sku"]]["alt"], "(min-width: 900px) 58vw, 100vw", eager=(i == 0))}</figure>' for i, h in enumerate(LIGHT_HERO))
    fam_img = {'aneis': 'legacy/cat-aneis-p', 'brincos': 'legacy/cat-brincos-p', 'colares': 'legacy/colar-topazio-p', 'pulseiras': 'legacy/pulseira-rosa-p',
               'relogios': 'legacy/cat-relogios-p', 'homem': 'legacy/cat-homem-p', 'loja': 'legacy/cat-loja-p'}
    fams = ''.join(f'<a class="tile" href="#{k}">{fig(fam_img[k], "", "(min-width: 1024px) 23vw, 46vw", "fig--45", attrs=" data-reveal")}<span class="tile__t">{v} <small>{count_cat(k)}</small></span></a>' for k, v in FAM.items())
    feats = ''.join(card(BY[s], 'h3', 'home') for s in FEATURED)
    mats = ''.join(f'<a class="tile" href="#colecoes?mat={k}">{fig(i, "", "(min-width: 1024px) 18vw, 46vw", "fig--45")}<span class="tile__t">{MAT[k]}</span><p>{l}</p></a>' for k, i, l in MAT_TILES)
    nums = ''.join(f'<div class="num"><b>{n}</b><span>{esc(l)}</span><small>{esc(s)}</small></div>' for n, l, s in NUMBERS)
    arts = ''.join(art_card(a) for a in ARTICLES[1:4])
    b0 = BY[LIGHT_HERO[0]['sku']]
    body = f'''<section class="lhero" aria-labelledby="hero-t" data-lhero>
<div class="lhero__text"><p class="idx">Grossista de bijuteria · Vila do Conde</p>
<h1 class="lhero__h" id="hero-t" data-focus>Bijuteria por grosso, escolhida peça a peça.</h1>
<p class="lede">956 referências em banho de ouro 18K, aço 316L, pérola e zircónia. Preços de revenda para lojas e revendedores com conta validada.</p>
<div class="btns"><a class="btn" href="#colecoes">Ver coleções</a><a class="btn btn--ghost" href="#entrar">Criar conta profissional</a></div>
<ul class="lhero__facts"><li><b class="tnum">956</b> referências</li><li><b>1 dia útil</b> para validar a conta</li><li><b>Showroom</b> na Varziela</li></ul></div>
<div class="lhero__media"><div class="lhero__frame">{slides}</div>
<div class="lhero__bar"><p><span data-lh-sku class="tnum">{b0["sku"]}</span> · <a class="link" data-lh-link href="#produto/{b0["sku"]}"><span data-lh-name>{esc(b0["name"])}</span></a></p>
<div class="lhero__dots" role="group" aria-label="Fotografias em destaque" data-js-only></div><button class="lhero__pause" type="button" data-lh-pause aria-pressed="false" data-js-only>Pausar</button></div></div></section>

<section class="sec wrap" aria-labelledby="l-fam">{head_block("01 — Coleções", "Sete famílias, um só fornecedor.", "Anéis, brincos, colares, pulseiras, relógios, linha homem e tudo o que a montra precisa — na mesma encomenda.", "l-fam", True)}<div class="tiles tiles--7">{fams}</div></section>

<section class="sec wrap" aria-labelledby="l-new">{head_block("02 — Seleção", "Acabado de entrar em stock.", "PVP recomendado. O preço de revenda, os mínimos e os escalões aparecem com conta validada.", "l-new", True)}<div class="cards">{feats}</div>
<p style="margin-top:48px;text-align:center"><a class="btn btn--ghost" href="#colecoes">Ver todas as peças</a></p></section>

<section class="sec lband" aria-labelledby="l-mat"><div class="wrap">{head_block("03 — Materiais", "Cinco materiais, uma regra: durar na montra.", None, "l-mat")}<div class="tiles tiles--5">{mats}</div>
{fig("mj/mj-g5-1-w", "Corrente cubana dourada em grande plano", "(min-width: 1440px) 1344px, 100vw", "fig--219", attrs=' data-reveal style="margin-top:clamp(40px,6vw,80px)"')}</div></section>

<section class="sec wrap lframes" aria-labelledby="l-fr"><div class="lframes__g">
<div class="lframes__t"><p class="idx">04 — Visto de perto</p><h2 class="h2" id="l-fr">Um fio fino, visto de perto.</h2>
<p class="lede">Colar com pendente em zircónia e banho de ouro 18K, em 48 fotogramas da nossa filmagem. Arraste para percorrer.</p>
<div class="field lframes__ctl" data-js-only><label for="lf-range">Fotograma <span class="tnum" data-lf-n>1</span> de 48</label><input id="lf-range" type="range" min="1" max="48" value="1" step="1"></div>
<p><a class="link" href="#colares">Ver colares</a></p></div>
<div class="lframes__stage"><img data-lf-img src="{BASE}video/frame-001-720.jpg" width="720" height="1280" alt="Colar com pendente em zircónia ao pescoço, fotograma 1 de 48" loading="lazy" decoding="async"></div></div></section>

<section class="sec wrap ledit" aria-labelledby="l-pele">{fig("legacy/anel-solitario-v", "Duas mãos com anéis finos dourados sobre fundo terracota", "(min-width: 900px) 42vw, 100vw", "ledit__m", attrs=" data-reveal")}
<div class="ledit__t"><p class="idx">05 — Na pele</p><h2 class="h2" id="l-pele">Feito para se usar.</h2>
<p class="lede">Anéis, brincos e colares passam o dia em contacto com a pele. Partilhamos a informação de materiais de cada referência com quem a vende.</p>
<p><a class="link arrow" href="#jornal-na-pele">Banho de ouro na pele: o que dizer ao cliente</a></p>
{fig("mj/mj-g2-1-w", "Mão com anel fino encostada ao pescoço com um fio delicado", "(min-width: 900px) 40vw, 100vw", "fig--219", attrs=' data-reveal style="margin-top:32px"')}</div></section>

<section class="sec wrap lmontra" aria-labelledby="l-loja"><div class="head head--split"><div class="head"><p class="idx">06 — Loja &amp; montra</p><h2 class="h2" id="l-loja">A peça vende-se pela montra.</h2></div><p class="lede">Expositores, taças e embalagem na mesma encomenda que as peças — a montra fica pronta no dia em que a caixa chega.</p></div>
<div class="lmontra__g">{fig("legacy/cat-loja-l", "Taça de madeira com pulseiras e anéis dourados", "(min-width: 900px) 58vw, 100vw", "fig--32", cap="Taça de madeira · LB-2001", attrs=" data-reveal")}{fig("mj/mj-g7-3-t", "Expositor em T com corrente e bloco de pedra", "(min-width: 900px) 34vw, 100vw", "fig--45", attrs=" data-reveal")}</div>
<p style="margin-top:32px"><a class="btn btn--ghost" href="#loja">Ver loja &amp; montra</a></p></section>

<section class="sec wrap" aria-labelledby="l-emp">{head_block("07 — Empresa", "Um fornecedor, não um catálogo anónimo.", "Stock próprio, showroom na Zona Industrial da Varziela e equipa comercial. O catálogo é fechado ao público para proteger as margens de quem já compra connosco.", "l-emp", True)}
<div class="nums">{nums}</div><p class="small muted" style="margin-top:12px">Referências por linha no catálogo atual.</p>
{fig("mj/mj-g1-1-w", "Montra com bustos de veludo e colares ao anoitecer", "(min-width: 1440px) 1344px, 100vw", "fig--219", attrs=' data-reveal style="margin-top:clamp(40px,6vw,72px)"')}
<p class="btns" style="margin-top:32px"><a class="btn btn--ghost" href="#showroom">Visitar o showroom</a><a class="link" href="#empresa">Sobre a empresa</a></p></section>

<section class="sec wrap" aria-labelledby="l-jor">{head_block("08 — Jornal", "Para quem vende, não só para quem compra.", None, "l-jor")}<div class="art-list art-list--3">{arts}</div></section>

<section class="lcta" aria-labelledby="l-cta"><div class="wrap lcta__g"><div><p class="idx">Próximo passo</p><h2 class="h2" id="l-cta">Pronto para ver os preços?</h2>
<p class="lede">Crie a conta profissional com o NIF da sua empresa. Validamos a atividade e abrimos o catálogo com os seus preços de revenda.</p>
<div class="btns"><a class="btn" href="#entrar">Criar conta profissional</a><a class="btn btn--ghost" href="#contactos">Falar com a equipa</a></div></div>
{fig("legacy/cat-pulseiras-p", "Anel dourado com a palavra love sobre malha de lã", "(min-width: 900px) 30vw, 100vw", "fig--45", attrs=" data-reveal")}</div></section>'''
    return view('inicio', 'LM BIJU — Bijuteria por grosso · Vila do Conde', body, 'home')


# ---------------------------------------------------------------- assembly
def data_json():
    prods = []
    for p in P:
        prods.append({k: p[k] for k in ('sku', 'name', 'fam', 'cats', 'mats', 'aud', 'occ', 'band', 'style', 'pvp', 'moq', 'img', 'alt', 'temp', 'size', 'desc', 'badge')}
                     | {'specs': p['specs'], 'tiers': [list(t) for t in tiers(p)]})
    d = dict(base=BASE, email=EMAIL, products=prods, fam={**FAM_FILTER, 'homem': 'Homem'}, mat=MAT, matinfo=MATINFO,
             cats={k: {'title': v['title'], 'n': count_cat(k)} for k, v in CATS.items()}, account={'company': ACCOUNT_DEMO['company']},
             img=img_js(sorted({p['img'] for p in P})))
    return json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


def jsonld():
    org = {"@context": "https://schema.org", "@type": "Organization", "@id": "#org", "name": "LM BIJU", "email": EMAIL,
           "address": {"@type": "PostalAddress", "streetAddress": "Zona Industrial da Varziela", "addressLocality": "Vila do Conde", "addressCountry": "PT"}}
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Seleção LM BIJU", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": {"@type": "Product", "sku": s, "name": BY[s]['name'], "brand": {"@id": "#org"}, "image": f"{BASE}img/{BY[s]['img']}-{A[BY[s]['img']]['jpg']}.jpg"}}
        for i, s in enumerate(FEATURED)]}
    return json.dumps([org, items], ensure_ascii=False)


def page(theme, showcase=False):
    USED_before = set(USED)
    other = 'demo-dark.html' if theme == 'dark' else 'demo-light.html'
    pre = other if showcase else ''
    css = (B / 'base.css').read_text(encoding='utf-8') + (B / f'{theme}.css').read_text(encoding='utf-8')
    fonts = (PD / 'assets/fonts/fonts.css').read_text(encoding='utf-8').replace('url(', f'url({BASE}fonts/')
    if theme == 'light':
        fonts = '\n'.join(l for l in fonts.splitlines() if 'Cormorant' not in l)
    home = home_dark() if theme == 'dark' else home_light()
    if showcase:
        views = [home]
    else:
        views = [home, v_colecoes(), *[v_cat(k) for k in CATS], v_produto(), v_empresa(theme), v_showroom(), v_pedido(), v_entrar(), v_conta(),
                 v_contactos(), v_jornal(), *[v_article(a) for a in ARTICLES], v_faq()]
    names = re.findall(r'data-view="([^"]+)"', ''.join(views))
    route_css = ''.join(f'.js[data-route="{n}"] [data-view="{n}"]' + ('{display:block}' if n != 'produto' else '{}') for n in names)
    app = (B / 'app.js').read_text(encoding='utf-8')
    tjs = (B / f'{theme}.js').read_text(encoding='utf-8')
    lcp = HERO[0]['img'] if theme == 'dark' else LIGHT_HERO[0]['img']
    la = A[lcp]
    lcp_set = ', '.join(f'{BASE}img/{lcp}-{w}.avif {w}w' for w in la['widths'])
    lcp_sizes = '(max-aspect-ratio: 4/5) 100vw, (min-width: 1024px) 60vw, 100vw' if theme == 'dark' else '(min-width: 900px) 58vw, 100vw'
    vendor = ''  # dark: GSAP/ScrollTrigger/Lenis are loaded by dark.js after the load event
    title = 'LM BIJU — Bijuteria por grosso · Vila do Conde' + (' · Apresentação' if showcase else '')
    loader = '<div class="loader" id="loader" aria-hidden="true" data-js-only><div class="loader__in"><span class="loader__logo"><span>LM</span> <em>Biju</em></span><i class="loader__line"></i></div></div>' if theme == 'dark' and not showcase else ''
    cursor = '<div class="cur cur-dot" aria-hidden="true"></div><div class="cur cur-ring" aria-hidden="true"><span>Ver</span></div>' if theme == 'dark' else ''
    sc_banner = (f'<aside class="sc-note" aria-label="Sobre esta página"><p>Apresentação numa só página. <a class="link" href="{other}">Abrir a demonstração completa</a> (catálogo, fichas, pedido de proposta, conta).</p></aside>') if showcase else ''
    body = '\n'.join(views)
    if showcase:  # links to other pages go to the full demo
        body = re.sub(r'href="#(?!inicio")', f'href="{other}#', body)
    doc = f'''<!DOCTYPE html>
<html lang="pt-PT" class="{theme}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="LM BIJU, grossista de bijuteria em Vila do Conde: 956 referências em banho de ouro 18K, aço 316L, pérola e zircónia para lojas e revendedores profissionais.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="{'#14120F' if theme == 'dark' else '#FFFFFF'}">
<meta property="og:type" content="website"><meta property="og:title" content="LM BIJU — Bijuteria por grosso"><meta property="og:description" content="Banho de ouro 18K, aço 316L, pérola e zircónia para lojas e revendedores.">
<meta property="og:image" content="{BASE}img/{lcp}-{la['jpg']}.jpg">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 fill=%27{'%2314120F' if theme == 'dark' else '%23FFFFFF'}%27/%3E%3Ctext x=%2716%27 y=%2721%27 font-family=%27Arial%27 font-weight=%27700%27 font-size=%2713%27 fill=%27{'%23FAF7F2' if theme == 'dark' else '%231A1A1A'}%27 text-anchor=%27middle%27%3ELM%3C/text%3E%3C/svg%3E">
<link rel="preload" as="font" type="font/woff2" href="{BASE}fonts/Inter-normal-latin.woff2" crossorigin>
<link rel="preload" as="image" type="image/avif" fetchpriority="high" imagesrcset="{lcp_set}" imagesizes="{lcp_sizes}">
<script>(function(){{var d=document.documentElement,h=location.hash.slice(1).split(/[?\\/]/)[0],v={json.dumps(names)};d.classList.add('js');d.setAttribute('data-route',v.indexOf(h)>-1?h:'inicio')}})()</script>
<script type="application/ld+json">{jsonld()}</script>
<style>{fonts}{css}{route_css}</style>
</head>
<body>
<a class="skip" href="#main">Saltar para o conteúdo</a>
{loader}
{header(theme, showcase, pre)}
{sc_banner}
<main id="main" tabindex="-1">
{body}
</main>
{footer(pre)}
<dialog class="lightbox" id="lightbox" aria-label="Fotografia ampliada"><button class="lightbox__x" type="button">Fechar</button><div class="lightbox__in lightbox__img"></div></dialog>
<div class="sr-only" aria-live="polite" id="live"></div>
{cursor}
<script type="application/json" id="lmb-data">{data_json()}</script>
{vendor}
<script>{app}</script>
<script>{tjs}</script>
</body>
</html>'''
    used = USED - USED_before if False else None
    return doc


def chooser():
    fonts = '\n'.join(l for l in (PD / 'assets/fonts/fonts.css').read_text(encoding='utf-8').replace('url(', f'url({BASE}fonts/').splitlines() if 'Cormorant' not in l)
    card = lambda href, img, alt, t, d, dark: (f'<a class="c{" c--d" if dark else ""}" href="{href}">{pic(img, alt, "(min-width: 900px) 44vw, 100vw")}'
                                              f'<span class="c__t"><b>{t}</b><span>{d}</span></span></a>')
    return f'''<!DOCTYPE html><html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>LM BIJU — Demonstrações</title><meta name="robots" content="noindex, nofollow">
<style>{fonts}*{{box-sizing:border-box}}body{{margin:0;font:400 16px/1.6 Inter,system-ui,sans-serif;color:#1A1A1A;background:#fff}}.w{{max-width:1200px;margin:0 auto;padding:56px 24px 72px}}
h1{{font-size:clamp(32px,4vw,48px);letter-spacing:-.03em;line-height:1.05;margin:0 0 12px}}p{{margin:0;color:#6B6B6B;max-width:62ch}}.g{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:40px}}@media (max-width:760px){{.g{{grid-template-columns:1fr}}}}
.c{{display:grid;text-decoration:none;color:#1A1A1A;background:#FAFAF8}}.c img{{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}}.c picture{{display:block}}.c__t{{display:grid;gap:4px;padding:18px 20px}}.c__t b{{font-size:20px}}.c__t span{{color:#6B6B6B;font-size:14px}}
.c--d{{background:#14120F;color:#FAF7F2}}.c--d .c__t span{{color:#CFC8BD}}.c:hover b{{text-decoration:underline}}.c:focus-visible{{outline:2px solid #1A1A1A;outline-offset:4px}}
.l{{margin-top:32px;display:flex;flex-wrap:wrap;gap:12px 28px;font-size:15px}}.l a{{color:#1A1A1A}}small{{display:block;margin-top:40px;color:#6B6B6B;font-size:13px}}</style></head>
<body><main class="w"><p style="font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#75603F;font-weight:600;margin-bottom:12px">LM BIJU · Proposta de site</p>
<h1>Duas direções para o novo site</h1><p>As duas versões têm as mesmas páginas e o mesmo conteúdo: coleções, famílias, fichas de produto, pedido de proposta, conta profissional, empresa, showroom, jornal, FAQ e contactos.</p>
<div class="g">{card("demo-dark.html", "legacy/hero-aco-v", "Corrente cubana em aço sobre fundo preto", "Versão escura", "Câmara escura: dramática, com movimento e filmagem ao scroll.", True)}
{card("demo-light.html", "legacy/hero-ouro-p", "Anel dourado sobre pedras brancas", "Versão clara", "Branco, limpo e direto: fotografia grande, movimento discreto.", False)}</div>
<div class="l"><a href="demo-showcase-dark.html">Apresentação numa página — escura</a><a href="demo-showcase-light.html">Apresentação numa página — clara</a><a href="assets/preview.html">Todas as imagens</a></div>
<small>Demonstração de design. Preços, escalões e dados de conta são exemplos. Imagens marcadas “Imagem ilustrativa gerada por IA” são ilustrativas.</small></main></body></html>'''


def build():
    out = {}
    usage = {}
    for theme in ('dark', 'light'):
        for sc in (False, True):
            USED.clear()
            doc = page(theme, sc)
            name = f'demo-showcase-{theme}.html' if sc else f'demo-{theme}.html'
            (PD / name).write_text(doc, encoding='utf-8')
            out[name] = (len(doc.encode('utf-8')), set(USED))
            for u in USED:
                usage.setdefault(u, []).append(name)
    # manifest: where each asset is used
    for a in MAN['assets']:
        if a['id'] in A and (a['id'].startswith('legacy/') or a['id'].startswith('mj/')):
            a['usedIn'] = sorted(usage.get(a['id'], []))
        elif a['id'].startswith('video/'):
            a['usedIn'] = ['demo-dark.html (scroll, 48 fotogramas)', 'demo-light.html (controlo deslizante, 48 fotogramas)', 'demo-showcase-dark.html', 'demo-showcase-light.html']
    (PD / 'index.html').write_text(chooser(), encoding='utf-8')
    (PD / 'assets/manifest.json').write_text(json.dumps(MAN, ensure_ascii=False, indent=1), encoding='utf-8')
    preview()
    img_ids = [a['id'] for a in MAN['assets'] if a['id'].startswith(('legacy/', 'mj/'))]
    for name, (size, used) in out.items():
        missing = [i for i in img_ids if i not in used]
        print(f'{name}: {size / 1024:.0f} KB · images used {len(used)}/{len(img_ids)}' + (f' · NOT USED: {missing}' if missing and 'showcase' not in name else ''))


def preview():
    rows = ''
    for a in MAN['assets']:
        if not a['id'].startswith(('legacy/', 'mj/')):
            continue
        v = next(x for x in a['variants'] if x['format'] == 'jpg')
        flags = ('<b class="ai">IA</b>' if a['ai'] else '') + ('<b class="tp">3.º</b>' if a.get('thirdParty') else '')
        temp = ', '.join(p['sku'] for p in P if p['img'] == a['id'] and p['temp'])
        rows += (f'<figure data-src="{"ai" if a["ai"] else "legacy"}"><a href="{v["file"]}"><img src="{v["file"]}" loading="lazy" alt=""></a><figcaption><b>{a["id"]}</b> {flags}<br>'
                 f'origem {esc(a["sourceSize"])} · recorte {a["crop"]} · larguras {", ".join(map(str, a["widths"]))}<br>'
                 f'{("Foto temporária para " + temp + "<br>") if temp else ""}{("⚠ " + esc(a["thirdParty"]) + "<br>") if a.get("thirdParty") else ""}usado em: {", ".join(a.get("usedIn", [])) or "—"}</figcaption></figure>')
    n = sum(1 for a in MAN['assets'] if a['id'].startswith(('legacy/', 'mj/')))
    html = f'''<!DOCTYPE html><html lang="pt-PT"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>LM BIJU — imagens da demonstração</title>
<style>body{{margin:0;font:14px/1.5 system-ui,sans-serif;background:#f6f6f4;color:#1a1a1a}}header{{padding:24px}}h1{{margin:0 0 6px;font-size:22px}}.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;padding:0 24px 40px}}
figure{{margin:0;background:#fff;border:1px solid #e5e5e5}}img{{width:100%;aspect-ratio:1;object-fit:contain;background:#ddd;display:block}}figcaption{{padding:10px;font-size:12px;color:#444}}.ai{{background:#1a1a1a;color:#fff;padding:1px 5px;font-size:11px}}.tp{{background:#b3261e;color:#fff;padding:1px 5px;font-size:11px}}
button{{font:inherit;padding:6px 12px;border:1px solid #999;background:#fff;cursor:pointer}}button[aria-pressed=true]{{background:#1a1a1a;color:#fff}}</style></head><body>
<header><h1>Imagens da demonstração ({n})</h1><p>AVIF + WebP em todas as larguras, 1 JPEG de recurso · sRGB · sem metadados. Clique para abrir o JPEG. Dados completos em manifest.json.</p>
<p><button type="button" data-f="" aria-pressed="true">Todas</button> <button type="button" data-f="legacy" aria-pressed="false">Fotografias LM BIJU</button> <button type="button" data-f="ai" aria-pressed="false">Geradas por IA</button></p></header>
<div class="g">{rows}</div>
<script>document.querySelectorAll('button[data-f]').forEach(b=>b.onclick=()=>{{document.querySelectorAll('button[data-f]').forEach(x=>x.setAttribute('aria-pressed',x===b));document.querySelectorAll('figure').forEach(f=>f.hidden=b.dataset.f&&f.dataset.src!==b.dataset.f)}})</script></body></html>'''
    (PD / 'assets/preview.html').write_text(html, encoding='utf-8')


if __name__ == '__main__':
    build()
