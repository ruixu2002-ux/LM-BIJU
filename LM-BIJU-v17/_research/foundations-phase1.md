# LM BIJU · 路径一：不依赖竞品的基础方案

> 日期：2026-09-25 · 所有数值在本会话实测（脚本在 scratchpad 里，本文件列出方法）
> 需要和竞品对比的地方统一标 **【待核实·竞品】**，等 `_research/<竞品>/` 材料到位后补齐。

---

## 1. 色彩系统

### 1.0 为什么重做

| 现状 | 问题 |
|---|---|
| `#B08D57`（oklch 66.4% 0.083 77.4） | 白底对比度 3.09、米色底 2.65，不能做文字色；一个颜色承担五种角色 |
| 另有 40 多个写死的米色和灰色 | 色相各不相同（59°–80° 都有），看起来发脏 |
| 你建议的 `#C9A96E` | 放在深色 `#1A1A1A` 上是 7.78，很好；但放在浅色 `#FBF7F4` 上只有 **2.10**，所以同样只能当装饰色 |
| 你建议的 `#1A1A1A` / `#C0C0C0` | 色度为 0 的纯中性色，和暖金放在一起会显得"冷、灰、便宜" |

**设计原则**：所有中性色共享金色的色相（约 75°–80°），色度控制在 0.007–0.018 之间。结果是整套色板看起来像**同一种材质的不同明度**，就像一块金属在不同光照下的样子。银色系（255°）是唯一的冷色，**只在 316L 钢材语境里出现**。

### 1.1 Primitive 层（全部 HEX + OKLCH + WCAG 2.x 对比度实测）

| Token | HEX | OKLCH | 对 paper-50 | 对 ink-900 | 对白 |
|---|---|---|---|---|---|
| ink-950 | `#14120F` | oklch(18.3% 0.007 78.1) | 17.50 | 1.07 | 18.70 |
| ink-900 | `#1C1915` | oklch(21.5% 0.009 75.1) | 16.39 | — | 17.51 |
| ink-800 | `#2A2621` | oklch(27.1% 0.011 73.5) | 14.06 | 1.17 | 15.03 |
| ink-700 | `#3D3832` | oklch(34.4% 0.012 72.4) | 10.86 | 1.51 | 11.60 |
| stone-600 | `#5E574E` | oklch(46.1% 0.017 74.2) | 6.66 | 2.46 | 7.12 |
| stone-500 | `#736B61` | 约 oklch(52% 0.018 73) | **4.91** | 3.34 | 5.24 |
| stone-450 | `#8A8278` | 约 oklch(60% 0.018 74) | 3.54 | **4.62** | — |
| stone-400 | `#A39B90` | oklch(69.3% 0.018 76.1) | 2.57 | 6.38 | 2.75 |
| stone-300 | `#CFC8BD` | oklch(83.5% 0.017 79.3) | 1.55 | 10.55 | 1.66 |
| stone-200 | `#E4DED4` | oklch(90.3% 0.015 80.7) | 1.25 | 13.09 | 1.34 |
| stone-100 | `#F1ECE4` | oklch(94.5% 0.012 79.8) | 1.10 | 14.89 | 1.18 |
| paper-50 | `#FAF7F2` | oklch(97.7% 0.007 80.7) | — | 16.39 | 1.07 |
| white | `#FFFFFF` | oklch(100% 0 0) | 1.07 | 17.51 | — |
| **gold-300**（深底文字金） | `#E2CFA4` | oklch(86.0% 0.060 87.0) | 1.43 | **11.42** | 1.53 |
| **gold-400**（装饰金） | `#CDB079` | oklch(77.0% 0.080 82.9) | 1.95 | **8.41** | 2.08 |
| gold-500（中间调，仅用于图形） | `#B8955A` | oklch(68.9% 0.088 79.6) | 2.63 | 6.24 | 2.81 |
| **gold-700**（浅底文字金） | `#7D5E2C` | oklch(50.3% 0.078 77.3) | **5.60** | 2.93 | **5.98** |
| gold-800（按下 / hover） | `#5E4520` | oklch(40.9% 0.063 75.1) | 8.37 | 1.96 | 8.94 |
| silver-300 | `#C9CCD0` | oklch(84.4% 0.006 255.5) | 1.51 | 10.87 | 1.61 |
| silver-600 | `#6B7077` | oklch(54.3% 0.012 256.7) | 4.67 | 3.51 | 4.99 |
| green-700 / 300 | `#2F6B4F` / `#8FC7A8` | oklch(47.9% .078 161) / (78.2% .073 160) | 5.89 / — | — / 9.09 | |
| amber-700 / 300 | `#8A5A12` / `#E3B868` | oklch(50.9% .103 71) / (80.4% .110 82) | 5.53 / — | — / 9.44 | |
| red-700 / 300 | `#9E2B25` / `#EE9A92` | oklch(46.8% .152 28) / (76.9% .102 26) | 6.95 / — | — / 8.07 | |
| blue-700 / 300 | `#2D5A8C` / `#9DBDE3` | oklch(46.0% .096 253) / (78.8% .065 253) | 6.66 / — | — / 9.02 | |

stone-500 和 stone-450 是为了过 AA 线专门校准出来的，OKLCH 值按插值估算；HEX 和对比度是实测值。

### 1.2 两种金色的职责（硬规则）

| 角色 | Token | 允许的场景 | 禁止的场景 |
|---|---|---|---|
| **装饰金** | gold-400 `#CDB079` | 深底上的细线、分隔符、焦点环、Logo 金箔、深底上的小字（8.41） | **浅底上的任何文字**（1.95）、按钮底色 |
| **文字金** | gold-700 `#7D5E2C` | 浅底上的链接、eyebrow、SKU 高亮、价格锁图标（5.60 / 5.98） | 大面积色块 |
| 深底文字金 | gold-300 `#E2CFA4` | 暗色模式里的链接和强调（对 ink-900 为 11.42） | 浅底 |
| 金色的用量上限 | — | **每屏金色像素不超过 3%**：金色只出现在"这件事重要"的地方 | 按钮、卡片边框、图标描边的默认色 |

主操作按钮用**墨色**（ink-900 底 + paper-50 字，16.39），**不用金色**。奢侈品牌的主按钮几乎都是黑的；金色的按钮只会让人想到"金价回收"。

### 1.3 Semantic 层（亮色 / 暗色映射）

| Semantic token | 亮色 | 暗色 | 实测对比度（亮 / 暗） |
|---|---|---|---|
| `--bg` | paper-50 | ink-950 | — |
| `--surface` | white | ink-900 | — |
| `--surface-sunken` | stone-100 | ink-800 | — |
| `--text` | ink-900 | paper-50 | 16.39 / 17.50 |
| `--text-2` | stone-600 | stone-300 | 6.66 / 11.26 |
| `--text-muted` | stone-500 | stone-400 | 4.91 / 6.81 |
| `--border-hair`（装饰线，不参与对比度要求） | stone-200 | ink-800 | — |
| `--border-control`（输入框边框，需 ≥3:1） | stone-500 | stone-450 | 4.91 / 4.62 |
| `--accent-text` | gold-700 | gold-300 | 5.60 / 12.19 |
| `--accent-decor` | gold-400（仅深底） | gold-400 | — / 8.98 |
| `--focus-ring` | gold-700（2px + 2px offset） | gold-400 | ≥3:1 通过 |
| `--action-bg` / `--action-fg` | ink-900 / paper-50 | paper-50 / ink-950 | 16.39 / 17.50 |
| `--success` | green-700 | green-300 | 5.89 / 9.71 |
| `--warning` | amber-700 | amber-300 | 5.53 / 10.08 |
| `--danger` | red-700 | red-300 | 6.95 / 8.61 |
| `--info` | blue-700 | blue-300 | 6.66 / 9.64 |
| `--material-gold` | gold-700 | gold-300 | 材质标签文字 |
| `--material-steel` | silver-600 | silver-300 | 4.99 / 11.60 |

