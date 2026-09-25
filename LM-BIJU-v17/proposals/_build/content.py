# -*- coding: utf-8 -*-
"""LM BIJU demo v3 — shared content (PT-PT, AO90).

Facts marked [v17] come from LM-BIJU-v17/index.html, empresa.html, catalogo.html.
Product tagging for audience / occasion / style is demo tagging (to be confirmed by the client).
"""

EMAIL = 'geral@lmbiju.pt'                      # [v17]
WHATSAPP = '+351 000 000 000'                  # placeholder agreed with the user
ADDRESS = 'Zona Industrial da Varziela, Vila do Conde, Portugal'   # [v17]
HOURS = 'Segunda a sexta, 09h00 – 18h30'       # [v17 empresa.html]
MAPS = 'https://www.google.com/maps/search/?api=1&query=Zona+Industrial+da+Varziela+Vila+do+Conde'
LIVRO = 'https://www.livroreclamacoes.pt/'

# [v17] home: "342 refs Ouro 18K · 486 refs Aço 316L · 128 refs Relógios & Homem"
NUMBERS = [
    (956, 'referências no catálogo', 'Soma das três linhas'),
    (486, 'em aço 316L', 'A linha de maior rotação'),
    (342, 'em banho de ouro 18K', 'A coleção ouro 18K'),
    (128, 'relógios e linha homem', 'Com expositores próprios'),
]

FAM = {  # families (category pages) — order = navigation order
    'aneis': 'Anéis', 'brincos': 'Brincos', 'colares': 'Colares', 'pulseiras': 'Pulseiras',
    'relogios': 'Relógios', 'homem': 'Homem', 'loja': 'Loja & montra',
}
FAM_FILTER = {'aneis': 'Anéis', 'brincos': 'Brincos', 'colares': 'Colares', 'pulseiras': 'Pulseiras',
              'relogios': 'Relógios', 'conjuntos': 'Conjuntos', 'loja': 'Loja & montra'}
MAT = {'aco': 'Aço 316L', 'ouro18': 'Banho de ouro 18K', 'banho': 'Banho de ouro', 'perola': 'Pérola', 'zirconia': 'Zircónia'}
AUD = {'mulher': 'Mulher', 'homem': 'Homem', 'crianca': 'Criança'}
OCC = {'dia': 'Dia-a-dia', 'festa': 'Festa', 'noiva': 'Noiva', 'fe': 'Fé'}
PRICE = {'economico': 'Económico · até 12 €', 'medio': 'Médio · 12 – 25 €', 'premium': 'Premium · mais de 25 €'}
STYLE = {'minimal': 'Minimalista', 'classico': 'Clássico', 'moderno': 'Moderno', 'vintage': 'Vintage'}

MATINFO = {
    'aco': 'Aço inoxidável AISI 316L, a liga das caixas de relógio. Não escurece com o uso diário e resiste à água e ao suor. Limpa-se com um pano macio.',
    'ouro18': 'Camada de ouro 18K sobre base metálica; a base de cada referência vem indicada na ficha técnica. Para conservar o brilho, evitar perfume e produtos de limpeza diretamente na peça e guardar em bolsa individual.',
    'banho': 'Banho de ouro. A composição da base vem indicada na ficha técnica de cada referência.',
    'perola': 'Pérola sintética montada em base de aço 316L. Evitar perfume e cremes; limpar com um pano seco.',
    'zirconia': 'Zircónias cúbicas lapidadas, cravadas em peças com banho de ouro 18K. Limpar com escova macia e água morna.',
}


def band(pvp):
    return 'economico' if pvp < 12 else ('medio' if pvp <= 25 else 'premium')


def r05(x):
    return round(x * 20) / 20


def tiers(p):
    """Example wholesale tiers: PVP without VAT / 2.4, then −8 % and −15 % at 4× and 16× the minimum."""
    b = r05(p['pvp'] / 1.23 / 2.4)
    return [(p['moq'], b), (p['moq'] * 4, r05(b * .92)), (p['moq'] * 16, r05(b * .85))]


