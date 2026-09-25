# 方案 B "Câmara Escura" · 阶段 0：图片资产盘点与生成计划

> 日期：2026-09-25 · 只有方案，**没有生成任何图片**
> 实测工具：sharp（尺寸、亮度、锐度、角落色）、ffmpeg 7.0.2（imageio-ffmpeg，已按你的授权装在 scratchpad）、Playwright
> 基准视口：1440×900 CSS（主流笔记本）和 1920×1080 CSS；Retina 按 DPR 2 计算

---

## 0. 先说三件会改变计划的事实

| # | 事实 | 证据 | 影响 |
|---|---|---|---|
| F1 | **本会话不能直接调用 Midjourney，也没有任何图像生成工具** | 工具清单里没有图像生成类工具（按"image generation midjourney"检索，结果为零）；环境变量里没有 MJ、OpenAI、Replicate、fal、Stability、Gemini、Ideogram 的密钥 | "直接生成、不需要人工在 MJ 操作"这一前提**不成立**。可选路径见 §C |
| F2 | **现有照片没有一张能达到 21:9、宽 2880px** | 最宽只有 1200px（hero-aco、cat-homem、brincos-safira）；21:9 × 2880 要求源图 2880×1234 | 21:9 全屏 Hero 必须用新图（AI 生成或补拍）。现有竖图改用"竖幅整高 + 暗场融合"的方式（§E），能在不放大图片的前提下做到大、满 |
| F3 | **你划掉了 M06 3D 戒指**，所以 **Poly Haven HDRI 已经不需要** | HDRI 只给 M06 用 | 不下载，省约 1–2 MB 和一次授权 |

环境里有 `AWS_ACCESS_KEY_ID` 和 `AWS_SECRET_ACCESS_KEY`，**用途不明**。我**不会**用这组凭证。如果它们属于你、并且开通了 Amazon Bedrock 的图像模型，这可以是一条路径，但需要你明确授权（见 §C）。

---

## A. 现有 17 张图逐张分类

计算口径：
- 产品卡 3 列（1440 宽视口，左右边距 64，列间距 24）→ 卡宽 **421 CSS px**，2x 需要 **842 设备像素**
- 竖幅整高 Hero（900 高视口）2x 需要源图高 **1800**；1080 高视口需要 **2160**
- lapSD 是拉普拉斯标准差，数值越高越锐，统一缩到 900 宽后测量

| 文件 | 尺寸 | 亮度 | lapSD | 决定 | 用途 / 理由 |
|---|---|---|---|---|---|
| hero-aco | 1200×1800 | 5 | 27.8 | **保留** | Hero 第 1 帧（竖幅整高：900 高视口下正好 2.0x，1080 高下 1.67x）；角落色 `#050505` 和暗场几乎一致，能无缝融合 |
| cat-homem | 1200×1600 | 31 | 19.4 | **保留** | Hero 第 2 帧（900 高视口下 1.78x，接近 Retina）；**锐度偏低**，只做氛围用，不做细节展示 |
| cat-relogios | 900×1350 | 54 | **64.1**（全部图里最锐） | **保留，降级** | 整高 Hero 只有 1.5x，**不进 Hero**；放进 Showroom 大图区，按 675 CSS 高以内显示（2x） |
| cat-moda | 900×506 | 37 | 27.0 | **保留，降级** | 横图全屏只有 0.62x，**不能做 Hero**；作为 3:2 场景图，显示宽度 ≤ 450 CSS |
| hero-ouro | 900×1350 | 196 | 21.7 | **保留** | LB-1001 产品卡（900 ≥ 842 ✓） |
| colar-topazio | 900×1350 | 152 | — | **保留** | LB-1002 |
| argolas-pave | 900×1200 | 109 | — | **保留** | LB-1003 |
| brincos-safira | 1200×1200 | 196 | — | **保留** | LB-1006（裁成 4:5 后 960×1200 ✓） |
| cat-colares | 900×1200 | 147 | — | **保留** | LB-1005 Colares Olho Grego（启用未引用图） |
| cat-pulseiras | 900×1109 | 108 | — | **保留** | LB-1012 Anel Script "Love"（启用未引用图） |
| pulseira-rosa | 900×1350 | 187 | — | **保留** | LB-1004（只用在这一处） |
| hero-still | 900×1125 | 231 | — | **保留** | LB-1007，放在亮场区 |
| cat-aneis | 900×1350 | 172 | — | **保留** | LB-1011（已改名为 Anéis Finos Lisos，名字和画面一致） |
| **pendente-halo** | 900×1125 | 189 | — | **替换** | 画面里有第三方品牌"EMIZA JEWELLERY"；LB-1005 已改用 cat-colares |
| **cat-brincos** | 900×675 | 177 | — | **弃用** | 裁成 4:5 后只剩 540×675，小于 842，**分辨率不足**；LB-1010 改为"a fotografar"（待拍摄）占位 |
| **cat-loja** | 900×600 | 173 | — | **弃用** | 裁成 4:5 后只剩 480×600；陈列场景改用 AI 场景图 S-04 |
| **anel-solitario** | 900×1600 | 102 | — | **弃用** | 构图问题：产品在画面里只占几个像素，看不清；陶土色背景和暗场配色冲突 |