### 1.4 Component 层（示例）

```css
/* primitives → semantic → component；组件只引用 semantic token */
:root{
  --btn-primary-bg:var(--action-bg); --btn-primary-fg:var(--action-fg);
  --price-lock-fg:var(--text-muted); --price-lock-icon:var(--accent-text);
  --tag-material-gold-fg:var(--material-gold); --tag-material-steel-fg:var(--material-steel);
  --tier-row-active-bg:var(--surface-sunken); --tier-row-active-rule:var(--accent-text);
  --stock-in:var(--success); --stock-low:var(--warning); --stock-out:var(--danger);
}
@media (prefers-color-scheme:dark){ :root:not([data-theme=light]){ /* 只重映射 semantic 层 */ } }
```

### 1.5 禁用清单

- 紫蓝渐变
- 玻璃拟态（`backdrop-filter`）
- 发光按钮（彩色 `box-shadow`）
- 金色渐变文字
- 第二种金色
- 社交平台的品牌色块（改用单色线性图标）

---

## 2. 字体系统

### 2.1 候选实测

测试方法：
- 从 `github.com/google/fonts/ofl/*` 下载原始 TTF
- 解析 `cmap` 表，检查 36 个葡语和排版字符：`ãõçáéíóúâêôàÃÕÇÁÉÍÓÚÂÊÔÀüºª€–—“”‘’«»…`
- 解析 `GSUB` 表，检查 OpenType 特性
- 用 Playwright 渲染样张：`evidence/font-specimen-pt.png`

| 字体 | 许可 | 轴 | 字形数 | 葡语缺字 | x 高/大写高 | tnum | zero | 渲染观察 |
|---|---|---|---|---|---|---|---|---|
| **Fraunces** | OFL 1.1 | opsz 9–144 · wght 100–900 · SOFT · WONK | 625 | 无 | 0.689 | ✗ | ✗ | 在 opsz 144 / wght 300 下，发丝线在屏幕上可见；变音符号贴合字身。**选用** |
| Cormorant Garamond | OFL | wght 300–700 | 975 | 无 | 0.618（x/UPM **0.386**，最小） | ✓ | ✓ | 54px 时 **â ê 的扬抑符浮得明显过高**；默认使用旧式数字，"18K"会渲染成"ı8K"；另外这是当下"AI 奢侈品模板"最常见的字体 |
| Bodoni Moda | OFL | opsz 6–96 · wght 400–900 | 429 | 无 | 0.613 | ✓ | ✗ | opsz 96 下 **A 的发丝线和破折号在屏幕上直接消失**（见样张），不适合屏幕 UI |
| Instrument Serif | OFL | 只有 400（加斜体） | 334 | 无 | 0.708 | ✗ | ✗ | 窄体、有力；但它是 2024 年起创业公司网站的流行字体，AI 味风险高 |
| Newsreader | OFL | opsz 6–72 · wght 200–800 | 565 | 无 | 0.636 | ✓ | ✗ | 适合长文阅读，缺少珠宝感。方案 A 的长文正文**备选** |
| **Inter Tight** | OFL | wght 100–900 | **2505** | 无 | 0.750 | ✓ | ✓ | 字面紧凑，信息密度高；覆盖西里尔和希腊字母，方便扩展到其他欧盟语言。**选用** |
| Geist | OFL | wght 100–900 | 729 | 无 | 0.746 | ✓ | ✗ | 质量好，但辨识度绑定 Vercel 和 SaaS 圈 |
| DM Sans | OFL | opsz 9–40 · wght 100–1000 | 404 | 无 | 0.751 | **✗** | ✗ | **没有等宽数字**，价格列没法对齐，B2B 场景直接淘汰 |
| **JetBrains Mono** | OFL | wght 100–800 | 977 | 无 | 0.753 | 天然等宽 | ✓ | 斜线 0 能区分 O 和 0，SKU 不会看错。**选用** |
| Geist Mono / IBM Plex Mono | OFL | — | 890 / 931 | 无 | — | 天然等宽 | ✗ / ✓ | 备选 |

**Montserrat 当前的体积**：5 个字重，latin + latin-ext 两个子集共 106 KiB，而且两个子集都走 Google 直连。

### 2.2 选型

| 层 | 字体 | 字重 / 轴 | 理由 |
|---|---|---|---|
| **Display** | **Fraunces** | wght 300–400；opsz 自动；`SOFT 0, WONK 0`；斜体只用于编辑体强调 | 高反差、opsz 可变（小字号时自动加粗发丝线）、变音符号位置正确，和竞品及现有 demo 都拉开距离【待核实·竞品字体】 |
| **Body / UI** | **Inter Tight** | 400 / 500 / 600 | 紧凑、有 tnum 和 zero、字形覆盖最广。说实话，它本身是中性字体，品牌个性由 Display 层和排版承担，正文层不需要"有个性" |
| **Mono** | **JetBrains Mono** | 400 / 500 | 用于 SKU、EAN、数量、批次号；斜线 0 |
| 中文 | 系统字体栈（不下载 Web 字体） | — | `"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",sans-serif`；只有 /zh 页面的大标题按需加载 Noto Serif SC 子集。Noto 的 CJK 全量是 MB 级，不适合全站加载 |

**来源与许可**：
- 三款选用字体都是 SIL Open Font License 1.1，允许商用、自托管、子集化
- 源文件：`github.com/google/fonts/tree/main/ofl/{fraunces,intertight,jetbrainsmono}`
- **Web 字体体积实测**（Google Fonts woff2，latin + latin-ext，本会话下载测量）：

| 组合 | 体积 |
|---|---|
| Fraunces（正体 + 斜体，opsz 全轴，wght 300–500） | 273 KiB（4 个文件） |
| Inter Tight 400–600 | 131 KiB |
| JetBrains Mono 400–500 | 42 KiB |

- 葡语页面实际只触发 `latin` 子集，latin-ext 按 unicode-range 按需下载，所以实际首屏体积约为上表的一半（**推测**，执行阶段实测）
- **执行时的预算**：
  - 用 `pyftsubset` 固定 Fraunces 的 opsz 范围，只保留正体
  - 首屏字体 ≤ 120 KiB
  - **全部自托管**：GDPR 考虑，也省掉跨域连接
  - 需要安装 `fonttools`，届时会请你确认

### 2.3 字号阶梯（基准 16px；UI 用 1.25 比例；Display 用 clamp 流体）

