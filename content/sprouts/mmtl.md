---
title: 新芽专题介绍：多模态多任务统一模型
date: 2025-09-17T01:31:00Z
draft: false
math: true
---

> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。

## 一、专题介绍

### 1.1  研究背景
随着多源遥感数据的爆炸式增长和应用需求的日益复杂化，传统的单模态、单任务模型在效率和性能上的局限性愈发凸显。特别是在需要同时识别多种目标（目标检测）、理解场景布局（语义分割）并融合多源情报的场景下，构建一个能够**协同处理多模态数据、并发执行多项任务**的统一感知框架，是提升信息利用效率和决策智能化的核心环节 。也因此，发展多模态多任务统一模型已成为智能遥感领域备受关注的前沿技术方向 。   

### 1.2  研究意义
对**多模态多任务统一模型**的研究，并非仅仅是对现有遥感图像处理技术的增量式改进，而是一场旨在重塑地球观测范式、迈向遥感通用基础模型的关键探索：

* **军民应用价值**：通过对异构数据的协同利用，模型可生成远超单一数据源的、更鲁棒、更完整的场景理解 ，这对于**灾害应急、环境监测及国家安全**等需要高时效性与高可靠性的关键领域，构建**全天候、全要素**的综合感知能力，具有不可替代的战略价值 。   

* **推动技术革新**：通过共享表征与多任务协同优化，统一模型不仅能**显著提升计算与部署效率** ，更能利用任务间的互补性引入归纳偏置（Inductive Bias），从而增强模型的**泛化能力与综合性能** 。直接推动了模态融合、任务优化等AI核心算法前沿的持续创新。   

* **未来的可能性**：多模态多任务统一模型作为一个强大通用的地球观测智能体，未来能够通过自然语言查询等交互方式，**快速适应多样化的下游应用**，从而极大地降低遥感信息的分析门槛，奠定**遥感通用基础模型**的技术基石。

因此，这一研究主题不仅是迈向遥感通用基础模型的关键路径，更是一个融合了多模态学习、多任务优化与前沿网络架构的典型研究案例，非常适合作为探索人工智能前沿领域的训练课题。

### 1.3  当前主要挑战
构建一个能够智能解译多样化遥感数据（如SAR和光学影像），并同时执行多种复杂任务（如目标检测和语义分割）的单一统一模型，是一项艰巨的工程。在追求这种“一体化”范式的过程中，研究人员正积极应对三个基本且相互关联的挑战：

1. **数据制约：数据稀缺收集难**

   * 高质量、多模态、多任务标注数据集的严重匮乏是该领域的核心瓶颈，创建**精准匹配的对齐数据集成本极高**且极其耗费人力 。

   * 现有通用架构（如 Transformer）严重**依赖数据驱动**，遥感数据的稀缺性严重限制了这类先进架构的潜力。

   * 在遥感应用领域中，变化或事件类别与无变化的背景相比极为罕见，导致**正负样本极不平衡**，模型难以有效学习。  

2. **融合难题：异构模态协调难**

   * SAR与光学、红外等传感器在**成像机理上的本质差异**，直接比较或融合非常困难。

   * 简单的融合策略易引发**信息干扰与噪声传递**，如 SAR 的相干斑噪声可能会污染另一模态的干净特征，造成信息丢失。

3. **优化“拔河”：任务竞争平衡难**

   * 不同任务（如分割与检测）对共享特征的**偏好存在冲突**，网络难以学习到对所有任务均最优的通用表示 。

   * 不同任务的**损失量级差异与梯度方向冲突**，会严重干扰优化过程的稳定性与收敛性，亟需复杂的动态优化策略予以平衡 。

综上所述，由于在数据基础、模态融合与任务优化上存在多重瓶颈，多模态多任务统一模型仍处于活跃的探索期。正因如此，这一方向构成了极具价值的研究课题：它不仅紧密结合了遥感应用的迫切需求，也处在通用人工智能技术演进的最前沿，为研究者提供了绝佳的切入点。

![](https://imgtu.com/uploads/qgtddsx7/r-sm3det_pres.webp)

▲ 以 SM3Det 等前沿工作为代表的持续探索，正不断突破技术瓶颈。
## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

***

### 2.1  基础教材与学习材料

在开始探险之前，你需要掌握一些基础的“内功心法”，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)

* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材

* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门（难度不小）

此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。

* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2  入门文献（多任务经典方法）

> 学生第一阶段的阅读训练，主要包含 Mask RCNN 等分阶段多任务框架的参考文献，可辅助学生初步了解经典多任务方法。**仅用于入门，不可选择此部分文献汇报**。

* **[MCG](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/mcg/resources/MCG_CVPR2014.pdf): Multiscale Combinatorial Grouping (CVPR 2014)**
* **[SDS](https://arxiv.org/pdf/1407.1808): Simultaneous Detection and Segmentation (ECCV 2014)**
* **[PFN](https://arxiv.org/pdf/1509.02636): Proposal-free Network for Instance-level Object Segmentation (ICCV 2015)**
* **[DeepMask](https://arxiv.org/pdf/1506.06204): Learning to Segment Object Candidates (NIPS 2015)**
* **[MNC](https://arxiv.org/pdf/1512.04412): Instance-Aware Semantic Segmentation via Multi-task Network Cascades (CVPR 2016)**
* **[FoveaNet](https://arxiv.org/pdf/1708.02421): Perspective-Aware Urban Scene Parsing (CVPR 2017)**
* **[BAIS](https://arxiv.org/pdf/1612.03129): Boundary-Aware Instance Segmentation (CVPR 2017)**
* **[TrackR-CNN](https://arxiv.org/pdf/2103.08808): Track to Detect and Segment: An Online Multi-Object Tracker (CVPR 2019)**
* **[YOLACT](https://arxiv.org/pdf/1904.02689): Real-Time Instance Segmentation (ICCV 2019)**
* **[HTC](https://arxiv.org/pdf/1901.07518): Hybrid Task Cascade for Instance Segmentation (CVPR 2019)**
* **[BlendMask](https://arxiv.org/pdf/2001.00309): BlendMask: Top-Down Meets Bottom-Up for Instance Segmentation (CVPR 2020)**
* **[SOLO](https://arxiv.org/pdf/1912.04488): Segmenting Objects by Locations (ECCV 2020)**
* **[SOLOv2](https://arxiv.org/pdf/2003.10152):  Dynamic and Fast Instance Segmentation (NeurIPS 2020)**
* **[DenseViT](https://arxiv.org/pdf/2103.13413): Vision Transformers for Dense Prediction (ICCV 2021)**
* **[TA-OD](https://arxiv.org/pdf/2104.04782): Target-Aware Object Discovery and Association for Unsupervised Video Multi-Object Segmentation (CVPR 2021)**
* **[MaskDINO](https://arxiv.org/pdf/2206.02777): Towards A Unified Transformer-based Framework for Object Detection and Segmentation (CVPR 2023)**


***

### 2.3  进阶文献（遥感多模态前沿方法）

> 主要包含 可见光、红外 多模态融合或跨模态对齐相关工作，学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* **[Wasserstein CNN](https://arxiv.org/pdf/1708.02412): Learning Invariant Features for NIR-VIS Face Recognition (CVPR 2017)**
* **[DeepFuse](https://arxiv.org/pdf/1804.06992): Infrared and Visible Image Fusion using a Deep Learning Framework (CVPR 2018)**
* **[DenseFuse](https://arxiv.org/pdf/1804.08361): A Fusion Approach to Infrared and Visible Images (TIP 2019)**
* **[MMF-Track](https://arxiv.org/pdf/1908.11714): Multi-Modal Fusion for End-to-End RGB-T Tracking (ICCV 2019)**
* **[Hi-CMD](https://arxiv.org/pdf/1912.01230): Hierarchical Cross-Modality Disentanglement for Visible-Infrared Person Re-Identification (CVPR 2020)**
* **[NestFuse](https://arxiv.org/pdf/2007.00328):  An Infrared and Visible Image Fusion Architecture based on Nest Connection and Spatial Channel Attention (IJCV 2020)**
* **[MFR-CFR](https://arxiv.org/pdf/2009.12664): Multispectral Fusion for Object Detection with Cyclic Fuse-and-Refine Blocks (ECCV 2020)**
* **[RFN-Nest](https://arxiv.org/pdf/2103.04286): An End-to-End Residual Fusion Network for Infrared and Visible Images (IJCAI 2021)**
* **[AlignGAN](https://arxiv.org/pdf/2108.07422): Learning by Aligning: Visible-Infrared Person Re-Identification using Cross-Modal Correspondences (AAAI 2021)**
* **[TADAL](https://arxiv.org/pdf/2203.16220): Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible Images for Object Detection (CVPR 2022)**
* **[MoE-Fusion](https://arxiv.org/pdf/2302.01392): Multi-modal Gated Mixture of Local-to-Global Experts for Dynamic Image Fusion (CVPR 2023)**
* **[DFNet](https://arxiv.org/pdf/2109.07662): Dynamic Fusion Network for RGBT Tracking (ICCV 2023)**
* **[MUNet](https://arxiv.org/pdf/2309.06262): Modality Unifying Network for Visible-Infrared Person Re-Identification (TIP 2023)**
* **[C²Former](https://arxiv.org/pdf/2306.16175):  Calibrated and Complementary Transformer for RGB-Infrared Object Detection (CVPR 2024)**
* **[RTS](https://arxiv.org/pdf/2401.10731): Removal then Selection: A Coarse-to-Fine Fusion Perspective for RGB-Infrared Object Detection (ECCV 2024)**


***

### 2.4  多模态多任务统一模型领域相关文献

> 结合本专题的研究背景，逐渐引导学生进入多模态多任务统一模型领域。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* **[GradNorm](https://arxiv.org/pdf/1711.02257): Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks (ICML 2018)**
* **[MTL-Uncertainty](https://arxiv.org/pdf/1705.07115): Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics (CVPR 2018)**
* **[DAMTL](https://arxiv.org/pdf/1708.00260): Deep Asymmetric Multi-task Feature Learning (ECCV 2018)**
* **[DEN](https://arxiv.org/pdf/1909.04860): Deep Elastic Networks with Model Selection for Multi-Task Learning (NeurIPS 2019)**
* **[Stochastic Filter Groups for Multi-Task CNNs](https://arxiv.org/pdf/1908.09597): Learning Specialist and Generalist Convolution Kernels (CVPR 2019)**
* **[NDDR-CNN](https://arxiv.org/pdf/1801.08297): Layerwise Feature Fusing in Multi-Task CNNs by Neural Discriminative Dimensionality Reduction (CVPR 2019)**
* **[Generalization in Multitask Deep Neural Classifiers](https://arxiv.org/pdf/1910.13593):  A Statistical Physics Approach (arXiv 2019)**
* **[MTL-Attention](https://arxiv.org/pdf/1803.10704): End-to-End Multi-Task Learning with Attention (CVPR 2019)**
* **[PAP](https://arxiv.org/pdf/1906.03525): Pattern-Affinitive Propagation across Depth, Surface Normal and Semantic Segmentation (CVPR 2019)**
* **[AdaShare](https://arxiv.org/pdf/1911.12423): Learning What To Share For Efficient Deep Multi-Task Learning (NeurIPS 2020)**
* **[OneFormer](https://arxiv.org/pdf/2211.06220): One Transformer to Rule Universal Image Segmentation (CVPR 2022)**
* **[PromptIR](https://arxiv.org/pdf/2306.13090): Prompting for All-in-One Blind Image Restoration (CVPR 2023)**
* **[MQT](https://arxiv.org/pdf/2205.14354): Multi-Task Learning with Multi-Query Transformer for Dense Prediction (ICCV 2023)**
* **[All in One and One for All: ](https://arxiv.org/pdf/2402.09834): A Simple yet Effective Method towards Cross-domain Graph Pretraining (ICLR 2024)**
* **[SM3Det](https://arxiv.org/pdf/2412.20665):  A Unified Model for Multi-Modal Remote Sensing Object Detection (arXiv 2024)**
* **[All in One](https://arxiv.org/pdf/2307.03373): Exploring Unified Vision-Language Tracking with Multi-Modal Alignment (CVPR 2025)**

***

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。多模态多任务统一模型是一个充满挑战与机遇的领域，它既是实现遥感通用基础模型的‘必由之路’，也是检验前沿 AI 算法综合能力的‘试金石’。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
