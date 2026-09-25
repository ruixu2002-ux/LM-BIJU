# 竞品页面结构对比 + LM BIJU 页面结构方案

> 证据来源：你上传的四家截图包，分析见 `_research/<竞品>/analysis.md`：Shebiju 14 张、Cellibiju 7 张、Grupobelle 30 张、Maxbiju 9 张。竞品网站本身在这个环境里访问不了（代理返回 403），所以下文只写截图里看得到的内容。
> 标注说明：
> - **✓**：截图里直接看到这一页
> - **链接**：只在页脚或菜单里看到入口，页面本身没截到（**推测**存在）
> - **—**：截图范围内没有看到

## 1. 四家各有哪些页面

| 页面 | Shebiju | Cellibiju | Grupobelle | Maxbiju |
|---|---|---|---|---|
| 首页 | ✓ 01–05 | ✓ 01–04 | ✓ 01–06 | ✓ 01–04 |
| 品类落地页（先讲再卖） | — | — | ✓ BijuBelle 09–16、Malabelle 28–29、Acessórios Moda 26 | — |
| 分类列表 PLP | ✓ Aço › Colares 11–13 | 链接 `/collections/aneis`（02 状态栏） | ✓ Anéis 17–18、22–23；Acessórios para Loja 25；Acessórios Moda 27 | ✓ Rings 05–06；Window Stand 07 |
| 系列 / Coleções 总览 | — | 首页区块"Coleções"（02–03） | ✓ Coleções 页 24（下拉 16 项平铺） | — |
| 新品聚合 | 导航 NOVIDADES | 导航 NOVIDADES › Nova Coleção / Reposição（06） | 首页按钮 Novos Produtos / Best Sellers（03） | ✓ NEWS 页 08 |
| 产品详情 PDP | — | — | ✓ 19–21 | — |
| 关于 | 链接（页脚 MAIS INFORMAÇÃO，04） | 链接"Quem somos?"（05） | 首页有公司简介段落（05、06） | — |
| 门店 / Showroom | — | 首页区块"As Nossas Lojas"：Porto、Lisboa（03） | 首页区块"As nossas lojas"，带视频（04） | — |
| 联系 | 页脚 FALE CONNOSCO：WhatsApp、WeChat（04） | — | 页脚联系方式（06） | 页脚电话和邮箱（03） |
| 登录 | ✓ 与注册同页 `login.php?l=1`（10） | ✓ "Início de Sessão"（07） | ✓ "Inicie sessão na sua conta"（30） | ✓ Returning / New Customer（09） |
| 注册 | ✓ 同上（只截到部分字段） | 链接"Como Registar?"、"Registar"（05） | 首页"Criar conta de cliente"（05） | 链接 New Customer → CONTINUE（09） |
| 门禁弹窗 | ✓ AVISO 弹窗（14） | — | PDP 内嵌登录条（19） | — |
| 购物车 | 图标 | 图标 | 图标 👜0（01） | — |
| FAQ / 购买指南 | — | — | — | 链接 FAQ、Purchase Guide（03） |
| 博客 / 内容 | 链接：SEO 文章"Bijuterias em aço""Acessórios de Moda: Pequenos Detalhes, Grandes Vendas"（04） | — | — | — |
| 询价 RFQ | — | — | — | — |
| 客户账户（登录后） | 链接 ÁREA PESSOAL（04），登录后的页面没截到 | 链接 Área Pessoal（05） | — | 面包屑 Account（09） |

**结论**：
- 四家都没有**询价（RFQ）**。
- 截图里没有任何一家展示过**登录后的账户页**。
- 只有 Grupobelle 截到了**产品详情页**。
- 只有 Grupobelle 有"先讲故事再卖货"的品类落地页。

所以 LM BIJU 的差异化空间在：询价、账户、产品详情里的 B2B 信息、品类落地页。

## 2. 每家的结构特点

