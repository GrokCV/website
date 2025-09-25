---
title: 新芽专题介绍（9）：遥感视觉定位
date: 2025-09-17T01:42:00Z
draft: false
math: true
---

> 此专题由非南开大学老师发布，选修南开大学 2025 秋《人工智能实践课-初级》课程的同学请勿选择此专题。非本课程选修同学可自由选择。

## 一、专题介绍

### 1.1  研究背景

遥感视觉定位旨在让AI模型根据自然语言描述在遥感图像中准确地定位（以水平框、旋转框或像素级掩码的形式）所指代的特定目标或区域。该技术极大地增强了**人机交互的直觉性和效率**，是构建下一代智能遥感解译系统的基石。

### 1.2  研究意义

遥感影像具有俯瞰视角、尺度多变、目标密集、背景复杂等特点，这使得许多为自然图像设计的多模态模型难以直接应用，也赋予了遥感视觉定位独特的研究价值和挑战。成功的遥感视觉定位技术能直接应用于：

1. **军事与安全**：快速定位和识别感兴趣的军事设施、装备部署，支持情报分析和战场态势感知。

2. **灾害应急响应**：根据无人机图像快速定位受灾区域和民众，指导救援行动。

3. **城市管理**：助力智慧交通以及城市数字化管理。

因此，这一研究主题不仅意义重大，而且是多模态学习和遥感科学的交叉研究领域的一个典型研究案例，非常适合作为本科生进入科研领域的启蒙训练。

