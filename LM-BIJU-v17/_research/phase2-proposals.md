# LM BIJU · 第二阶段：竞品综合 · 审美升级 · 三个 Demo 方案 · 推荐

> 日期：2026-09-25
>
> 竞品依据：用户提供的 60 张视口截图（shebiju 14、cellibiju 7、grupobelle 30、maxbiju 9），逐站分析见 `_research/<竞品>/analysis.md`。
> - **没有 HAR、HTML、Lighthouse**，所以技术栈只能从截图上可见的线索推断，**CDN、HTTP 版本、图片格式、性能一律标"无法确认"**。
> - **像素尺寸前提**：截图按 1:1 CSS px 记录。两位分析者都发现有迹象表明截图时系统缩放是 **125%**。如果属实，所有竞品 px 数值要 ÷1.25。**这一项待你用 `devicePixelRatio` 确认。**
>
> 基础规格（色板、字体、视频、图片、线框）见 `foundations-phase1.md`，本文只写增量和"待核实"项的结论。

---

## Part 1 · 竞品综合

### 1.1 四家速写

| | Shebiju | Cellibiju | Grupobelle | Maxbiju |
|---|---|---|---|---|
| **平台** | 定制 PHP（推测；`/pt/login.php?l=1` 已确认） | Shopify · Dawn 主题（推测，把握较高：`/collections/aneis` 加 Shopify 政策页） | PrestaShop（推测，把握较高：URL `/16836-83490-slug.html#/…`、核心翻译串"Existem 282 produtos."）+ Bootstrap 灰阶 | OpenCart（推测，把握较高：登录页文案与默认语言包逐字相同）· 主题商 AikeInf Technologies（已确认，见页脚） |
| **气质** | 编辑感大片 + 模板化外壳 | Dawn 原样 + 插件拼装 | 暖米色棚拍 + 金色过量 + 字形拼贴 | 米色生活照撑门面 + OpenCart 零售壳 |
| **展示字体** | Playfair 类衬线（推测） | 无（系统字体，Windows 下是 Segoe） | 无衬线字体；几何粗体、手写体、斜体混用 | 无；全站 Lato（推测） |
| **正文字体** | Montserrat（推测）；登录页换成了 Arial 类 | Segoe / 系统字体；登录页换成了 Roboto 类 | Inter 类 | Lato |
| **金色 / 强调色** | `#7F653B`（大字 3.83，小字 3.49 不通过）；外加两个无关的橙色 `#FFA500`（1.97）、`#FF9100`（2.26） | 没有金色；Logo 青绿 `#83D8D0`（1.65，只出现在 Logo 上） | `#C3995B` 同时当文字色和底色（2.62）；半透明标签 `#C79F68`（白字 2.45）；另一个金 `#7A6442` | `#C3AA5B` 用于当前项和悬停（2.28 / 2.08） |
| **吸顶头部占视口** | 约 290px + 底部固定的欧盟资助条约 76px，内容区只剩约 65% | 432px（41%） | 约 150px（14%），半透明底会透出下层内容 | 未测出问题 |
| **摄影** | 编辑级模特大片，系列感强 | 白色卵石加硬光，统一 | **四家里最统一**：暖米色石灰华棚拍 | 米色生活照；**产品图压了"MAXBIJU"大水印** |
| **访客价格门禁** | 目录可以浏览，价格隐藏，点击时弹出 Bootstrap 弹窗 | 文案写"注册后看价" | PDP 公开 PVPR，批发价隐藏，有登录提示框 | 价格消失，**但没有任何提示** |
| **MOQ / 分级价 / 快速下单 / RFQ** | 截图里都没看到（只有"满 150€+IVA 免运费"） | 只有首单 100€+IVA；有"Reposição"补货菜单 | 有 10 件装起步套装 KIT44；其余没看到 | 都没看到 |
| **最便宜的信号** | 橙色标签；290px 头部；PLP 上 SKU 重复 | 432px 头部；"**ATENÇÃO**"；登录页风格断裂 | 金色标签不达标；Bootstrap 默认分页；语言混杂 | 水印；图标字体显示成方框；OpenCart 默认登录页 |
| **最值钱的地方** | Hero 模特大片 | 分类大图摄影统一 | 摄影统一 + 3000m² 展厅 + 2008 年起步的历史 | 子类缩略图是统一棚拍 |
| **地址** | 截图里未见 | **Porto 门店在 Zona Industrial de Varziela** | **Z. Industrial Varziela，Vila do Conde** | 截图里未见 |

### 1.2 行业共性（这是最重要的发现）

1. **行业的视觉默认值是"暖米色 + 金色 + 石头/布料静物"。**
   - 四家里三家（Shebiju、Grupobelle、Maxbiju）的首页主调都在米色区间：`#DFD7C5`、`#F0E5DA` 等。Cellibiju 是白色卵石，也属于同一套语言。
   - v17 也在这个区间（`--sand #F2EDE4`）。
   - **结论**：继续用"米色 + 金"，就算做得再精致，也会和同一条街上的三家长得一样。
2. **地缘上直接竞争。** LM BIJU、Cellibiju、Grupobelle 都在 **Varziela 工业区**。客户去实地看货时，一天之内能逛完三家。网站是在到店之前就拉开差距的唯一地方。
3. **四家都没把 B2B 做成产品。**
   - 截图范围内，没有一家在 PLP 上显示 MOQ、分级价、快速下单或 RFQ。
   - 门禁做得最好的是 Grupobelle 的 PDP（公开 PVPR，加一个登录提示框）。
   - 最差的是 Maxbiju：价格直接消失，页面上没有任何提示。
