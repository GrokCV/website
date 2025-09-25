---
title: 新芽专题介绍（26）：恶劣环境视觉感知
date: 2025-09-17T01:25:00Z
draft: false
math: true
---


## 一、专题介绍

### 1.1  研究背景

基于人工智能的视觉感知技术在在广泛领域得到了应用.然而，在恶劣环境下的视觉感知仍然是一个需要不断探索和克服的挑战。
恶劣环境通常包括**恶劣大气条件**（如雨、雪、雾等）、**不利光照环境**（如低光照或者过曝）以及
**复杂成像环境**（如水下场景）。这些极端条件下，视觉感知系统往往会失效或其性能显著下降。

恶劣环境下视觉感知技术的目的在于开发在恶劣环境中能够稳定工作的视觉感知系统，在自动驾驶、安全监控、国防应用、灾难响应等领域具有重要的实际意义。


### 1.2  研究意义

在恶劣环境下实现可靠的视觉感知对于多种实际应用至关重要：


1. **交通安全与自动驾驶**：车辆能够在各种天气和光照条件下安全导航，从而减少交通事故。


2. **军事与国防**：在战场和极端条件下保持态势感知的能力，为战术决策提供支持。


3. **灾难救援**：在自然灾害或事故现场，快速定位和识别幸存者，提升救援效率。


研究恶劣环境下的视觉感知有助于推动图像处理、深度学习等领域的发展。
同时，该主题为本科生和研究生提供了一个可以结合实际问题进行创新研究的平台。

