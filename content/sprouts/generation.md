---
title: 新芽专题介绍（X）：面向下游任务的生成模型
date: 2025-08-02T12:25:00Z
draft: false
math: true
---
> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。


## 一、专题介绍

### 1.1 研究背景

目标检测和目标跟踪已经广泛应用于自动驾驶、机器人、遥感解译和无人机视频分析。自动驾驶系统需要持续感知车辆与行人，遥感与无人机平台需要从大范围图像或视频中发现并跟踪船舶、飞机和车辆。随着应用逐渐从受控环境走向开放世界，系统不仅要处理常见目标，还要应对罕见类别、复杂天气、拥挤遮挡和快速运动等情况。

#### 下游任务面临的数据瓶颈

过去十余年，检测与跟踪模型的能力有了显著提升，但这种进步很大程度上建立在大规模人工标注数据之上。检测数据需要为每个目标标注类别和边界框；跟踪数据还要在连续帧之间维持统一的身份编号。场景越拥挤、视频越长、遮挡越频繁，标注工作就越困难，也越容易出现错误。除此之外，真正决定系统可靠性的往往是少见的困难场景，例如夜间与恶劣天气、小目标与密集目标、严重遮挡、高速运动、异常视角以及目标消失后再次出现。这些样本在真实世界中难以系统地采集，却正是模型最需要学习的内容。

![从三维对象与虚拟环境生成图像和自动标注的原理示意](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-023-42898-9/MediaObjects/41467_2023_42898_Fig1_HTML.png)