4. **四家都有无障碍硬伤**：金色文字对比度 2.1–2.6；两家登录页和主站风格断裂；表单用占位符代替标签。
5. **可以学的**：
   - Grupobelle 摄影的统一度
   - Cellibiju 的"Reposição"补货入口和"Como medir com uma moeda"（用硬币量尺寸）这类实用内容
   - Grupobelle PDP 上"公开 PVPR + 隐藏批发价"的做法
   - Shebiju 的 SKU 可见性和规模数字（+20 MIL referências）

### 1.3 新增 P0（补进 v17 审计）

**v17 的 empresa 页"三问卡"和 Cellibiju 首页文案几乎逐句相同**

| v17 `empresa.html:78/86/94` | Cellibiju `04.png` |
|---|---|
| "Tem uma página no Instagram ou Facebook que vende bijuteria?" | "Possui uma página no Instagram ou Facebook que vende bijuteria?" |
| "Tem uma loja online ou física de bijuteria?" | "Possui uma loja online ou física que vende bijuteria?" |
| "Está a pensar começar um negócio com bijuteria?" | "Está a pensar em começar um negócio com bijuteria?" |

- **影响**：对方在同一个工业区，文案雷同一眼就能认出来。这既是版权和不正当竞争的风险，也会损害品牌可信度。
- **处理**：三个方案都**删除**这组文案，改为"客户类型切换"模块，文案全部重写（见 §3）。

### 1.4 综合对比表（✓ 有 / ✗ 截图里没看到 / ? 截图没覆盖）

| 维度 | Shebiju | Cellibiju | Grupobelle | Maxbiju | v17 | **LM BIJU 目标** |
|---|---|---|---|---|---|---|
| 统一的字体系统 | ✗（登录页不一致） | ✗ | ✗（4 类字形） | 部分（只有 Lato） | 部分（只有 Montserrat） | **✓ 三层体系** |
| 金色对比度达 AA | ✗ | —（没有金色） | ✗ | ✗ | ✗ | **✓ 文字金 5.60** |
| 头部 ≤ 15% 视口 | ✗ | ✗ | ✓（边缘） | ? | ✓ | **✓** |
| 统一摄影 | ✓（大片） | ✓ | **✓✓** | 部分（有水印） | ✗ | 部分：Demo 靠布局兜底，上线需要补拍 |
| 访客的价格状态被设计过 | 弹窗 | 文案 | **PDP 提示框** | ✗ | 锁图标 | **✓ 行内状态 + PVP + 毛利倍率预告** |
| PLP 上的 MOQ | ✗ | ✗ | ✗ | ✗ | ✗ | **✓** |
| 分级价 | ? | ? | ? | ? | ✗ | **✓** |
| 快速下单 / CSV | ✗ | ✗ | ✗ | ✗ | ✗ | **✓** |
| RFQ | ✗ | ✗ | ✗ | ✗ | 假按钮 | **✓ 真实提交** |
| 补货 / 再订购 | ? | ✓ 菜单 | ? | ? | ✗ | **✓** |
| 筛选（多维） | 侧栏计数 | ? | ✗（只有排序和分页） | ✓ 颜色和子类 | 单选 chips | **✓ 多维 + URL 状态** |
| 实体展厅 | ? | ✓ 两处 | ✓ 3000m² | ? | ✓ Varziela | ✓（需要真实照片） |
| 动效叙事 | ✗ | 轮播 | ✗ | ✗ | 淡入 | **✓（按方案不同）** |
| 原生 App | ✓ | ✗ | ✗ | ✗ | 假徽章 | ✗（不做；网站做成 PWA 即可） |

### 1.5 超越 / 持平 / 做不到

- **能超越，按优先级排**：
  1. **B2B 工具深度**：MOQ、分级价、快速下单、RFQ、再订购。四家都没有，开发成本中等，对转化的影响最大。
  2. **字体与色彩系统的完整性和可访问性**：四家全部不及格，我们成本低、收益确定。
  3. **访客门禁体验**：把"看不到价格"变成"看到你的毛利空间"（登录前展示 PVP 和倍率区间的预告）。
  4. **动效叙事**：四家都是零，这是"第一眼就不一样"最快的办法。
  5. **视觉差异化**：走出米色区间，见 §3 各方案。
- **能持平**：
  - 摄影统一度：需要补拍，Grupobelle 是标杆
  - 展厅信任感：需要真实照片或视频
  - 政策页和支付完整度
- **做不到（或者短期做不到）**：
  - Grupobelle 的 3000m² 展厅、2008 年起的历史、自有工厂叙事
  - Shebiju 的"+20 MIL referências / +15 MIL clientes / PME Líder"，以及原生 App
  - 大规模统一棚拍：需要预算和时间
  - LM BIJU 的真实规模数据**需要你补充**，Demo 里只能用明确标注的占位

---

## Part 2 · 审美升级方案（在 foundations 之上的增量）

### 2.1 "待核实·竞品"项的结论

