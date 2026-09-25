# Demo B "Câmara Escura" · 交付状态 v2（2026-09-25）

## 文件
| 文件 | 说明 |
|---|---|
| `proposals/demo-b.html` | 完整 Demo（首页、目录、详情、询价、注册），单文件，内联 CSS 和 JS，约 121 KB |
| `proposals/demo-showcase.html` | 一页式展示：Hero、四个章节、逐帧、橱窗、6 款精选、B2B 功能、Showroom、结尾 CTA。由 `_build/build.py` 从 demo-b 生成，两边保持同步 |
| `proposals/vendor/` | GSAP 3.15.0、ScrollTrigger、Lenis 1.3.26，**本地文件**（不再走 CDN），附许可证 |
| `proposals/fonts/` | Fraunces、Inter Tight、JetBrains Mono 的 woff2（latin 和 latin-ext 两个子集），OFL 许可证 |
| `proposals/_build/build.py` | 把字体注入 demo-b，并生成 demo-showcase |
| `proposals/_build/pack_offline.py` | 生成离线包：路径改写成 `assets/`，并去掉 file:// 下会报 CORS 的字体 preload |
| `demo-showcase-offline.zip` | 离线包，11.8 MB，264 个文件。解压后双击即可打开，不需要 Python |
| `start-demo.bat` / `start-demo.sh` | 一键启动本地服务器并打开浏览器 |
| `DEMO-GUIDE.md` | 演示指南：打开方式、浏览顺序、每页亮点、FAQ 回答模板 |
| `demo-b-assets.zip` | v1 的打包，**已过时**（里面是 v1 的 demo-b，走 CDN）。请改用 `demo-showcase-offline.zip` |

## 动效（10 个）
| 编号 | 内容 |
|---|---|
| M01 | Hero 标题逐行揭开 |
| M02 | 视差，以及 48 帧滚动逐帧播放 |
| M03 | 图片遮罩揭开 |
| M04 | 1.5 秒开场：暗场、金线、品牌名。可以跳过；每个标签页只播一次 |
| M05 | Showroom 数字从 0 滚到目标值 |
| M06 | Hero 里金色光晕跟随鼠标 |
| M07 | 章节编号"Nº 0X"从左侧滑入 |
| M08 | 自定义光标（只在有鼠标的设备上启用） |
| M09 | 产品卡片 hover 推近 |
| M15 | "Acender a luz"开灯转场（View Transitions） |

## 实测（Playwright + axe-core，Chromium）
| 项 | 结果 |
|---|---|
| axe 违规 | 桌面 1440×900：首页、目录（网格和列表）、详情、询价**全部 0**；手机 390×844：首页、询价 0；减少动效：首页、询价 0；showcase 桌面和手机 0 |
| 控制台错误 | 0（demo-b 和 showcase，http 与 file:// 都是 0） |
| 横向滚动 | 手机端首页和目录都没有 |
| 离线包 file:// | 严格模式（不带 `--allow-file-access-from-files`）：4 个字体加载成功、GSAP 和 Lenis 可用、图片无损坏、路由、localStorage、showcase 跳转 demo-b 都正常 |
| B2B | MOQ 25 → 30；询价进度条；参考图只在本机预览；阶梯价 30 件 = 4,85 € × 30 = 145,50 € |
| 减少动效 | 无开场，Hero 固定第 1 帧，章节不钉住，逐帧改为静态图，数字直接显示终值 |
| JS 体积 | demo-b：本地库 136 KB + 内联 44 KB = **180 KB**；showcase：**151 KB**（都未压缩，预算 300 KB） |
| 未验证 | `start-demo.bat` 没有在 Windows 上实际运行过（这个环境是 Linux），只做了逐行检查；`start-demo.sh` 已在 Linux 上验证 |

## v2 修复的问题
- 自定义光标的圆环在触屏设备上露出左上角：原因是 `.cur-ring{display:grid}` 覆盖了 `.cur{display:none}`
- 首页滚过 Hero 后，页头改成实色背景（原先是半透明渐变，手机上会和正文叠在一起）
- 手机目录的筛选改成两列网格
- 询价的文件选择框：浏览器自带的英文"Choose File"换成葡语按钮"Escolher imagem"
- 章节小标签在亮图上看不清：加了暗色描边
- 逐帧字幕第 1 句和标题重复：改为"A luz corre pelo fio."
- favicon 404：改为内联 SVG

## 临时方案（上线前必须替换）
| 位置 | 当前 | 替换为 |
|---|---|---|
| Hero 第 3、4 帧 | MJ G3_2、G4_0，1680 宽（1440 视口下 1.17x，Retina 屏略软） | MJ Upscale (Subtle) 后约 3360 宽 |
| Hero 第 4 帧 | G4_0 银色古巴链 | 锆石火彩图（H-02 v2 提示词） |
| 章节配图、橱窗、结尾背景 | MJ 1680 宽 | Upscale 版本 |
| 场景图（G6_0 / G7_2 / G2_0 / G3_1 / G1_0） | 从 21:9 裁出的 3:2，1080×720 | Upscale，或用 `--ar 3:2` 重新生成 |
| 品类入口"Embalagens""Expositores" | 从 21:9 裁出的 4:5，576×720 | 用 `--ar 4:5` 重新生成 |
| Showroom 数字 | 956（v17 各品类数量之和）、1200 和 2012（示例），页面标注"Valores ilustrativos" | 真实数据 |
| 营业时间 | "Segunda a sexta, 09h00 – 18h30"（示例） | 真实时间 |
| 邮箱 | `geral@lmbiju.pt`（沿用 v17） | 确认后的销售邮箱 |
| WhatsApp | +351 000 000 000（占位） | 真实号码 |
| 批发价、阶梯价 | 前端写死的演示数据 | 由服务端按客户角色输出 |
| hero.mp4 授权 | "自有拍摄，模特已授权"（你临时填的） | 上线前确认 |

## 必须实拍的 SKU（AI 不能冒充）
LB-1010、LB-2001、LB-2002、LB-2003、LB-1014、LB-1015、LB-1016。目录里这 7 个显示"Fotografia em preparação"。另外，所有现有产品照要达到 1600 宽，也需要补拍（现有原图最宽 900–1200px）。

## 没有使用
- `pendente-halo.jpg`：画面里有第三方品牌"EMIZA JEWELLERY"，没有修掉 logo 继续用
- `cat-brincos.jpg`、`cat-loja.jpg`：分辨率不足
- `anel-solitario.jpg`：产品在画面里太小