| 档 | Token | 字体 | 字号 / 行高 | 字距 | 场景 |
|---|---|---|---|---|---|
| 0 | `--fs-caption` | Inter Tight 500 | 12 / 16 | +0.02em | 标签、法律小字（**全站最小字号 12px**） |
| 1 | `--fs-small` | Inter Tight 400 | 14 / 20 | 0 | 卡片元信息、表格 |
| 2 | `--fs-body` | Inter Tight 400 | 16 / 26 | 0 | 正文 |
| 3 | `--fs-lead` | Inter Tight 400 / Fraunces 300 斜体 | 20 / 30 | 0 | 导语、引文 |
| 4 | `--fs-h4` | Inter Tight 600 | 25 / 32 | −0.01em | UI 小标题、价格 |
| 5 | `--fs-h3` | Fraunces 400 | 31 / 38 | −0.01em | 产品名（PDP） |
| 6 | `--fs-h2` | Fraunces 300 | clamp(39px, 4.2vw, 61px) / 1.05 | −0.015em | 区块标题 |
| 7 | `--fs-display` | Fraunces 300，opsz 144 | clamp(56px, 8.5vw, 128px) / 0.95 | −0.025em | Hero（每页最多出现一次） |
| — | `--fs-eyebrow` | Inter Tight 500 大写 | 12 / 16 | +0.14em | **全站唯一的大写样式** |
| — | `--fs-mono` | JetBrains Mono 400 | 13 / 20 | 0 | SKU / EAN / 数量 |

数字规则：
- 所有价格和数量加 `font-variant-numeric: tabular-nums lining-nums`
- **Fraunces 不用于显示任何数字**：它没有 tnum
- 价格格式：`1.234,50 €`，符合 pt-PT 规范，用 `Intl.NumberFormat('pt-PT',{style:'currency',currency:'EUR'})` 生成

### 2.4 中英葡混排

- 用 `lang` 属性切换字体栈：`:lang(zh){font-family:var(--font-zh)}`。拉丁字符仍走 Inter Tight，CJK 字符回落到系统字体，行高提高到 1.75
- 中文里夹带 SKU 或数字时，拉丁部分自动由 Inter Tight 渲染，两侧不加空格（由 `text-autospace` 支持时处理，**推测**：浏览器支持度有限，执行阶段测试）
- 葡语长单词（"Hipoalergénico"、"responsabilidade"）在窄栏里断行：`hyphens:auto` 加 `lang="pt-PT"`；Chromium 已支持葡语连字符字典（**推测**，执行阶段测试）
- 不要对葡语使用 `text-transform:uppercase` 的大段文字，大写会弱化变音符号的辨识度。大写只保留给 eyebrow

---

## 3. 视频方案（hero.mp4）

### 3.1 现状（容器解析实测）

| 属性 | 值 |
|---|---|
| 编码 | H.264 High @ L4.2 |
| 分辨率 | **1080 × 1920 竖屏** |
| 帧率 | **59.94 fps** |
| 时长 | 28.7 s |
| 码率 | 约 5.0 Mbps |
| 大小 | 18.08 MB |
| 关键帧 | 12 个 |
| 音轨 | **含 AAC 音轨**（无用） |

**问题排序**：
1. **竖屏素材放在横屏容器里**：桌面端只显示 28% 的画面高度，还放大了 1.33 倍
2. 60fps 对慢节奏的珠宝画面毫无必要
3. 音轨是冗余字节
4. 28.7 秒太长，作为循环背景用 8–12 秒足够

### 3.2 编码参数（目标值）

以下体积是按码率 × 时长**推算**的，执行阶段转码后再实测。

| 输出 | 编码 | 分辨率 | fps | 码率 / 质量 | 12 秒体积（推算） | 用途 |
|---|---|---|---|---|---|---|
| hero-portrait.av1.mp4 | AV1（libsvtav1 preset 6，CRF 36，`-g 60`） | 720 × 1280 | 24 | 约 0.7 Mbps VBR | 约 1.0 MB | Chrome / Firefox / Edge / Safari 17+（仅限带硬件 AV1 解码的机型，**推测**） |
| hero-portrait.hevc.mp4 | HEVC（x265 CRF 28，`-tag:v hvc1`） | 720 × 1280 | 24 | 约 0.9 Mbps | 约 1.35 MB | Safari 回退 |
| hero-portrait.h264.mp4 | H.264 High @ 4.0（CRF 24，maxrate 1.6M，bufsize 3.2M，`-g 48`，`-pix_fmt yuv420p`，`-movflags +faststart`） | 720 × 1280 | 24 | ≤ 1.6 Mbps | ≤ 2.4 MB | 通用回退 |
| hero-portrait-m.h264.mp4 | H.264 Main | 540 × 960 | 24 | ≤ 0.8 Mbps | ≤ 1.2 MB | 手机 |
| hero-poster.avif | AVIF q50 | 1080 × 1350（4:5 裁切） | — | — | ≤ 60 KB | **这才是 LCP 元素**，视频不参与 LCP |

所有输出都要：
- `-an` 去掉音轨
- 选一个 8–12 秒可无缝循环的片段（首尾帧用交叉淡化或选同构帧）
- 需要安装完整版 ffmpeg（`pip install imageio-ffmpeg`，或者用 static build）。容器里 Playwright 自带的 ffmpeg 是精简版，读不了 H.264。**执行时会请你确认安装**

```bash
# 示例（执行阶段才运行）
ffmpeg -ss 00:00:04 -t 12 -i hero.mp4 -an -vf "scale=720:-2:flags=lanczos,fps=24" \
  -c:v libx264 -profile:v high -level 4.0 -crf 24 -maxrate 1.6M -bufsize 3.2M -g 48 \
  -pix_fmt yuv420p -movflags +faststart hero-portrait.h264.mp4
```

### 3.3 竖屏素材的正确用法（关键）

**不要**再做横向全屏视频 Hero。竖屏素材应该放进**竖向画框**：
- 桌面端：做非对称分栏，视频占 5/12 栏宽，比例 4:5 或 9:16；另外 7/12 放标题和 B2B 入口（线框见 §5.1）
- 手机端：竖屏素材天然适合全屏
- 如果一定要横向全出血，**需要补充**横版原片（16:9 或 21:9，至少 2560 宽）

### 3.4 加载与降级策略

| 条件 | 行为 |
|---|---|
| 默认 | `<video preload="none" muted playsinline loop poster="hero-poster.avif">`，LCP 完成之后，在 `requestIdleCallback` 里设置 `src` 并调用 `play()` |
| `navigator.connection.saveData` 或 `effectiveType` 为 2g / 3g | 不加载视频，只显示海报 |
| `prefers-reduced-motion: reduce` | 只显示海报，并提供"播放"按钮 |
| 视频滚出视口（IntersectionObserver）或页面隐藏（visibilitychange） | 暂停 |
| 手机宽度 ≤ 640 | 用 540p 源；电量低时不自动播放（无法检测，放弃） |
| 播放 / 暂停控件 | 必须有，WCAG 2.2.2 要求能暂停自动播放超过 5 秒的内容 |

`<source>` 按 `type="video/mp4; codecs=av01.0.05M.08"` → `hvc1` → `avc1` 的顺序排列，浏览器会自动选第一个能播的。

---

## 4. 图片重新分配与处理管道

### 4.1 17 张图的实际内容（目检，证据：`evidence/images-contact-sheet.jpg`）