**四组图文不符的处理**：

图片本身没有问题，问题出在 SKU 名称。foundations §4.2 已经把 SKU **改名成和画面一致**：
- LB-1009 → Fio com Cruz（cat-homem）
- LB-1011 → Anéis Finos Lisos（cat-aneis）
- LB-1012 → Anel Script "Love"（cat-pulseiras）
- LB-2002 → Relógio + Braceletes（cat-moda）

**原来的 4 个产品**（Kit Kraft 包装套装、男士链节手链、拉丝钢戒指、网球手链）**目前没有任何真实照片**：
- 产品卡用"A fotografar"（待拍摄）占位
- AI 生成的对应品类图**只放在品类入口或氛围区块**，并标注"Imagem ilustrativa"（示意图），**不放在 SKU 卡上**

合计：**保留 13 张**（其中 2 张降级使用），**替换 1 张**，**弃用 3 张**。

---

## B. AI 生成清单

### B.0 统一规格

**比例和最终尺寸**：

| 类型 | 比例 | 最终宽度（2x） | MJ 直出（推测） | MJ 2x 放大后（推测） |
|---|---|---|---|---|
| Hero | 21:9 | ≥ 2880 | 约 1.5K 宽 | 约 3K 宽 ✓ |
| 产品 | 4:5 | ≥ 1600 | — | 约 1.8K 宽 ✓ |
| 场景 | 3:2 | ≥ 2400 | — | — |

MJ 分辨率是推测值，以你账号的实际输出为准。

**MJ 参数**（按你的规范）：
- 公共后缀：`--style raw --v 6.1 --q 2 --no text, watermark, logo, brand name, distorted chains, fake gems`
- 按图追加：`--ar 21:9`、`--ar 4:5` 或 `--ar 3:2`
- 注：截至我的知识范围，MJ 已经发布 V7（**推测**）；`--q` 在不同版本里的可取值不同，**需要你在平台上核实**。下面提示词里的参数全部照你的规范写

**统一风格基底**（每条提示词里都已写入）：
- warm charcoal-black background（MJ 读不懂 HEX，所以用文字描述 `#14120F`）
- 单一硬光：主光从左上 45° 打入，**光比 8:1**，阴影快速衰减
- 金属边缘用黑白反光板勾勒
- 100mm 微距，f/11，景深合成
- 5500K

**珠宝的硬性要求**：
- 链节必须完整、连续、不断裂，扣头必须合理
- 锆石要有**色散火彩**（光谱色的闪点），不能像玻璃
- **不得出现知名品牌的标志性造型**：Cartier Love 螺丝手镯、Van Cleef 四叶草、Tiffany 心形吊牌、Bulgari Serpenti 等。出现就淘汰，避免知识产权风险

**人像类**：按 anti-ai-photorealism-prompting skill 写法，不写"电影感"，写具体的偏离项：
- 可见毛孔
- 不对称
- 光比数值
- 胶片型号
- 解剖学正确的双手

### B.1 清单