# img = asset id in proposals/assets/manifest.json ; temp = stand-in photo (badge "Foto temporária")
P = [
    dict(sku='LB-1001', name='Anel Pavé Dourado', fam='aneis', cats=['aneis'], mats=['ouro18', 'zirconia'], aud=['mulher'], occ=['festa', 'noiva'], style='classico',
         pvp=24.90, moq=6, img='legacy/hero-ouro-p', badge='Novo', size='Aro ajustável',
         alt='Anel pavé com banho de ouro 18K pousado sobre pedras brancas',
         desc='Anel com banho de ouro 18K e zircónias em pavé. O aro ajustável resolve todos os tamanhos com uma só referência.',
         specs=[('Material', 'Banho de ouro 18K'), ('Pedras', 'Zircónias em pavé'), ('Medida', 'Aro ajustável')]),
    dict(sku='LB-1002', name='Colar Corrente Fina Dourada', fam='colares', cats=['colares'], mats=['ouro18'], aud=['mulher'], occ=['dia'], style='minimal',
         pvp=18.00, moq=6, img='legacy/colar-topazio-p', badge='Novo', size='45 cm + 5 cm de extensor',
         alt='Corrente fina com banho de ouro 18K sobre um disco de vidro',
         desc='Corrente fina com banho de ouro 18K. A peça base que se usa sozinha ou em camadas.',
         specs=[('Material', 'Banho de ouro 18K'), ('Comprimento', '45 cm + 5 cm de extensor'), ('Fecho', 'Mosquetão')]),
    dict(sku='LB-1003', name='Argolas Largas Polidas', fam='brincos', cats=['brincos'], mats=['ouro18'], aud=['mulher'], occ=['dia', 'festa'], style='moderno',
         pvp=15.50, moq=6, img='legacy/argolas-pave-p', size='Ø 25 mm',
         alt='Dois pares de argolas largas polidas com banho de ouro 18K',
         desc='Argolas largas de superfície polida, com banho de ouro 18K. Diâmetro de 25 mm e fecho de clique.',
         specs=[('Material', 'Banho de ouro 18K'), ('Diâmetro', '25 mm'), ('Fecho', 'Clique')]),
    dict(sku='LB-1004', name='Conjunto Brincos e Pulseira', fam='conjuntos', cats=['pulseiras', 'brincos'], mats=['ouro18', 'zirconia'], aud=['mulher'], occ=['festa'], style='classico',
         pvp=29.90, moq=3, img='legacy/pulseira-rosa-p', size='2 peças',
         alt='Pulseiras de corrente com pendentes e argolas douradas num tabuleiro de vidro',
         desc='Conjunto de brincos e pulseira com banho de ouro 18K, com caixa de oferta incluída. Vende-se como presente pronto.',
         specs=[('Material', 'Banho de ouro 18K'), ('Composição', '2 peças'), ('Embalagem', 'Caixa de oferta incluída')]),
    dict(sku='LB-1005', name='Colares Olho Grego — Mix', fam='colares', cats=['colares'], mats=['banho'], aud=['mulher'], occ=['dia', 'fe'], style='vintage',
         pvp=12.50, moq=12, img='legacy/cat-colares-p', badge='Best seller', size='Sortido por caixa',
         alt='Taça com colares dourados e contas olho grego azuis',
         desc='Colares com banho de ouro e contas olho grego, em sortido por caixa. Muito procurado em zonas de turismo.',
         specs=[('Material', 'Banho de ouro'), ('Contas', 'Olho grego'), ('Venda', 'Sortido por caixa')]),
    dict(sku='LB-1006', name='Brincos de Pérola Clássicos', fam='brincos', cats=['brincos'], mats=['perola', 'aco'], aud=['mulher', 'crianca'], occ=['noiva', 'dia'], style='classico',
         pvp=9.99, moq=12, img='legacy/brincos-safira-p', size='Argola pequena',
         alt='Brincos de argola com pérola pendente sobre tabuleiro branco',
         desc='Pequenas argolas com pérola pendente, em base de aço 316L. Um clássico que roda o ano inteiro.',
         specs=[('Material', 'Pérola sintética, base aço 316L'), ('Medida', 'Argola pequena'), ('Fecho', 'Tarraxa de pressão')]),
    dict(sku='LB-1007', name='Anéis Zircónia Cor — Série 7', fam='aneis', cats=['aneis'], mats=['ouro18', 'zirconia'], aud=['mulher'], occ=['festa'], style='moderno',
         pvp=19.90, moq=7, img='legacy/hero-still-p', size='Série de 7 cores',
         alt='Sete anéis dourados com zircónias de cores diferentes alinhados',
         desc='Série de sete anéis com zircónia de cor, com banho de ouro 18K. Mínimo de uma série completa.',
         specs=[('Material', 'Banho de ouro 18K'), ('Pedras', 'Zircónias de cor'), ('Venda', 'Série de 7 cores')]),
    dict(sku='LB-1008', name='Relógio Bracelete Milanesa', fam='relogios', cats=['relogios'], mats=['aco'], aud=['mulher', 'homem'], occ=['dia'], style='minimal',
         pvp=39.00, moq=3, img='legacy/cat-relogios-p', size='Caixa em aço',
         alt='Relógio com bracelete milanesa em aço sobre uma carteira de pele',
         desc='Relógio de quartzo com caixa em aço e bracelete milanesa. Mostrador limpo, para homem e mulher.',
         specs=[('Caixa', 'Aço'), ('Bracelete', 'Milanesa'), ('Movimento', 'Quartzo')]),
    dict(sku='LB-1009', name='Fio com Cruz — Homem', fam='colares', cats=['colares', 'homem'], mats=['ouro18'], aud=['homem'], occ=['fe', 'dia'], style='classico',
         pvp=22.00, moq=6, img='legacy/cat-homem-p', size='60 cm',
         alt='Fio dourado com pendente em cruz sobre t-shirt branca',
         desc='Fio com pendente em cruz, com banho de ouro 18K. Comprimento de 60 cm, usado por cima ou por baixo da camisola.',
         specs=[('Material', 'Banho de ouro 18K'), ('Pendente', 'Cruz'), ('Comprimento', '60 cm')]),
    dict(sku='LB-1010', name='Brincos Mármore Banho de Ouro', fam='brincos', cats=['brincos'], mats=['ouro18'], aud=['mulher'], occ=['festa'], style='moderno',
         pvp=27.50, moq=6, img='legacy/cat-brincos-p', badge='Exclusivo', size='Discos de resina',
         alt='Brincos de discos efeito mármore com topo dourado sobre pelo claro',
         desc='Discos de resina efeito mármore com topo em banho de ouro 18K. Grandes à vista, leves na orelha.',
         specs=[('Material', 'Resina efeito mármore, banho de ouro 18K'), ('Formato', 'Discos sobrepostos'), ('Fecho', 'Tarraxa')],
         lowres=True),
    dict(sku='LB-1011', name='Anéis Finos Lisos — Par', fam='aneis', cats=['aneis'], mats=['ouro18'], aud=['mulher'], occ=['dia', 'noiva'], style='minimal',
         pvp=12.75, moq=6, img='legacy/cat-aneis-p', size='Par',
         alt='Dois anéis finos lisos dourados entre seixos brancos',
         desc='Par de anéis lisos e finos com banho de ouro 18K, feitos para empilhar.',
         specs=[('Material', 'Banho de ouro 18K'), ('Venda', 'Par'), ('Acabamento', 'Polido')]),
    dict(sku='LB-1012', name='Anel Script “Love”', fam='aneis', cats=['aneis'], mats=['ouro18'], aud=['mulher', 'crianca'], occ=['dia'], style='moderno',
         pvp=14.90, moq=6, img='legacy/cat-pulseiras-p', size='Aro ajustável',
         alt='Anel dourado com a palavra love em letra manuscrita sobre malha de lã',
         desc='Anel com a palavra “love” em letra manuscrita, com banho de ouro 18K. Aro ajustável.',
         specs=[('Material', 'Banho de ouro 18K'), ('Medida', 'Aro ajustável'), ('Detalhe', 'Letra manuscrita')]),
    dict(sku='LB-1013', name='Corrente Cubana — Homem', fam='colares', cats=['colares', 'homem'], mats=['aco'], aud=['homem'], occ=['dia'], style='moderno',
         pvp=28.00, moq=6, img='legacy/hero-aco-p', size='60 cm · elos de 6 mm',
         alt='Corrente cubana em aço 316L sobre fundo preto',
         desc='Corrente cubana em aço 316L polido, elos de 6 mm. Não escurece nem perde o brilho.',
         specs=[('Material', 'Aço 316L'), ('Comprimento', '60 cm'), ('Elos', '6 mm')]),
    dict(sku='LB-1014', name='Pulseira de Elos — Homem', fam='pulseiras', cats=['pulseiras', 'homem'], mats=['aco'], aud=['homem'], occ=['dia'], style='minimal',
         pvp=21.00, moq=6, img='legacy/hero-aco-p2', temp=True, size='21 cm',
         alt='Fotografia temporária: corrente em aço 316L sobre fundo preto',
         desc='Elos planos em aço 316L escovado, com fecho de joalheiro. 21 cm.',
         specs=[('Material', 'Aço 316L escovado'), ('Comprimento', '21 cm'), ('Fecho', 'Fecho de joalheiro')]),
    dict(sku='LB-1015', name='Anéis Aço Escovado — Pack 3', fam='aneis', cats=['aneis'], mats=['aco'], aud=['mulher', 'homem'], occ=['dia'], style='minimal',
         pvp=12.75, moq=6, img='legacy/cat-aneis-p2', temp=True, size='Pack de 3',
         alt='Fotografia temporária: anéis lisos entre seixos brancos',
         desc='Três aros lisos em aço 316L com acabamento escovado, em larguras diferentes.',
         specs=[('Material', 'Aço 316L escovado'), ('Venda', 'Pack de 3'), ('Larguras', 'Três diferentes')]),
    dict(sku='LB-1016', name='Pulseira Tennis Zircónia', fam='pulseiras', cats=['pulseiras'], mats=['ouro18', 'zirconia'], aud=['mulher'], occ=['festa', 'noiva'], style='classico',
         pvp=23.00, moq=6, img='legacy/pulseira-rosa-p2', temp=True, size='18 cm',
         alt='Fotografia temporária: pulseiras douradas num tabuleiro de vidro',
         desc='Fiada contínua de zircónias em base com banho de ouro 18K. 18 cm.',
         specs=[('Material', 'Banho de ouro 18K'), ('Pedras', 'Zircónias'), ('Comprimento', '18 cm')]),
    dict(sku='LB-2001', name='Taça de Madeira para Montra', fam='loja', cats=['loja'], mats=[], aud=[], occ=[], style='minimal',
         pvp=14.00, moq=4, img='legacy/cat-loja-p', size='Madeira',
         alt='Taça de madeira com pulseiras e anéis dourados sobre fundo claro',
         desc='Taça em madeira para expor anéis, brincos e pulseiras ao balcão.',
         specs=[('Material', 'Madeira'), ('Uso', 'Balcão e montra')], lowres=True),
    dict(sku='LB-2002', name='Relógio + Braceletes Intercambiáveis', fam='relogios', cats=['relogios', 'homem'], mats=['aco'], aud=['homem', 'mulher'], occ=['dia'], style='moderno',
         pvp=34.00, moq=3, img='legacy/cat-moda-p', temp=True, size='2 braceletes',
         alt='Fotografia temporária: relógio com bracelete de pele e acessórios sobre fundo castanho',
         desc='Caixa em aço com duas braceletes de troca rápida. Um relógio, dois estilos.',
         specs=[('Caixa', 'Aço'), ('Braceletes', '2, troca rápida'), ('Movimento', 'Quartzo')]),
    dict(sku='LB-2003', name='Kit de Embalagem Kraft', fam='loja', cats=['loja'], mats=[], aud=[], occ=[], style='minimal',
         pvp=8.50, moq=10, img='legacy/cat-loja-p2', temp=True, size='Pack de 10',
         alt='Fotografia temporária: pulseiras e renda sobre fundo claro',
         desc='Saco, caixa e cartão em kraft e algodão, em packs de 10. Para fechar a venda ao balcão.',
         specs=[('Composição', 'Saco + caixa + cartão'), ('Material', 'Kraft e algodão'), ('Venda', 'Pack de 10')]),
]
for p in P:
    p.setdefault('temp', False); p.setdefault('badge', None); p.setdefault('lowres', False)
    p['band'] = band(p['pvp'])