| # | 文件 | 实际内容 | 尺寸 / 比例 | 平均亮度 | 判定 |
|---|---|---|---|---|---|
| 0 | anel-solitario | 陶土色背景上的两只手，戴细戒指（产品很小） | 900×1600 · 9:16 | 102 | **氛围图**，不能当产品卡 |
| 1 | argolas-pave | 粗款金色圈耳环两对（一对在深色盒里，一对在白台面上） | 900×1200 · 3:4 | 109 | 产品 ✓ |
| 2 | brincos-safira | 白色波浪托盘上的珍珠小圈耳环 | 1200×1200 · 1:1 | 196 | 产品 ✓（文件名写"蓝宝石"，与内容不符） |
| 3 | cat-aneis | 白色卵石上两个细金圈（**推测**：细圈戒指或细圈耳环） | 900×1350 · 2:3 | 172 | 产品 ✓（不是"拉丝钢"） |
| 4 | cat-brincos | 粉色毛绒上的仿大理石圆片耳环 | 900×675 · 4:3 | 177 | 产品 ✓ |
| 5 | **cat-colares**（未引用） | 奶白毯子上一只碗，里面是金链和**蓝眼睛（olho grego）串珠** | 900×1200 · 3:4 | 147 | 产品 ✓，**非常适合旅游纪念品店客群** |
| 6 | cat-homem | 男士黑夹克，佩戴金链和**十字架吊坠** | 1200×1600 · 3:4 | 31 | 男士项链 ✓（不是手链） |
| 7 | cat-loja | 木碗、手镯、戒指、吊坠的平铺摆拍 | 900×600 · 3:2 | 173 | 陈列 / 氛围 ✓（不是"三层展架"） |
| 8 | cat-moda | 手表、皮表带、手机、墨镜的棕色平铺 | 900×506 · 16:9 | 37 | 手表与男士配件 ✓（**不是包装套装**） |
| 9 | **cat-pulseiras**（未引用） | 针织毛衣上的**"love"字样戒指**（**推测**：戒指，不是手链） | 900×1109 · ≈4:5 | 108 | 产品 ✓ |
| 10 | cat-relogios | 皮夹上的钢带（米兰尼斯网带）手表 | 900×1350 · 2:3 | 54 | 产品 ✓ |
| 11 | colar-topazio | 玻璃圆盘加亚麻布上的细金链 | 900×1350 · 2:3 | 152 | 产品 ✓ |
| 12 | hero-aco | 纯黑背景上的银色古巴链 | 1200×1800 · 2:3 | **5** | 产品 ✓，316L 男士 |
| 13 | hero-ouro | 白色碎石上的金色镶钻戒指 | 900×1350 · 2:3 | 196 | 产品 ✓ |
| 14 | hero-still | 奶油色背景上纵向排列的 7 枚彩色宝石戒指 | 900×1125 · 4:5 | 231 | 产品 / 编辑图 ✓ |
| 15 | **pendente-halo** | 带 **"EMIZA JEWELLERY"** 字样的礼盒、名字项链、K 字母吊坠 | 900×1125 | 189 | **❌ 三个 Demo 全部弃用** |
| 16 | pulseira-rosa | 玻璃托盘上的金色链条手链、吊饰，加圈耳环 | 900×1350 · 2:3 | 187 | 产品 ✓ |

### 4.2 Demo 用的 SKU 与图片对应（修正图文不符）

| SKU | 原名 → **新名** | 图片 | 变更 |
|---|---|---|---|
| LB-1001 | Anel Fino Empilhável → **Anel Pavé Dourado** | hero-ouro | 原图 anel-solitario 改作氛围图 |
| LB-1002 | Colar Corrente Fina Dourada | colar-topazio | 不变 |
| LB-1003 | Argolas Douradas Polidas → **Argolas Largas Polidas** | argolas-pave | 名称对齐画面 |
| LB-1004 | Conjunto Brincos e Pulseira | pulseira-rosa | 不变，但**只此一处使用** |
| LB-1005 | Pendente Dourado → **Colares Olho Grego — Mix** | **cat-colares** | 替换 EMIZA 图；启用未引用图 |
| LB-1006 | Brincos de Pérola Clássicos | brincos-safira | 不变（建议文件改名 `brincos-perola.jpg`） |
| LB-1007 | Conjunto Private Label → **Anéis Zircónia Cor — Série 7** | hero-still | 名称对齐画面（彩色锆石正好是产品线之一） |
| LB-1008 | Relógio Couro & Aço → **Relógio Bracelete Milanesa** | cat-relogios | 画面是网带，不是皮带 |
| **LB-1009** | Pulseira de Elos — Homem → **Fio com Cruz — Homem** | cat-homem | **修正图文不符** |
| LB-1010 | Brincos Mármore Banho de Ouro | cat-brincos | 不变 |
| **LB-1011** | Anéis Aço Escovado — Pack 3 → **Anéis Finos Lisos — Par** | cat-aneis | **修正图文不符**（画面是金色抛光细圈） |
| **LB-1012** | Pulseira Tennis → **Anel Script "Love"** | **cat-pulseiras** | **修正**：不再和 LB-1004 共用一张图；启用未引用图 |
| LB-1013 | Corrente Cubana — Homem（316L） | hero-aco | 不变 |
| LB-2001 | Expositor de Montra em Madeira → **Taça de Madeira para Montra** | cat-loja | 名称对齐画面（**推测**：画面里是木碗，不是展架） |
| **LB-2002** | Kit de Embalagem Kraft → **Relógio + Braceletes Intercambiáveis** | cat-moda | **修正**：当前**没有任何包装类图片** |
| — | 氛围 / 编辑用图 | anel-solitario | 方案 A 的"关于"章节、方案 B 的转场用图 |

**合计使用 16 张**（全部，除 pendente-halo），cat-colares 和 cat-pulseiras 都已启用。

**需要补拍或补图**（Demo 里用"待拍摄"占位，**不用 AI 生成图冒充产品**）：
- 包装套装（Kraft 盒、袋、卡片）
- 门店展架（多层 / 丝绒）
- 网球手链
- 男士手链
- 316L 拉丝戒指
- 白底标准产品照（全部 SKU）

### 4.3 摄影规范（给补拍用）

| 项目 | 规范 |
|---|---|
| 镜头 | 全画幅 90–105mm 微距（APS-C 用 60mm）；光圈 f/8–f/11，**加景深合成**（5–15 张），否则戒指前后无法同时清晰 |
| 光源 | 连续 LED，5500K，**CRI ≥ 95 / TLCI ≥ 95**；柔光箱或柔光棚 + 黑白反光卡控制金属反射（金属的"质感"来自反射里的黑白边，不是来自亮度） |
| 背景 | 两条线分开拍：① **标准照**：纯白无缝（`#FFFFFF`，兼容 Google Merchant 和各电商平台）；② **编辑照**：统一的石材或亚麻道具库，限定 3 种色调（暖石、米亚麻、深墨） |
| 构图 | 标准照统一 4:5，产品占画面宽度 60–70%，底部阴影一致；每个 SKU 拍 5 个角度：正面、45°、细节微距、上手或上身（示意尺寸）、包装 |
| 输出 | 母版 16-bit TIFF（AdobeRGB）→ 交付 **sRGB 2400×3000 JPEG q90**（4:5）+ 2000×2000（1:1，给平台用）。你要求的 2000×2000 保留作平台版，站内主图用 4:5 |
| 调色 | 一套 LUT 或 preset 管所有图；白平衡锁 5500K；**严禁磨掉金属划痕以外的真实结构**，否则退货纠纷会增加 |
| 命名 | `{SKU}_{角度序号}_{视角}.jpg`，例如 `LB-1003_02_45.jpg` |
| alt 规范 | `{产品名} em {材质}, {视角}`，例如"Argolas largas em aço 316L com banho de ouro 18K, vista a 45°"。装饰图 `alt=""` |

