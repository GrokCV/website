---
title: 新芽专题介绍：红外弱小目标检测
date: 2025-09-17T01:50:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1  研究背景

在现代军事和国防系统中，红外成像设备是必不可少的核心感知手段。它可以**全天候监视、远距离观测、探测热源目标**，因此在精确制导和态势感知任务中发挥着重要作用。特别是在高价值战略武器系统中，远距离成像条件下的红外弱小目标检测，能够提供无源探测和发射前锁定功能，是保证武器系统生存性和作战效能的关键环节。也因此，红外弱小目标检测已成为各国高度重视的前沿技术方向。

### 1.2  研究意义

红外弱小目标通常指在远距离拍摄条件下，目标在红外图像中只占据**几个像素**，亮度信号微弱，很容易被复杂背景淹没。然而，能否在第一时间精准发现并跟踪这些“几乎不可见”的点，直接关系到：

1. **军事防御与预警**：提前发现隐身飞机、导弹等威胁目标，提升战略防御能力。

2. **民用与安全**：应用于空中监测、海上搜救、空间探测、卫星监控等领域。

3. **技术推动**：促进低信噪比图像建模、实时检测算法、轻量化计算等关键技术的发展。

因此，这一研究主题不仅意义重大，而且是深度学习、图像处理与目标探测领域的一个典型研究案例，非常适合作为本科生进入科研领域的启蒙训练。