| 项 | 结论 |
|---|---|
| 字体差异化 | 竞品在用：Playfair 类 / Montserrat / Segoe / Inter 类 / Lato / 手写体。**Fraunces、JetBrains Mono 都没人用**。Inter Tight 和 Grupobelle 的"Inter 类"相近，属于可以接受的中性正文字体，差异化由 Display 层承担 |
| 金色 | 竞品的金 `#7F653B`、`#C3995B`、`#C3AA5B`、`#C79F68` 和我们的 `#7D5E2C`、`#CDB079` **色值很接近**。说实话，任何能过 AA 的"文字金"最后都会落在这个色域里。**差异不在色值，而在规则**：金色 ≤ 3% 的像素、主按钮不用金、金色只出现在深底上，或者作为 ≥4.5 的文字金 |
| 米色区间 | foundations 里的 `paper-50 #FAF7F2` 仍然偏暖。在 §3 各方案里：A 把底色换成**冷一点、更白**的 `#FBFBF9` 加大面积纯白；B 走深色；C 走中性白。**三个方案都不再用 `#F2EDE4` 这类米色做大面积底色** |
| PDP 毛利倍率 | 竞品截图里都没出现，是**独有**的做法 |
| 金色标签按钮（v17 从 Grupobelle 学来的） | 实测 2.45:1，而且半透明导致颜色不稳定，**三个方案都废弃** |
| 双行头部 | 竞品的实测数据（150–432px）证明它吃掉首屏。三个方案的头部都控制在 **64px（桌面）/ 56px（手机）** 以内 |

### 2.2 动效规格总表（三个方案按需取用，各方案的开关见 §3）

动效 Token：
- `--ease-out: cubic-bezier(.16,1,.3,1)`：进入、揭示
- `--ease-inout: cubic-bezier(.76,0,.24,1)`：遮罩、转场
- `--ease-ui: cubic-bezier(.2,0,0,1)`：UI 反馈
- 时长：`--t-1 120ms`（微反馈）、`--t-2 240ms`（UI）、`--t-3 480ms`（组件）、`--t-4 900ms`（揭示）、`--t-5 1400ms`（场景）

**全局规则**：
- 只动 `transform`、`opacity`、`clip-path`
- `prefers-reduced-motion` 时全部降级为瞬时切换或淡入 ≤ 120ms
- **目录、表格、RFQ、结账页禁用平滑滚动和装饰性动效**：效率优先

| # | 位置 | 当前状态 | 建议动效 | 技术 | 时长 / 缓动 / 触发 | 性能风险 | 移动端降级 |
|---|---|---|---|---|---|---|---|
| M01 | Hero 标题 | 两行 translateY | **按词拆分**，词从 `yPercent:110` 升起，外层 `overflow:hidden` 做遮罩，stagger 0.04s | GSAP SplitText（GSAP 3.13 起全部插件免费）；在 `document.fonts.ready` 之后才运行，避免字体切换时跳动 | 1100ms / `--ease-out` / 加载 | 低（≤ 20 个词） | 按行拆分，不按词；800ms |
| M02 | 图像遮罩揭示（产品大图、编辑图） | 淡入上移 18px | `clip-path: inset(100% 0 0 0)` → `inset(0)`，同时图片 `scale 1.15→1`（反向缩放，保持"窗口不动、画面沉入"的感觉） | GSAP + ScrollTrigger，`once:true` | 1200ms / `--ease-inout` / 进入视口 80% | 中：clip-path 每帧重绘，**同屏 ≤ 3 个** | 800ms，去掉缩放 |
| M03 | 平滑滚动 | 原生 | Lenis，`lerp 0.1`，只在编辑型页面启用 | Lenis（MIT） | — | 低；要处理锚点和 ScrollTrigger 同步 | **触屏不启用**（`syncTouch:false`）；目录、RFQ 页不启用 |
| M04 | 滚动叙事"Da matéria à montra" | 无 | pin 住 300vh，分 4 章（材质 → 电镀 → 质检 → 陈列），图像交叉淡化，章节编号计数，文字逐章替换 | ScrollTrigger `pin` + `scrub:0.6` | 跟随滚动 | 中；pin 在 iOS 上可能抖动 | **不 pin**，改为纵向 4 张卡片，每张用 M02 揭示 |
| M05 | 视频 | 横屏全出血，竖屏素材被裁 | A：竖框播放；B：滚动逐帧（canvas 帧序列）；C：点击才播放 | `<video>`；B 用 canvas + 预解码的 AVIF 帧（参照 scroll-scrub-hero skill） | B：帧序列 48 帧 × 约 30KB，在 LCP 之后分批加载 | B 高：内存和带宽，需要 `saveData` 检测 | 540p 循环视频，或者只显示海报 |
| M06 | 3D 产品 | 无 | 程序化生成的金色素圈戒指：`MeshPhysicalMaterial`（metalness 1、roughness 0.18、clearcoat），加 HDRI 环境贴图；拖拽旋转，空闲时自转 0.15 rad/s | Three.js（MIT），在该区块进入视口时动态 `import()` | 进场 1400ms `--ease-out`；帧率跟随 rAF | **高**：约 150KB gz + GPU。`DPR ≤ 1.5`，离屏暂停 | 24 帧 360° 图片序列，或静态图 |
| M07 | 页面转场 | 硬跳转 | 跨文档 View Transitions：页面整体淡入淡出 + PLP 卡片图到 PDP 主图的**共享元素**变形（`view-transition-name: p-LB-1003`） | CSS `@view-transition{navigation:auto}` | 450ms / `--ease-inout` / 导航 | 低；不支持的浏览器直接降级为普通跳转（Firefox 支持度**推测为不支持**，执行时核实） | 同桌面；reduced-motion 下关闭 |
| M08 | 自定义光标 | 无 | 8px 实心点 + 40px 圆环（lerp 0.18）；悬停在产品图上时圆环扩到 72px，显示"Ver"；在 3D 区块显示"Arrastar"；**表单和输入框区域一律恢复系统光标** | 原生 JS + rAF | 跟随 | 低 | `(pointer:coarse)` 下完全不加载；键盘导航时隐藏 |
| M09 | 分级价联动 | 无 | 改数量时，当前价格档那一行底色渐变高亮，价格数字**只让变化的那一位**上下滚动 | CSS transition + 轻量 JS | 240ms / `--ease-ui` | 低 | 同桌面 |
| M10 | 加入订单 / RFQ | 无 | 缩略图以 FLIP 动画飞向右上角的计数器，计数器 `scale 1→1.15→1`，同时 `aria-live` 播报 | GSAP Flip | 600ms / `--ease-out` | 低 | 不飞，只做计数器反馈 |
| M11 | 产品卡悬停 | 上浮 + 阴影 + 放大三件套 | **只保留一个效果**：图片交叉淡化到第二张图（45° 角度） | CSS | 400ms / `--ease-ui` | 低 | 无悬停效果；左右滑动切换图片 |
| M12 | 材质索引（A） | 图片瓦片 | 文字列表；悬停时，一张预览图以 lerp 跟随光标，并用 clip 揭示 | JS + CSS | 300ms | 低 | 点击后在列表内展开图片 |
| M13 | 头部 | 滚动后加阴影 | 向下滚动时隐藏、向上滚动时出现；C 方案始终固定 | CSS + IntersectionObserver | 240ms | 低 | 同桌面 |
| M14 | 筛选结果 | 直接 `display:none` | 网格重排用 FLIP 动画，结果数由 `aria-live` 播报 | GSAP Flip | 320ms / `--ease-ui` | 低；≥ 200 个元素时关闭 FLIP | 同桌面 |
| M15 | 暗色聚光（B） | 无 | 深色幕布上，一个径向渐变遮罩跟随光标，"照亮"产品图 | CSS `mask-image: radial-gradient(...)` + CSS 变量 | 跟随，lerp 0.12 | 低到中 | 聚光改为围绕屏幕中心呼吸式缓慢变化；reduced-motion 下完全照亮 |