### 4.4 处理管道（sharp 本会话试跑实测）

```
上传（WP 媒体库 / 母版目录）
  → sharp：rotate() 按 EXIF 纠正方向 → 去除 EXIF 和 GPS，保留 sRGB ICC
  → fit:cover + position:'attention'（智能焦点裁切）→ 4:5
  → 宽度 320 / 480 / 640 / 960 / 1280 / 1600（withoutEnlargement:true）
  → AVIF q50 effort 6 ｜ WebP q78 ｜ JPEG mozjpeg q80 progressive
  → 主色 + 16px LQIP（sharp stats() 取值，作为占位背景）
  → CDN（长缓存 immutable + 内容哈希文件名）
```

**实测**（17 张原图，裁成 960×1200，4:5）：

| 格式 | 总体积 | 相比原图 |
|---|---|---|
| 原 JPEG | 1765 KiB | — |
| AVIF | **581 KiB** | −67% |
| WebP | 959 KiB | −46% |
| mozjpeg q80 | 约 1.3 MiB | — |

单张示例：`cat-pulseiras` 从 194K 降到 80K（AVIF 960）；`hero-still` 从 40K 降到 13K。

**注意**：原图最大只有 900–1200px 宽，**1280 和 1600 两档会被 withoutEnlargement 截掉**。Retina 大图需要补拍的高分辨率原片。

```html
<picture>
  <source type="image/avif" srcset="/img/lb-1003-480.avif 480w, /img/lb-1003-960.avif 960w" sizes="(min-width:1200px) 22vw, (min-width:768px) 33vw, 50vw">
  <source type="image/webp" srcset="/img/lb-1003-480.webp 480w, /img/lb-1003-960.webp 960w" sizes="(min-width:1200px) 22vw, (min-width:768px) 33vw, 50vw">
  <img src="/img/lb-1003-960.jpg" width="960" height="1200" loading="lazy" decoding="async"
       alt="Argolas largas polidas com banho de ouro 18K, vista frontal" style="background:#6f6e6b">
</picture>
<!-- LCP 图：loading="eager" fetchpriority="high"，并在 <head> 里 preload imagesrcset -->
```

亮度统一：同一个网格里，底色按亮度分组（亮图组 / 暗图组），**不要**亮暗交错。`hero-aco`（亮度 5）和 `cat-homem`（亮度 31）只放在深色区块。

---

## 5. 布局骨架（信息架构，三个方案通用；视觉表达在 A/B/C 中各不相同）

格式：**当前 → 改进后 → 设计原则**

### 5.1 首页

```
当前（v17）                          改进后
┌─────────────────────────────┐     ┌─────────────────────────────────────────┐
│ 黑色促销条 −50%                 │     │ 顶栏：PT·ES·EN   ·   Área profissional ⟶ │  ← 一行，无促销
│ 🔍     LM BIJU     Login 🛒     │     │ LM BIJU      Coleções  Catálogo  Empresa │
│ 7 项居中导航 + mega           │     │                    Pedido rápido  Entrar │
├─────────────────────────────┤     ├──────────────────────┬──────────────────┤
│                             │     │ 7 栏                  │ 5 栏              │
│   全屏横向视频（竖屏素材硬裁）    │     │ Fraunces display：    │ ┌──────────────┐ │
│   粗体标题 + 两个按钮            │     │ "Joias por grosso,    │ │ 竖屏视频 4:5    │ │
│   底部模糊条 + 假轮播            │     │  para quem as vende." │ │ （原素材合理用法）│ │
│                             │     │ 1 行说明 · 1 个主 CTA   │ └──────────────┘ │
├─────────────────────────────┤     │ + 次级文字链          │ caption·SKU mono │
│ 信任四格（Shopify 模板）       │     ├──────────────────────┴──────────────────┤
├─────────────────────────────┤     │ 材质索引（不是瓦片）：                         │
│ 3 块等高图片瓦片 + 金色标签     │     │ Ouro 18K ─── Banho 18K ─── Aço 316L ─── │
├─────────────────────────────┤     │ Pérola ─── Zircónia ─── Relógios       │  ← 文字列表 + hover 预览图
│ 5 列 × 2 行产品网格             │     ├────────────┬────────────┬───────────────┤
├─────────────────────────────┤     │ 大图 1 件    │ 2 件叠放     │ 数据块：         │
│ 钢分栏 · 深色三步分栏          │     │ （编辑式不对称）│            │ MOQ 从 6 件起     │
│ newsletter · 超长 footer      │     │            │            │ 48h 发往 PT 大陆  │
└─────────────────────────────┘     ├────────────┴────────────┴───────────────┤
                                    │ 客户类型切换：Loja | Online | Turismo | Nova │  ← 替代"三问卡"
                                    │ → 每类显示对应系列与起订方案                  │
                                    ├─────────────────────────────────────────┤
                                    │ 门禁说明（一次，不重复）：注册→验证→价格      │
                                    │ + 内联注册入口（NIF 字段直接在此）            │
                                    ├─────────────────────────────────────────┤
                                    │ Showroom Varziela（地图/照片/预约）          │
                                    │ 精简 footer（法定信息 + Livro Reclamações）  │
                                    └─────────────────────────────────────────┘
```

**设计原则**：
- **节奏**：区块间距在 120 / 64 / 200px 之间变化，打破统一的 66px
- **一屏一件事**
- 视频放进竖框
- 材质索引用**文字**驱动，不用图片瓦片
- B2B 信息（MOQ、配送时效、门禁）作为"数据"呈现，不作为"卖点"呈现
- **竞品对比**：【待核实·竞品】

### 5.2 产品列表页（Catálogo）

```
当前                                  改进后
┌─────────────────────────────┐     ┌─────────┬───────────────────────────────┐
│ 页头 + 4 图瓦片（重复首页）      │     │ 筛选侧栏  │ 面包屑 · "Brincos" · 128 refs       │
│ chips 单选 8 项                │     │ ─────── │ 排序 ▾   视图 [▦ 网格][☰ 列表]   │
│ 5 列卡片，button 包整卡          │     │ Família  │ ─────────────────────────────── │
│ 卡片：图/名/SKU/RRP/锁           │     │ Material │ ┌────┐┌────┐┌────┐┌────┐       │
│                             │     │ ☐ Ouro18K│ │ 4:5 ││    ││    ││    │       │
│                             │     │ ☐ Banho  │ │     ││    ││    ││    │       │
│                             │     │ ☐ 316L   │ └────┘└────┘└────┘└────┘       │
│                             │     │ Preço PVP│ Nome (Inter 14)                   │
│                             │     │ MOQ ≤ 6  │ LB-1003 (mono) · [Banho 18K]      │
│                             │     │ Stock ✓  │ PVP 15,50 €                       │
│                             │     │ Novidade │ 访客：🔒 Preço de revenda → Entrar  │
│                             │     │         │ 登录：9,20 € · MOQ 6 · [−][6][+] ⊕ │
│                             │     │         │      ● Em stock  · + RFQ          │
│                             │     │         │ 列表视图 = 表格：SKU|名|材质|MOQ|     │
│                             │     │         │   阶梯价|库存|数量输入 → 批量加入      │
└─────────────────────────────┘     └─────────┴───────────────────────────────┘
```