BY = {p['sku']: p for p in P}
FEATURED = ['LB-1013', 'LB-1001', 'LB-1003', 'LB-1009', 'LB-1002', 'LB-1006', 'LB-1007', 'LB-1010']

CATS = {
    'aneis': dict(title='Anéis', lede='Do aro fino para empilhar ao pavé de zircónias, em banho de ouro 18K e aço 316L. Aros ajustáveis para vender sem gerir tamanhos.',
                  imgs=['legacy/hero-ouro-p', 'mj/mj-g2-0-s']),
    'brincos': dict(title='Brincos', lede='Argolas, pérola e peças de festa. A família que mais roda ao balcão, com mínimos a partir de 6 unidades.',
                    imgs=['legacy/cat-brincos-l', 'legacy/argolas-pave-p']),
    'colares': dict(title='Colares', lede='Correntes base, medalhas, olho grego e a linha homem. Comprimentos indicados em cada referência.',
                    imgs=['legacy/colar-topazio-p', 'mj/mj-g3-2-s']),
    'pulseiras': dict(title='Pulseiras', lede='Correntes com pendentes, tennis de zircónia e elos em aço para homem.',
                      imgs=['legacy/pulseira-rosa-p', 'mj/mj-g5-1-t']),
    'relogios': dict(title='Relógios', lede='Caixas em aço, bracelete milanesa e braceletes de troca rápida, para homem e mulher.',
                     imgs=['legacy/cat-moda-l', 'legacy/cat-relogios-p']),
    'homem': dict(title='Homem', lede='Correntes cubanas, fios com cruz, elos e relógios. Aço 316L e banho de ouro 18K que aguentam o uso diário.',
                  imgs=['legacy/cat-homem-v', 'mj/mj-g4-0-w']),
    'loja': dict(title='Loja & montra', lede='Expositores, taças e embalagem na mesma encomenda que as peças — para a montra estar pronta no dia em que chega.',
                 imgs=['legacy/cat-loja-l', 'mj/mj-g7-3-t']),
}