> 这幅图展示了合成数据从三维模型到训练样本的生成过程。研究者首先建立带有纹理、骨骼和关节的三维对象，再将其放入虚拟环境，通过改变对象姿态、数量、背景、光照和相机视角生成多样化图像。由于计算机掌握每个对象的类别、位置、身份和几何信息，渲染图像时可以同步输出边界框、对象 ID、关键点、深度图和分割掩码。这些标注可直接用于目标检测、目标跟踪、姿态估计和图像分割，减少逐张、逐帧人工标注的成本。图源：[replicAnt](https://www.nature.com/articles/s41467-023-42898-9)。

#### 从“使用数据”走向“制造数据”

生成模型为这一数据瓶颈提供了新的思路。GAN、扩散模型和生成式 Transformer 不仅可以学习图像或视频的分布，还可以在文本、布局、边界框、轨迹等条件约束下生成新的样本。于是，研究问题从“怎样用已有数据训练模型”进一步发展为“能否按照任务需要主动制造数据”。**这里所说的“面向下游任务”，强调的不是单纯追求图像好看，而是让合成数据能够被准确标注、覆盖真实数据缺口，并最终提升检测或跟踪性能。**

这一专题关注的完整链路可以概括为：

1. 分析真实数据和下游模型的薄弱环节；
2. 利用可控生成模型合成针对性样本；
3. 将生成条件转化为检测或跟踪标注；
4. 通过下游指标验证合成数据是否真正有效。

生成模型因而不再是孤立的内容生产工具，而成为感知系统数据闭环的一部分。

### 1.2 问题定义

本专题研究的问题可以表述为：

> **如何利用生成模型，按照目标检测和目标跟踪任务的实际需求，生成带有可靠标注、能够补充真实数据缺口，并最终提升下游模型性能的图像或视频数据？**

#### 数学定义

严格来说，“面向下游任务的生成模型”是多个研究方向交叉形成的问题，目前并不存在由某个标准组织或单篇论文规定的唯一“官方定义”。这里对一些代表性工作中的定义进行总结：合成数据是否有价值，应由使用这些数据训练出的模型在真实下游任务上的表现决定。

设真实训练集为

$$
\mathcal{D}_{r}=\{(x_i,y_i)\}_{i=1}^{N},
$$

其中，$x_i$ 表示真实图像或视频，$y_i$ 表示相应的检测或跟踪标注。生成模型 $G_{\phi}$ 根据控制条件 $c$ 和随机噪声 $z$ 产生带标注的合成样本：

$$
(\tilde{x},\tilde{y})=G_{\phi}(c,z), \qquad
\mathcal{D}_{s}(\phi)=\{(\tilde{x}_j,\tilde{y}_j)\}_{j=1}^{M}.
$$

下游模型 $f_{\theta}$ 首先在真实数据与合成数据上训练：

$$
\theta^{*}(\phi)
=\arg\min_{\theta}
\left[
\mathcal{L}_{\mathrm{train}}(\theta;\mathcal{D}_{r})
+\lambda\mathcal{L}_{\mathrm{train}}(\theta;\mathcal{D}_{s}(\phi))
\right],
$$

其中，$\lambda$ 控制合成数据在训练中的权重。生成模型的目标不是单纯让图像更逼真，而是选择最有利于下游任务的参数 $\phi$，使训练后的模型在独立的真实验证集 $\mathcal{D}_{v}$ 上损失最小：

$$
\phi^{*}
=\arg\min_{\phi}
\mathcal{L}_{\mathrm{task}}\!\left(\theta^{*}(\phi);\mathcal{D}_{v}\right).
$$

对于目标检测，标签可写为 $y_i=\{(k_{ij},b_{ij})\}_{j=1}^{n_i}$，其中 $k_{ij}$ 是类别，$b_{ij}$ 是边界框；对于目标跟踪，标签还要扩展到时间维度，可写为 $y_i=\{(b_{t,j},\mathrm{id}_j)\}_{t,j}$，其中 $\mathrm{id}_j$ 表示目标在不同帧中保持不变的身份编号。由此可见，这一专题的数学核心是：**优化生成的数据，使其训练出的检测或跟踪模型在真实数据上性能更好，而不是只优化生成图像的视觉质量。**

要理解这一问题，首先需要区分“下游任务”和“数据生成”分别承担什么角色。

#### 目标检测

给定一张图像，目标检测模型需要输出图像中每个目标的类别与空间位置。空间位置通常用边界框表示，因此一个检测样本至少包含图像、类别标签和边界框标注。面向检测的数据生成不仅要生成目标，还要保证目标真实地出现在指定位置，并使生成结果与边界框、类别等标签一致。

![根据类别与边界框条件生成的目标检测场景示例](https://arxiv.org/html/2405.15199v2/teaser.png)

> 图中展示了由类别和边界框条件控制的多目标图像。边界框既约束“生成在哪里”，也可作为下游检测训练的候选标注。图源：[ODGEN](https://arxiv.org/abs/2405.15199)。
>

#### 目标跟踪

目标跟踪处理连续视频。除了逐帧定位目标，还要为同一对象分配稳定的身份编号（ID），并把各帧中的位置连接成轨迹。因此，面向跟踪的数据生成必须同时保证空间定位、运动连续性和身份一致性。尺度变化、多个目标相互遮挡，以及目标消失后再次出现，都会增加身份关联的难度。

![多目标跟踪中的尺度变化、目标重叠与消失后重现](https://arxiv.org/html/2312.00651v1/t1.png)

> 多目标跟踪中的三类典型时序情形：尺度变化、目标重叠和消失后重现。彩色轨迹表示同一目标在不同帧中的位置变化。图源：[TrackDiffusion](https://arxiv.org/abs/2312.00651)。
>

#### 本专题中的“面向下游任务”

普通图像或视频生成主要关心结果是否清晰、自然并符合文本描述；面向下游任务的生成还必须回答三个问题：

1. **生成什么：** 是否覆盖小目标、长尾类别、遮挡或高速运动等模型薄弱场景？
2. **标签是否可信：** 生成图像是否与类别、边界框、轨迹和身份编号严格一致？
3. **是否真正有用：** 加入合成数据后，真实测试集上的 mAP、HOTA 或 IDF1 是否提高？

因此，本专题的研究对象并不是一般意义上的“生成漂亮图片”，而是以检测与跟踪性能为最终评价标准的**任务导向数据生成**。

### 1.3 研究意义

#### 1. 突破真实数据的采集限制

这一方向首先改变了训练数据的获取方式。对于极端天气、罕见类别、高风险环境、特殊遥感场景等难以采集的数据，生成模型可以补充样本数量，也可以主动调整类别、尺度、位置、视角和背景。与随机翻转、裁剪等传统增强方式相比，可控生成有机会创造训练集中原本不存在的新组合，使模型看到更丰富的长尾情况。

#### 2. 为目标检测生成“有训练价值”的样本

“更多数据”并不天然等于“更好的数据”。面向目标检测的生成应围绕模型需求展开：如果模型不擅长识别小目标，就需要增加合理尺度和清晰边界的小目标；如果模型在密集遮挡场景中容易漏检，就应控制目标数量、空间布局与遮挡关系；如果某一类别样本稀少，则需要在不破坏类别结构和背景语义的前提下补齐长尾类别。生成质量因此需要同时考虑视觉真实性、标注一致性和训练价值。

#### 3. 为目标跟踪补充连续、可控的运动数据

目标跟踪进一步提出了时间层面的要求。同一对象在连续帧中必须保持相对稳定的外观与身份，其运动轨迹应符合场景规律，遮挡、交互、消失和重现也要自然发生。只把若干独立生成的图片拼成视频，往往会造成外观闪烁、身份漂移或运动突变，无法构成可靠的跟踪训练数据。轨迹条件视频生成的价值，就在于能够同时控制“对象在哪里”和“对象是谁”。

#### 4. 构建“生成—训练—反馈”闭环

从更长远的角度看，这一方向把“生成”与“理解”连接成闭环：

> **下游模型暴露薄弱场景 → 生成模型制造针对性样本 → 数据筛选与自动标注 → 模型再训练与评测 → 继续分析新的错误**

当这一过程能够稳定迭代时，系统就不再只是被动使用数据，而具备了围绕任务目标主动构建数据的能力。

### 1.4 当前主要挑战

#### 挑战一：人眼感知友好不等于任务有效

这一方向最核心的矛盾是：生成的内容符合人眼感知不等于对下游任务有效，一张视觉效果很好的船舶图像，如果船体结构失真、位置不合理，或者边界框与实际目标不一致，仍可能向检测器提供错误监督。FID、IS 或 CLIP Score 能够从不同侧面衡量图像分布或语义匹配，却不能直接说明某批数据能否提高 mAP、HOTA 或 IDF1。一张视觉效果很好的船舶图像，如果船体结构失真、位置不合理，或者边界框与实际目标不一致，仍可能向检测器提供错误监督。因此，**最终评价必须回到下游实验，并与仅使用真实数据、传统数据增强以及等量随机合成等基线公平比较。**

![相同训练轮数下真实数据与合成数据对下游检测和跟踪的影响](https://wm-research.github.io/Dream4Drive/static/images/teaser.png)

> 这组对比说明：如果没有控制训练轮数、合成数据数量和评价条件，大量合成数据未必稳定优于真实数据基线。它体现了本方向的核心挑战——生成质量和数据规模不能替代严格的下游验证。图源：[Dream4Drive 项目页与论文](https://wm-research.github.io/Dream4Drive/)。
>

#### 挑战二：图像与标签必须同步生成

第二个难题是图像与标签必须同步生成。目标检测需要类别和边界框，目标跟踪还需要跨帧身份与轨迹。最直接的办法是将边界框、分割掩码或轨迹作为生成条件，使条件本身成为标签；但条件与生成结果并不总能严格一致，仍可能出现漏生成、对象越界、类别混淆和多个对象融合。因此，生成之后通常还需要检测器、分割模型或人工抽查进行质量过滤。

#### 挑战三：复杂场景难以精确控制

复杂场景的可控性同样尚未解决。多目标场景不仅包含对象本身，还包含尺度、朝向、遮挡、相对位置以及对象与背景之间的语义关系。文本提示难以精确描述这些几何约束，而布局控制又可能牺牲图像自然度。遥感图像中的旋转目标尤其典型：水平边界框不足以描述飞机、船舶等目标的朝向，需要旋转框控制与领域纹理建模共同发挥作用。

#### 挑战四：视频需要维持时间与身份一致性

视频生成还要面对时间一致性与身份一致性。外观细节随帧漂移、遮挡后身份改变、目标数量突然变化等问题，都会破坏跟踪标签。即使生成视频看起来连贯，也要检查轨迹是否与画面中的实际运动吻合，以及这些序列是否覆盖了跟踪模型容易发生 ID Switch 的交互模式。

#### 挑战五：合成数据与真实数据仍有领域差距

合成数据与真实数据之间仍存在领域差距。纹理、光照、成像噪声、运动模糊和目标结构上的细微偏差，都可能让模型学习到“合成痕迹”。实践中通常需要混合真实数据与合成数据，并研究合适的采样比例、质量过滤和领域适配策略。**生成数据并非越多越好；低质量或分布失衡的合成样本甚至可能降低真实测试集上的性能。**

***

## 二、学习资料与参考文献

本专题按照“深度学习基础—检测与跟踪—生成模型—可控数据生成—任务闭环实验”的顺序进行内容推荐。

### 2.1 基础教材与学习材料

#### 深度学习基础

开始论文阅读前，需要理解卷积神经网络、Transformer、损失函数、反向传播与优化，并能够使用 PyTorch 完成数据读取、训练和评测。推荐材料如下：

* [《动手学深度学习》](https://zh.d2l.ai/)及配套[课程视频](https://space.bilibili.com/1567748478/lists/358497?type=series)——适合中文初学者建立完整知识框架；
* [PyTorch 官方教程](https://pytorch.org/tutorials/)——用于学习模型实现、数据处理与训练流程。

#### 计算机视觉基础

进入计算机视觉实验前，应熟悉边界框、IoU、Precision、Recall、AP 与 mAP；目标跟踪部分还要理解轨迹、目标关联、ID Switch，以及 MOTA、IDF1 和 HOTA 的区别。建议尽早使用 COCO 格式的小型数据集跑通训练与评测流程，在实际结果中理解这些概念。

> **学习建议：** 不必等到所有基础知识全部掌握后才开始科研。更推荐“学习基础 → 阅读论文 → 运行代码 → 发现问题 → 回头补充知识”的循环式学习方式。

### 2.2 入门文献（一）：目标检测基础

这一阶段的目标不是记住所有模型结构，而是理解检测器如何表示目标、如何匹配预测与标签，以及尺度不平衡和类别不平衡为什么会影响训练。

* [YOLO](https://arxiv.org/abs/1506.02640)：You Only Look Once: Unified, Real-Time Object Detection（CVPR 2016）。将目标检测统一为单次前向传播的回归问题，奠定了实时单阶段检测器的代表性范式。

* [Faster R-CNN](https://arxiv.org/abs/1506.01497)：Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks（NeurIPS 2015）。用可训练的区域提议网络替代外部候选框算法，形成经典的两阶段检测框架。

* [FPN](https://arxiv.org/abs/1612.03144)：Feature Pyramid Networks for Object Detection（CVPR 2017）。通过自顶向下路径与横向连接融合多尺度特征，显著改善不同尺寸目标的检测效果。

* [RetinaNet](https://arxiv.org/abs/1708.02002)：Focal Loss for Dense Object Detection（ICCV 2017；[代码](https://github.com/facebookresearch/Detectron)）。提出 Focal Loss 抑制易分类负样本的影响，缓解密集单阶段检测中的类别不平衡。

* [FCOS](https://arxiv.org/abs/1904.01355)：FCOS: Fully Convolutional One-Stage Object Detection（ICCV 2019；[代码](https://github.com/tianzhi0549/FCOS)）。以逐像素预测取代锚框设计，展示了无锚单阶段目标检测的简洁方案。

* [DETR](https://arxiv.org/abs/2005.12872)：End-to-End Object Detection with Transformers（ECCV 2020；[代码](https://github.com/facebookresearch/detr)）。把检测建模为集合预测，并通过二分图匹配实现无需锚框和非极大值抑制的端到端训练。

* [Deformable DETR](https://arxiv.org/abs/2010.04159)：Deformable DETR: Deformable Transformers for End-to-End Object Detection（ICLR 2021；[代码](https://github.com/fundamentalvision/Deformable-DETR)）。用稀疏的多尺度可变形注意力加快 DETR 收敛，并提升小目标检测能力。

### 2.3 入门文献（二）：目标跟踪基础

这一阶段先把 Tracking-by-Detection 的流程跑通：逐帧检测目标，提取运动或外观信息，再完成跨帧关联。阅读时重点关注一次错误检测如何传递为断裂轨迹或身份切换。

* [SORT](https://arxiv.org/abs/1602.00763)：Simple Online and Realtime Tracking（ICIP 2016）。以卡尔曼滤波和匈牙利匹配构成轻量级在线多目标跟踪基线。

* [DeepSORT](https://arxiv.org/abs/1703.07402)：Simple Online and Realtime Tracking with a Deep Association Metric（ICIP 2017）。在 SORT 的运动关联基础上加入深度外观特征，以减少遮挡场景中的身份切换。

* [ByteTrack](https://arxiv.org/abs/2110.06864)：ByteTrack: Multi-Object Tracking by Associating Every Detection Box（ECCV 2022；[代码](https://github.com/ifzhang/ByteTrack)）。同时关联高、低置信度检测框，利用原本会被丢弃的候选框恢复被遮挡目标的轨迹。

* [BoT-SORT](https://arxiv.org/abs/2206.14651)：BoT-SORT: Robust Associations Multi-Pedestrian Tracking（arXiv 2022；[代码](https://github.com/NirAharon/BOT-SORT)）。结合相机运动补偿、改进的卡尔曼滤波状态与外观信息，增强复杂场景下的轨迹关联。

* [FairMOT](https://arxiv.org/abs/2004.01888)：FairMOT: On the Fairness of Detection and Re-Identification in Multiple Object Tracking（IJCV 2021；[代码](https://github.com/ifzhang/FairMOT)）。在单一网络中平衡目标检测与行人重识别任务，兼顾跟踪精度与推理效率。

* [HOTA](https://arxiv.org/abs/2009.07736)：HOTA: A Higher Order Metric for Evaluating Multi-Object Tracking（IJCV 2021）。从检测、关联与定位三个维度综合评价多目标跟踪，便于诊断不同类型的跟踪错误。

### 2.4 入门文献（三）：生成与可控生成基础

这一阶段需要理解生成模型怎样学习数据分布，以及文本、边界框、掩码等条件如何进入生成过程。对本专题而言，**<u>可控性</u>**比单纯提高视觉质量更重要。

* [GAN](https://arxiv.org/abs/1406.2661)：Generative Adversarial Nets（NeurIPS 2014）。通过生成器与判别器的对抗训练学习数据分布，开创了现代生成建模的重要路线。

* [DDPM](https://arxiv.org/abs/2006.11239)：Denoising Diffusion Probabilistic Models（NeurIPS 2020；[代码](https://github.com/hojonathanho/diffusion)）。通过学习逐步逆转加噪过程生成样本，奠定了扩散生成模型的基础框架。

* [Latent Diffusion](https://arxiv.org/abs/2112.10752)：High-Resolution Image Synthesis with Latent Diffusion Models（CVPR 2022；[代码](https://github.com/CompVis/latent-diffusion)）。把扩散过程移至压缩潜空间，在保持生成质量的同时显著降低高分辨率图像生成成本。

* [Layout2Im](https://arxiv.org/abs/1811.11389)：Image Generation From Layout（CVPR 2019）。根据类别与边界框布局合成图像，是布局可控生成的代表性早期工作。

* [GLIGEN](https://arxiv.org/abs/2301.07093)：GLIGEN: Open-Set Grounded Text-to-Image Generation（CVPR 2023；[项目页](https://gligen.github.io/)）。在预训练文本生成模型中注入位置与文本等 grounding 条件，实现开放词汇的空间可控生成。

* [ControlNet](https://arxiv.org/abs/2302.05543)：Adding Conditional Control to Text-to-Image Diffusion Models（ICCV 2023）。通过可训练的条件分支为预训练扩散模型加入边缘、深度和姿态等结构控制。

### 2.5 进阶文献：面向目标检测的数据生成

建议围绕三个问题阅读：生成时如何控制目标布局，生成条件能否直接转化为可靠标注，以及加入合成数据后真实测试集上的检测性能是否提高。

* [GeoDiffusion](https://arxiv.org/abs/2306.04607)：GeoDiffusion: Text-Prompted Geometric Control for Object Detection Data Generation（ICLR 2024）。将边界框等几何条件转化并注入文本到图像扩散过程，以生成带布局约束的检测训练数据。

* [InstaGen](https://arxiv.org/abs/2402.05937)：InstaGen: Enhancing Object Detection by Training on Synthetic Dataset（CVPR 2024；[项目页与代码](https://fcjian.github.io/InstaGen/)）。利用实例级生成与自动标注构建合成检测数据，探索扩展类别与提升检测性能的训练范式。

* [ODGEN](https://arxiv.org/abs/2405.15199)：ODGEN: Domain-specific Object Detection Data Generation with Diffusion Models（NeurIPS 2024）。通过区域级与整图领域适配及边界框条件生成，为多类、密集和遮挡场景合成检测数据。

* [AeroGen](https://arxiv.org/abs/2411.15497)：AeroGen: Enhancing Remote Sensing Object Detection with Diffusion-Driven Data Generation（CVPR 2025；[代码](https://github.com/Sonettoo/AeroGen)）。针对遥感目标的尺度、方向与纹理特征，以水平框和旋转框控制生成可用于检测训练的图像。

* [X-Paste](https://arxiv.org/abs/2212.03863)：X-Paste: Revisiting Scalable Copy-Paste for Instance Segmentation Using CLIP and Stable Diffusion（ICML 2023；[代码与模型](https://github.com/yoctta/XPaste)）。借助 CLIP 筛选和扩散模型生成实例，扩展可用于实例分割的高质量复制粘贴素材。

* [DatasetDM](https://arxiv.org/abs/2308.06160)：DatasetDM: Synthesizing Data with Perception Annotations Using Diffusion Models（NeurIPS 2023；[项目页](https://weijiawu.github.io/DatasetDM/)）。从扩散模型特征中预测多类感知标注，使合成图像能够服务于检测、分割与姿态等任务。

* [Gen2Det](https://arxiv.org/abs/2312.04566)：Gen2Det: Generate to Detect（arXiv 2023）。以 grounded 图像生成、两级质量过滤和针对性训练策略组成模块化的合成检测数据管线。

* [AnySynth](https://arxiv.org/abs/2411.16749)：AnySynth: Harnessing the Power of Image Synthetic Data Generation for Generalized Vision-Language Tasks（arXiv 2024）。统一任务布局、可控图像生成与任务标注三个模块，为多种视觉及视觉—语言任务合成数据。

### 2.6 进阶文献：面向目标跟踪的视频与数据生成

目标跟踪方向的任务专用生成研究仍相对较少。阅读时可以把方法分成两条路线：一条使用游戏引擎或三维仿真获得完整真值，另一条利用视频生成模型按照轨迹合成连续帧。两者分别在标注精度与视觉域差距、生成灵活性与时间一致性之间作出取舍。

* [MOTSynth](https://arxiv.org/abs/2108.09518)：MOTSynth: How Can Synthetic Data Help Pedestrian Detection and Tracking?（ICCV 2021）。利用游戏引擎生成大规模行人视频与完整真值，系统研究合成数据对行人检测和多目标跟踪的作用。

* [TrackDiffusion](https://arxiv.org/abs/2312.00651)：TrackDiffusion: Tracklet-Conditioned Video Generation via Diffusion Models（WACV 2025；[项目页](https://kaichen1998.github.io/projects/trackdiffusion/)）。以目标轨迹片段控制视频扩散生成，并通过实例增强机制改善跨帧外观和身份一致性。

* [PointOdyssey](https://arxiv.org/abs/2307.15055)：PointOdyssey: A Large-Scale Synthetic Dataset for Long-Term Point Tracking（ICCV 2023；[数据与代码](https://pointodyssey.com/)）。构建包含长时间运动、遮挡和复杂视角变化的合成数据集，用于长期像素点跟踪研究。

* [Kubric](https://arxiv.org/abs/2203.03570)：Kubric: A Scalable Dataset Generator（CVPR 2022）。提供基于物理仿真的可扩展数据生成框架，可输出光流、深度、分割和对象轨迹等精确真值。

* [DrivingDiffusion](https://arxiv.org/abs/2310.07771)：DrivingDiffusion: Layout-Guided Multi-View Driving Scene Video Generation with Latent Diffusion Model（ECCV 2024；[项目页](https://drivingdiffusion.github.io/)）。以布局为条件联合生成多视角驾驶视频，重点保持相邻视角与时间维度的一致性。

* [MagicDrive](https://arxiv.org/abs/2310.02601)：MagicDrive: Street View Generation with Diverse 3D Geometry Control（ICLR 2024；[项目页](https://flymin.github.io/magicdrive/)）。融合相机参数、三维框与道路地图等条件，生成具有多样三维几何约束的街景图像。

### 2.7 综述推荐

- [Synthetic Data Augmentation Survey](https://doi.org/10.1007/s11633-022-1411-7)：A Survey of Synthetic Data Augmentation Methods in Machine Vision（Machine Intelligence Research 2024）。系统梳理三维图形、神经风格迁移、可微渲染及 GAN、VAE 等合成数据方法，并讨论公开数据集、适用任务和真实场景泛化问题。

## 三、结语与期望

“面向下游任务的生成模型”把生成式人工智能与计算机视觉的实际需求连接在一起。它要求研究者同时理解生成模型能够制造什么、检测和跟踪模型真正缺少什么，以及怎样用实验判断合成数据是否有价值。这里的核心不在于“为了生成而生成”，而在于围绕具体任务设计数据、监督和评价。

未来的智能系统或许不仅能够从人类提供的数据中学习，还能够发现自身不足并主动构建新的训练经验。期待大家在专题学习和最终汇报中，提出属于自己的问题，并用扎实的实验回答它。