**设计原则**：
- 筛选支持**多选**，状态写进 URL，用 `aria-live` 播报结果数
- 网格和表格两种视图（C 方案默认表格）
- 卡片是 `article`，标题是 `a`，快速查看是独立按钮
- 价格区块**由服务端按角色输出**：访客收到的 HTML 里**没有**批发价字段
- 数量输入的 step 等于 MOQ

### 5.3 产品详情页（当前**不存在**，只有快速查看弹窗）

```
┌──────────────────────────────┬──────────────────────────────┐
│ 图库：主图 4:5                   │ Brincos · Banho de ouro 18K     │  eyebrow
│ ┌──────────────────────────┐ │ Argolas Largas Polidas          │  Fraunces h3
│ │                          │ │ LB-1003 · EAN 560…  [复制]       │  mono
│ │  hover：微距放大镜          │ │ ───────────────────────────── │
│ │  drag：角度切换（若有 5 角度）│ │ PVP recomendado  15,50 €        │
│ └──────────────────────────┘ │ ┌ 访客 ───────────────────────┐ │
│ [正][45°][细节][上身][包装]     │ │ 🔒 Preço de revenda,         │ │
│                              │ │   escalões e stock: Entrar    │ │
│                              │ │   [Criar conta profissional]  │ │
│                              │ └───────────────────────────────┘ │
│                              │ ┌ 登录后 ──────────────────────┐ │
│                              │ │ Qtd      Preço/un   Margem    │ │
│                              │ │ 6–23     9,20 €     1,7×      │ │
│                              │ │ 24–95 ▶  8,40 €     1,8×      │ │  当前档高亮
│                              │ │ 96+      7,60 €     2,0×      │ │
│                              │ │ [−][ 24 ][+]  MOQ 6 · ×6      │ │
│                              │ │ [Adicionar à encomenda]        │ │
│                              │ │ [+ Pedido de proposta]         │ │
│                              │ │ ● 340 em stock · envio 48h    │ │
│                              │ └───────────────────────────────┘ │
│                              │ Especificações（表格）：材质/尺寸/  │
│                              │ 重量/扣型/镍释放/包装单位/产地     │
├──────────────────────────────┴──────────────────────────────┤
│ 同系列（横向滚动）· 常一起下单 · 陈列建议（配套展架）                │
└─────────────────────────────────────────────────────────────┘
```

**设计原则**：
- 规格表**必须有"镍释放"一项**：欧盟 REACH 附录 XVII 第 27 条对穿刺类和长时间接触皮肤的首饰有镍释放限值，零售商会问
- "Margem"（毛利倍率）按 PVP 除以阶梯价计算。这是说服零售商的核心信息【待核实·竞品是否提供】

### 5.4 关于页（Empresa）

```
当前                                  改进后
┌─────────────────────────────┐     ┌─────────────────────────────────────────┐
│ 页头                          │     │ 编辑式开场：一句话 + anel-solitario 竖图      │
│ 三问卡（图+问题+链接）×3        │     ├─────────────────────────────────────────┤
│ 三步分栏（标题不可见 bug）       │     │ 数字带（真实数据，需提供）：成立年·SKU·客户数·   │
│ 保证四格（图标卡）              │     │   日均发货 —— 数字用 Inter Tight tnum        │
│ Showroom 1大2小图 + 信息        │     │ 章节 1 Origem · 2 Controlo de qualidade（316L │
│ newsletter · footer          │     │   检测/镍释放/镀层厚度 μm）· 3 Logística       │
│                             │     │ Showroom：大图 + 预约日历（可选时段）           │
│                             │     │ 合规条：NIF · Livro de Reclamações · RAL      │
│                             │     │ 【若 LM BIJU 为上市公司】投资者关系 · ESG       │
└─────────────────────────────┘     └─────────────────────────────────────────┘
```

**设计原则**：
- 用**可验证的事实**替代"信任图标"
- "三问卡"合并进首页的客户类型切换
- ESG / IR 模块是否需要，取决于上市主体【需要补充】

### 5.5 询盘页（Pedido de Proposta / RFQ，当前**不存在**）

```
┌─────────────────────────────────┬────────────────────────────┐
│ 1 · Itens                        │ Resumo                     │
│ SKU [LB-10__ ▾ 自动补全] Qtd [ 24 ] │ 6 refs · 212 un            │
│ ─ 或 粘贴清单（SKU;Qtd 每行一条）─── │ PVP total 3.140 €          │
│ ─ 或 上传 CSV ──────────────────── │ 预计交期 48–72h             │
│ 表格：SKU | 名 | MOQ 校验 ✓/⚠ | 数量 │ [Enviar pedido]             │
│ 2 · Empresa（已登录则自动填）          │ 提交后：状态页 + 邮件 + 编号   │
│ NIF [ 5xx xxx xxx ] ✓VIES（欧盟客户）  │ RFQ-2026-000123             │
│ 类型：Loja física / Online / Turismo │ 销售 24h 内回复（承诺需确认） │
│ 3 · Observações · 个性化/Private label│                            │
│ ☐ 同意隐私政策（必填，未预勾选）         │                            │
└─────────────────────────────────┴────────────────────────────┘
```

**设计原则**：
- **三种输入方式**：单条添加、粘贴清单、上传 CSV
- MOQ **逐行**校验：前端提示，**后端复核**
- 必须有真实提交、编号和状态反馈，**禁止出现 `onsubmit="return false"`**
- 访客也可以提交 RFQ，这等于是一个获客入口
- 欧盟客户用 VIES 校验增值税号（适用反向征税）

### 5.6 注册门禁流程（五项 B2B 能力的交汇点）

```
访客 ──浏览（仅 PVP）──▶ 注册表单（公司名·NIF·CAE·类型·证明文件·同意）
   │                         │ 服务端：NIF 校验位 + 欧盟 VIES
   │                         ▼
   │                   状态：pending ──人工/规则审批──▶ approved（分配等级：Retalho / Online / Distribuidor）
   │                         │                              │
   ▼                         ▼ 邮件                          ▼
RFQ（无需登录）          "em validação" 页面           价格/阶梯/MOQ/库存 由服务端按等级输出
                                                      下单：MOQ + step 后端复核（add_to_cart & checkout 双钩子）
```

---

## 6. 从 Demo 到 WordPress 的迁移路径

### 6.1 技术选型对比

| 维度 | ① 继续静态 | ② WordPress + WooCommerce + 自定义 Block Theme（**推荐**） | ③ Headless：WP/Woo + WPGraphQL + Next.js |
|---|---|---|---|
| 服务端隐藏批发价 | **做不到** | ✓ B2B 插件和 PHP 钩子原生支持 | ✓ 但要在 GraphQL resolver 里自己实现角色裁剪 |
| MOQ / 分级定价 / 注册审批 | ✗ | ✓ 插件现成 | 要把插件逻辑搬到 API 层，大部分 B2B 插件**不暴露 GraphQL 字段**（推测，需逐个核实） |
| 结账（MB Way / Multibanco / 发票） | ✗ | ✓ 葡萄牙本地支付和认证发票插件基于 Woo 结账（插件名见 6.2） | 要重写结账，或跳回 Woo 结账页，体验割裂 |
| 高端动效（GSAP / Lenis / WebGL） | ✓ | ✓ 在主题里用 enqueue 按页加载 | ✓ 最灵活 |
| 性能 | 最好 | 访客页面**可以全页缓存**（价格本来就不给访客看，所以访客 HTML 对所有人都一样）；登录用户走对象缓存 | 好，但需要 ISR 加上按用户的动态区块 |
| 团队与维护 | — | 葡萄牙本地 WP 开发者多、成本低（推测） | 需要 React 加 WP 双栈，成本高 |
| 供应商锁定 | 低 | 中（B2B 插件） | 中高（Vercel 或同类托管、WooGraphQL 维护节奏） |
| 结论 | 只能做展示 | **B2B 功能与视觉兼顾，风险最低** | 视觉上限更高，但 B2B 部分要重造轮子，**性价比低** |