| ID | 类别 | 比例 | 候选数 | 最终入选 | 页面用途 | 优先级 |
|---|---|---|---|---|---|---|
| H-01 | Hero：金链与玄武岩 | 21:9 | 4 | 1 | Hero 第 3 帧 | **P0** |
| H-02 | Hero：锆石火彩微距 | 21:9 | 4 | 1 | Hero 第 4 帧 | **P0** |
| H-03 | Hero：316L 钢戒指叠放 | 21:9 | 4 | 1 | 316L 章节横幅 / Hero 备用 | **P0** |
| H-04 | Hero：锁骨与细金链（人像） | 21:9 | 4 | 1 | Hero 备用 / 关于页 | P1 |
| P-01 | 品类：包装盒（kraft + 黑色） | 4:5 | 4 | 1–2 | "Embalagens" 品类入口 | **P0** |
| P-02 | 品类：陈列道具（丝绒胸像、戒指托盘） | 4:5 | 4 | 1–2 | "Expositores" 品类入口 | **P0** |
| P-03 | 品类：网球手链（锆石） | 4:5 | 4 | 1 | "Pulseiras" 品类入口 | P1 |
| P-04 | 品类：男士 316L 链节手链 | 4:5 | 4 | 1 | "Homem" 品类入口 | P1 |
| P-05 | 品类：拉丝钢戒指 | 4:5 | 4 | 1 | "Aço 316L" 品类入口 | P1 |
| P-06 | 品类：淡水珍珠 | 4:5 | 4 | 1 | "Pérolas" 品类入口 | P2 |
| S-01 | 场景：颈部佩戴（人像） | 3:2 | 4 | 1 | 首页第 2 屏 | P1 |
| S-02 | 场景：耳饰佩戴（人像） | 3:2 | 4 | 1 | 首页第 3 屏 | P1 |
| S-03 | 场景：手腕叠戴 + 手表（人像） | 3:2 | 4 | 1 | Relógios 区块 | P1 |
| S-04 | 场景：暗调门店橱窗陈列 | 3:2 | 4 | 1 | "Para a sua montra" 区块 | **P0** |
| S-05 | 场景：打开的珠宝盒 | 3:2 | 4 | 1 | 包装区块 | P2 |
| S-06 | 场景：手部特写戴戒指 | 3:2 | 4 | 1 | Anéis 入口 | P2 |
| M-01 | 材质：316L 拉丝纹理微距 | 3:2 | 4 | 1 | 材质章节 | P1 |
| M-02 | 材质：镀金层边缘（**示意图**） | 3:2 | 4 | 1 | 材质章节，必须标注"ilustração" | P2 |
| M-03 | 材质：锆石切面火彩 | 3:2 | 4 | 1 | 材质章节 | P1 |
| D-01 | 暗场静物：金链与皮革 | 4:5 | 4 | 1 | 亮度与现有暗调图统一 | P2 |
| D-02 | 暗场静物：手表与钢 | 4:5 | 4 | 1 | Showroom | P2 |
| D-03 | 暗场静物：戒指群像 | 4:5 | 4 | 1 | 产品区顶部 | P2 |

**合计**：22 条提示词 × 4 张候选 = **88 张候选**，最终入选约 24 张。P0 共 6 条（24 张候选）。

### B.2 提示词全文

公共后缀 `{SFX}` = `--style raw --v 6.1 --q 2 --no text, watermark, logo, brand name, distorted chains, fake gems`