**动效 JS 预算（gzip）**：A ≤ 60KB（GSAP 核心 + ScrollTrigger + SplitText + Lenis）；B ≤ 230KB（再加 Three.js 子集和 Flip，**按区块懒加载**）；C ≤ 25KB（只用 Flip，或者不用库）。

**INP 目标**：< 200ms。

---

## Part 3 · 三个差异化 Demo 方案

**三个方案共用的约束**：
- B2B 的 5 项能力都要有设计
- 图片按 foundations §4.2 的对应表使用，**不用** `pendente-halo.jpg`，并且启用 `cat-colares` 和 `cat-pulseiras`
- 视频按 foundations §3 的编码参数处理
- 文案全部新写，**不沿用竞品文案**
- 没有真实后端的交互，要**明确标注为"原型"并给出能实际使用的替代路径**，不做 `return false` 那样的假交互（见 §3.4）

### 3.1 方案 A · "Edição" 极致编辑风

**一句话**：一本每季出版的珠宝批发刊物，用排版代替装饰，用留白代替信任图标。

**关键词**：克制 · 编辑 · 章节 · 负空间 · 衬线

**布局语言**：
- 12 栏，外边距 `clamp(20px,5vw,96px)`
- **非对称**：内容占 7/12 + 5/12，或者 4/12 + 8/12；页面里没有任何居中的大段文字
- 区块间距在 96 / 160 / 240px 之间变化
- 页面组织成"刊物章节"：Nº 01 Coleções、Nº 02 Matéria、Nº 03 Para o seu negócio、Nº 04 Showroom
- 图片比例只用 4:5 和 3:4 两种

**色彩**：
| 角色 | 色值 |
|---|---|
| 底色 | `#FBFBF9`（比米色冷、比纯白暖；**特意离开米色区间**） |
| 卡片 / 面板 | `#FFFFFF` |
| 文字 | `ink-900 #1C1915` |
| 次级文字 | `stone-600 #5E574E` |
| 细线 | `stone-200 #E4DED4` |
| 文字金 | `#7D5E2C`（只用于 eyebrow、链接下划线、价格锁图标） |
| 装饰金 `#CDB079` | 只出现在深色的"Showroom"一章 |

**字体**（许可证与来源见 foundations §2）：
- Fraunces 300，opsz 144：Hero 和章节标题；斜体只用于引文
- Inter Tight：正文和 UI
- JetBrains Mono：SKU

**动效基调**：慢、少、准。用到 M01、M02、M03（仅编辑型页面）、M07、M08（简化版，只有圆环）、M09、M10、M11、M12、M13；**不用** M04、M05 滚动逐帧、M06、M15。

**技术**：静态 HTML、CSS 和原生 JS；GSAP、SplitText、ScrollTrigger、Lenis 走 CDN（jsDelivr）；View Transitions。