MAT_TILES = [  # (key, image, line)
    ('aco', 'mj/mj-g5-0-t', 'Não escurece, aguenta água e suor.'),
    ('ouro18', 'mj/mj-g5-1-t', 'A cor e o brilho do ouro, a preço de revenda.'),
    ('banho', 'legacy/cat-colares-p', 'Peças de rotação rápida e preço de entrada.'),
    ('perola', 'legacy/brincos-safira-p', 'O clássico de noiva e de todos os dias.'),
    ('zirconia', 'legacy/hero-still-p', 'Brilho de festa, em série de cores.'),
]
AUD_TILES = [
    ('mulher', 'legacy/anel-solitario-p', 'Anéis, brincos e colares para o dia e para a festa.'),
    ('homem', 'legacy/hero-aco-v', 'Aço 316L, cruz e relógio.'),
    ('crianca', 'legacy/cat-pulseiras-p', 'Pérolas pequenas e anéis ajustáveis.'),
]

CHAPTERS = [
    dict(no='01', key='Matéria', title='Aço inoxidável', em='316L', img='mj/mj-g5-0-w', alt='Elos de corrente em aço polido, em grande plano',
         text='A liga das caixas de relógio. Não escurece com o uso diário, aguenta água, suor e perfume — peças que continuam bonitas muito depois de saírem da sua loja.',
         data=['Liga · AISI 316L', 'Acabamentos · polido · escovado'], link=('#colecoes?mat=aco', 'Ver peças em aço 316L')),
    dict(no='02', key='Banho', title='Banho de', em='ouro 18K', img='mj/mj-g5-1-w', alt='Corrente cubana dourada em grande plano, desfocada nas pontas',
         text='Uma camada de ouro 18K dá a cor e o brilho do ouro a peças com preço de revenda. Anéis, argolas, correntes e conjuntos de oferta.',
         data=['342 referências', 'Ficha técnica por referência'], link=('#colecoes?mat=ouro18', 'Ver peças em banho de ouro 18K')),
    dict(no='03', key='Na pele', title='Feito para', em='se usar', img='mj/mj-g2-1-w', alt='Mão com anel fino encostada ao pescoço com um fio delicado',
         text='Anéis, brincos e colares passam o dia em contacto com a pele. Partilhamos a informação de materiais de cada referência com quem a vende.',
         data=['Ficha técnica a pedido', 'Informação por referência'], link=('#jornal-na-pele', 'Ler: banho de ouro na pele')),
    dict(no='04', key='Montra', title='Pronto', em='a expor', img='mj/mj-g7-3-w', alt='Expositor em T com corrente, tabuleiros de veludo e bloco de pedra',
         text='Expositores, taças e embalagem na mesma encomenda que as peças. Reposição por referência, sem esperar pela próxima coleção.',
         data=['Expositores · tabuleiros', 'Embalagem kraft'], link=('#loja', 'Ver loja & montra')),
]

