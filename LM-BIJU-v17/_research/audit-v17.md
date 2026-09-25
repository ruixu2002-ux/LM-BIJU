# LM BIJU v17 · 现有 Demo 代码审计

> 审计对象：`LM-BIJU-v17/`（index.html / catalogo.html / empresa.html / main.js / styles.css / images / media）
> 日期：2026-09-25 · 全部数据在云端容器实测；证据文件见 `_research/evidence/`
> 工具：Lighthouse 13、axe-core、Playwright Chromium（1440 / 768 / 390 截图 + 键盘走查）、sharp（图片元数据）、MP4 容器手动解析

---

## 0. 测量总览

注意：本地静态服务没有 CDN、HTTP/2 和缓存头；Lighthouse 跑的时候 Google Fonts 因代理证书没加载成功，所以**性能分数偏乐观**。

| 页面 | 移动端 Perf / A11y / BP / SEO | 移动端 LCP | 传输量 | 桌面端 Perf / A11y |
|---|---|---|---|---|
| index | 96 / **85** / 96 / 100 | 2.4 s（Speed Index 3.8 s） | 644 KiB | 100 / 90 |
| catalogo | **87** / **80** / 96 / 100 | **3.8 s** | 809 KiB | 98 / 88 |
| empresa | 99 / **78** / 96 / 100 | 1.7 s | 278 KiB | 100 / 87 |

原始数据：`evidence/lighthouse-v17-summary.json`

**结论：性能不是这个 demo 的主要问题，审美和 B2B 逻辑才是。**

### hero.mp4（容器解析实测）

| 属性 | 值 |
|---|---|
| 大小 | 18,080,466 B |
| 时长 | 28.7 s |
| 平均码率 | 约 5.0 Mbps |
| 编码 | H.264 **High Profile @ Level 4.2** |
| 分辨率 | **1080 × 1920（竖屏 9:16）** |
| 帧率 | **59.94 fps**（1719 帧） |
| 关键帧 | 12 个（GOP 约 2.4 s） |
| 音轨 | **含 AAC 音轨**（48 kHz，但视频是 `muted` 播放，音轨纯属浪费） |
| moov 位置 | 文件头（faststart 正确） |

**关键发现**：竖屏视频被塞进 1440 × 720（2:1）的横向 Hero，`object-fit:cover` 之后：
- 只显示原画面**约 28% 的高度**
- 同时放大 1.33 倍

Lighthouse 没把视频算进传输量（`preload="metadata"`，只取了 moov）。但真实浏览器自动播放时，会在前 30 秒拉满 18 MB。**判定 P0。**

---

## 1.1 代码结构

### HTML 语义

| # | 级别 | 问题 | 证据 | 影响 | 修复方向 |
|---|---|---|---|---|---|
| S1 | P1 | 三页都没有 `<main>`，也没有 skip-link | axe `landmark-one-main`；`region` 共 44 个节点 | 读屏没法跳到主内容 | 包一层 `<main id="main">` 并加跳转链接 |
| S2 | P1 | 标题层级错乱：6 个 mega `<h5>` 排在 `<h1>` 之前；footer 用 `<h4>` | DOM 顺序：H5×6 → H1 → H2；axe `heading-order` | 页面大纲混乱 | 菜单分组标题改成非标题元素；footer 改用 h2 |
| S3 | P1 | 整张产品卡是一个 `<button>`，里面包着 div、img、svg | `index.html:145` 起 | 内容模型非法；产品没有 URL，没法分享、没法被索引 | 改成 `article` + 标题 `<a>`，快速查看单独做成按钮 |
| S4 | P1 | header、footer 在三个文件里各复制一份，而且已经不一致 | index footer 多了 TikTok、Pinterest 和 App 徽章；empresa 的导航没有 mega 菜单 | 维护时漂移 | 组件化 |
| S5 | P2 | 34 处内联 `style` | index 11 / catalogo 8 / empresa 15 | 绕过 Token | 收进 class |
| S6 | P2 | "342 / 486 / 128 refs" 是写死的数字 | `index.html:129-131` | 上线后可能构成虚假陈述 | 由数据驱动 |
| S7 | P2 | 语言切换全部是 `href="#"`，也没有 hreflang | `index.html:24` | 承诺了多语言却不兑现 | WPML / Polylang + hreflang |
| S8 | P2 | 缺 favicon（404）、OG、JSON-LD | Lighthouse 控制台 | 链接分享预览是空的 | 补齐 |