**页面结构**：
- **首页**
  - 7/12 栏：Fraunces 128px 标题"Joias por grosso, / *escritas à mão da montra.*"（初稿）
  - 5/12 栏：竖框 4:5 视频（hero.mp4 转码版）
  - 下方是一行"刊头信息"：`Edição Outono 2026 · 486 referências · Envio 48h` —— 数字是占位，**需要你提供真实数据**
  - Nº 01 材质索引（M12）
  - Nº 02 三件精选，不对称排布：hero-still 大图 + cat-colares + cat-pulseiras
  - Nº 03 客户类型切换：Loja / Online / Turismo / Nova loja
  - Nº 04 Showroom：深色一章，用 cat-relogios 和 cat-homem
  - 门禁说明 + 内联注册入口
- **PLP**：左侧 220px 文字筛选（没有图标）；右侧 3 列 4:5 卡片，卡片之间用 24px 间隙加细线分隔；每 12 个产品插一张编辑图（anel-solitario / cat-loja），打破节奏
- **PDP**：左 7/12 画廊（纵向滚动的大图，不用缩略图条）；右 5/12 信息栏吸顶（sticky）：分级价表、MOQ 步进器、RFQ
- **关于页**：长文编辑排版（Fraunces 斜体引文 + Inter Tight 正文）；数字带用 tnum；质检章节写镍释放和镀层厚度（**需要你提供真实数据**）
- **询价页**：按 foundations §5.5 的线框，做成"订货单"的纸面感（细线表格 + 等宽 SKU）

**与竞品的差异**：
- 四家都没有展示字体层级，Shebiju 的 Playfair 只用在 Hero
- 四家都是"图片瓦片 + 金色标签"，A 用**文字索引**代替
- 底色离开米色区间

**对 v17 的改进**：修掉 Montserrat 700 单一字重、66px 均等间距、金色标签、横屏视频这几个问题；B2B 从零做起。

**优点**：
- 可以用现有素材直接实现
- 性能最好（LCP 是海报图，JS ≤ 60KB）
- 最容易迁移到 WP Block Theme

**缺点**：
- 大图配大留白会**放大现有图库照片风格不统一的问题**：亮度从 5 到 231，而且画面都是 lifestyle 图库风
- 底色虽然换了，整体气质仍然接近"精致版的行业默认"
- 对同行的冲击力中等

**难度**：★★☆☆☆（执行后约 1 天出 Demo）

**关键代码片段**：
```html
<!-- Hero：7/12 标题 + 5/12 竖框视频；海报是 LCP 元素 -->
<section class="hero grid-12">
  <h1 class="display col-1-7" data-split>Joias por grosso,<br><em>escritas para a montra.</em></h1>
  <figure class="col-8-12 frame-45">
    <video muted playsinline loop preload="none" poster="img/hero-poster.avif" data-src-set='{"av1":"media/hero.av1.mp4","hevc":"media/hero.hevc.mp4","h264":"media/hero.h264.mp4"}'></video>
    <figcaption class="mono">LB-1001 · Anel Pavé Dourado · Banho 18K</figcaption>
  </figure>
</section>
```
```js
// 材质索引：预览图跟随光标（M12）；触屏改为点击展开
const idx=document.querySelector('.material-index'), pv=idx.querySelector('.pv');
if(matchMedia('(pointer:fine)').matches){let x=0,y=0,tx=0,ty=0;
  idx.addEventListener('pointermove',e=>{tx=e.clientX;ty=e.clientY});
  (function loop(){x+=(tx-x)*.15;y+=(ty-y)*.15;pv.style.transform=`translate(${x}px,${y}px)`;requestAnimationFrame(loop)})();
  idx.querySelectorAll('li').forEach(li=>li.addEventListener('pointerenter',()=>{pv.src=li.dataset.img;pv.classList.add('on')}));}
```
```css
@view-transition{navigation:auto}
.card img{view-transition-name:var(--vt)} /* PLP 卡片：style="--vt:p-LB-1003"，PDP 主图用同名 */
::view-transition-group(*){animation-duration:.45s;animation-timing-function:cubic-bezier(.76,0,.24,1)}
@media (prefers-reduced-motion:reduce){::view-transition-group(*){animation:none}}
```

---

### 3.2 方案 B · "Câmara Escura" 沉浸动态风

**一句话**：一间暗室里的珠宝展。首页是被聚光照亮的橱窗；一进入目录，"灯就亮了"，暗室变成明亮的工作台。

**关键词**：暗室 · 聚光 · 叙事 · 材质 · 开灯

**布局语言**：
- 首页和关于页是深色的全屏"场景"，每一屏只放一件物体
- 文字压到极小，贴在画面边角，像博物馆展签（mono 编号 + 材质）
- 从首页或关于页进入 PLP、PDP、RFQ 时，执行一次"开灯"转场：背景从 `#14120F` 过渡到 `#FBFBF9`，时长 700ms
- 进入之后是明亮、克制、高效的工作界面。这些页面的组件规格和 C 方案的"效率层"一致，**但视觉外观属于 B 的品牌体系**

**色彩**：
| 场景 | 色值 |
|---|---|
| 暗场底色 | `ink-950 #14120F` |
| 暗场面板 | `ink-900 #1C1915` |
| 暗场正文 | `paper-50 #FAF7F2`（17.50） |
| 暗场次级文字 | `stone-300 #CFC8BD`（11.26） |
| 暗场强调 | `gold-300 #E2CFA4`（12.19） |
| 暗场装饰线 | `gold-400 #CDB079` |
| 亮场 | 与 A 相同的 `#FBFBF9` / `#FFFFFF` / `ink-900` / `gold-700` |

深色是**四家竞品都没有的**。四家全部是白底或米色底。