### Shebiju（14 张截图）
- **主导航 10 项（01）**：AÇO / HOMEM / RELÓGIOS / ACESSÓRIOS DE LOJA / ACESSÓRIOS DE MODA / BIJUTERIA / HALLOWEEN / HALO BY ME / PROMOÇÕES / NOVIDADES。**材质、人群、品类、季节、自有品牌、促销六种分类维度混在同一排**。
- **子页面**：
  - 下拉都是 500px 宽的单列。AÇO 带橙色"NOVIDADE!"标签（06）；RELÓGIOS 只有 1 项"Relógios Mulher"（08）。
  - ACESSÓRIOS DE LOJA 下有 6 个子类：Autocolantes、Embalagens、Etiquetas & Pinos、Expositores、Guarda Jóias、Sacos Embrulho（09）。
- **PLP**：面包屑 HOME › AÇO › COLARES，左侧手风琴带数量（Ver todos 893 / Brilhantes 151…），3 列卡片只有名称 + SKU（11）。
- **副标题模式**：
  - Hero：两行 H1"UM SÓ LUGAR. TODOS OS ESTILOS." + 一句对象说明"Para lojistas, revendedores e profissionais da área" + CRIAR CONTA + 3 个数字（+20 MIL / MAIOR / +15 MIL）。
  - 品类图只有标签，没有副标题；PLP 只有 H1，没有描述。
- **门禁**：用弹窗（14），不在页面里说明注册的好处。

### Cellibiju（7 张截图，推测是 Shopify）
- **主导航**：两行 10 项；NOVIDADES 下分 Nova Coleção / Reposição（06），这是懂"补货"的分法。
- **首页区块顺序**：Hero"Bijuteria para Revenda" → "Coleções"网格（Anéis / Brincos / Colares / Pulseiras / Colares de Aço sem medalhas / Medalhas de Aço，02–03）→ "As Nossas Lojas"（Porto、Lisboa、每天 10:00–19:00、Obter Direções）→ 品牌介绍（04）。
- **页脚 4 列（05）**：Sobre nós / Informações / Mapa do Site / Área Pessoal，里面有"Quem somos?""Como Registar?"。
- **副标题模式**：Hero 副标题"Registe-se para ver os preços…"（B2B 门禁写进副标题），CTA 只是模糊的"Saiba mais"。
- **分类逻辑**：按品类，并按材质或有无吊坠做子线（"Colares de Aço sem medalhas"）。

### Grupobelle（30 张截图，推测是 PrestaShop）
- **两个事业部当一级导航**：BIJUBELLE（首饰）、MALABELLE（包袋），再加 FIM DE STOCK、ACESSÓRIOS MODA 等（01、07、08）。
- **品类落地页（09–16），结构是整个竞品里最完整的**：面包屑 → 横幅 → 手写标语 → 介绍段落 → "Comprar por Categoria" → "Destaques da Temporada" → "Comprar por Coleção" → "Catálogo BijuBelle" + 子类按钮 → B2B 门禁段落 + 注册按钮。
- **PLP（17、22、23）**：
  - H1 + 子类按钮 + "Existem 282 produtos." + 排序 + 4 列 + NOVO 角标。
  - 分页"Mostrando 1-24 de um total de 282 artigo(s)"。
- **PDP（19–21）**：标题 → REF → PVPR 30,00 € → 登录提示条 → 尺码 → B2B 框（Entrar / Registar）→ "Dados do produto"手风琴 → "Ficha informativa"（Metal）→ 信任条。
- **副标题模式**：Hero 是**活动名**（"– NOVA COLEÇÃO – AZULEJO PORTUGUÊS"），没有 CTA；每个区块是"金色区块标题 + 图块"。
- **分类逻辑**：事业部 → 品类 → 系列（Eternity、BeloveBelle、GB Festa、Encanto Portugal、Prestige）→ 材质（Moissanite、Zircónias）；另有 Novos Produtos / Best Sellers / Fim de stock，新客户有"Kit de Iniciação - 10 peças"（17）。

### Maxbiju（9 张截图，英文界面，推测是 OpenCart）
- **主导航 8 项（01、05）**：HOME / JEWELRY / FASHION ACC. / ACC.&CRAFTS / WINDOW STAND & PKG / TOOLS / NEWS / PORTUGAL。
- **子页面**：
  - PLP 顶部有子类缩略图（Rings 下是 Steel / Men / Rhodium / Adjustable，05）。
  - 左侧手风琴 + FILTER BY（Search / Subcategory / COLOR 带数量，06）。
  - NEWS 聚合页有 7 个子类缩略图（08）。