**诚实补充**：如果不限定 WordPress，**Shopify Plus 的 B2B 功能**（公司账户、目录价、数量规则）是原生的，开发量更小。代价是平台锁定和月费，而且葡萄牙的认证发票要靠第三方应用。你指定了 WordPress，所以只作为风险对照列出。

### 6.2 推荐栈（②）

| 层 | 选择 | 备注 |
|---|---|---|
| CMS / 电商 | WordPress 6.x + WooCommerce（HPOS） | — |
| 主题 | 自研 Block Theme（`theme.json` 由 Token 生成）+ 少量 PHP 模板（产品卡、价格区块） | 不用 Elementor 之类的页面构建器（性能差、锁定强） |
| B2B | **B2BKing** 或 **Wholesale Suite**（二选一，**执行前核实**当前版本、许可价格和 HPOS 兼容性） | 需要覆盖：角色隐藏价格、分级价、MOQ / step、注册字段加审批、询价 |
| 询价 | B2B 插件自带的 quote 功能，或 YITH Request a Quote | 要能粘贴清单或导入 CSV，需自定义 |
| 支付 | ifthenpay 或 Eupago（MB Way、Multibanco 参考号）、银行转账、Stripe（卡） | 插件名称**需核实**当前维护状态 |
| 发票 | 连接 AT 认证的开票软件（InvoiceXpress / Moloni / Vendus 等） | 葡萄牙法律要求认证开票软件；**具体取决于 ERP**【需要补充 ERP 状态】 |
| 多语言 | WPML（功能全，付费）或 Polylang Pro | 5 种语言 + hreflang |
| 税务 | 欧盟 VIES 校验 + 反向征税规则（西班牙、法国的 B2B 客户） | — |
| 缓存 / CDN | 服务器页面缓存（访客）+ Redis 对象缓存 + CDN（图片 AVIF） | 欧盟节点 |
| 同意管理 | Complianz 或 CookieYes（IAB TCF v2.2） | 字体自托管后，第三方请求会更少 |
| 动效 | GSAP 3（2025 年起在 Webflow 名下**全部免费，含插件**，许可为 GSAP Standard License，不是 OSI 开源）+ Lenis（MIT）+ Three.js（MIT，仅方案 B） | 按页面条件加载 |

### 6.3 迁移步骤

1. **设计定稿**（Figma）：选定 A、B、C 中的一个方向；定稿 Token（色彩、字体、间距、圆角、阴影、动效时长和缓动）
2. **组件拆分**：Header、导航、Hero 变体、材质索引、产品卡（访客态 / 登录态）、价格区块（阶梯表）、数量输入（MOQ）、RFQ 行、筛选侧栏、表格视图、Footer（法定信息）。**每个组件都要有访客态、登录态和错误态**
3. **主题开发**：Block Theme 骨架 → `theme.json`（由 Style Dictionary 生成）→ 用 PHP 渲染产品卡和价格区块（服务端判断角色）→ 自定义区块（材质索引、客户类型切换）→ 按页加载 GSAP 和 Lenis
4. **B2B 配置**：客户组、价格表、MOQ 规则、注册字段（NIF / CAE / 证明）、审批流、邮件模板（5 种语言）、询价流程
5. **数据迁移**：SKU 主数据（需要从 ERP 导出 CSV）→ WP All Import 或 WooCommerce CSV 导入 → 分类（材质 × 品类双轴：品类用分类，材质用属性）→ 图片按 `{SKU}_{序号}` 自动关联 → 变体
6. **SEO**：
   - 用 Yoast 或 Rank Math（选一）生成 sitemap
   - JSON-LD：Organization、LocalBusiness（showroom）、Product（**访客态不输出 offers 批发价**，只输出 PVP 或不输出价格）、BreadcrumbList
   - hreflang
   - 旧 URL 做 301
   - Core Web Vitals 预算：LCP < 2.5s、INP < 200ms、CLS < 0.1（移动端 p75）
7. **合规**：
   - Livro de Reclamações Eletrónico 链接（强制）
   - RAL 争议解决机构信息
   - 隐私政策与 Cookie 政策（CNPD）
   - 条款：B2B 专用、最低订单、退货
   - 同意日志
   - 无障碍：欧洲无障碍法（EAA）自 2025-06-28 起适用于面向消费者的电商服务；纯 B2B 是否在适用范围内**需法律确认**，但按 WCAG 2.2 AA 做成本很低，建议直接达标
8. **测试与上线**：
   - Playwright E2E：注册 → 审批 → 登录见价 → MOQ 拒绝 → 下单 → 询价
   - 安全测试：访客抓 HTML 和 REST（`/wp-json/wc/store/products`）**不能拿到批发价**
   - axe 零严重问题
   - Lighthouse CI 预算
   - 负载测试
   - 灰度上线 + 回滚预案

### 6.4 设计 Token 同步

```
Figma Variables（Primitive / Semantic 两个集合，Light/Dark 两个 mode）
   │ 导出：Tokens Studio 插件（免费档可导出 JSON）或 Figma Variables REST API
   │       （REST 的变量接口需要 Enterprise 方案——需核实你们的 Figma 方案）
   ▼
tokens/*.json（W3C DTCG 格式，进 git）
   │ Style Dictionary v4（CI 中运行）
   ├──▶ build/tokens.css      （CSS 自定义属性：Demo / 主题共用）
   ├──▶ theme.json 片段       （WP 全局样式：palette / fontSizes / spacing —— 编辑者只能选品牌值）
   └──▶ build/tokens.js       （GSAP 时长与缓动常量）
CI：Token PR → 构建 → 可视回归截图对比（Playwright）→ 合并
```

### 6.5 3–5 年生命周期评估

| 组件 | 3–5 年判断 | 锁定风险 | 降级方案 |
|---|---|---|---|
| WordPress 核心 | 稳定，份额最大的 CMS，社区极大 | 低（GPL，可自托管） | — |
| WooCommerce | 稳定（Automattic 主导），HPOS 迁移已完成 | 低到中 | 数据是标准 MySQL，可以导出 |
| Block Theme / FSE | 核心方向，API 仍在演进 | 低 | PHP 模板兜底 |
| B2B 插件 | **单一供应商风险最高**：更新停滞，或者和 Woo 大版本不兼容 | 中 | 价格规则**同时存进 SKU 元数据或 CSV**；关键逻辑（隐藏价格、MOQ 复核）用自写的小插件实现，只把 UI 部分交给第三方 |
| WPML / Polylang | 稳定，付费 | 中 | 翻译可以导出成 XLIFF |
| GSAP | 被 Webflow 收购后免费，但许可证不是开源 | 中低 | 动效层可以换成 Motion One（MIT）或 CSS 滚动驱动动画 |
| Lenis / Three.js | MIT，活跃 | 低 | 可以直接删掉（渐进增强，没有它们网站照样能用） |
| 托管 | 选欧盟机房的托管 WP | 低 | 标准 LAMP，可以整站迁移 |
| （若选 ③）Next.js / WPGraphQL | Next.js 升级节奏快；WPGraphQL 已成为 WordPress.org 规范插件（推测，需核实）；WooGraphQL 由社区维护，节奏较慢 | 中高 | 保留 Woo 原生结账作为兜底 |