**字体**：
- Fraunces 300，opsz 144，**大量使用斜体**，作为暗场里的"手写展签"
- Inter Tight：UI
- JetBrains Mono：展签编号，例如 `Nº 012 · LB-1013 · Aço 316L`

**动效基调**：电影化，但每个动效都在交代"材质"或"位置"，不做纯炫技。用到 M01、M02、M03（仅暗场页）、M04、M05（滚动逐帧）、M06、M07（包括开灯转场）、M08（全套）、M09、M10、M13、M15。

**技术**：
- GSAP（核心 + ScrollTrigger + SplitText + Flip）、Lenis、Three.js（动态 `import`）、canvas 帧序列
- 环境贴图 HDRI 用 Poly Haven 的 CC0 素材（**执行时需要确认下载**，1K 分辨率约 1–2MB，只取一张）

**页面结构**：
- **首页**
  - **S1 聚光 Hero**：`hero-aco.jpg`（纯黑背景上的银色古巴链，亮度 5，简直是为暗场而拍的）铺满全屏，聚光（M15）跟随光标；左下角放 Fraunces 斜体标题，右下角放 mono 展签
  - **S2 "Da matéria à montra"**：pin 住的 4 章（M04），依次使用 hero-aco → hero-ouro → cat-aneis → cat-loja；章节文字讲 316L、镀金 18K、质检、陈列
  - **S3 金属的光**：程序化生成的 3D 素圈戒指（M06），旁边是材质对照：银色 316L 对照金色镀 18K，点击就切换材质参数
  - **S4 滚动逐帧**：从 hero.mp4 抽 48 帧（M05），放进竖框，让滚动来"播放"视频
  - **S5 客户类型切换** + 门禁说明
  - **S6 开灯**：进入目录的 CTA，点击后执行开灯转场
- **PLP、PDP、RFQ**：进入亮场，信息架构与 A 相同，但卡片更密（4 列，gutter 16px），PDP 画廊里加一个**暗场灯箱**，产品回到暗室里单独看
- **关于页**：暗场长卷；Showroom 用 cat-relogios、cat-homem、cat-moda 三张暗调图，这三张在 A 方案里很难安排，在 B 方案里正好是主角
- **询价页**：亮场；提交成功时有一个"盖章"动效（一次，240ms）

**与竞品的差异**：
- 唯一的深色品牌
- 唯一有动效叙事的一家
- 唯一有 3D 或材质交互的一家
- "开灯"这个隐喻把品牌体验和 B2B 效率连在了一起

**对 v17 的改进**：v17 的 4 张暗调图（hero-aco 亮度 5、cat-homem 31、cat-moda 37、cat-relogios 54）从"不协调"变成主角；亮调图放进暗场的"展柜框"里，统一的黑色边框把亮度差异变成"画廊里的挂画"，而不是拼贴。

**优点**：
- 第一眼辨识度最高，和整个行业拉开最大距离
- 能利用现有的暗调素材
- 叙事能力强，能讲清楚 316L、镀层这些专业内容

**缺点**：
- 技术和性能风险最高：WebGL、帧序列、pin
- 深色长页面在户外强光下的可读性不如亮色（所以工作页面一律是亮场）
- **没有真实产品的 3D 模型**：Demo 里只能程序化生成素圈戒指，上线后如果要展示具体 SKU 的 3D，需要 CAD 文件或摄影测量
- 维护需要前端动效能力

**难度**：★★★★☆（执行后约 2–3 天出 Demo）

**关键代码片段**：
```css
/* M15 聚光：深色幕布 + 跟随光标的径向遮罩（reduced-motion 时全亮） */
.stage{position:relative;background:#14120F}
.stage img{display:block;width:100%;height:100svh;object-fit:cover;
  -webkit-mask-image:radial-gradient(circle var(--r,34vmax) at var(--x,50%) var(--y,45%),#000 0 38%,rgba(0,0,0,.18) 70%,rgba(0,0,0,.06));
          mask-image:radial-gradient(circle var(--r,34vmax) at var(--x,50%) var(--y,45%),#000 0 38%,rgba(0,0,0,.18) 70%,rgba(0,0,0,.06))}
@media (prefers-reduced-motion:reduce){.stage img{-webkit-mask-image:none;mask-image:none}}
```
```js
// M06 程序化素圈戒指：只在进入视口时加载 three（约 150KB gz）
new IntersectionObserver(async([e],io)=>{if(!e.isIntersecting)return;io.disconnect();
  const THREE=await import('https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js');
  const r=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});r.setPixelRatio(Math.min(devicePixelRatio,1.5));
  const ring=new THREE.Mesh(new THREE.TorusGeometry(1,.16,64,256),
    new THREE.MeshPhysicalMaterial({color:0xE2C28A,metalness:1,roughness:.18,clearcoat:.6}));
  /* + RGBELoader 加载 CC0 HDRI 作 scene.environment；离屏时暂停 rAF；材质切换：316L → color 0xC9CCD0 */
},{rootMargin:'200px'}).observe(canvas);
```
```js
// M07 "开灯"：从暗场进入目录（View Transitions 可用时；否则直接跳转）
link.addEventListener('click',e=>{if(!document.startViewTransition||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
  e.preventDefault();document.documentElement.dataset.light='on';   /* CSS 用 700ms 把 --bg 从 ink-950 过渡到 #FBFBF9 */
  setTimeout(()=>location.href=link.href,700);});
```

---

### 3.3 方案 C · "Balcão" 功能密度风

