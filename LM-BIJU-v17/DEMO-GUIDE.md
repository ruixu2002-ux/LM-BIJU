# LM BIJU · Demo B "Câmara Escura" 演示指南

> 给你自己看的讲解稿：怎么打开、按什么顺序走、每页点什么、客户常问的问题怎么答。
> 页面文字是葡萄牙语。下文的"PT 原句"可以直接念给客户听。

---

## 1. 怎么打开（三种方式，任选一种）

| 方式 | 适合 | 步骤 |
|---|---|---|
| **A. 离线包（推荐发给客户）** | 客户电脑，没有 Python，没有网络 | 解压 `demo-showcase-offline.zip` → 打开 `LM-BIJU-demo` 文件夹 → 双击 `demo-showcase.html`（一页展示），或双击 `demo-b.html`（完整网站） |
| **B. 一键脚本（你自己演示）** | 你的电脑，已安装 Python 3 | Windows：双击 `start-demo.bat`；macOS / Linux：终端运行 `./start-demo.sh`。浏览器会自动打开 `http://localhost:8080/proposals/demo-b.html` |
| **C. 手动** | 脚本打不开时 | 在 `LM-BIJU-v17` 文件夹里运行 `python -m http.server 8080`，浏览器打开 `http://localhost:8080/proposals/demo-b.html` |

注意：
- 离线包**必须先解压**。在压缩包里直接双击，图片和字体加载不了。
- 8080 端口被占用时：`start-demo.bat 8765` 或 `./start-demo.sh 8765`。
- 推荐浏览器：最新版 Chrome / Edge / Safari / Firefox。
- 演示前建议全屏（F11），把浏览器缩放调到 100%。
- **重看开场动画**：开场加载动画每个标签页只播一次。想再看一次，关掉标签页重新打开。

---

## 2. 浏览顺序（约 8–10 分钟）

**首页 → 目录 → 详情 → 询价 → 注册**

| # | 页面 | 时长 | 做什么 |
|---|---|---|---|
| 1 | 首页（暗场） | 3 分钟 | 看完开场，慢慢往下滚，一直滚到"Acender a luz" |
| 2 | 目录（亮场） | 2 分钟 | 点"Entrar no catálogo"，看开灯转场；筛选、切换网格/列表 |
| 3 | 产品详情 | 2 分钟 | 打开 LB-1003 Argolas Largas Polidas，看阶梯价 |
| 4 | 询价单 | 1–2 分钟 | 加入询价，看进度条、最小起订量自动校正、CSV |
| 5 | 注册 | 1 分钟 | 回首页注册区，演示 NIF 校验 |

一页式版本 `demo-showcase.html` 用来发给客户自己看，或者在会议开头放 1 分钟。

---

## 3. 每页亮点（点什么、说什么）

### 首页（暗场）
1. **开场（M04）**：1.5 秒，深色背景 + 金线 + 品牌名。点击或按任意键可以跳过。
2. **Hero 四帧轮播**：钢链 → 男士十字链 → 金链配玄武岩 → 银色古巴链，每帧 5 秒，遮罩揭开，带轻微 3D 转动；每帧有自己的副标题和 SKU 标注。
   - 鼠标在 Hero 上移动，**金色光晕跟着走（M06）**。
   - 左下角"Pausar"可以暂停（无障碍要求）。
3. **四个章节（Nº 01–04）**：往下滚时章节被钉住，大号编号从左侧滑入（M07），右下角有章节索引。说法：*"从材质到橱窗，四步讲清楚为什么这些货卖得动。"*
4. **逐帧视频（48 帧）**：跟着滚动逐帧播放，字幕同步切换。滚过一半出现"Ver a coleção completa →"。
5. **橱窗三图**：三张错落排列的场景图，每张有说明文字。
6. **客户类型（三个标签）**：Revendedor online / Loja física / Novo negócio，右边是注册表单。
7. **Showroom**：四个数字从 0 滚动到目标值（M05）。旁边注明"Valores ilustrativos"，**这些数字是示例**。
8. **Acender a luz**：页面的焦点。点"Entrar no catálogo"，画面从点击处以圆形"开灯"切换到亮场目录（M15）。
9. **结尾 CTA**："Pronto para ver os preços?"，两个按钮：Criar conta profissional / Falar com a equipa。

### 目录（亮场）
- 三列网格；顶部是品类入口条（横向滚动）。
- 筛选：**Família / Material / Ordenar** 三个下拉 + "Grelha / Lista"切换 + "Limpar"。筛选条件会写进网址，可以直接复制链接发给别人。
- 右上角开关 **"Ver como cliente"**：模拟已登录的批发客户。**打开后**，每张卡片显示批发价、最小起订量、利润倍数；**关闭时**只显示建议零售价（PVP），批发价锁住。**这是整个 B2B 逻辑的核心卖点，一定要演示。**
- 7 个 SKU 显示"Fotografia em preparação"：这些产品还没有实拍照片（见第 5 节）。