---

## 7. Skills / Agents / Obsidian / Harness 工作流

### 7.1 Skills（本会话实际可用 → 本项目用途）

| Skill | 用途 | 阶段 |
|---|---|---|
| `hallmark` | 反 AI 味审计（已用来建 1.2 清单）；A/B/C 生成后再审一遍 | 设计、审查 |
| `ai-design-stack` | 竞品材料到位后，走"扒结构 → 抽设计语言 → 骨架 → 动效 → 体检"流程 | 竞品分析、Demo 生成 |
| `scroll-scrub-hero` | 方案 B 的滚动逐帧 Hero（视频抽帧后用 canvas 播放） | Demo B |
| `code-review` | 审查三个 Demo 和后续主题代码 | 执行后 |
| `opengraph-twitter-cards` | Demo 与正式站的 OG 标签 | 执行后 |
| `artifact-design` | 报告或 Demo 需要发布成私有网页时使用 | 按需 |
| `session-start-hook` | 给仓库加 SessionStart 钩子，让云端新会话自动安装 lighthouse、sharp、axe | 建议现在就做 |
| `skill-creator` | 创建下面两个项目专用 Skill | 执行后 |
| `zora` / `obsidian-memory` / `harness-repos` | 依赖的 MCP 未连接，本会话只能遵循方法论 | 连接后 |

**建议新建的 Skill 模板**：`.claude/skills/lm-biju-brand/SKILL.md`

```markdown
---
name: lm-biju-brand
description: LM BIJU 品牌与 B2B 规则。在为 LM BIJU 写任何页面、组件、文案、图片 alt 或产品数据前加载。
---
# 必须遵守
- Token：只用 tokens/*.json 生成的变量；金色 gold-400 禁止在浅底做文字；主按钮用墨色
- 字体：Fraunces（Display，不用于数字）/ Inter Tight（UI，tnum）/ JetBrains Mono（SKU）
- 最小字号 12px；全站唯一大写样式 = eyebrow
- B2B：批发价只由服务端按角色输出；MOQ 前后端双校验；禁止假表单
- 图片：禁用 pendente-halo.jpg；alt = "{产品} em {材质}, {视角}"
- 文案：pt-PT（非 pt-BR）；禁止 "até −50%"、"vende por si" 类话术
# 检查清单
- [ ] axe 零 serious  - [ ] 访客 HTML 无批发价  - [ ] reduced-motion 降级
```

第二个 Skill `wp-b2b-qa`：按照 §6.3 第 8 步写成可执行的检查脚本，每次提交 PR 前运行。

### 7.2 Agents 分工（本会话可用：general-purpose / Explore / Plan / claude-code-guide）

| 角色 | 实现方式 | 输入 → 输出 | 调用时机 |
|---|---|---|---|
| 设计分析 | 4 个 general-purpose 并行，每家竞品一个 | `_research/<竞品>/`（HAR、HTML、截图）→ 统一模板的分析 md | 竞品材料到位后 |
| 代码生成 | 3 个 general-purpose 并行，每个方案一个，**用 worktree 隔离** | 方案规格 + Token → `proposals/demo-{a,b,c}.html` | 你发"执行"后 |
| 审查 | general-purpose 加载 `hallmark` + `code-review` | Demo → P0/P1/P2 清单 | 每个 Demo 生成后 |
| SEO | general-purpose（WebSearch 只能查美国区结果，葡语关键词数据**会偏**，建议另配 Google Keyword Planner 或 Semrush 的导出） | 关键词表、结构化数据草稿 | 设计定稿后 |
| 架构 | Plan | 主题和插件的实施计划 | 迁移启动时 |

本地自定义 Agent 模板（`.claude/agents/design-critic.md`）：

```markdown
---
name: design-critic
description: 以 LM BIJU 品牌规则审查页面截图与代码，输出 P0/P1/P2。
tools: Read, Grep, Glob, Bash
---
你是高端珠宝 B2B 网站的设计审查员。先加载 lm-biju-brand skill。
每条问题必须给出：证据（文件:行号 或 截图坐标）→ 影响 → 修复。不确定标“推测”。
```

### 7.3 Obsidian vault 结构（由你在本地连接后执行）

```
LM-BIJU/
├── 00-Inbox/
├── 10-竞品/            Shebiju.md · Cellibiju.md · Grupobelle.md · Maxbiju.md · 对比矩阵.md
├── 20-设计系统/        色彩.md · 字体.md · 间距.md · 动效.md · 组件/*.md · 摄影规范.md
├── 30-决策记录/        ADR-001-放弃Montserrat.md · ADR-002-金色拆分.md · ADR-003-WP经典+BlockTheme.md …
├── 40-任务/            路线图.md · 迭代-YYYY-WW.md
├── 50-审计/            audit-v17.md（本仓库同步）· lighthouse/*.json
└── 90-模板/            竞品.md · ADR.md · 组件.md · 周报.md
```

**ADR 模板**：

```markdown
---
id: ADR-00X
status: proposed | accepted | superseded
date: 2026-09-25
---
# 标题
## 背景（含证据链接：audit-v17.md#…）
## 选项（≥2，含被否决理由）
## 决定
## 后果（成本/风险/回滚）
```

**竞品笔记模板**：

```markdown
---
competitor: Shebiju
url: https://www.shebiju.pt
captured: 2026-09-xx
evidence: [[_research/shebiju/]]
---
## 技术栈（确认/推测）
## 色彩（HEX/OKLCH/对比度）
## 字体（家族/阶梯/字重）
## 首屏 / PLP / PDP 结构
## 看起来贵 / 便宜（附截图坐标）
## P0/P1/P2
## 我们的超越点
```

**Claude 读写约定**（MCP 连接后）：
- 开工前按项目标签检索 `30-决策记录`，避免推翻已经做出的决定
- 收工时把新结论写成 ADR 或更新组件笔记，文件名固定，方便检索

### 7.4 Harness

**无法确认**你本地 harness 的具体形态：`harness-repos` 所依赖的 MCP 没有连接，我读不到 harness-engineering 和 learn-claude-code 两个仓库。下面用 Claude Code 原生机制加 GitHub Actions 给出一个等价的编排方案，连接后再和你的 harness 对齐。

| 目标 | 机制 |
|---|---|
| Agent 编排 | 主会话按 7.2 表派发并行 Agent（worktree 隔离）→ 审查 Agent 汇总 → 人工确认 |
| Token 与代码同步 | `tokens/` 目录的 PR 触发 Style Dictionary 构建，产物与 `theme.json` 一起提交；PostToolUse 钩子：编辑 `*.css` 时检查是否出现 Token 以外的 HEX，出现就报警 |
| 质量门 | GitHub Actions：Lighthouse CI（预算见 §6.3）+ axe + Playwright 可视回归 + "访客 HTML 不含批发价"安全测试 |
| 部署追踪 | 环境分三级：staging → preview → prod；每次部署把 Lighthouse 分数写回 Obsidian 的 `50-审计/`（连接后） |
| 会话延续 | SessionStart 钩子自动安装审计工具；审计和方案文档都放在 `_research/`，已经进 git |