**一句话**：一张精密的采购柜台。像 Linear 一样安静、快速，打开就能下单；品牌感只来自排版的精度和少量的衬线。

**关键词**：效率 · 密度 · 键盘 · 精确 · 可信

**布局语言**：
- 应用式外壳：左侧 240px 导航（品类、材质、我的清单、补货、RFQ），中间是工作区，右侧 360px 是可以收起的"订单 / RFQ 托盘"
- 默认用**表格视图**，每行 56px，64px 缩略图 + SKU + 名称 + 材质 + MOQ + 分级价 + 库存 + 数量
- 可以切换到网格视图
- **公开页面**（首页、关于页）也用同一套外壳的"只读"模式：首页就是一个**搜索框**加"本周新品 / 补货"两个列表，再加一段关于 LM BIJU 的短编辑块

**色彩**：
| 角色 | 亮色 | 暗色 |
|---|---|---|
| 底色 | `#FFFFFF` | `ink-950` |
| 面板 | `#FAFAF8` | `ink-900` |
| 文字 | `ink-900` | `paper-50` |
| 次级文字 | `stone-500 #736B61`（4.91） | `stone-400`（6.81） |
| 选中 | `gold-700` 左边线 + `stone-100` 底 | 对应暗色 |
| 状态色 | green-700 / amber-700 / red-700 | green-300 / amber-300 / red-300 |

完整支持亮色和暗色两种模式。

**字体**：
- Inter Tight 400/500/600，13–14px 为主（全站最小 12px）
- JetBrains Mono 13px：SKU、EAN、数量
- **Fraunces 只出现在 Logo 和页面 H1**（每页一次），是唯一的"珠宝感"来源

**动效基调**：几乎不可见。只用 M09、M10、M13（始终固定）、M14，时长 120–240ms，**不用**平滑滚动、光标、揭示和 3D。

**技术**：原生 JS，可选 GSAP Flip；⌘K 命令面板（在 SKU 和名称上做模糊匹配，Demo 里用 16 个 SKU 的本地数组）；键盘快捷键：`/` 搜索、`j`/`k` 上下移动、`+`/`-` 按 MOQ 调整数量、`r` 加入 RFQ。

**页面结构**：
- **首页**：⌘K 搜索（大）→ "Novidades · semana 39" 表格（10 行）→ "Reposição"（补货）→ 客户类型切换 → 一段 3 行的品牌说明 + Showroom 小卡
- **PLP**：表格 / 网格切换；左侧是多维筛选（材质、品类、价格带、MOQ ≤ n、有库存、新品）；筛选状态写在 URL 里；批量操作是勾选多行后"加入订单"或"加入 RFQ"
- **PDP**：右侧抽屉（不离开列表）：图（3 张）+ 规格表 + 分级价 + 数量；也可以打开成完整页面
- **关于页**：同一套外壳下的文档页（像 Stripe Docs）：公司数据表、质检参数表、物流 SLA 表
- **询价页**：就是右侧的托盘；支持粘贴清单和上传 CSV，每行校验 MOQ

**与竞品的差异**：四家都是 B2C 零售外壳。C 是唯一一个"为采购动作设计"的界面。Maxbiju 的侧栏筛选是最接近的，但没有表格、没有数量输入、没有托盘。

**对 v17 的改进**：B2B 功能从零做到行业第一。

**优点**：
- 转化和复购效率最高；对真实客户（店主、电商卖家）最实用
- 性能最好
- 最容易直接映射到 WooCommerce 的 B2B 插件

**缺点**：
- 公开页面的"惊艳感"最弱。上市公司、同行、首次访客会觉得它"像 SaaS，不像珠宝"
- 图片被压缩到 64px 缩略图，**浪费了珠宝最强的卖点：视觉**
- 对图库照片不敏感，这一点其实是优点

**难度**：★★★☆☆（交互逻辑多，但没有视觉特效；执行后约 2 天出 Demo）

**关键代码片段**：
```html
<!-- 表格行：MOQ 步进 + 分级价联动（Demo 中价格来自本地 JSON，生产由服务端按角色输出） -->
<tr data-sku="LB-1003" data-moq="6" data-step="6">
  <td><img src="img/lb-1003-160.avif" width="64" height="80" alt="Argolas largas polidas, banho de ouro 18K"></td>
  <td class="mono">LB-1003</td><td>Argolas Largas Polidas</td><td><span class="tag tag-gold">Banho 18K</span></td>
  <td class="num">6</td>
  <td class="tiers num"><span data-min="6">9,20</span><span data-min="24" class="on">8,40</span><span data-min="96">7,60</span></td>
  <td><input type="number" inputmode="numeric" min="6" step="6" value="24" aria-label="Quantidade LB-1003 (múltiplos de 6)"></td>
  <td><button class="icon" aria-label="Adicionar LB-1003 ao pedido de proposta">＋RFQ</button></td>
</tr>
```
```js
// MOQ 校验（前端提示；生产环境后端复核）
input.addEventListener('change',()=>{const {moq,step}=tr.dataset;let q=+input.value;
  if(q<+moq)q=+moq; q=Math.ceil(q/ +step)*+step;
  if(q!==+input.value){input.value=q;live.textContent=`Quantidade ajustada para ${q} (MOQ ${moq}, múltiplos de ${step}).`}
  tr.querySelectorAll('.tiers span').forEach(s=>s.classList.toggle('on',q>=+s.dataset.min&&!(s.nextElementSibling&&q>=+s.nextElementSibling.dataset.min)));});
```

