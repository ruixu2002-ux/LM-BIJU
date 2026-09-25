#!/usr/bin/env python3
"""Offline package for the v3 demos: LM-BIJU-v17/lm-biju-demo-offline.zip

LM-BIJU-demo/
  index.html                 chooser (double-click this)
  demo-dark.html  demo-light.html  demo-showcase-dark.html  demo-showcase-light.html
  assets/                    img/ video/ fonts/ vendor/ manifest.json preview.html
  LEIA-ME.txt
Run after site.py: python3 proposals/_build/pack.py
"""
import pathlib, re, zipfile

PD = pathlib.Path(__file__).resolve().parent.parent      # proposals/
OUT = PD.parent / 'lm-biju-demo-offline.zip'
TOP = 'LM-BIJU-demo/'
PAGES = ['index.html', 'demo-dark.html', 'demo-light.html', 'demo-showcase-dark.html', 'demo-showcase-light.html']

README = """LM BIJU — Demonstração do novo site (offline)
============================================

PT
--
1. Descompacte o ficheiro (botão direito > Extrair tudo).
2. Abra a pasta LM-BIJU-demo e faça duplo clique em index.html.
3. Escolha a versão escura ou a versão clara. Funciona sem internet e sem instalar nada.

Navegadores: Chrome, Edge, Safari ou Firefox atualizados.
Preços, escalões e dados de conta são exemplos. Imagens marcadas
"Imagem ilustrativa gerada por IA" não representam referências do catálogo.

中文
----
1. 先解压（右键 > 全部解压缩）。不要在压缩包里直接双击。
2. 打开 LM-BIJU-demo 文件夹，双击 index.html。
3. 选择深色版或白色版。不需要网络，不需要安装任何东西。

也可以直接双击：
  demo-dark.html            深色版完整网站（12 类页面）
  demo-light.html           白色版完整网站（12 类页面）
  demo-showcase-dark.html   深色版一页式展示
  demo-showcase-light.html  白色版一页式展示
  assets/preview.html       全部图片一览
"""


def page(name):
    s = (PD / name).read_text(encoding='utf-8')
    # file:// has origin "null": a crossorigin font preload is refused and logs a CORS error;
    # the @font-face rules themselves load fine, so the preload is dropped in the offline copy.
    s = re.sub(r'<link rel="preload" as="font"[^>]*>\n?', '', s)
    return s.encode('utf-8')


def main():
    n = 0
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in PAGES:
            z.writestr(TOP + name, page(name)); n += 1
        z.writestr(TOP + 'LEIA-ME.txt', README.replace('\n', '\r\n').encode('utf-8-sig')); n += 1
        for f in sorted((PD / 'assets').rglob('*')):
            if f.is_file():
                media = f.suffix in ('.avif', '.webp', '.jpg', '.mp4', '.woff2')
                z.write(f, TOP + 'assets/' + f.relative_to(PD / 'assets').as_posix(), compress_type=zipfile.ZIP_STORED if media else zipfile.ZIP_DEFLATED); n += 1
    print(f'{OUT.name}: {n} files, {OUT.stat().st_size / 1e6:.1f} MB')


if __name__ == '__main__':
    main()