### 可访问性

| # | 级别 | 问题 | 证据 | 修复方向 |
|---|---|---|---|---|
| A1 | **P0** | 快速查看弹窗**没有焦点陷阱** | 打开后按 10 次 Tab，焦点全部跑到弹窗后面；`main.js:89-105` | 原生 `<dialog>.showModal()` 或 `inert` |
| A2 | **P0** | empresa 页"三步"的标题**几乎看不见** | `.steps3 b{color:#F2EDE4}`（`styles.css:244`）复用到了白底上，对比度 **1.17:1**；截图 `evidence/empresa-1440-steps-invisible.jpg` | 颜色按上下文 Token 派生 |
| A3 | P1 | 对比度不达标：index 20 处 / catalogo 26 / empresa 28 | footer `#877F72`/`#1B1813` = 4.47；`.brand .sub` 金色/白底 = 3.09（字号 8px）；`.svc span` = 3.66；`.fcopy` = 3.21；`.sku` = 2.69；瓦片标签白字/金底 ≈ 3.1 | 重建色板 |
| A4 | P1 | 功能性文字用 8–10px | `styles.css:65, 196` 等多处 | 功能文字至少 12px |
| A5 | P1 | 手机端 Login 链接没有可访问名称；触控区小于 24px | Lighthouse `link-name` / `target-size` | 加 `aria-label`，触控区 ≥ 44px |
| A6 | P1 | 手机端头部重叠：搜索图标压在 logo 上 | `evidence/index-390-header-overlap.jpg` | 手机端头部改成三等分布局 |
| A7 | P1 | `.rv` 默认 `opacity:0`，完全依赖 JS 才显示 | `styles.css:395`；锚点直达 `#novidades` 时 1/12 区块仍不可见 | 用 `.js` 类门控 |
| A8 | P2 | `aria-label` 挂在没有 role 的 `span` 上 | axe `aria-prohibited-attr` | 加 `role="img"` |
| A9 | P2 | `aria-label` 与可见文字不一致 | Lighthouse `label-content-name-mismatch` | label 里包含可见文字 |
| A10 | P2 | 数量是 `span` 加 ±按钮，上限写死 99 | `main.js:118-119` | 改成 `input type=number`，step 等于 MOQ |

### CSS

| # | 级别 | 问题 | 证据 | 修复方向 |
|---|---|---|---|---|
| C1 | P1 | 只有 13 个色彩变量，另有 40 多个写死的米色和灰色 | styles.css 全文 | 分三层：primitive → semantic → component |
| C2 | P1 | 共 17 种字号（8–17px），没有阶梯 | grep `font-size` | 定模块化比例 |
| C3 | P1 | 只有 `--gut` 一个间距 Token | 散落的 clamp | 4px 基数阶梯 |
| C4 | P2 | `filter:saturate/contrast` 重复 5 次，在运行时修图 | :159 / :194 / :224 / :252 / :276 | 放到图片管道里处理 |
| C5 | P2 | 未使用 CSS 16 KiB；有 `;;` 残留 | Lighthouse；`:45` | 按页拆分 |
| C6 | P2 | 注释写明"依据竞品实测重排"、"Montserrat 与 Shebiju 同族" | `styles.css:3-10` | 方法论错误：设计来源是模仿竞品 |

### JS

| # | 级别 | 问题 | 证据 | 修复方向 |
|---|---|---|---|---|
| J1 | 通过 | 用 IIFE 包裹、strict 模式、无全局污染、无第三方库 | `main.js:2` | 保持 |
| J2 | P1 | 价格是 `data-rrp="24,90 €"` 这样的字符串 | `index.html:145` | 改成结构化数据或 API |
| J3 | P1 | 筛选靠 `display:none`：没有 URL 状态、没有结果计数、没有 aria-live | `main.js:74-77` | 查询参数 + `aria-live` |
| J4 | P2 | Hero 轮播只换文案，视频不变 | `main.js:43-62` | 删掉 |
| J5 | P2 | stagger 的 index 把隐藏元素也算进去 | `main.js:130-132` | 筛选后重算 |
| J6 | P2 | 锁滚动时没有补偿滚动条宽度 | `main.js:103` | 补偿约 15px |