HERO = [  # dark home hero frames
    dict(img='legacy/hero-aco-v', kind='v', cap='Nº 01 · Corrente cubana · Aço 316L', sku='LB-1013',
         sub='Corrente cubana em aço 316L. Não escurece, não perde o brilho — a peça que a sua montra repõe todos os meses.'),
    dict(img='legacy/cat-homem-v', kind='v', cap='Nº 02 · Fio com cruz · Banho de ouro 18K', sku='LB-1009',
         sub='Fio com cruz em banho de ouro 18K. A linha Homem, com mínimos por referência que cabem em qualquer loja.'),
    dict(img='mj/mj-g3-2-w', kind='w', cap='Nº 03 · Corrente sobre basalto', sku=None, ai=True,
         sub='Banho de ouro 18K: a cor e o brilho do ouro, em 342 referências com preço de revenda.'),
    dict(img='mj/mj-g4-0-w', kind='w', cap='Nº 04 · Malha cubana fina', sku=None, ai=True,
         sub='Do fio fino à malha cubana: 486 referências em aço 316L, a linha de maior rotação do catálogo.'),
]
LIGHT_HERO = [
    dict(img='legacy/hero-ouro-p', sku='LB-1001'), dict(img='legacy/colar-topazio-p', sku='LB-1002'),
    dict(img='legacy/argolas-pave-p', sku='LB-1003'), dict(img='legacy/brincos-safira-p', sku='LB-1006'),
]