### 产品详情
- 点主图 → 暗场灯箱（"câmara escura"）。
- 阶梯价表（打开 "Ver como cliente"）：LB-1003 为 6+ 件 5,25 €、24+ 件 4,85 €、96+ 件 4,45 €（**示例价格**）。改数量时对应的档位会高亮。
- 输入 25 → 离开输入框 → **自动校正为 30**（6 的倍数）。
- 折叠区：Especificações / Detalhes do material / Conformidade e ficha técnica。
- 底部 "Da mesma família"：3 个相关产品。

### 询价单（Pedido de proposta）
- 顶部进度条：Produtos → Os seus dados → Confirmar → Enviado。
- 可以粘贴 `LB-1003;24` 这样的列表，或导入 CSV。
- "Imagem de referência"：选一张图片后只在本机预览，**不会上传**（按要求做成占位）。
- 提交：下载 CSV 文件，并生成一封预填好的邮件，编号格式为 `RFQ-YYYYMMDD-XXXX`。**这是演示**：不会真的发出去，也没有后台。

### 注册
- NIF 校验：输入 `501964843` → 有效；改任意一位 → 提示无效（按葡萄牙 NIF 校验位规则计算）。
- 提交后打开预填邮件，不会假装"注册成功"。

---

## 4. 客户常见问题：回答模板

**Q1. 这些价格是真的吗？**
中文要点：不是。批发价和阶梯价都是按 PVP 推算的示例；正式网站由后台按客户账号输出。
PT：*"Os preços desta demonstração são exemplos. No site final, cada conta validada vê os seus preços e escalões, calculados no servidor."*

**Q2. 图片是 AI 生成的吗？**
中文要点：氛围图是 AI 生成的，每张都标了"Imagem ilustrativa gerada por IA"。产品图全部是现有实拍，AI 图不冒充任何具体产品。上线前氛围图会换成更高清的版本或实拍。
PT：*"As imagens de ambiente são ilustrativas e estão identificadas. As fichas de produto usam só fotografias reais das peças."*

**Q3. 手机上能看吗？**
中文要点：可以。手机上 Hero 只放竖图，逐帧动画换成一段轻量循环视频，滚出屏幕会自动暂停。
PT：*"Sim — no telemóvel a página usa imagens verticais e um vídeo leve em vez da animação por fotogramas."*

**Q4. 动效会不会让网站变慢？对不喜欢动效的用户呢？**
中文要点：动画库本地加载，约 150 KB（GSAP + ScrollTrigger + Lenis）。系统开启"减少动态效果"时，所有动效自动关闭，内容一样完整。
PT：*"Quem tem 'reduzir movimento' ativo no sistema vê o site sem animações, com o mesmo conteúdo."*

**Q5. 客户注册以后怎么审核？**
中文要点：正式版里，注册进入后台待审核列表，销售核对 NIF 后开通，客户收到邮件后就能看到批发价。Demo 只模拟了前端。
PT：*"O pedido entra numa lista de aprovação; a equipa confirma o NIF e ativa a conta, e o cliente recebe um e-mail."*

**Q6. 能放到 WordPress 上吗？多久能上线？**
中文要点：可以。计划用 WooCommerce + 自定义区块主题 + B2B 插件（按角色显示价格、最小起订量、询价）。工期要看产品数量和数据导入方式，**以下是推测**：设计定稿后 6–10 周。
PT：*"Sim, em WordPress com WooCommerce. O prazo depende do número de referências e da importação de dados; fazemos uma estimativa depois de fechar o design."*

**Q7. 能对接库存 / ERP 吗？**
中文要点：WooCommerce 支持 CSV 导入，也可以通过 API 同步。具体要看你们现在用什么系统，需要先确认。
PT：*"Sim, por importação CSV ou por API — depende do sistema que usam hoje."*

**Q8. 联系方式、营业时间、数字是真的吗？**
中文要点：邮箱 geral@lmbiju.pt 沿用旧站；WhatsApp 是占位号码；营业时间和四个数字是示例，上线前替换成真实数据。
PT：*"Contactos, horário e números são provisórios nesta demonstração."*

**Q9. 能改颜色、字体吗？**
中文要点：可以，颜色、字体、间距都集中在一套设计变量里，改一处全站生效。金色刻意用得很少（不超过画面的 3%），主按钮不用金色。
PT：*"Sim — cores e tipos de letra estão centralizados; uma alteração aplica-se ao site inteiro."*

**Q10. 为什么首页是深色、目录是浅色？**
中文要点：首页负责"卖氛围"，深色背景让金属和宝石更亮；目录是"干活的地方"，浅色看价格、比参数更快。两者之间的"开灯"转场就是这个概念。
PT：*"A página inicial mostra as peças como numa montra à noite; o catálogo é o espaço de trabalho, claro e rápido."*

---

## 5. 演示前检查清单

- [ ] 先解压离线包（不要在压缩包里打开）
- [ ] 浏览器缩放 100%，全屏
- [ ] "Ver como cliente"开关先保持关闭，演示到目录时再打开
- [ ] 如果之前演示过：询价单里有上次加入的产品。在询价页逐行点"Remover"清空，或者换一个浏览器 / 无痕窗口
- [ ] 准备好回答"价格是不是真的"和"图片是不是 AI"（Q1、Q2）