- **页脚（03）**：Newsletter、FOLLOW US、3 条服务承诺（Delivery / Secure Payment / Customer Service）、链接条（Complaint Book、Terms、Privacy、FAQ、Purchase Guide）。
- **副标题模式**：首屏**没有**价值主张，只有公告条轮播（"FREE SHIPPING ON PURCHASE OVER 150€" / "EXCLUSIVE FOR PROFESSIONALS (B2B)"）；PLP 只有 H1。
- **分类逻辑**：按品类，子类混着材质和人群（Steel / Men / Rhodium），用颜色做筛选；工具和手工配件单独成类。

## 3. 副标题模式对比

| 位置 | Shebiju | Cellibiju | Grupobelle | Maxbiju | **LM BIJU 采用** |
|---|---|---|---|---|---|
| Hero | 价值主张 + 对象 + CTA + 3 个数字 | 定位 + 门禁说明 + 模糊 CTA | 活动名，无 CTA | 无 | **一句价值主张 + 对象 + 两个 CTA（Ver coleções / Criar conta）+ 帧说明（SKU 链接）** |
| 区块 | 无 | 区块名（"Coleções"） | 金色区块名 | 无 | **idx 小标签（01 — Coleções）+ 大标题 + 1–2 句 lede** |
| 分类页 | H1 | — | H1 + 子类按钮 + 数量 | H1 + 子类缩略图 | **H1 + 品类描述 + 数量 + 子类筛选** |
| 产品页 | — | — | 标题 + REF + PVPR | — | **材质 · 尺寸 · 技术资料说明 + REF + PVP + 起订量** |
| 关于 | — | 品牌介绍段落 | 公司简介 | — | **品牌故事 + 可以证实的数字（v17 的 956 / 342 / 486 / 128 款）** |
| 登录 | 只有标题 | 只有标题 | 面包屑标题 | 平台默认文案 | **注册能得到什么（3 条）+ 两栏：登录 / 创建账户** |

## 4. 内容分类逻辑对比

| 维度 | Shebiju | Cellibiju | Grupobelle | Maxbiju | LM BIJU（v17 已有） |
|---|---|---|---|---|---|
| 品类 | ✓ | ✓ | ✓ | ✓ | ✓ Anéis / Brincos / Colares / Pulseiras / Conjuntos |
| 材质 | AÇO 一级 | 子线 | Moissanite 等 | 子类 | ✓ Aço 316L / Ouro 18K / Banho de ouro / Pérola |
| 人群 | HOMEM | — | — | Men 子类 | ✓ Homem |
| 场合 | HALLOWEEN（季节） | — | GB Festa（系列） | — | — |
| 价格带 | PROMOÇÕES | PROMOÇÕES | FIM DE STOCK | — | ✓ Promoções |
| 风格 | — | — | 系列 | 颜色筛选 | — |
| 店铺耗材 | ✓ 6 个子类 | ✓ | ✓ 216 件 | ✓ | ✓ Expositores / Embalagens / Etiquetas & pinos / Sacos |

**问题**：竞品把好几个维度塞进同一排导航（Shebiju 一排里有六种维度）。
**LM BIJU 的做法**：
- **一级导航只放品类**，另外 5 个维度放进 Coleções 的 mega menu 和筛选里。
- 每个维度在 URL 里有自己的参数，筛选结果可以直接分享。

## 5. LM BIJU 页面结构方案

两个版本（深色、白色）用同一套结构。都是单文件多页面：
- 用 `#路由` 做真实导航，浏览器前进、后退都能用，每页有独立标题。
- 页面切换有转场动画。
- 关闭 JS 时，所有页面按顺序展开显示，关键内容不丢。

