---
title: 新芽专题介绍：心脏磁共振重建
date: 2025-09-16T01:48:00Z
draft: false
math: true
authors:
- lichengkang
---

## 一、专题介绍

### 1.1 研究背景

心脏磁共振成像（CMR）是心血管疾病诊断的金标准，但受限于磁共振物理采样定律，获取高时空分辨率图像通常需要漫长的扫描时间，导致患者憋气困难并产生运动伪影。为加速成像，**欠采样（Under-sampling）**技术被广泛应用，但其导致的病态逆问题会使重建图像出现严重的混叠伪影。传统的并行成像（PI）与压缩感知（CS）方法在高加速因子下易出现图像过度平滑且计算开销巨大。近年来，**深度学习（Deep Learning）通过级联卷积网络或生成对抗网络，能够从海量数据中自动学习复杂的时空先验特征，结合数据一致性（Data Consistency）**约束，实现了在极短时间内从欠采样数据中恢复高质量、高保真度心脏动态图像的目标。

### 1.2 研究意义

CMR重建通常指从加速采集的欠采样k空间数据中重建完整图像，以减少扫描时间。然而，能否高效准确地重建这些"欠缺"的数据，直接关系到：

1. **临床诊断与治疗**：缩短扫描时间，减少患者不适，提升心脏病早期检测能力。
2. **科研与创新**：应用于实时心脏成像、胎儿心脏评估、多对比度成像等领域。
3. **技术推动**：促进欠采样信号恢复、深度学习重建算法、跨域泛化等关键技术的发展。

因此，这一研究主题不仅意义重大，而且是深度学习、图像重建与医学影像领域的一个典型研究案例，非常适合作为本科生进入科研领域的启蒙训练。

![CMR重建示例](https://mdpi-res.com/diagnostics/diagnostics-13-01120/article_deploy/html/images/diagnostics-13-01120-g001.png?1678892221)

▲ 一个典型的 CMR 重建全链路流程： 该图展示了从数据采集到模型部署的完整生命周期。在数据准备阶段，原始全采样 k 空间数据被人工回溯性欠采样，生成带有相干伪影的“混叠图像”作为输入。在模型训练阶段，采用生成对抗网络（GAN）架构：生成器负责将欠采样图像映射回高清图像，判别器则通过真伪对比强化细节恢复。最终，模型部署阶段将训练好的权值应用于临床实时扫描，实现从稀疏采集数据到高保真心脏解剖结构的快速转化。（图片来源：MDPI Applied Sciences 2023）

### 1.3 当前主要挑战

尽管方向重要，但实现CMR重建仍然面临多重挑战：

1. **挑战一：欠采样导致伪影，信号丢失严重**
   * 加速采集时，k空间数据欠采样，**导致图像模糊、伪影和细节丢失**。
   * 信噪比低，尤其在动态心脏成像中，运动进一步复杂化重建。
   * 随着更高加速率的需求，重建难度指数级增加。

2. **挑战二：心脏动态复杂，域移问题突出**
   * 真实临床场景下，心脏运动、呼吸伪影等**干扰因素众多**，影响重建稳定性。
   * 不同扫描仪、协议或患者间的域移，导致模型泛化差。

3. **挑战三：计算资源有限，实时性要求高**
   * CMR数据体量巨大，重建需处理高维动态序列。
   * 临床应用中，计算速度成为瓶颈。
   * 移动或低端设备上，资源受限，难以部署复杂模型。

综上，CMR重建技术仍在探索突破阶段，相关指标不如常规图像重建领域，这是一个很好的学习窗口：既能接触实际需求，又能跟随前沿研究。

***

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

***

### 2.1 基础教材与学习材料

在开始探险之前，你需要掌握一些基础的"内功心法"，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)
* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材
* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)
* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门（难度不小）

此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。
* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

**Tips**：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2 入门文献（MRI重建经典方法）

> 学生第一阶段的阅读训练，可帮助理解MRI重建/压缩感知/并行成像这一通用方向。**仅用于入门，不可选择此部分文献汇报**。

