# LM BIJU 新站 Demo v3 · 交付状态（2026-09-25）

两个完整的多页 Demo：**深色版** `proposals/demo-dark.html` 和 **白色版** `proposals/demo-light.html`。页面结构、内容和数据相同，视觉、布局和动效分别设计。

## 1. 文件
| 文件 | 说明 |
|---|---|
| `proposals/index.html` | 选择页：深色 / 白色 / 一页展示 / 图片一览 |
| `proposals/demo-dark.html` | 深色版完整网站：22 个视图（12 类页面），10 条动效 |
| `proposals/demo-light.html` | 白色版完整网站：22 个视图，4 条动效，不依赖任何 JS 库 |
| `proposals/demo-showcase-dark.html` · `demo-showcase-light.html` | 一页式展示（首页全部区块），链接跳到完整 Demo |
| `proposals/assets/` | 图片（img/legacy、img/mj）、视频帧（video）、字体（fonts，Inter 和 Cormorant，OFL）、vendor（GSAP、ScrollTrigger、Lenis，只有深色版用） |
| `proposals/assets/manifest.json` · `preview.html` | 55 条素材、397 个文件的清单（含每张图用在哪些页面）；预览页可以筛选 |
| `proposals/_build/` | `images.js`（统一图片管道）、`content.py`（数据和文案）、`site.py`（生成 5 个页面、manifest 和 preview）、`pack.py`（离线包）、各版本的 CSS 和 JS |
| `lm-biju-demo-offline.zip` | 离线包，15.3 MB，418 个文件。解压后双击 `index.html` 即可打开 |
| `start-demo.bat` · `start-demo.sh` | 启动本地服务器并打开选择页 |
| `_research/page-structure-comparison.md` | 竞品页面结构分析和我们的页面结构方案 |
| `_research/design-system.md` | 字体、色板、字号、间距、组件、动效规范 |

## 2. 页面（两版相同）
首页 · Coleções（目录总览）· 7 个分类页（Anéis / Brincos / Colares / Pulseiras / Relógios / Homem / Loja & montra）· 产品详情（19 个 SKU，`#produto/LB-xxxx`）· Empresa · Showroom · 询价单 · 登录 / 注册 · 客户账户 · 联系 · Jornal（列表 + 4 篇文章）· FAQ。

- 用 `#路由` 做真实导航：前进和后退都能用；每页有独立 `<title>`；切换页面后焦点移到 H1；有页面转场。
- **关闭 JS 时**：21 个静态视图按顺序全部展开（只有产品详情需要 JS），表单改为通过 mailto 提交。

## 3. 测试结果（Playwright + axe-core 4.x + Lighthouse，Chromium）
| 项 | 深色 | 白色 |
|---|---|---|
| axe 违规：桌面 1440×900，23 个路由 | **0** | **0** |
| axe 违规：手机 390×844，23 个路由 | **0** | **0** |
| 每个路由的图片全部加载成功（桌面和手机） | ✓ | ✓ |
| JS 报错 / 控制台错误 / 4xx 请求 | 0 / 0 / 0 | 0 / 0 / 0 |
| 功能测试 35 项：链接、筛选、排序、URL 同步、列表视图、搜索、起订量校正、灯箱、阶梯价、账户、粘贴清单、CSV、参考图、询价步骤、4 个表单、NIF 校验、周末日期拦截、退出登录、mega 菜单、标签页、浏览器后退 | **35/35** | **35/35** |
| 内部链接（341 个）全部指向存在的页面 | ✓ | ✓ |
| 减少动效：无开场、Hero 不轮播、无固定滚动、无隐藏内容、axe 0 | ✓ | ✓ |
| 关闭 JS：21/21 视图可见，图片 124/124（深色）、125/125（白色），无开场遮罩 | ✓ | ✓ |
| 离线包 file://：5 个页面 0 错误，字体和 GSAP 都能加载，路由和图片正常 | ✓ | ✓ |
| 一页展示：桌面和手机 axe 0，图片全部加载 | ✓ | ✓ |
| **Lighthouse 手机 Performance**（gzip 服务器，等同正式托管） | **98** | **99** |
| Lighthouse 手机 Performance（Python 服务器，不压缩） | 86 | 94 |
| Lighthouse Accessibility / Best Practices | 100 / 100 | 100 / 100 |
| Lighthouse SEO | 63：只扣了 is-crawlable，因为 Demo 故意加了 `noindex`；上线去掉后没有其它扣分项 | 同左 |
| 手机端 LCP / CLS（gzip） | 2.0 s / 0.009 | 2.1 s / 0.001 |