---

### 3.4 三个方案共用：B2B 五项能力的设计

| 能力 | Demo 中的呈现（静态原型） | 生产环境实现（WooCommerce，见 foundations §6） |
|---|---|---|
| **注册门禁** | 完整的注册表单：公司名、NIF（**校验位算法在前端真实运行**）、CAE、客户类型、证明文件、同意勾选；提交后进入"Em validação"状态页 | B2B 插件的注册字段 + 审批流；NIF 在服务端校验；欧盟客户走 VIES |
| **批发价隐藏** | 右上角"Simular sessão"开关，明确标注为"Modo demonstração"，用来切换访客态和登录态。**Demo 的批发价写在前端 JSON 里，页面上明确注明这只是原型行为** | **服务端按角色输出**：访客收到的 HTML、REST（`/wp-json/wc/store/*`）和 JSON-LD 里都不包含批发价字段；上线前做一次抓取测试 |
| **MOQ 校验** | 数量输入 `min` / `step`，失焦时自动校正，通过 `aria-live` 说明原因 | 前端加上后端 `woocommerce_add_to_cart_validation` 和结账两处复核 |
| **分级定价** | 阶梯表 + 当前档高亮（M09）+ 毛利倍率（PVP ÷ 单价） | 插件价格表：客户组 × 数量阶梯 |
| **RFQ** | 多行（逐行 MOQ 校验）、粘贴清单、上传 CSV；提交后**真实生成**：① 下载 CSV 格式的询价单；② 打开预填好的 `mailto:` 邮件（收件人为你们的销售邮箱，**需要你提供**）；③ 显示编号和状态页。页面上注明"原型：生产环境直接进入后台" | quote 插件 / 自建 REST 端点 → 后台询价单 + 邮件或 WhatsApp Business 通知 |

Newsletter 在 Demo 里**不做**（没有后端就不放）。上线后接 ESP（服务商待定），采用双重确认（double opt-in）。

---

## Part 4 · 推荐

### 推荐：**方案 B "Câmara Escura"**，前提是严格执行 §3.2 的"开灯"分层

**为什么选 B**：
1. **行业默认值是米色加金色**（§1.2），而且两家直接竞争对手就在同一个工业区。A 即使做到顶级，也只是"最精致的米色网站"；B 是整个行业里**唯一的深色品牌**，访客三秒内就能分辨出来，这正是一家上市公司需要的"让同行眼前一亮"。
2. **B 最能兜住现有的素材缺陷**。现有图片亮度从 5 到 231，风格不统一。A 的大图大留白会**放大**这种不统一；B 的暗场和统一的黑色展柜框会把它**收敛**成"画廊挂画"。另外，4 张暗调图在 B 里正好是主角。
3. **"开灯"让 B2B 效率不受牺牲**：PLP、PDP、RFQ 全部是亮场的高效界面，C 的核心交互（表格视图、MOQ 步进、分级价、托盘）作为 B 的工作层组件来实现。采购经理的效率不会因为首页是暗场而受损。
4. **叙事能讲清楚专业内容**：316L、镀层、质检、陈列这些，是三个方案里唯一能讲明白的。竞品全都没讲。

**为什么淘汰 A**：它是三个方案里最安全的，也最接近行业默认。它的核心资产（大图、留白、编辑摄影）恰恰是 LM BIJU **目前最缺的**：没有统一的高端摄影。所以 A 要成立，必须先完成一次完整的补拍。在补拍之前，A 会暴露问题而不是解决问题。

**为什么淘汰 C（作为整站方向）**：它是对 B2B 客户最实用的方案，但**公开页面没有品牌冲击力**，把珠宝缩成 64px 的缩略图，不符合"上市公司、高端、眼前一亮"这个前提。C 的交互规格没有被丢弃，而是**全部并入 B 的亮场工作层**。所以淘汰的是 C 的视觉方向，不是 C 的功能。

**B 的风险与护栏**（执行时强制执行）：
- 性能预算：首页 LCP < 2.5s（p75 移动端）；Three.js 和帧序列只在对应区块进入视口时加载；`saveData` 或 2G/3G 网络下不加载 3D 和帧序列
- 可访问性：暗场正文对比度 ≥ 11:1（实测 paper-50 在 ink-950 上是 17.50）；聚光和光标在 reduced-motion 或触屏下全部关闭；所有信息**不依赖光标就能看到**
- 3D 只用程序化生成的素圈戒指，**不冒充具体 SKU**
- 如果真机测试里 3D 区块的 INP 超过 200ms，就降级为 360° 图片序列

**如果你不接受 B 的风险**，次选是 **A 的版式 + C 的工作层**，但前提是先完成补拍（摄影规范见 foundations §4.3）。

---

## Part 5 · 执行后的交付（等"执行"命令）

- `proposals/demo-a.html`、`proposals/demo-b.html`、`proposals/demo-c.html`：三个单文件 Demo，都能直接打开预览；图片走 `../images/`，视频走转码后的版本
- 需要你确认的依赖：
  - `imageio-ffmpeg`（转码 hero.mp4）
  - `fonttools`（字体子集化）
  - 一张 Poly Haven CC0 HDRI（仅 B 需要）
  - Demo 可以先用 Google Fonts CDN，上线时再改为自托管
- 每个 Demo 生成之后跑一遍 Lighthouse、axe 和 `hallmark` 反 AI 味审查，结果写回 `_research/`
