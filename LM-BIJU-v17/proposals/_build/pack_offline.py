#!/usr/bin/env python3
"""Packs the offline demo: LM-BIJU-v17/demo-showcase-offline.zip

Layout inside the zip (one root folder, opens by double-click, no server needed):
  LM-BIJU-demo/
    demo-showcase.html   single-page presentation
    demo-b.html          full demo (catalogue, product page, RFQ, registration)
    assets/              legacy / mj / video (paths rewritten from ../_research/demo-b/assets/)
    vendor/  fonts/      GSAP, ScrollTrigger, Lenis, self-hosted woff2 + licences
    LEIA-ME.txt          how to open (PT + 中文)
Run after build.py: python3 proposals/_build/pack_offline.py
"""
import pathlib, re, zipfile

P = pathlib.Path(__file__).resolve().parent.parent      # proposals/
ROOT = P.parent                                          # LM-BIJU-v17/
ASSETS = ROOT / '_research' / 'demo-b' / 'assets'
OUT = ROOT / 'demo-showcase-offline.zip'
TOP = 'LM-BIJU-demo/'

README = """LM BIJU — Demonstração de design (offline)
==========================================

PT
--
1. Descompacte este ficheiro (botão direito > Extrair tudo).
2. Abra a pasta LM-BIJU-demo e faça duplo clique em demo-showcase.html.
   Abre no navegador, sem internet e sem instalar nada.
3. Para o site completo (catálogo, ficha de produto, pedido de proposta,
   registo), abra demo-b.html ou use os botões dentro da apresentação.

Navegadores recomendados: Chrome, Edge, Safari ou Firefox atualizados.
Preços, escalões e números da empresa são valores de exemplo.
Imagens marcadas "Imagem ilustrativa gerada por IA" não representam
referências do catálogo.

中文
----
1. 先解压（右键 > 全部解压缩）。不要在压缩包里直接双击打开。
2. 打开 LM-BIJU-demo 文件夹，双击 demo-showcase.html：一页式展示，
   不需要网络，不需要安装 Python。
3. 完整网站（目录、详情、询价、注册）：双击 demo-b.html，
   或者点击展示页里的按钮进入。

推荐浏览器：最新版 Chrome / Edge / Safari / Firefox。
价格、阶梯价、公司数字都是示例数据。
标有"Imagem ilustrativa gerada por IA"的图片是 AI 氛围图，不代表具体商品。
"""


def html(name):
    s = (P / name).read_text(encoding='utf-8')
    # file:// pages have origin "null": a crossorigin font preload is refused (CORS) and logs an error,
    # while the @font-face rules themselves load fine, so the preload is dropped offline.
    s = re.sub(r'<link rel="preload" as="font"[^>]*>\n?', '', s)
    return s.replace('../_research/demo-b/assets/', 'assets/').encode('utf-8')


def main():
    n = 0
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in ('demo-showcase.html', 'demo-b.html'):
            z.writestr(TOP + name, html(name)); n += 1
        z.writestr(TOP + 'LEIA-ME.txt', README.replace('\n', '\r\n').encode('utf-8-sig')); n += 1
        for sub in ('legacy', 'mj', 'video'):
            for f in sorted((ASSETS / sub).rglob('*')):
                if f.is_file():
                    # already-compressed media: store, don't deflate
                    z.write(f, TOP + 'assets/' + f.relative_to(ASSETS).as_posix(), compress_type=zipfile.ZIP_STORED); n += 1
        for sub in ('vendor', 'fonts'):
            for f in sorted((P / sub).rglob('*')):
                if f.is_file():
                    z.write(f, TOP + sub + '/' + f.relative_to(P / sub).as_posix()); n += 1
    print(f'{OUT.name}: {n} files, {OUT.stat().st_size / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