CUSTOMERS = [
    dict(id='online', tab='Revendedor online', img='mj/mj-g3-1-s', alt='Corrente de elos alongados dourada sobre pedra escura',
         title='Fotografias prontas para publicar', text='Tem uma página no Instagram ou Facebook, ou uma loja online? Damos-lhe catálogo fotográfico e preços com margem para vender desde o primeiro dia.',
         points=['Catálogo fotográfico por referência', 'Exportação CSV de cada pedido', 'Mínimos por referência, não por encomenda']),
    dict(id='fisica', tab='Loja física', img='mj/mj-g2-0-s', alt='Mão com dois anéis finos dourados',
         title='Reposição sem parar a montra', text='Reposição semanal, expositores e embalagem na mesma fatura — e visita acompanhada ao showroom.',
         points=['Novidades e reposições todas as semanas', 'Expositores e embalagem na mesma encomenda', 'Visita ao showroom com marcação']),
    dict(id='novo', tab='Novo negócio', img='mj/mj-g1-0-s', alt='Rua com montra iluminada ao anoitecer',
         title='Abrir com o sortido certo', text='Está a pensar começar um negócio de bijuteria? Kits de arranque com mínimos reduzidos e conselhos sobre o que roda melhor em loja.',
         points=['Kits de arranque com mínimos reduzidos', 'Sortido montado a partir do que já roda', 'Acompanhamento comercial']),
]