对照：v17 手机端 Accessibility 为 80–88（`_research/evidence/lighthouse-v17-summary.json`）。

## 4. 与四家竞品对比（证据见 `_research/<竞品>/analysis.md`）
| 维度 | 竞品现状（截图证据） | LM BIJU v3 |
|---|---|---|
| 头部占用 | Shebiju 约 290–307px；Cellibiju 432px（占视口 41%）；Grupobelle 约 150px | 单行 72px，手机 60px |
| 搜索 | Shebiju 只有约 85px 宽的文本框；其余三家截图里没有 SKU 搜索 | 全站搜索框，支持 SKU、名称、材质、品类 |
| 列表页的 B2B 信息 | Shebiju、Maxbiju 卡片只有名称 + SKU；Grupobelle 只有"Ver detalhes" | 卡片显示 PVP、锁价提示或阶梯起价、起订量，可以直接加入询价 |
| 筛选 | Shebiju 只有侧栏分类；Maxbiju 有子类 + 颜色；Grupobelle 只有排序 | 6 个维度（品类、材质、人群、场合、价格带、风格）+ 排序 + 网格/列表，筛选写进 URL |
| 询价（RFQ） | 四家都没有 | 有：粘贴清单、导入 CSV、导出 CSV、编号、进度条 |
| 客户账户 | 四家截图都没有登录后的页面 | 有：订单、询价单、常购商品、一键再下单 |
| 门禁方式 | Shebiju 用 Bootstrap 警告弹窗 | 页面里直接显示锁价提示，加一键演示登录 |
| 对比度 | Shebiju 1.97:1 和 2.26:1；Grupobelle 金色 2.62:1；都不达标 | axe 0 违规，最低 4.5:1 |
| 字体 | Montserrat 混 Arial（Shebiju）；系统字体（Cellibiju）；Lato（Maxbiju） | Inter 贯穿全站，价格和 SKU 用等宽数字 |
| 动效 | 截图里只看到轮播 | 深色版 10 条、白色版 4 条，都遵守减少动效设置 |

## 5. 图片使用（53 个图片资产 + 48 帧 + 视频，两版都真实使用）
- **LM BIJU 实拍**：17 张全部使用，做成 27 个裁切版本。
- **MJ 图**：12 张保留图 + 7 张可接受图全部使用，做成 26 个裁切版本。淘汰的 8 张不用（有结构错误）。
- **48 帧**：深色版随滚动逐帧播放；白色版用滑杆拖动查看；手机上用循环视频。
- **带"Foto temporária"标注的 SKU（用最接近的现有实拍顶上）**：LB-1014、LB-1015、LB-1016、LB-2002、LB-2003。
- **分辨率偏低的真实产品图**：LB-1010（cat-brincos，裁切后 540×675）、LB-2001（cat-loja，480×600）。卡片尺寸下可以用，放大后发软。
- **pendente-halo（盒子上有第三方品牌 Emiza Jewellery）**：只放在 Jornal"Embalagem"一文里，标"Fotografia temporária"，不当作 LM BIJU 的商品。
- **AI 图**：每处都带"Imagem ilustrativa gerada por IA"，只用于氛围、章节和场景，没有一张当产品图。