![Figure](https://img.remit.ee/api/file/BQACAgUAAyEGAASHRsPbAAECKWtozKfCpsJtZVVNE97tfPhzaQM-ZwACdh4AAhwQYVaEF_E-qI2HpjYE.png)

▲一些典型的恶劣环境。

### 1.3  当前主要挑战

尽管技术前景广阔，但在恶劣环境下实现精确的视觉感知面临多重挑战：

1. **挑战一：数据获取困难，样本不足**

   * 恶劣环境中的数据收集通常较为困难，包括极端天气条件、突发事件或高动态场景，这些场景的数据难以系统地获取和标注。

   * 缺乏大规模、多样化的训练数据集，导致模型在训练阶段面临样本不足的问题，从而影响其在实际应用中的表现。

2. **挑战二：低质量视觉输入，噪声干扰明显**

   * 恶劣环境下的视觉输入通常存在低光照、模糊、动态模态等多种问题，严重影响视觉信息的有效传递。

   * 环境中的干扰，如雨滴、雪花、烟雾等，掩盖了关键的目标信息，进一步降低了模型提取有效特征的能力。

3. **挑战三：特征分布差异，泛化能力受限**

   * 恶劣环境与正常环境之间的特征分布差异显著，这对模型的泛化能力提出了新的要求，需要在不同场景条件下保持稳健的性能。

   * 模型往往在标准和理想条件下训练，而在面对未见过的恶劣条件时性能急剧下降，显现出较差的适应性和鲁棒性

这些挑战共同构成了恶劣环境下视觉感知技术发展的主要瓶颈，但也为新方法和创新技术的研究提供了广阔的空间和机遇。



## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下三部分：

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

### 2.2  入门文献（视觉感知经典方法）

> 学生在第一阶段的阅读训练应覆盖广泛的计算机视觉任务，尤其以目标检测和语义分割为基础。这将帮助理解视觉感知的基础方法。**仅用于入门，不可选择此部分文献汇报**。


* **[YOLO](https://arxiv.org/pdf/1506.02640): You Only Look Once:  Unified, Real-Time Object Detection (CVPR 2016)**

* **[Faster R-CNN](https://arxiv.org/pdf/1506.01497): Towards Real-Time Object Detection with Region Proposal Networks (NeurIPS 2015）**

* **[FCOS](https://arxiv.org/pdf/1904.01355): Fully Convolutional One-Stage Object Detection (ICCV 2019)**

* **[DETR](https://arxiv.org/pdf/2005.12872): End-to-End Object Detection with Transformers (ECCV 2020)**

* **[RepPoints](https://arxiv.org/pdf/1904.11490): Point Set Representation for Object Detection (ICCV 2019)**

* **[FCN](https://arxiv.org/pdf/1605.06211v1): Fully Convolutional Networks for Semantic Segmentation (CVPR 2015)**

* **[U-Net](https://arxiv.org/abs/1505.04597): U-Net: Convolutional Networks for Biomedical Image Segmentation (ArXiv 2015)**

* **[SegNet](https://ieeexplore.ieee.org/document/7803544): SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentatio (TPAMI 2017)**

* **[DeepLab](https://arxiv.org/abs/1606.00915): DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs (TPAMI 2017)**

***

### 2.3  恶劣环境视觉感知领域相关文献

> 结结合本专题的研究背景，逐步引导学生深入恶劣环境视觉感知。学生可在此部分选择相关进阶文献进行专题汇报，或自行查找最新的重要文献。
>
> 现实中的恶劣环境多种多样，为此，我们将焦点放在恶劣天气环境、光照条件以及成像环境这三种情况，选择了雨雪天气中的视觉感知、暗光条件下的视觉感知以及水下环境的视觉感知等具体任务，供学生进行探究和分析。


**雨雾天气中视觉感知**

在雨雾天气条件下，视觉感知面临的主要挑战是模糊和遮挡现象，以及由此导致的与常规图像之间的领域偏差。为了解决这些问题，一些学者尝试采用图像复原和图像增强技术，以有效消除雨雾对图像质量的影响。另一方面，另一些研究者则通过域适应技术来缩小与正常图像之间的差异，从而提升模型在恶劣天气条件下的性能。这样的多重策略为改善雨雾天气中的视觉感知提供了有力的解决方案。


1. **[AOD-Net](https://arxiv.org/abs/1707.06543)：AOD-Net: All-in-One Dehazing Network（ICCV 2017）**

2. **[FoggyCityscapes](DOI:10.1109/CVPR.2018.00352)：Domain Adaptive Faster R-CNN for Object Detection in the Wild (CVPR 2018)**

3. **[IA-YOLO](https://arxiv.org/abs/2112.08088)：Image-Adaptive YOLO for Object Detection in Adverse Weather Conditions（AAAI 2022）**

4. **[BADNet](https://ieeexplore.ieee.org/document/10012056)：Detection-Friendly Dehazing: Object Detection in Real-World Hazy Scenes（TPAMI 2023）**

5. **[CycleGAN](https://ieeexplore.ieee.org/document/10012056)：Vision in Adverse Weather: Augmentation using CycleGANs with Various Object Detectors for Robust Perception in Autonomous Racing (ICML 2022)**

6. **[DSNet](https://ieeexplore.ieee.org/document/9022905)：DSNet: Joint Semantic Learning for Object Detection in Inclement Weather Conditions.(TPAMI 2021)**

7. **[Unified](10.1609/aaai.v36i2.20033): Close the Loop: A Unified Bottom-Up and Top-Down Paradigm for Joint Image Deraining and Segmentation (AAAI2022)**

**暗光条件下的视觉感知**

与雨雾天气类似，暗光条件也被一些学者视为一种图像退化现象，他们尝试通过暗光增强和域适应技术来解决这一问题。然而，由于其他模态图像（尤其是红外图像）在暗光条件下不易受到干扰，许多研究者选择采用多模态融合的方法来改善暗光下的视觉感知。值得注意的是，尽管多模态融合有其优势，由于可见光在现实中的广泛应用，单一模态下的暗光条件视觉感知仍然具有重要的研究意义。

单一模态
1. **[WiiD](https://github.com/ZhangYh994/WiiD): Watching it in Dark: A Target-aware Representation Learning Framework for High-Level Vision Tasks in Low Illumination (ECCV 2024)** 

2. **[PE-YOLO](https://arxiv.org/abs/2307.10953): PE-YOLO: Pyramid Enhancement Network for Dark Object Detection (ICANN 2023)**

3. **[MAET](https://ieeexplore.ieee.org/document/9711331): Multitask AET with Orthogonal Tangent Regularity for Dark Object Detection (ICCV 2022)**


多种模态

3. **[UA-CMDet](http://arxiv.org/abs/2003.02437): Drone-based RGB-Infrared Cross-Modality Vehicle Detection via Uncertainty-Aware Learning (TCSVT 2021)**

4. **[E2E-MFD](https://arxiv.org/pdf/2403.09323v3): E2E-MFD: towards end-to-end synchronous multimodal fusion detection (NeurIPS 2024)**

5. **[FD2-Net](https://arxiv.org/abs/2412.09258): FD2-Net: Frequency-Driven Feature Decomposition Network for Infrared-Visible Object Detection （AAAI 2025）**

5. **[DAMSDet](https://arxiv.org/pdf/2403.00326): DAMSDet: Dynamic Adaptive Multispectral Detection Transformer with Competitive Query Selection and Adaptive Feature Fusion （ECCV 2024）**


**水下环境视觉感知**

与雨雾天气和暗光条件不同，水下环境感知面临的挑战更加复杂，主要是由于水下特有的光传播特性和环境干扰。在水下，光的折射和散射会导致图像质量显著下降，影响物体的识别和分类。此外，水下图像往往缺乏有效的其他模态（如红外）应用来辅助视觉感知，以及缺少可利用的增强参考，使得研究者在这种环境下的图像处理技术选择面临更大的限制。因此，许多学者专注于通过图像增强或者特征增强方法来提升图像和特征的质量，以便更好地恢复和提取目标信息。

1. **[Brackish](https://openaccess.thecvf.com/content_CVPRW_2019/papers/AAMVEM/Pedersen_Detection_of_Marine_Animals_in_a_New_Underwater_Dataset_with_CVPRW_2019_paper.pdf)：Detection of marine animals in a new underwater dataset with varying visibility（CVPRW 2019）**

2. **[RoIAttn](https://ieeexplore.ieee.org/document/9897515)：Excavating RoI Attention for Underwater Object Detection（ICIP 2022）**

3. **[WFDif](https://arxiv.org/abs/2311.16845)：Wavelet-based Fourier Information Interaction with Frequency Diffusion Adjustment for Underwater Image Restoration（CVPR 2024）**



***

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。

恶劣环境视觉感知是一个充满挑战与可能性的前沿领域，不仅涉及到公共安全的实际需求，也是推动学术研究和技术创新的重要驱动力。

通过本专题，希望同学们能深刻理解恶劣环境对视觉感知系统的影响，以及在此背景下所面临的各类技术挑战。这一研究旅程不仅能帮助大家掌握人工智能和计算机视觉的前沿知识，更将培养你们的问题解决能力、创新思维和实践能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！