| # | 页面 | 路由 | H1 / 副标题模式 | 主要区块 |
|---|---|---|---|---|
| 1 | 首页 | `#inicio` | 价值主张 + 对象 + 2 个 CTA | Hero（4 帧）→ 品类入口 → 材质章节 → 逐帧视频 → 精选 → 客户类型 → Showroom 数字 → 结尾 CTA |
| 2 | 目录总览 Coleções | `#colecoes` | "Coleções" + 覆盖范围 + 总数 | 7 个品类入口 → 按材质 / 人群 / 场合 → 全部产品（6 个维度筛选 + 排序 + 网格/列表） |
| 3 | 分类页 ×7 | `#aneis` `#brincos` `#colares` `#pulseiras` `#relogios` `#homem` `#loja` | 品类名 + 品类描述 + 数量 | 封面图 + 子筛选 + 产品网格 + 编辑图带 + 跳到其它品类 |
| 4 | 产品详情 | `#produto/LB-1003` | 名称 + "材质 · 尺寸 · 技术资料"副标题 | 大图 → REF / PVP / 起订量 → 阶梯价（客户视角）→ 加入询价 → 手风琴 → 同系列 3 款 |
| 5 | 关于 Empresa | `#empresa` | 品牌故事 + 数字 | 三类客户 → 三步开户 → 四项保障 → 数字 → 图片 |
| 6 | Showroom | `#showroom` | 地点 + 预约方式 | 大图 → 地址、营业时间、地图 → 预约表单（生成邮件）→ 环境图 |
| 7 | 询价 RFQ | `#pedido` | "Pedido de proposta" + 流程说明 | 四步进度 → 行项目（起订量校验）→ 粘贴或导入 CSV → 参考图 → 提交（CSV + 邮件 + 编号） |
| 8 | 登录 / 注册 | `#entrar` | 注册能得到什么 | 左：登录（演示账户）；右：创建账户（NIF 校验） |
| 9 | 客户账户 | `#conta` | "A minha conta" + 公司名 | 概览、最近订单（示例数据）、询价单、常购商品、公司资料 |
| 10 | 联系 | `#contactos` | 联系渠道 + 响应方式 | 邮箱 / WhatsApp / 地址 → 联系表单（生成邮件） |
| 11 | 内容 Jornal | `#jornal` + 4 篇文章 `#jornal-...` | "Jornal" + 给零售店主的实用内容 | 文章列表 → 正文（材质、橱窗、包装、佩戴） |
| 12 | FAQ | `#faq` | "Perguntas frequentes" + 分组 | 账户 / 价格与起订量 / 付款与开票 / 发货 / Showroom，每组 3–4 问 |

**导航**：
- 头部：Logo · Coleções（mega menu：品类、材质、人群、场合）· Empresa · Showroom · Jornal · 搜索（可按名称或 SKU 搜）· Entrar / A minha conta · Pedido（数量）。
- 头部单行，桌面端高度 72px。竞品头部要占 150–432px。

**页脚 4 列**：
1. LM BIJU：地址、邮箱、WhatsApp
2. Coleções
3. Área profissional
4. Informação：Empresa / Showroom / Jornal / FAQ / Contactos / Livro de Reclamações

**分类维度（6 个）**：
| 维度 | 取值 |
|---|---|
| 品类 | Anéis / Brincos / Colares / Pulseiras / Relógios / Conjuntos |
| 材质 | Aço 316L / Banho de ouro 18K / Banho de ouro / Pérola / Zircónia |
| 人群 | Mulher / Homem / Criança |
| 场合 | Dia-a-dia / Festa / Noiva / Fé |
| 价格带（按 PVP） | Económico < 12 € / Médio 12–25 € / Premium > 25 € |
| 风格 | Minimalista / Clássico / Moderno / Vintage |

- **"Ouro 18K"改名为"Banho de ouro 18K"**：v17 菜单里写的是"Ouro 18K"，但 v17 的产品描述都是镀层（如"Colecção ouro 18K"，产品是"banho"）。在葡语里单写"Ouro 18K"会被理解成实心金，所以改名，避免误导。这一点属于**推测**：v17 没有写明是不是实心金，需要客户确认。
- **人群、场合、风格的标注是演示用的示例**：v17 没有这些数据，需要客户按真实商品重新标注。