![](https://imgtu.com/uploads/q5qc9i8r/file_4a47a0.png)

▲一个典型的遥感视觉定位示意图：目标占比极小，对多模态理解能力要求较高。

### 1.3  当前主要挑战

尽管前景广阔，但实现高精度的遥感视觉定位仍面临诸多严峻挑战：

1. **挑战一：目标尺度差异巨大，显著性低**

   * 遥感图像从千米级宏观场景到米级精细地物并存，目标尺度跨度极大。

   * 许多感兴趣目标（如特定车辆、小型建筑）在图像中占比小，纹理和细节特征微弱，极易被复杂背景或同类地物淹没。

2. **挑战二：空间关系复杂，描述歧义性强**

   * 自然语言描述中充满了“左上角”、“A和B之间”、“河流北岸”等相对空间关系，要求模型对空间几何和方位有深刻理解。

   * 同一场景可能存在多个相似物体，描述中的细微差别（如“较小的那座雷达站”）需要模型具备极强的分辨和推理能力。

3. **挑战三：输出形式多样，需统一框架**

   * 实际应用中对定位精度的要求不同，需要模型能灵活输出水平边界框、定向边界框或精确的分割掩码。

   * 传统的专用模型通常只为一种输出形式设计，难以泛化。设计一个能统一处理多种定位任务的框架是一项重要挑战。

因此，遥感视觉定位是一个充满机遇的研究方向，它既需要解决实际的应用难题，也推动着多模态人工智能技术的前沿探索，非常适合作为深入科研的切入点。

***

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

### 2.2  入门文献（视觉定位经典方法）

> 学生第一阶段的阅读训练，可帮助理解目标检测/语义分割/关键点检测这一通用方向。**仅用于入门，不可选择此部分文献汇报**。

* **[RefCOCO](https://arxiv.org/pdf/1608.00272): Modeling context in referring expressions (ECCV 2016)**

* **[TransVG](https://arxiv.org/pdf/2104.08541): TransVG: End-to-End Visual Grounding with Transformers (ICCV 2021)**

* **[GLIP](https://arxiv.org/pdf/2112.03857): Grounded Language-Image Pre-training (CVPR 2022)**

* [GRES](https://arxiv.org/pdf/2306.00968): GRES: Generalized Referring Expression Segmentation (CVPR 2023)

* [TransVG++](https://arxiv.org/pdf/2206.06619): End-to-End Visual Grounding With Language Conditioned Vision Transformer (T-PAMI 2023)

* [Dynamic MDETR](https://arxiv.org/pdf/2209.13959): Dynamic MDETR: A Dynamic Multimodal Transformer Decoder for Visual Grounding (T-PAMI 2024)

***

### 2.3  进阶文献（遥感视觉定位方法）

> 结合本专题的研究背景，逐渐引导学生进入遥感视觉定位。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>
> 遥感视觉定位可分为区域级和像素级两种。

**区域级遥感视觉定位**

* **[RSVG](https://dl.acm.org/doi/abs/10.1145/3503161.3548316): Visual Grounding in Remote Sensing Images (ACM MM 2022)**

* **[DIOR-RSVG](https://arxiv.org/pdf/2210.12634): RSVG: Exploring Data and Models for Visual Grounding on Remote Sensing Data (TGRS 2023)**

* [GeoText-1652](https://arxiv.org/pdf/2311.12751): Towards Natural Language-Guided Drones: GeoText-1652 Benchmark with Spatial Relation Matching (ECCV 2024)

* [RSVG-HR](https://ieeexplore.ieee.org/abstract/document/10542207): Language Query-Based Transformer With Multiscale Cross-Modal Alignment for Visual Grounding on Remote Sensing Images (TGRS 2024)

* [OPT-RSVG](https://ieeexplore.ieee.org/abstract/document/10584552): Language-Guided Progressive Attention for Visual Grounding in Remote Sensing Images (TGRS 2024)

* [AerialVG](https://arxiv.org/pdf/2504.07836): AerialVG: A Challenging Benchmark for Aerial Visual Grounding by Exploring Positional Relations (arXiv 2025)

* [RefDrone](https://arxiv.org/pdf/2502.00392): RefDrone: A Challenging Benchmark for Referring Expression Comprehension in Drone Scenes (arXiv 2025)

**像素级遥感视觉定位**

* **[RRSIS](https://ieeexplore.ieee.org/abstract/document/10458079): RRSIS: Referring Remote Sensing Image Segmentation（TGRS 2024)**

* **[RMSIN](https://arxiv.org/abs/2312.12470): Rotated Multi-Scale Interaction Network for Referring Remote Sensing Image Segmentation (CVPR 2024)**

* [CroBIM](https://arxiv.org/pdf/2410.08613): Cross-Modal Bidirectional Interaction Model for Referring Remote Sensing Image Segmentation (arXiv 2024)

* [RemoteSAM](https://arxiv.org/pdf/2505.18022): RemoteSAM: Towards Segment Anything for Earth Observation (arXiv 2025)

* [NWPU-Refer](https://arxiv.org/abs/2506.03583): A Large-Scale Referring Remote Sensing Image Segmentation Dataset and Benchmark (arXiv 2025)

***

### 2.4  基于多模态大模型的视觉定位相关文献

> 结合本专题的研究背景，逐渐引导学生进入最新的基于多模态大模型的遥感视觉定位。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

1. **[Text4Seg](https://arxiv.org/abs/2410.09855)：Text4Seg: Reimagining Image Segmentation as Text Generation (ICLR 2025)**

2. **[GeoGround](https://arxiv.org/pdf/2411.11904)：GeoGround: A Unified Large Vision-Language Model for Remote Sensing Visual Grounding (arXiv 2024)**

3. **[GeoPix](https://arxiv.org/pdf/2501.06828)：GeoPix: Multi-Modal Large Language Model for Pixel-level Image Understanding in Remote Sensing (GRSM 2025)**

4. [GeoPixel](https://arxiv.org/pdf/2501.13925)：GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing（ICML 2025)

5. [AirSpatialBot](https://ieeexplore.ieee.org/document/11006099): AirSpatialBot: A Spatially Aware Aerial Agent for Fine-Grained Vehicle Attribute Recognition and Retrieval (TGRS 2025)

6. [SegEarth-R1](https://arxiv.org/abs/2504.09644): SegEarth-R1: Geospatial Pixel Reasoning via Large Language Model (arXiv 2025)

7. [RemoteReasoner](https://arxiv.org/pdf/2507.19280)：RemoteReasoner: Towards Unifying Geospatial Reasoning Workflow (arXiv 2025)

***

## 三、结语与期望

“新芽计划”旨在播撒科研的种子，培育探索的精神。遥感视觉定位是一个融合了计算机视觉、自然语言处理和遥感科学的交叉研究领域，它不仅技术挑战性强，而且具有明确且重要的应用价值。

我们热切期待，在最终的汇报中，能看到大家对这个充满挑战的领域展现出独到的见解和创新的火花！