**H-01**
```
luxury jewelry still life, a heavy polished gold curb chain with every link intact and continuous, lying in a loose S-curve across a rough slab of dark basalt stone, warm charcoal-black background, single hard spotlight from upper left at 45 degrees, 8:1 lighting ratio with fast falloff into deep shadow, crisp specular highlights on each link, black and white flags shaping the metal edges, 100mm macro lens at f/11, focus-stacked sharpness across the chain, fine stone grain visible, 5500K neutral color, generous negative space on the right third --ar 21:9 {SFX}
```
**H-02**
```
extreme macro of two round brilliant cut cubic zirconia stud earrings in yellow gold four-prong settings resting on black polished obsidian, warm charcoal-black background, pinpoint spotlight from upper left, visible spectral dispersion fire with small rainbow flashes inside the stones, sharp facet edges, prongs cleanly formed, soft reflection on the obsidian surface, 8:1 lighting ratio, 100mm macro f/8 focus stacked, shallow falloff at frame edges, subject placed on left third --ar 21:9 {SFX}
```
**H-03**
```
three stainless steel rings stacked and slightly offset on dark slate, one mirror polished, one brushed satin with fine parallel grain, one with a thin gold plated edge, warm charcoal-black background, cool narrow spotlight from upper left, long clean reflections, 8:1 lighting ratio, macro product photography 100mm f/11 focus stacked, true metal texture, no scratches on polished surface except natural micro swirl, composition on right third with dark negative space left --ar 21:9 {SFX}
```
**H-04**（人像，按 anti-AI 写法）
```
close crop of a woman's collarbone and lower neck, no face visible, a fine gold chain with a small plain bar pendant resting slightly off center, visible skin pores and faint freckles, natural skin texture with a subtle razor-free fine vellus hair sheen, one shoulder slightly higher than the other, black knit fabric edge with natural creases at frame bottom, warm charcoal-black background, single hard key light from upper left, 8:1 lighting ratio with visible shadow falloff across the sternum, shot on Kodak Portra 400, 85mm lens, shallow depth of field, light film grain, no over-smoothing, no plastic skin --ar 21:9 {SFX}
```
**P-01**
```
product flat composition of unbranded jewelry packaging: two matte black rigid boxes with lids ajar, one natural kraft paper box, a folded kraft gift bag and a cotton pouch, plain surfaces with no printing, arranged on dark oak board, warm charcoal-black background, soft directional light from upper left, 4:1 lighting ratio, realistic paper fibers and slight corner wear, 50mm lens f/8, top-down 30 degree angle --ar 4:5 {SFX}
```
**P-02**
```
jewelry shop display props on dark walnut counter: a black velvet necklace bust, a black velvet ring tray with empty slots, a small tiered acrylic earring stand, all plain and unbranded, dust visible on velvet nap, warm charcoal-black background, narrow spotlight from upper left, 8:1 lighting ratio, realistic velvet texture with directional pile, 70mm lens f/8 --ar 4:5 {SFX}
```
**P-03**
```
a gold plated tennis bracelet with a single continuous row of identical small round cubic zirconia stones, clasp closed and visible, laid in a gentle curve on black suede, every link aligned and complete, stones showing spectral fire, warm charcoal-black background, hard spotlight upper left, 8:1 lighting ratio, 100mm macro f/11 focus stacked --ar 4:5 {SFX}
```
**P-04**
```
men's stainless steel link bracelet with brushed flat links and a polished fold-over clasp, all links connected and continuous, resting on dark worn leather with natural creases, warm charcoal-black background, cool narrow spotlight from upper left, 8:1 lighting ratio, crisp edge highlights, 100mm macro f/11 focus stacked --ar 4:5 {SFX}
```
**P-05**
```
four plain band rings in brushed 316L stainless steel of different widths standing on edge on dark basalt, fine parallel satin grain clearly visible, one ring slightly out of focus in the background, warm charcoal-black background, single hard light from upper left, 8:1 lighting ratio, 100mm macro f/11 --ar 4:5 {SFX}
```
**P-06**
```
small freshwater pearl huggie earrings in gold plated steel, pearls slightly irregular in shape with natural surface nacre variations, on black slate with a drop of water beside them, warm charcoal-black background, soft spotlight upper left, 4:1 lighting ratio, 100mm macro f/8 --ar 4:5 {SFX}
```
**S-01**（人像）
```
side view of a woman's neck and jawline, face cropped at the lips, wearing two layered fine gold chains of different lengths, visible skin texture and small mole, a few loose hair strands crossing the neck, black silk top with natural folds, warm charcoal-black background, single hard key light from the left, 8:1 lighting ratio with shadow falloff under the jaw, shot on Kodak Portra 400, 85mm lens, shallow depth of field, light grain, no plastic skin --ar 3:2 {SFX}
```
**S-02**（人像）
```
close crop of a woman's ear and hairline, dark hair tucked behind the ear, two small gold hoop earrings and one tiny zirconia stud, visible skin pores and fine peach fuzz, ear shape natural and slightly asymmetric, warm charcoal-black background, hard key light from upper left, 8:1 lighting ratio, shot on Kodak Portra 400, 100mm macro, shallow depth of field, light grain, no over-smoothing --ar 3:2 {SFX}
```
**S-03**（人像）
```
a man's forearm and wrist resting on a dark wooden desk, wearing a stainless steel mesh strap watch and a thin brushed steel link bracelet, anatomically correct hand with five distinct fingers and visible knuckles, uneven nail lengths, natural arm hair and veins, dark wool sleeve pushed up with creases, warm charcoal-black background, single hard light from upper left, 8:1 lighting ratio, shot on Kodak Gold 200, 50mm lens, shallow depth of field --ar 3:2 {SFX}
```
**S-04**
```
interior of a small independent jewelry boutique at night, a dark glass display window with three black velvet busts and ring trays holding gold and steel pieces, warm pinpoint display lights creating isolated pools of light, reflections on the glass, everything plain and unbranded, no signage, warm charcoal-black surroundings, 35mm lens, 8:1 lighting ratio, realistic dust and fingerprints on glass --ar 3:2 {SFX}
```
**S-05**
```
an open matte black rigid jewelry box with black foam insert holding a gold pendant necklace neatly coiled, lid shadow falling across the insert, box corners slightly worn, on dark oak surface, warm charcoal-black background, spotlight from upper left, 8:1 lighting ratio, 70mm lens f/8 --ar 3:2 {SFX}
```
**S-06**（人像）
```
close-up of a woman's hand resting on dark linen, wearing three stacked thin gold rings on the ring finger and one plain steel band on the index finger, anatomically correct hand with five distinct fingers, visible knuckle creases, short natural unpainted nails of slightly uneven length, faint veins, warm charcoal-black background, hard light from upper left, 8:1 lighting ratio, shot on Kodak Portra 400, 100mm macro, shallow depth of field, light grain --ar 3:2 {SFX}
```
**M-01**
```
extreme macro texture of brushed 316L stainless steel surface, fine parallel satin grain running diagonally, a single polished bevel edge catching a sharp highlight, raking light from upper left, 8:1 lighting ratio, industrial precision, 100mm macro f/11 --ar 3:2 {SFX}
```
**M-02**（示意图，必须标注）
```
macro illustration style photograph of the cut edge of a gold plated stainless steel ring, showing a thin bright gold layer over grey steel core, clean polished cross-section, dark background, raking light, technical and precise, scientific product photography --ar 3:2 {SFX}
```
**M-03**
```
extreme macro of a single large round brilliant cubic zirconia seen from above, crisp facet pattern, strong spectral dispersion with rainbow flashes, black background, pinpoint light from upper left, 100mm macro with extension tube, f/11 focus stacked --ar 3:2 {SFX}
```
**D-01**
```
a gold paperclip chain necklace draped over a folded dark brown leather wallet, all links continuous, warm charcoal-black background, hard spotlight from upper left, 8:1 lighting ratio, leather grain visible, 100mm macro f/11 --ar 4:5 {SFX}
```
**D-02**
```
stainless steel mesh strap watch with a plain white dial and no logo on the dial, lying on dark slate beside a coiled steel chain, warm charcoal-black background, narrow spotlight upper left, 8:1 lighting ratio, 100mm macro f/11 --ar 4:5 {SFX}
```
**D-03**
```
a loose group of seven gold plated rings with small colored cubic zirconia stones scattered on black velvet, each stone with natural fire, warm charcoal-black background, pinpoint spotlight upper left, 8:1 lighting ratio, 100mm macro f/11 focus stacked --ar 4:5 {SFX}
```