| 素材 | 类型 | 原图 → 裁切 | 深色版使用位置 | 白色版使用位置 |
|---|---|---|---|---|
| `legacy/hero-aco-v` | 实拍 | 1200x1800 → 1200x1800 | colecoes, inicio | colecoes |
| `legacy/hero-aco-p` | 实拍 | 1200x1800 → 1200x1500 | colecoes, inicio, jornal-aco-316l, 产品页(JS) | colecoes, inicio, jornal-aco-316l, 产品页(JS) |
| `legacy/hero-aco-p2` | 实拍 | 1200x1800 → 1200x1500 | colecoes, 产品页(JS) | colecoes, 产品页(JS) |
| `legacy/cat-homem-v` | 实拍 | 1200x1600 → 1200x1600 | homem, inicio | homem |
| `legacy/cat-homem-p` | 实拍 | 1200x1600 → 1200x1500 | colecoes, inicio, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/hero-ouro-p` | 实拍 | 900x1350 → 900x1125 | aneis, colecoes, inicio, 产品页(JS) | aneis, colecoes, inicio, 产品页(JS) |
| `legacy/colar-topazio-p` | 实拍 | 900x1350 → 900x1125 | colares, colecoes, inicio, 产品页(JS) | colares, colecoes, inicio, 产品页(JS) |
| `legacy/argolas-pave-p` | 实拍 | 900x1200 → 900x1125 | brincos, colecoes, inicio, 产品页(JS) | brincos, colecoes, inicio, 产品页(JS) |
| `legacy/pulseira-rosa-p` | 实拍 | 900x1350 → 900x1125 | colecoes, inicio, pulseiras, 产品页(JS) | colecoes, inicio, pulseiras, 产品页(JS) |
| `legacy/pulseira-rosa-p2` | 实拍 | 900x1350 → 900x1125 | colecoes, 产品页(JS) | colecoes, 产品页(JS) |
| `legacy/cat-colares-p` | 实拍 | 900x1200 → 900x1125 | colecoes, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/brincos-safira-p` | 实拍 | 1200x1200 → 960x1200 | colecoes, inicio, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/hero-still-p` | 实拍 | 900x1125 → 900x1125 | colecoes, inicio, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/cat-relogios-p` | 实拍 | 900x1350 → 900x1125 | colecoes, inicio, relogios, 产品页(JS) | colecoes, inicio, relogios, 产品页(JS) |
| `legacy/cat-aneis-p` | 实拍 | 900x1350 → 900x1125 | colecoes, inicio, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/cat-aneis-p2` | 实拍 | 900x1350 → 900x1125 | colecoes, 产品页(JS) | colecoes, 产品页(JS) |
| `legacy/cat-pulseiras-p` | 实拍 | 900x1109 → 887x1109 | colecoes, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/cat-brincos-p` | 实拍 | 900x675 → 540x675 | colecoes, inicio, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/cat-brincos-l` | 实拍 | 900x675 → 900x600 | brincos | brincos |
| `legacy/cat-loja-p` | 实拍 | 900x600 → 480x600 | colecoes, inicio, 产品页(JS) | colecoes, inicio, 产品页(JS) |
| `legacy/cat-loja-p2` | 实拍 | 900x600 → 480x600 | colecoes, 产品页(JS) | colecoes, 产品页(JS) |
| `legacy/cat-loja-l` | 实拍 | 900x600 → 900x600 | inicio, loja | inicio, loja |
| `legacy/cat-moda-p` | 实拍 | 900x506 → 405x506 | colecoes, 产品页(JS) | colecoes, 产品页(JS) |
| `legacy/cat-moda-l` | 实拍 | 900x506 → 759x506 | relogios | relogios |
| `legacy/anel-solitario-v` | 实拍 | 900x1600 → 900x1600 | empresa, inicio | empresa, inicio |
| `legacy/anel-solitario-p` | 实拍 | 900x1600 → 900x1125 | colecoes | colecoes |
| `legacy/pendente-halo-p` | 实拍 | 900x1125 → 900x1125 | jornal-embalagem | jornal-embalagem |
| `mj/mj-g3-2-w` | AI | 1680x720 → 1680x720 | colecoes, inicio | colecoes |
| `mj/mj-g3-2-s` | AI | 1680x720 → 1080x720 | colares | colares |
| `mj/mj-g4-0-w` | AI | 1680x720 → 1680x720 | homem, inicio | homem |
| `mj/mj-g5-0-w` | AI | 1680x720 → 1680x720 | inicio, jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele | jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele |
| `mj/mj-g5-0-t` | AI | 1680x720 → 576x720 | colecoes | colecoes, inicio |
| `mj/mj-g5-1-w` | AI | 1680x720 → 1680x720 | inicio | inicio |
| `mj/mj-g5-1-t` | AI | 1680x720 → 576x720 | colecoes, pulseiras | colecoes, inicio, pulseiras |
| `mj/mj-g2-1-w` | AI | 1680x720 → 1680x720 | inicio, jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele | inicio, jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele |
| `mj/mj-g2-1-t` | AI | 1680x720 → 576x720 | jornal-na-pele | jornal-na-pele |
| `mj/mj-g2-0-s` | AI | 1680x720 → 1080x720 | aneis, empresa, inicio | aneis, empresa |
| `mj/mj-g3-1-s` | AI | 1680x720 → 1080x720 | empresa, inicio | empresa |
| `mj/mj-g3-1-t` | AI | 1680x720 → 576x720 | entrar | entrar |
| `mj/mj-g1-1-w` | AI | 1680x720 → 1680x720 | inicio, showroom | inicio, showroom |
| `mj/mj-g1-0-s` | AI | 1680x720 → 1080x720 | empresa, inicio, showroom | empresa, showroom |
| `mj/mj-g6-0-s` | AI | 1680x720 → 1080x720 | inicio, jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele | inicio, jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele |
| `mj/mj-g6-0-t` | AI | 1680x720 → 576x720 | conta | conta |
| `mj/mj-g7-3-w` | AI | 1680x720 → 1680x720 | inicio, jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele | inicio, jornal, jornal-aco-316l, jornal-embalagem, jornal-montra, jornal-na-pele |
| `mj/mj-g7-3-t` | AI | 1680x720 → 576x720 | loja | inicio, loja |
| `mj/mj-g7-2-s` | AI | 1680x720 → 1080x720 | inicio, showroom, 菜单 | showroom, 菜单 |
| `mj/mj-g2-3-s` | AI | 1680x720 → 1080x720 | inicio, jornal-na-pele | jornal-na-pele |
| `mj/mj-g1-2-s` | AI | 1680x720 → 1080x720 | jornal-montra | jornal-montra |
| `mj/mj-g1-3-s` | AI | 1680x720 → 1080x720 | contactos | contactos |
| `mj/mj-g6-1-s` | AI | 1680x720 → 1080x720 | empresa, jornal-embalagem | empresa, jornal-embalagem |
| `mj/mj-g6-3-t` | AI | 1680x720 → 576x720 | jornal-embalagem | jornal-embalagem |
| `mj/mj-g7-0-s` | AI | 1680x720 → 1080x720 | empresa, jornal-montra | empresa, jornal-montra |
| `mj/mj-g7-1-t` | AI | 1680x720 → 576x720 | jornal-montra, showroom | jornal-montra, showroom |

## 6. 已知限制
- **MJ 图**：只有 1680 宽，在 Retina 屏上的 21:9 大图会略软，需要 MJ Upscale。
- **实拍原图**：最宽只有 900–1200px，全屏展示时在 2x 屏上会发软。
- **示例数据**：人群、场合、风格的分类是演示用标注；阶梯价按公式推算；账户里的订单是虚构的。页面上都写明了是示例。
- **"Ouro 18K"改名为"Banho de ouro 18K"**：理由见 `page-structure-comparison.md` §5，需要客户确认。
- **联系方式**：WhatsApp 号码是占位；邮箱 `geral@lmbiju.pt` 和营业时间沿用 v17。
- **表单**：都通过 mailto 生成邮件，没有后台。登录是演示账户，页面上已写明。
- **兼容性**：只用 Chromium 测过；Safari 和 Firefox **推测**可用，但没有实测。View Transitions 在不支持的浏览器里会直接切换页面。
- **`start-demo.bat`**：没有在 Windows 上实际运行过。