---

## 1.2 AI 味 / 模板感清单（20 条）

| # | 特征 | 是否命中 | 证据 |
|---|---|---|---|
| 1 | 无理由用 Montserrat | 命中 | 理由是"与 Shebiju 同族" |
| 2 | 所有标题同一字重 | 命中 | H1–H5 全部 700 |
| 3 | 玻璃拟态 | 部分命中 | 2 处 `backdrop-filter:blur` |
| 4 | 等宽卡片配小图标 | 命中 | `.svc` 4 格、`.gua` 4 格、`.who3` 3 卡 |
| 5 | Hero 配两个 CTA 模板 | 命中 | `index.html:91-94` |
| 6 | 所有区块上下内边距相同 | 命中 | 所有 section 的 padding-top 都是 66.24px |
| 7 | 千篇一律的淡入 | 命中 | 17 处 `.rv` 效果完全一样 |
| 8 | 悬停时放大、上浮、加阴影三件套 | 命中 | `.pcard:hover` |
| 9 | eyebrow + 大标题 + 灰色导语 | 命中 | 出现 13 次 |
| 10 | 套话文案 | 部分命中 | "Bijuteria que vende por si"；"não X, mas Y" 句式 |
| 11 | 01/02/03 步骤重复 | 命中 | index 和 empresa 各讲一遍"三步注册" |
| 12 | 图标风格混用 | 命中 | 线性图标、彩色方块、CSS 拼的徽标、`✕` 字符混在一起 |
| 13 | 配色没有品牌逻辑 | 命中 | 金色一身五角；还有第二个金色 `#A98550` |
| 14 | 圆角不成系统 | 命中 | 0 / 2 / 3 / 7 / 8 / 9 px 混用 |
| 15 | 图片风格不统一 | **严重命中** | 7 种长宽比，亮度从 5 到 231 |
| 16 | 动效没有叙事 | 命中 | 见 1.4 |
| 17 | Shopify 式信任条 | 命中 | `.svc` |
| 18 | 促销话术破坏奢侈感 | 命中 | "até −50%"、"−30%" |
| 19 | 虚假的完整性 | 命中 | 没有 App 却放 App 徽章；语言切换全是假的；Klarna |
| 20 | 全部居中对称，没有张力 | 命中 | logo、导航、newsletter、支付条全部居中 |

### 1.2b 图片专项

截图：`evidence/images-contact-sheet.jpg`、`evidence/images-zoom-ambiguous.jpg`

| # | 级别 | 问题 | 证据 |
|---|---|---|---|
| I1 | **P0** | 画面里有第三方品牌 **"EMIZA JEWELLERY"** | `pendente-halo.jpg` 礼盒盖左上方；这张图用在 LB-1005 |
| I2 | **P0** | 推测是图库图，许可证未知 | 17 张全部带 EXIF、无 ICC；构图是典型图库生活风格 |
| I3 | **P0** | 图文不符 | LB-2002 "Kit Kraft" 配的图是手表、手机和墨镜；LB-1009 "Pulseira Elos" 配的是十字架项链；LB-1011 "Aço Escovado" 配的是金色细圈；LB-1012 "Tennis" 与 LB-1004 共用一张图，而且画面是古巴链 |
| I4 | P1 | 7 种长宽比 | 9:16 到 16:9 |
| I5 | P1 | 亮度极差悬殊 | `hero-aco` 为 5，`hero-still` 为 231 |
| I6 | P1 | 分辨率不够（900–1200px 宽）；900px 的图被拉成 1440px 宽的 Hero | sharp 元数据 |
| I7 | P1 | 首屏同一张图出现两次 | `hero-ouro.jpg` 在 `index.html:81/84/129` |
| I8 | P2 | baseline JPEG，4:2:0 采样，没有 AVIF/WebP 和 srcset | 总计 1765 KiB |
| I10 | **P0** | **文案雷同**：empresa 页的"三问卡"和 Cellibiju 首页文案几乎逐句相同（Tem/Possui uma página no Instagram ou Facebook…；…loja online ou física…；Está a pensar (em) começar um negócio com bijuteria?） | `empresa.html:78/86/94` 对照 `_research/cellibiju/` 04.png；两家同在 Varziela 工业区 |
| I9 | P2 | `cat-colares.jpg`、`cat-pulseiras.jpg` 没有被任何页面引用 | grep |