* **[SENSE](https://onlinelibrary.wiley.com/doi/pdf/10.1002/%28SICI%291522-2594%28199911%2942:5%3C952::AID-MRM16%3E3.0.CO%3B2-S): Sensitivity Encoding for Fast MRI (MRM 1999)**
* **[GRAPPA](https://apps.mriquestions.com/uploads/3/4/5/7/34572113/griswold-grappa.pdf): Generalized Autocalibrating Partially Parallel Acquisitions (MRM 2002)**
* **[Compressed Sensing MRI](https://pubmed.ncbi.nlm.nih.gov/17969013/): Sparse MRI: The Application of Compressed Sensing for Rapid MR Imaging (MRM 2007)**
* **[k-t BLAST](https://pubmed.ncbi.nlm.nih.gov/14587014/): k-t BLAST and k-t SENSE: Dynamic MRI with High Frame Rate Exploiting Spatiotemporal Correlations (MRM 2003)**
* **[Iterative Reconstruction](https://ieeexplore.ieee.org/document/6185677): Regularization Parameter Selection for Nonlinear Iterative Image Restoration and MRI Reconstruction Using GCV and SURE-Based Methods (IEEE Transactions on Image Processing, 2012)**
* **[Low-Rank Models](https://ieeexplore.ieee.org/document/6678771): Low-rank modeling of local k-space neighborhoods (LORAKS) for constrained MRI (IEEE TMI 2014)**
* **[ADMM for MRI](https://ieeexplore.ieee.org/document/7094474): An Efficient ADMM-Based Sparse Reconstruction Strategy for Multi-Level Sampled MRI (IEEE ISBI 2015)**
* **[Wavelet-Based CS](https://proceedings.neurips.cc/paper_files/paper/2012/file/65658fde58ab3c2b6e5132a39fae7cb9-Paper.pdf): Compressive Sensing MRI with Wavelet Tree Sparsity (NeurIPS 2012)**
* **[Parallel Imaging Review](https://arxiv.org/abs/1501.06209): Parallel Magnetic Resonance Imaging (arXiv 2015)**
* **[Dynamic MRI](https://onlinelibrary.wiley.com/doi/full/10.1002/mrm.24980): Golden-Angle Radial Sparse Parallel MRI (MRM 2014)**

***

### 2.3 进阶文献（MRI重建前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* **[Deep Cascade](https://arxiv.org/abs/1704.02422): A Deep Cascade of Convolutional Neural Networks for Dynamic MR Image Reconstruction (arXiv 2017)**
* **[MoDL](https://arxiv.org/abs/1712.02862): Model-Based Deep Learning Architecture for Inverse Problems in Imaging (IEEE TMI 2018)**
* **[DAGAN](https://arxiv.org/abs/1711.04340): Image Synthesis for Data Augmentation in MRI Reconstruction (arXiv 2018)**
* **[E2E-VarNet](https://arxiv.org/abs/2004.06688): End-to-End Variational Networks for Accelerated MRI Reconstruction (MICCAI 2020)**
* **[Unrolled Networks](https://arxiv.org/abs/1907.11711): Deep Unrolled Reconstruction Networks for MRI (arXiv 2019)**
* **[Score-Based Generative](https://arxiv.org/abs/2303.14795): MRI Reconstruction with Side Information using Diffusion Models (arXiv 2023)**
* **[Stable Deep MRI](https://arxiv.org/abs/2210.13834): Stable Deep MRI Reconstruction using Generative Priors (arXiv 2022)**
* **[Quantitative MR](https://arxiv.org/abs/2402.19396): Machine Learning for Quantitative MR Image Reconstruction (arXiv 2024)**
* **[Guided Reconstruction](https://arxiv.org/abs/2411.14269): Guided MRI Reconstruction via Schrödinger Bridge (arXiv 2024)**
* **[Transform Learning](https://arxiv.org/abs/1903.11431): Transform Learning for Magnetic Resonance Image Reconstruction (arXiv 2019)**

***

### 2.4 心脏磁共振重建领域相关文献

> 结合本专题的研究背景，逐渐引导学生进入心脏磁共振重建。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>
> CMR重建可分为静态重建、动态重建和多对比度重建。

**静态重建**

1. **[GENRE-CMR](https://arxiv.org/abs/2508.20600): Generalizable Deep Learning for Diverse Multi-Domain Cardiac MRI Reconstruction (arXiv 2025)**
2. **[HierAdaptMR](https://arxiv.org/abs/2508.13026): Cross-Center Cardiac MRI Reconstruction with Hierarchical Adaptation (arXiv 2025)**
3. **[UPCMR](https://arxiv.org/abs/2502.14899): A Universal Prompt-guided Model for Random Sampling Cardiac MRI Reconstruction (arXiv 2025)**
4. **[All-in-one CMR](https://arxiv.org/abs/2411.10787): An All-in-one Approach for Accelerated Cardiac MRI Reconstruction (arXiv 2024)**
5. **[Deep ADMM CMR](https://arxiv.org/abs/2310.06628): Deep Cardiac MRI Reconstruction with ADMM (arXiv 2023)**

**动态重建**

1. **[Fetal CMR](https://arxiv.org/abs/2308.07885): The Challenge of Fetal Cardiac MRI Reconstruction Using Deep Learning (arXiv 2023)**
2. **[From 2D to 3D](https://arxiv.org/abs/2510.01296): From 2D to 3D, Deep Learning-based Shape Reconstruction in Cardiac MRI (arXiv 2025)**
3. **[Multi-contrast CMR](https://arxiv.org/abs/2411.01291): Deep Multi-contrast Cardiac MRI Reconstruction via vSHARP with Multi-Contrast Attention (arXiv 2024)**

**多对比度重建**

1. **[Quality-aware Framework](https://arxiv.org/abs/2205.01673): A Deep Learning-based Integrated Framework for Quality-aware Undersampled Cine Cardiac MRI Reconstruction and Analysis (arXiv 2022)**
2. **[State-of-the-art CMR](https://arxiv.org/abs/2404.01082): The State-of-the-art in Cardiac MRI Reconstruction (arXiv 2024)**

***

## 三、结语与期望

"新芽计划"的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。心脏磁共振重建是一个充满挑战与机遇的领域，它既是临床需求的"硬骨头"，也是学术创新的"试金石"。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。


我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