STEPS = [  # [v17 empresa.html]
    ('01', 'Criar conta', 'Registo com NIF e dados da empresa — cinco minutos.'),
    ('02', 'Validação', 'Confirmamos a atividade comercial — em regra, num dia útil.'),
    ('03', 'Preços por grosso', 'Catálogo completo, mínimos e escalões, encomenda por referência.'),
]
GUARANTEES = [  # [v17 empresa.html]
    ('Empresa registada em Portugal', 'Fatura com IVA em todas as encomendas e Livro de Reclamações eletrónico.'),
    ('Showroom físico visitável', 'Um espaço de exposição real em Vila do Conde, com equipa que acompanha a escolha.'),
    ('Pagamentos que já usa', 'MB Way, Multibanco, transferência bancária, cartão e PayPal.'),
    ('Preços protegidos', 'O catálogo é fechado ao público e cada conta é validada: o seu preço não fica exposto à concorrência.'),
]

ARTICLES = [
    dict(id='jornal-aco-316l', tag='Matéria', title='Aço 316L: porque não escurece', read='4 min',
         cover='mj/mj-g5-0-w', cover_alt='Elos de corrente em aço polido, em grande plano',
         lede='O que dizer ao cliente que pergunta se a peça “vai ficar preta”. E porque é que o 316L é a base mais segura de uma montra.',
         body=[
             ('p', 'O aço inoxidável 316L é uma liga de ferro com crómio, níquel e molibdénio. O crómio forma na superfície uma película invisível que protege o metal; o molibdénio reforça essa proteção contra o sal e o cloro. É por isso que o 316L é usado em caixas de relógio e em ambientes húmidos.'),
             ('h', 'Três frases para o balcão'),
             ('ul', ['Não escurece com o uso diário.', 'Pode ir à água e aguenta o suor.', 'Limpa-se com um pano macio — não precisa de produtos.']),
             ('img', 'legacy/hero-aco-p', 'Corrente cubana em aço 316L sobre fundo preto', 'LB-1013 · Corrente Cubana — Homem'),
             ('p', 'Na nossa linha, o aço 316L aparece polido ou escovado, e é também a base das peças de pérola. A ficha técnica de cada referência está disponível a pedido.'),
         ]),
    dict(id='jornal-montra', tag='Montra', title='Cinco regras para uma montra que vende', read='5 min',
         cover='mj/mj-g7-3-w', cover_alt='Expositor em T com corrente, tabuleiros de veludo e bloco de pedra',
         lede='Uma montra não precisa de mais peças; precisa de menos, bem arrumadas. Cinco regras que qualquer loja aplica numa tarde.',
         body=[
             ('ol', ['Uma cor de fundo por montra: veludo escuro para o dourado, pedra clara para o aço.', 'Três alturas — tabuleiro, busto e expositor em T — para o olhar não ficar parado.', 'Uma peça-herói à altura dos olhos, com espaço à volta.', 'Preços visíveis mas discretos: etiqueta pequena, sempre no mesmo sítio.', 'Trocar a montra quando entra a reposição semanal, não quando “parece velha”.']),
             ('img', 'mj/mj-g7-0-s', 'Expositor em T dourado sobre base de pedra com tabuleiros de veludo', None),
             ('p', 'Os expositores, tabuleiros e a embalagem podem ir na mesma encomenda que as peças — a montra fica pronta no dia em que a caixa chega.'),
             ('img', 'mj/mj-g1-2-s', 'Rua histórica ao anoitecer com uma montra iluminada ao fundo', None),
             ('img', 'mj/mj-g7-1-t', 'Tabuleiros de veludo preto com brincos, iluminados de cima', None),
         ]),
    dict(id='jornal-embalagem', tag='Embalagem', title='Embalagem: a última impressão', read='3 min',
         cover='mj/mj-g6-0-s', cover_alt='Caixa rígida preta aberta com interior de cetim e pulseira',
         lede='A peça vende-se na montra; a cliente volta por causa da caixa. Como escolher embalagem sem pesar na margem.',
         body=[
             ('p', 'Para peças de entrada, um saco de papel kraft e um cartão simples bastam. Para conjuntos e peças acima de 25 € de PVP, uma caixa rígida transforma a compra numa oferta.'),
             ('img', 'mj/mj-g6-1-s', 'Caixa rígida preta com pulseira sobre cetim, vista de lado', None),
             ('img', 'mj/mj-g6-3-t', 'Caixa aberta com interior dourado e pulseira enrolada', None),
             ('p', 'Seja qual for a escolha, a embalagem deve ser igual em toda a loja: é ela que o cliente leva para casa e mostra a quem recebe a oferta.'),
             ('img', 'legacy/pendente-halo-p', 'Caixa de oferta aberta com colar de inicial, pétalas e rosa seca', 'Fotografia temporária: a caixa mostra a marca de outra empresa e será substituída.'),
         ]),
    dict(id='jornal-na-pele', tag='Na pele', title='Banho de ouro na pele: o que dizer ao cliente', read='4 min',
         cover='mj/mj-g2-1-w', cover_alt='Mão com anel fino encostada ao pescoço com um fio delicado',
         lede='Como explicar em trinta segundos a diferença entre banho de ouro e ouro maciço — e como a peça dura mais tempo bonita.',
         body=[
             ('p', 'Banho de ouro é uma camada de ouro aplicada sobre uma base metálica. A cor é a do ouro; a estrutura é a da base, indicada na ficha técnica de cada referência.'),
             ('img', 'mj/mj-g2-1-t', 'Mão com anel fino encostada ao pescoço com um fio delicado', None),
             ('h', 'Para durar mais tempo bonita'),
             ('ul', ['Pôr o perfume e o creme antes da peça, não depois.', 'Tirar para a piscina e para o mar.', 'Guardar cada peça numa bolsa, sem tocar nas outras.']),
             ('img', 'mj/mj-g2-3-s', 'Mão encostada ao pescoço com fio fino, em luz baixa', None),
         ]),
]