---

## 1.3 关键诊断

- **`--gold:#B08D57`（oklch 66.4% 0.083 77.4）不合格**
  - 对比度：白底 3.09，米色底 2.65，深底 5.72 → 只在深底上成立
  - 一个颜色身兼五个角色，没有稀缺感
  - 处理：拆成装饰金和文字金，见 foundations 文档 §1
- **Montserrat 不合适**
  - 典型的模板默认字体
  - 几何无衬线字面宽、密度低，笔画没有反差
  - 选它的理由是"和竞品同款"
  - 替代方案见 foundations 文档 §2
- **"视频 + 文字压底"不够高端**，而且这里的执行更差
  - 三层叠加（遮罩、模糊条、粗体标题）
  - 用的是假轮播
  - 竖屏视频被硬塞进横向容器
- **产品卡缺少的 B2B 信息**
  - 显性材质标签
  - MOQ 和步长
  - 分级价阶梯
  - 库存状态
  - 快速加购
  - 变体数
  - 可复制的 SKU（≥12px 等宽）
  - 包装单位
  - PVP 对比与毛利倍率
  - 加入 RFQ
  - EAN（"OE 号"是汽配行业术语，在这里不适用）

## 1.4 动效清单

| # | 位置 | 触发 | 时长 / 缓动 | 判定 |
|---|---|---|---|---|
| M1 | Hero 标题逐行揭示 | 加载后 120ms | 900ms，`cubic-bezier(.2,.65,.3,1)` | 服务于理解 |
| M2 | 文案轮播 | 每 6s | 淡入淡出 220ms | 廉价（假轮播） |
| M3 | `.rv` 淡入上移 18px | IO，阈值 0.08 | 700ms，stagger 60ms | 廉价，17 处完全相同 |
| M4 | 卡片 hover | hover | 350 / 700 / 300ms | 过度，三效叠加 |
| M5 | 瓦片 hover | hover | 800 / 250ms | 普通 |
| M6 | Mega 菜单 | hover / focus | 250ms，位移 8px | 合理 |
| M7 | 快速查看弹窗 | click | 300ms，`scale(.985)` | 合理但平庸 |
| M8 | 链接 hover 改 `padding-left` | hover | 200ms | 廉价，触发重排 |
| M9 | 社交图标上浮 | hover | 200ms | 廉价 |
| M10 | sticky 阴影 | scroll | 300ms | 服务于理解 |

**缺失的动效**：
- 滚动叙事与 pin
- View Transitions 页面转场
- clip-path 或 mask 图像揭示
- 衬线拆字动画
- 自定义光标
- Lenis 平滑滚动
- 3D / 360 产品展示
- 微距放大
- 数字滚动
- 加入询价单的反馈

`prefers-reduced-motion` 的处理**合格**。

## 1.5 B2B 功能

| # | 级别 | 功能 | 现状 | 证据 |
|---|---|---|---|---|
| B1 | **P0** | 注册门禁 | 不存在，"Criar conta" 是 `href="#"` | `empresa.html:114-115` |
| B2 | **P0** | 批发价隐藏 | 页面上根本没有批发价；设计思路是前端隐藏，上线时必须由服务端按角色输出 | 只有 `data-rrp` |
| B3 | **P0** | MOQ 校验 | 没有，范围 1–99，步长 1 | `main.js:118-119` |
| B4 | **P0** | 分级定价 | 没有，也没有支撑它的数据结构 | — |
| B5 | **P0** | RFQ / 表单 | "Pedir proposta" 是锚点；newsletter 用 `onsubmit="return false"`，提交后没有任何反馈 | `index.html:232, 279` |
| B6 | P1 | 快速批量下单 | 没有 | — |
| B7 | P1 | 账户中心 | 链接指向 `#grosso` | — |
| B8 | P1 | 目录 PDF | 链接指向 `#grosso` | `catalogo.html:87` |
| B9 | P2 | GDPR | newsletter 没有同意勾选；没有 CMP；Google Fonts 直连会传输访客 IP | — |

**小结**：这是一个"看起来像 B2B 的 B2C 模板"。
- 视觉层：与竞品同源
- 功能层：B2B 功能为零
- 图片层：有法律风险，而且图文不符
- 跑分高，只是因为它什么都没做