---

## C. 生成执行计划

### C.1 可行路径（**需要你选一条**）

| 路径 | 我能否自动执行 | 需要你提供 | 风险 |
|---|---|---|---|
| **① Midjourney 人工半自动（推荐作画质首选）** | 否。你在 MJ 里运行，我负责提示词、筛选和后处理 | 把 88 张候选（或只挑入选的）上传给我，或放到 `_research/generated/raw/` 并推送 | 截至我的知识范围，MJ **没有官方公开 API**（**推测**，需要你核实 2026 年的现状）。第三方"MJ API"大多是在模拟账号操作，**违反 MJ 服务条款，可能封号**，所以不推荐 |
| **② 官方 API 模型（全自动）** | **能**，前提是完成配置 | 选一个：OpenAI Images（gpt-image 系列）、Google Imagen（Gemini API）、Black Forest Labs FLUX（官方 API）。把 **API Key 设为本环境的 secret**，并把对应域名加入网络允许列表（例如 `api.openai.com` / `generativelanguage.googleapis.com` / `api.bfl.ai`，以官方文档为准） | 各家的最大分辨率不同，部分需要再做 2x 放大（见 C.3）；风格一致性可能不如 MJ（**推测**） |
| **③ Amazon Bedrock** | 能，前提是你**明确授权**使用环境里已有的 AWS 凭证，并确认它开通了图像模型 | 授权、区域、模型 ID；把 `bedrock-runtime.<region>.amazonaws.com` 加入网络允许列表 | 这组凭证的用途**我无法确认**，未经授权我不会使用 |

**我的建议**：P0 的 6 条用 ①，也就是 MJ，画质和一致性最高；P1、P2 的 16 条如果你想省人工，可以用 ② 批量跑。

### C.2 预计时间（**推测**）

| 路径 | 预计耗时 |
|---|---|
| ① MJ | 22 个任务 × 约 1 分钟，加上约 24 次放大，人工约 60–90 分钟；我这边筛选和处理约 30 分钟 |
| ② API | 88 张约 20–40 分钟，受速率限制影响；筛选和处理约 30 分钟 |

### C.3 分辨率兜底

如果生成结果达不到目标宽度（Hero 2880 / 产品 1600 / 场景 2400）：
- 用 **Real-ESRGAN**（BSD-3 许可，开源）做 2x 放大
- 这是**新的依赖**，需要你另外确认
- 放大会"补出"细节，所以**只用在 AI 氛围图上，不用在真实产品照上**

### C.4 筛选标准（逐张打分，任何一条不及格就淘汰）

