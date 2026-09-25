# _research · LM BIJU 调研与方案

| 文件 | 内容 |
|---|---|
| `audit-v17.md` | 现有 demo v17 的完整审计（实测数据） |
| `foundations-phase1.md` | 路径一：色彩 / 字体 / 视频 / 图片 / 布局骨架 / WordPress 迁移 / 工作流 |
| `phase2-proposals.md` | 竞品综合、审美升级增量、动效总表、A/B/C 三个方案规格与关键代码、推荐 |
| `<竞品>/analysis.md` | 逐站分析（基于用户提供的截图；原始 PNG 未入库，只存了缩略总览 `screenshots-overview.jpg`） |
| `evidence/` | 截图、字体样张、图片联络图、Lighthouse 摘要 |
| `<竞品>/` | 竞品材料放置处（方式 B） |

## 竞品材料放置规范（方式 B）

每家竞品一个文件夹：`shebiju/`、`cellibiju/`、`grupobelle/`、`maxbiju/`。每个文件夹里：

```
home.png        home.har        home.html
plp.png         plp.har         plp.html        （列表页，写一下 URL 到 urls.txt）
pdp.png         pdp.har         pdp.html        （详情页）
lighthouse-mobile.json   lighthouse-desktop.json
urls.txt        （三个页面的实际 URL + 抓取日期）
```

- 全页截图：DevTools → Ctrl+Shift+P → "Capture full size screenshot"
- HAR：DevTools → Network → 勾 Preserve log、Disable cache → 刷新 → 右键 "Save all as HAR with content"
- HTML：Ctrl+S →"网页，仅 HTML"
- Lighthouse：DevTools → Lighthouse → Mobile / Desktop 各跑一次 → 右上角 ⋮ → Save as JSON

HAR 可能很大（>50MB 时请先压缩为 .zip）。竞品素材仅用于内部分析，不进入任何 Demo。
