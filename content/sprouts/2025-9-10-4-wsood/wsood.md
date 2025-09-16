---
title: 新芽专题介绍（4）：弱监督目标检测
date: 2025-09-10
draft: false
math: true
authors: 
- admin
---

## 一、专题介绍

### 1.1  研究背景
全监督旋转目标检测算法依赖于大量高质量旋转框标注数据，然而，旋转框的标注过程不仅极为繁琐、耗时，还对标注人员的专业经验有较高要求，导致整体训练成本十分高昂。这一瓶颈严重制约了旋转目标检测技术在实际场景中的大规模应用与推广。因此，近年来，在旋转目标检测领域，如何有效降低标注依赖、减轻人工标注负担，已成为一个备受关注的关键研究方向，推动着弱监督、自监督等低成本学习范式在该领域的深入探索。

### 1.2  研究意义
目前，在旋转目标检测领域，训练数据的标注形式主要包括旋转框、水平框、点标注等多种方式。不同的标注形式在标注粒度、信息完整性和人工耗时方面存在显著差异，例如旋转框标注精度高但成本昂贵，水平框和点标注虽效率较高却会损失方向或细节信息。因此，标注形式的选择及其标注规模，直接决定了模型训练数据的获取成本与质量，也影响了算法在实际应用中的性能上限。

我们可以通过一张图直观地对比不同旋转目标检测算法在标注成本上的差异：

![](https://gitee.com/sharkbest/img/raw/master/image.png)

### 1.3  主要挑战

在标注成本得以降低的同时，标注数据往往在质量与规模上会有所损失。这就给弱监督算法带来了一些挑战：

1. **挑战一：弱标注尺寸或方向尺度缺失**
    * 水平框仅能表达目标的位置与尺度信息，而无法提供方向信息。
    * 单点标注只包含目标的位置信息，尺度和方向信息均缺失。

2. **挑战二：部分或稀疏标注造成的训练数据量不足**
    * 在模型训练过程中，若仅依赖有限规模的标注数据进行学习，极易导致模型过拟合。具体表现为模型过度记忆训练集中的噪声与偏差，而非学习到泛化性强的本质特征，从而在验证集或实际场景中表现显著下降。
    * 在拥有海量未标注数据的现实背景下，如何高效挖掘并利用其中蕴含的丰富信息，已成为提升模型性能的关键挑战。
## 二、参考文献

为了引导新芽学子逐步进入研究，本专题将按照训练数据的不同配置对弱（半）监督旋转目标检测算法进行梳理：

## 2.1 弱标注
弱标注是为了解决强标注成本高昂的问题而提出的替代方案。它牺牲了一定的标注精度，以换取标注效率的大幅提升。

### 2.1.1 水平框监督
* [H2RBox](https://arxiv.org/pdf/2210.06742): Horizontal Box Annotation is All You Need for Oriented Object Detection (ICLR 2023)
* [H2RBox-v2](https://proceedings.neurips.cc/paper_files/paper/2023/file/b9603de9e49d0838e53b6c9cf9d06556-Paper-Conference.pdf): Incorporating Symmetry for Boosting
Horizontal Box Supervised Oriented Object Detection (NeurIPS 2023)
* [AFWS](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10731721): Angle-Free Weakly Supervised Rotating
Object Detection for Remote Sensing Images (TGRS 2024)
* [EIE-Det](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10535195): Explicit and Implicit Box Equivariance Learning for
Weakly-Supervised Rotated Object Detection（TETCI 2024）

### 2.1.2 点监督
* [Point2RBox](https://openaccess.thecvf.com/content/CVPR2024/papers/Yu_Point2RBox_Combine_Knowledge_from_Synthetic_Visual_Patterns_for_End-to-end_Oriented_CVPR_2024_paper.pdf):  Combine Knowledge from Synthetic Visual Patterns for End-to-end
Oriented Object Detection with Single Point Supervision (CVPR 2024)
* [Point2RBox-v2](https://openaccess.thecvf.com/content/CVPR2025/papers/Yu_Point2RBox-v2_Rethinking_Point-supervised_Oriented_Object_Detection_with_Spatial_Layout_Among_CVPR_2025_paper.pdf): Rethinking Point-supervised Oriented Object Detection
with Spatial Layout Among Instances (CVPR 2025)
* [PointOBB](https://openaccess.thecvf.com/content/CVPR2024/papers/Luo_PointOBB_Learning_Oriented_Object_Detection_via_Single_Point_Supervision_CVPR_2024_paper.pdf): Learning Oriented Object Detection via Single Point Supervision (CVPR 2024)
* [PointOBB-v2](https://arxiv.org/pdf/2410.08210): Towards Simpler, Faster, and Stronger Single Point Supervised Oriented Object Detection (ICLR 2025)
* [PointOBB-v3](https://arxiv.org/pdf/2501.13898): Expanding Performance Boundaries of Single Point-Supervised Oriented Object Detection (IJCV 2025)

### 2.1.3 混合监督
* [Wholly-WOOD](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10891210): Wholly Leveraging
Diversified-Quality Labels for Weakly-Supervised
Oriented Object Detection (TPAMI 2025)


### 2.2 部分标注
训练数据中包含少量标注数据，其余大量数据均为无标注数据。有效提升未标注数据的利用率，不仅能够显著降低对昂贵人工标注的依赖，更是推动模型突破标注数据瓶颈、实现更优泛化能力的重要途径。其核心在于通过先进的学习范式，引导模型从无标注数据中自主地提取有价值的知识与模式。
### 2.2.1 部分旋转框标注
* [Mixteacher](https://openaccess.thecvf.com/content/CVPR2023/papers/Liu_MixTeacher_Mining_Promising_Labels_With_Mixed_Scale_Teacher_for_Semi-Supervised_CVPR_2023_paper.pdf):  Mining Promising Labels with Mixed Scale Teacher
for Semi-Supervised Object Detection (CVPR 2023)
* [Unbiased Teacher](https://arxiv.org/pdf/2102.09480): Unbiased Teacher for Semi-Supervised Object Detection
* [Consistent-teacher](https://openaccess.thecvf.com/content/CVPR2023/papers/Wang_Consistent-Teacher_Towards_Reducing_Inconsistent_Pseudo-Targets_in_Semi-Supervised_Object_Detection_CVPR_2023_paper.pdf): Towards Reducing Inconsistent Pseudo-targets in
Semi-supervised Object Detection (CVPR 2023)
* [MCL](https://arxiv.org/pdf/2407.05909): Multi-clue Consistency Learning to Bridge Gaps Between General and Oriented Object in Semi-supervised Detection (AAAI 2025)
* [SOOD](https://openaccess.thecvf.com/content/CVPR2023/papers/Hua_SOOD_Towards_Semi-Supervised_Oriented_Object_Detection_CVPR_2023_paper.pdf): Towards Semi-Supervised Oriented Object Detection (CVPR 2023)

### 2.2.2 部分（稀疏）弱标注
* [PWOOD](https://arxiv.org/pdf/2507.02751): Partial Weakly-Supervised Oriented Object Detection

## 2.3 相关文献梳理
* https://zhuanlan.zhihu.com/p/620377685