![](https://imgtu.com/uploads/gdwi9xld/00001.png)

▲一个典型的红外弱小目标检测场景：目标面积极小，背景复杂。

### 1.3  当前主要挑战

尽管方向重要，但实现红外弱小目标检测仍然面临多重挑战：

1. **挑战一：目标小如尘埃，特征弱不可见**

   * 远距离图像中的目标通常只有几个像素大小，**几乎没有形状和纹理特征**。

   * 信号与背景噪声相差不大（信杂比低），导致很难提取稳定的可辨特征。

   * 随着隐身技术的发展，目标的红外信号被进一步抑制。

2. **挑战二：背景往往复杂，干扰伪装巧妙**

   * 真实场景下，地表、海面、云层等各种复杂背景会产生密集的**杂波**，掩盖目标信号。

   * 各类光电对抗措施（红外诱饵、烟幕、伪装等）也会严重干扰目标检测。

3. **挑战三：前端数据洪流，后端处理瓶颈**

   * 为了实现大范围快速监视，成像系统通常使用超大规模红外传感器。

   * 这些传感器生成的图像分辨率非常高，处理速度成为瓶颈。

   * 搭载这些传感器的平台（如无人机或卫星）计算资源有限，并且对功耗等要求比较高，难以支撑复杂算法。

综上，红外弱小目标检测技术仍在探索突破阶段，相关指标不如常规目标检测领域，这是一个很好的学习窗口：既能接触实际需求，又能跟随前沿研究。

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

### 2.2  入门文献（目标检测经典方法）

> 学生第一阶段的阅读训练，可帮助理解目标检测/语义分割/关键点检测这一通用方向。**仅用于入门，不可选择此部分文献汇报**。



* **[YOLO](https://arxiv.org/pdf/1506.02640): You Only Look Once:  Unified, Real-Time Object Detection (CVPR 2016)**

* **[Faster R-CNN](https://arxiv.org/pdf/1506.01497): Towards Real-Time Object Detection with Region Proposal Networks (NeurIPS 2015）**

* **[FCOS](https://arxiv.org/pdf/1904.01355): Fully Convolutional One-Stage Object Detection (ICCV 2019)**

* **[DETR](https://arxiv.org/pdf/2005.12872): End-to-End Object Detection with Transformers (ECCV 2020)**

* [RepPoints](https://arxiv.org/pdf/1904.11490): Point Set Representation for Object Detection (ICCV 2019)

* [GFL](https://arxiv.org/pdf/2006.04388):Generalized Focal Loss: Learning Qualified and  Distributed Bounding Boxes for  Dense Object Detection (NeurIPS 2020)

* [CenterNet](https://arxiv.org/pdf/1904.08189): Keypoint Triplets for Object Detection (ICCV 2019)

* [Focal Loss(RetinaNet)](https://arxiv.org/pdf/1708.02002v2): Focal Loss for Dense Object Detection (ICCV 2017)

* [SSD](https://arxiv.org/pdf/1512.02325): Single Shot MultiBox Detector (ECCV 2016)

* [CornerNet](https://arxiv.org/pdf/1808.01244v2): Detecting Objects as Paired Keypoints (ECCV 2018)

* [FPN](https://arxiv.org/pdf/1612.03144v2): Feature Pyramid Networks for Object Detection (CVPR 2017)

* [DCN](https://arxiv.org/pdf/1703.06211v3): Deformable Convolutional Networks (ICCV 2017)

* [FreeAnchor](https://arxiv.org/pdf/1909.02466): Learning to Match Anchors for Visual Object Detection (NeurIPS 2019)

* [VIT](https://arxiv.org/pdf/2010.11929): An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ICLR 2021)

* [GIOU Loss](https://arxiv.org/pdf/1902.09630): Generalized Intersection over Union: A Metric and A Loss for Bounding Box  Regression (CVPR 2019)

* [CIOU Loss](https://arxiv.org/pdf/1911.08287): Distance-IoU Loss: Faster and Better Learning for Bounding Box Regression (AAAI 2020)


***

### 2.3  进阶文献（目标检测前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* **[AutoAssign](https://arxiv.org/pdf/2007.03496): Differentiable Label Assignment for Dense Object Detection (arXiv 2020)**

* **[Deformable DETR](https://arxiv.org/pdf/2010.04159): Deformable Transformers for End-to-End Object Detection (ICLR 2021)**

* **[Sparse R-CNN](https://arxiv.org/pdf/2011.12450): End-to-End Object Detection with Learnable Proposals (CVPR 2021)**

* [LSKNet](https://arxiv.org/pdf/2303.09030): Large Selective Kernel Network for Remote Sensing Object Detection (ICCV 2023)

* [Cascade R-CNN](https://arxiv.org/pdf/1712.00726): Delving into High Quality Object Detection (CVPR 2018)

* [Grid R-CNN](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_Grid_R-CNN_CVPR_2019_paper.pdf) (CVPR 2019)

* [Libra R-CNN](https://arxiv.org/pdf/1904.02701): Towards Balanced Learning for Object Detection (CVPR 2019)

* [Cascade RPN](https://arxiv.org/pdf/1909.06720): Delving into High-Quality Region Proposal Network with Adaptive Convolution (NeurIPS 2019)

* [ATSS](https://arxiv.org/pdf/1912.02424): Bridging the Gap Between Anchor-based and Anchor-free Detection via Adaptive Training Sample Selection (CVPR 2020)

* [YOLOX](https://arxiv.org/pdf/2107.08430): Exceeding YOLO Series in 2021 (ArXiv 2021)

* [DAB-DETR](https://arxiv.org/pdf/2201.12329): Dynamic Anchor Boxes are Better Queries for DETR (ICLR 2022)

* [DINO](https://arxiv.org/pdf/2203.03605): DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection (ICLR 2023)

* [DiffusionDet](https://arxiv.org/pdf/2211.09788): Diffusion Model for Object Detection (ICCV 2023)

* [RT-DETR](https://arxiv.org/pdf/2304.08069): DETRs Beat YOLOs on Real-time Object Detection (CVPR 2024)

* [CO-DETR](https://arxiv.org/pdf/2211.12860): DETRs with Collaborative Hybrid Assignments Training (ICCV 2023)

* [Oriented R-CNN](https://arxiv.org/pdf/2108.05699): Oriented R-CNN for Object Detection (ICCV 2021)

***

### 2.4  红外弱小目标检测领域相关文献

> 结合本专题的研究背景，逐渐引导学生进入红外弱小目标检测。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>
> 红外弱小目标检测可分为单帧、多帧弱小目标检测和红外弱小目标解混。

**单帧弱小目标检测**

1. **[DNANet](https://arxiv.org/pdf/2106.00487)：Dense Nested Attention Network for Infrared Small Target Detection（TIP 2022）**

2. **[ACM](https://arxiv.org/pdf/2009.14530)：Asymmetric Contextual Modulation for Infrared Small Target Detection（WACV 2021）**

3. **[MSHNet](https://arxiv.org/pdf/2403.19366)：Infrared Small Target Detection with Scale and Location Sensitivity（CVPR 2024）**

4. **[SCTransNet](https://arxiv.org/pdf/2401.15583)：SCTransNet: Spatial-Channel Cross Transformer Network for Infrared Small Target Detection（TGRS 2024）**

5. **[UIUNet](https://arxiv.org/pdf/2212.00968)：UIU-Net: U-Net in U-Net for Infrared Small Object Detection（TIP 2022）**

6. [OSCAR](https://arxiv.org/pdf/2212.08472): One-Stage Cascade Refinement Networks for Infrared Small Target Detection (TGRS 2023)

7. [AuxDet](https://arxiv.org/pdf/2505.15184): Auxiliary Metadata Matters for Omni-Domain Infrared Small Target Detection (arXiv 2025)

8. [BAFE-Net](https://arxiv.org/pdf/2407.20078?): Background Semantics Matter: Cross-Task Feature Exchange Network for Clustered Infrared Small Target Detection With Sky-Annotated Dataset (arXiv 2024)

9. [ALCNet](https://arxiv.org/pdf/2012.08573)：Attentional Local Contrast Networks for Infrared Small Target Detection（TGRS 2020）

10. [ILNet](https://arxiv.org/pdf/2309.13646)：ILNet: Low-level Matters for Salient Infrared Small Target Detection（TAES 2025）

11. [ISTDU-Net](https://ieeexplore.ieee.org/document/9674870)：ISTDU-Net: Infrared Small-Target Detection U-Net（IEEE Geoscience and Remote Sensing Letters  2022）

12. [RDIAN](https://ieeexplore.ieee.org/document/10011452)：Receptive-field and Direction Induced Attention Network for Infrared Dim Small Target Detection with a Large-scale Dataset IRDST（TGRS 2023）

**多帧弱小目标检测**

1. **[RFR](https://arxiv.org/pdf/2409.12448v1)：Infrared Small Target Detection in Satellite Videos:  A New Dataset and A Novel Recurrent Feature  Refinement Framework（TGRS 2025）**

2. **[DeepPro](https://arxiv.org/pdf/2506.12766v1)：Probing Deep into Temporal Profile Makes the Infrared Small Target Detector Much Better（Arxiv 2025）**

**红外弱小目标解混**

1. [DISTA-Net](https://arxiv.org/pdf/2505.19148): Dynamic Closely-Spaced Infrared Small Target Unmixing (ICCV 2025)
2. [SeqCSIST](https://arxiv.org/pdf/2507.09556): Sequential Closely-Spaced Infrared  Small Target Unmixing (TGRS 2025)

***

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。红外弱小目标检测是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