1. **链节**：完整、连续，扣头合理（放大到 200% 检查）
2. **宝石**：有光谱色散火彩，切面清晰，不能像玻璃珠
3. **没有**文字、logo 或类似品牌字样的图案；**没有**知名品牌的标志性造型
4. **人像**：双手五指、关节和指甲自然；皮肤有纹理；没有"塑料感"
5. **光向统一**：主光来自左上 45°
6. **背景色**：四角 30×30 区域的均值和 `#14120F` 的 ΔE2000 ≤ 8（sharp 实测）；超出的在管道里校正，校正后仍 > 12 就淘汰
7. **分辨率**：达标，或者可以用 C.3 放大
8. **系列感**：6 张以上并排放在一张联络图里，没有一张"跳出来"

### C.5 合规

- **生成物的标注**：AI 生成图在页面上加小字"Imagem ilustrativa gerada por IA"（AI 生成的示意图）；sidecar JSON 记录模型、提示词、日期和 seed；IPTC 的 DigitalSourceType 写 `trainedAlgorithmicMedia`
- **欧盟 AI 法第 50 条**：透明度义务自 2026-08-02 起适用（**推测**，需要法律确认适用范围）
- **消费者保护**：AI 图不冒充 SKU，这一点前面已经写死
- **hero.mp4 里有真人模特**：只拍到嘴唇以下，**肖像授权和素材来源需要你确认**

---

## D. 图片处理管道

```
源（现有 JPG / AI PNG）
 → sharp：rotate()；统一转 sRGB；去除 EXIF、GPS、XMP（保留 ICC）
 → 暗场校正：只对 AI 图做；四角均值偏离 #14120F 时，用 linear/gamma 调整黑位（记录参数）
 → 裁切：Hero 21:9（cover，position 'attention'）｜产品 4:5｜场景 3:2｜竖幅 Hero 保留原比例
 → 尺寸阶梯（withoutEnlargement:true）：
     Hero 21:9：1440 / 2160 / 2880（/ 3840，仅当源图 ≥ 3840）
     竖幅 Hero：高 900 / 1350 / 1800（受源图限制）
     产品 4:5：480 / 840 / 1200 / 1600
     场景 3:2：800 / 1600 / 2400
 → 编码：AVIF q50 effort 6（Hero q55）｜WebP q78｜JPEG mozjpeg q82 progressive
 → 生成 16px LQIP 和主色（stats().dominant），用作占位背景
 → 写出 manifest.json（每张图：src、宽高、各尺寸、主色、alt、来源）
```

**命名规范**：`{区域}-{主题}-{比例}-{宽}.{ext}`
- 例：`hero-aco-2x3-1200.avif`、`prod-lb1003-4x5-840.webp`、`ai-h01-21x9-2880.avif`
- AI 图统一用 `ai-` 前缀

**性能提示（实测）**：sharp 在本容器里编码 AVIF 很慢，48 张 1080 宽的图耗时超过 120 秒。批量处理要**多进程并行**，或者降到 effort 4。

**R2 分发**：Demo 阶段**不上 R2**，图片走相对路径 `../images/…`。上线前需要补充：
- Cloudflare 账号 ID
- R2 bucket
- API Token（Access Key ID / Secret）
- 公开域名（自定义域名，或 r2.dev）
- 并把 `*.r2.cloudflarestorage.com` 加入网络允许列表

R2 本身不做图片变换，所以按上面预先生成的尺寸上传即可；缓存头用 `public, max-age=31536000, immutable`，文件名里带内容哈希。

---

## E. Hero 方案

- **结构**：100svh 全屏暗场，4 帧轮播，每帧 **5 秒**（第一帧 5.5 秒，给标题揭示留时间）
- **帧序与呈现**：

| 帧 | 图片 | 呈现方式 | 2x 达标情况 |
|---|---|---|---|
| 1 | hero-aco（现有） | **竖幅整高，contain**；舞台底色直接取这张图的角落色 `#050505`，边缘加径向暗角，图片和舞台融为一体，观感上接近全屏 | 900 高视口 2.0x ✓；1080 高视口 1.67x |
| 2 | cat-homem（现有） | 同上，舞台底色取角落色 `#201D22` | 900 高视口 1.78x |
| 3 | AI H-01 | 21:9，cover 铺满 | 2880 ✓ |
| 4 | AI H-02 | 21:9，cover 铺满 | 2880 ✓ |

  cat-relogios 和 cat-moda 因为分辨率不够，**不进 Hero**（见 §A）。你指定的"4 张暗调图轮播"只能满足 2 张现有图 + 2 张 AI 图。**如果不接受 AI 图进 Hero**，退路是：第 3、4 帧用 cat-relogios 和 cat-moda，按 contain 小尺寸显示，但会明显不满、不够大。