FAQ = [
    ('Conta e acesso', [
        ('Quem pode comprar na LM BIJU?', 'Só profissionais: lojas físicas, revendedores online e quem está a abrir um negócio. Pedimos o NIF da empresa ou da atividade para validar a conta.'),
        ('Quanto tempo demora a validação?', 'Em regra, um dia útil. Recebe a confirmação por e-mail e passa a ver preços, mínimos e escalões no catálogo.'),
        ('Posso ver o catálogo antes de ter conta?', 'Sim. As peças, as referências e o PVP recomendado estão abertos a todos; só o preço de revenda fica reservado a contas validadas.'),
    ]),
    ('Preços e mínimos', [
        ('Há um valor mínimo de encomenda?', 'Os mínimos são por referência (por exemplo, 6 unidades ou uma série completa), não por encomenda. Cada ficha de produto indica o seu.'),
        ('Como funcionam os escalões?', 'Cada referência tem três escalões de preço: o mínimo, quatro vezes o mínimo e dezasseis vezes o mínimo. Quanto maior a quantidade, menor o preço por unidade.'),
        ('O PVP recomendado é obrigatório?', 'Não. É uma referência para o preço de venda ao público, com IVA incluído, e ajuda a calcular a sua margem.'),
    ]),
    ('Pagamento e faturação', [
        ('Que métodos de pagamento aceitam?', 'MB Way, Multibanco, transferência bancária, cartão e PayPal.'),
        ('A fatura inclui IVA?', 'Sim, todas as encomendas são faturadas com IVA, com os dados da empresa registados na conta.'),
    ]),
    ('Envio e showroom', [
        ('De onde são enviadas as encomendas?', 'De Vila do Conde, a partir do nosso stock próprio. O prazo é indicado em cada proposta, de acordo com o stock das referências.'),
        ('Posso visitar o showroom?', 'Sim, com marcação, de segunda a sexta, das 09h00 às 18h30. Preparamos as famílias que lhe interessam antes de chegar.'),
        ('Posso pedir proposta para muitas referências de uma vez?', 'Sim. No Pedido de proposta pode colar uma lista de referências e quantidades ou importar um ficheiro CSV.'),
    ]),
]

ACCOUNT_DEMO = dict(
    company='Bijuteria Atlântico, Lda.',  # fictitious demo account
    nif='501964843',
    orders=[('LB-24-0198', 'Entregue', 18, 214.60), ('LB-24-0211', 'Em preparação', 24, 318.20), ('LB-24-0230', 'Proposta enviada', 42, 506.40)],
    favourites=['LB-1013', 'LB-1003', 'LB-1006', 'LB-1002'],
)