- **切帧动效**：新帧 `clip-path: inset(0 0 0 100%) → inset(0)`（从右往左擦入），耗时 1.2s，`--ease-inout`；同时旧帧 `scale 1 → 1.04`，淡出到 0.6
- **视差**：帧内图片随滚动 `yPercent 0 → 12`，这是 M02
- **Ken Burns**：每帧停留期间 `scale 1.06 → 1`，5 秒线性
- **标题**：Fraunces 300 斜体，`clamp(56px, 8vw, 132px)`，放在左下；M01 按词揭示；右下放 JetBrains Mono 展签，例如 `Nº 001 · Aço 316L · LB-1013`，随帧切换
- **加载策略**：
  - 第 1 帧是 LCP：`<link rel="preload" as="image" imagesrcset=… fetchpriority="high">`，AVIF 竖幅 900/1350/1800 三档
  - 第 2–4 帧在 `load` 之后用 `requestIdleCallback` 逐帧预取
  - 下一帧没有 decode 完，就不切过去
- **控制**：暂停/播放按钮（WCAG 2.2.2）；左右方向键切帧；悬停或获得焦点时暂停；`prefers-reduced-motion` 下停在第 1 帧；`saveData` 下只加载第 1 帧
- **移动端**：竖屏视口本身就是竖幅，第 1、2 帧 cover 铺满；第 3、4 帧裁成 4:5 的中心区域（AI 图源宽 2880，裁出来仍然足够）

---

## F. 产品卡布局（3 列）

| 视口 | 列数 | 边距 / 列间距 | 卡宽（CSS） | 2x 所需图宽 |
|---|---|---|---|---|
| ≥ 1440 | 3 | 64 / 24 | 421 | 842（现有 900 ✓） |
| 1920 | 3 | 96 / 32 | 555 | 1110（**现有 900 ✗**，1.62x）→ 容器最大宽度限制在 1600，卡宽 ≤ 512，需要 1024（仍然 ✗ 1.76x）|
| 768–1199 | 2 | 32 / 20 | — | 约 1000 |
| < 768 | 1（加右侧露出 12% 的横滑） | 16 | 约 340 | 680 ✓ |

说实话，**1920 宽的屏幕上，现有产品照达不到 2x**，只能做到约 1.6–1.8x。要满足"产品图 ≥ 1600 宽"，只能**补拍**。AI 图不能冒充 SKU，所以这里 AI 帮不上忙。

**卡片内元素，按优先级排**：
1. **图片**：4:5，占卡片高度约 78%
2. **名称**：Inter Tight 15/500
3. **材质标签**：`Banho 18K` 或 `Aço 316L`，文字金或银色
4. **SKU**：JetBrains Mono 12
5. **PVP**：`PVP 15,50 €`
6. **价格状态**：访客看到 "Preço de revenda · Entrar"（登录查看批发价）；登录后看到"9,20 € · MOQ 6"
7. **操作**：`+ Pedido`（加入订单）/ `+ RFQ`（加入询价）。桌面端悬停时出现，触屏上常显

- **暗场区的卡片**：图片外加 1px `ink-800` 边框，形成"展柜"；亮度很高的图（hero-still 231）也被框住，不会和暗场打架
- **亮场区**（PLP，开灯之后）：卡片无边框，间距 24

---

## G. 视频与逐帧方案

**hero.mp4 画质评估（实测）**：
- 1080×1920，H.264 High
- 第 10 秒帧的锐度 lapSD **57.8**，和最锐的现有照片（cat-relogios 64.1）同一档，**画质够用**
- 内容：模特锁骨，佩戴镶锆石的金项链，淡紫背景，暖肤色
- 在 **19.1s、21.5s、28.7s** 各有一次剪辑

**风格注意**：视频是暖调、淡紫背景，和暗场不一致。需要做一次调色：`eq=brightness=-0.05:saturation=0.85` 加暗角，这是参数建议，执行时再看效果调整。

**方案：用 2–18s 这段连续镜头（没有剪辑）做滚动逐帧**

| 项 | 参数 | 实测 / 推算 |
|---|---|---|
| 抽帧 | 2–18s，3 fps，共 48 帧 | 已实测抽出 48 帧 |
| 桌面端（DPR ≥ 1.5） | 1080 宽 AVIF q52（源分辨率，不放大） | **平均 26.2 KB / 帧 → 48 帧约 1.23 MB**（实测；WebP 28.0 KB / 帧） |
| 桌面端（DPR 1） | 720 宽 AVIF q50 | **平均 14.6 KB / 帧 → 48 帧约 700 KB**（实测） |
| 呈现 | 竖框 4:5 或 9:16，放在暗场中央，滚动 150vh 播完 48 帧，用 canvas 绘制 | — |
| 加载 | LCP 之后，先加载第 1、12、24、36、48 帧（关键帧），其余在空闲时补齐；帧没到齐时显示最近的已加载帧 | — |
| 移动端 | **不做逐帧**，改为静音自动播放循环视频：H.264 540p，12 秒，无音轨 | **实测 647 KB** |
| 720p H.264（备用） | 12 秒，CRF 24，无音轨 | **实测 1.45 MB**（原文件 18.08 MB） |
| 降级 | `saveData`、2G/3G 网络或 reduced-motion 时只显示单张海报（第 24 帧，AVIF） | — |
| 编码器 | 容器里的 ffmpeg 7.0.2 有 libx264、libx265、libaom-av1，**没有 SVT-AV1**；AV1 编码会很慢，可以接受 | — |

---

## H. 动效清单（按你的编号，只保留 6 条）

所有动效只动 `transform`、`opacity`、`clip-path`。`prefers-reduced-motion` 下全部改为瞬时切换或 ≤ 120ms 的淡入。

| # | 名称 | 位置 | 技术 | 时长 / 缓动 / 触发 | 移动端降级 |
|---|---|---|---|---|---|
| M01 | Hero 标题揭示 | Hero 标题；各屏大标题 | GSAP SplitText 按词拆分，`yPercent 110 → 0`，外层 overflow 遮罩，stagger 0.04；在 `document.fonts.ready` 之后才运行 | 1100ms / `cubic-bezier(.16,1,.3,1)` / 加载，或进入视口 | 按行拆分；800ms |
| M02 | 滚动视差（含逐帧） | Hero 帧内图片；第 2、3 屏大图；视频逐帧 | GSAP ScrollTrigger `scrub:true` + Lenis（lerp 0.1）；大图 `yPercent -8 → 8`；逐帧用 canvas 按滚动进度切换帧 | 跟随滚动 | 触屏关闭 Lenis；视差幅度减半；逐帧改为循环视频（见 G） |
| M03 | 图像遮罩揭示 | 第 2、3 屏大图；产品区首行；Showroom | `clip-path: inset(100% 0 0 0) → inset(0)`，同时图片 `scale 1.15 → 1`；ScrollTrigger `once` | 1200ms / `cubic-bezier(.76,0,.24,1)` / 进入视口 80%；同屏 ≤ 3 个 | 800ms，不做缩放 |
| M08 | 自定义光标 | 全站（暗场 + 亮场） | 8px 点 + 40px 圆环（lerp 0.18）；在图片上圆环扩到 72px 并显示"Ver"；Hero 上显示"Arrastar"表示可拖动切帧；表单和输入框区域恢复系统光标 | 跟随，rAF | `(pointer:coarse)` 下完全不加载；键盘操作时隐藏 |
| M09 | 产品卡悬停推近 | 产品卡图片 | `scale 1 → 1.06`，同时图片 `translate` 朝光标方向偏移 ≤ 8px | 900ms / `cubic-bezier(.16,1,.3,1)` / hover | 不做；触屏上左右滑动切第二张图（如果有） |
| M15 | 页面转场（含"开灯"） | 所有页面之间；暗场 → 亮场 | 跨文档 View Transitions（`@view-transition{navigation:auto}`）+ 共享元素（卡片图 → PDP 主图）；"开灯"是 `--bg` 从 `#14120F` 渐变到 `#FBFBF9` | **700ms** / `cubic-bezier(.76,0,.24,1)` / 导航 | 同桌面端；不支持的浏览器直接普通跳转 |

**不再做**：3D 戒指（M06）、聚光遮罩（原 M15）、pin 住的章节叙事（M04）、FLIP 飞入。这些是你划掉的，已经从计划里去掉。

---

## 需要你确认才能进入阶段 1

1. **生成路径**：① MJ 人工，② 官方 API（提供哪家、Key、放行域名），③ Bedrock（授权使用现有 AWS 凭证），还是组合？
2. **Hero 第 3、4 帧用 AI 图**（H-01、H-02）：接受，还是改用现有图降级显示？
3. **Real-ESRGAN**：是否允许在需要时装来放大 AI 图？
4. **视频素材的来源和模特肖像授权**：需要补充
5. **页面上的"Imagem ilustrativa gerada por IA"标注**：是否接受？（我建议保留）
