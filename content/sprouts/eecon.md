---
title: 新芽专题介绍（48）：MRI/CT医学图像重建
date: 2025-09-17T01:03:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1 研究背景

在现代医学诊断和治疗中，医学影像技术是至关重要的非侵入性诊断手段。其中，**磁共振成像（MRI）和计算机断层扫描（CT）** 作为两种核心的医学成像技术，在临床诊断、手术规划和治疗效果评估中发挥着不可替代的作用。随着人工智能技术的飞速发展，基于深度学习的医学图像重建技术正在革命性地改变传统成像流程，为**快速成像、低剂量扫描和高质量重建**提供了全新的解决方案。

特别是在资源有限的医疗环境下，如何通过算法优化减少扫描时间、降低辐射剂量，同时保证甚至提升图像质量，已成为医学影像分析领域的前沿研究方向。深度学习驱动的医学图像重建技术，正成为提升医疗效率、降低医疗成本的关键技术支撑。

### 1.2 研究意义

医学图像重建的核心挑战是在**欠采样、低剂量或噪声干扰**的条件下，恢复出高质量的诊断图像。这一技术突破将直接带来：

1. **患者安全保障**：显著降低CT扫描的辐射剂量，减少对患者的潜在伤害。
2. **诊断效率提升**：大幅缩短MRI扫描时间，提升医疗设备的吞吐量。
3. **医疗可及性**：使得高质量医学影像在资源匮乏地区成为可能。
4. **技术推动**：促进压缩感知、深度学习、逆问题求解等前沿技术的发展。

作为医学影像与人工智能的交叉领域，这一研究方向不仅具有重要的临床应用价值，也为本科生提供了接触多学科交叉研究的绝佳机会。
典型的MRI欠采样重建挑战：从左到右分别为欠采样k-space数据、零填充重建结果、深度学习重建结果。

### 1.3 当前主要挑战

医学图像重建面临着独特的技术挑战：

1. **挑战一：反问题的病态性**

   * 医学图像重建本质上是求解欠定反问题，存在**无穷多解**。
   * 需要有效的先验知识来约束解空间，确保重建结果的合理性和诊断价值。
   * 传统压缩感知方法依赖手工设计的稀疏变换，表达能力有限。

2. **挑战二：数据获取的物理约束**

   * MRI的k-space数据采集受物理定律约束，采样轨迹设计复杂。
   * CT投影数据受辐射剂量限制，低剂量扫描导致噪声严重。
   * 不同设备、不同序列的参数差异巨大，算法需要良好的泛化能力。

3. **挑战三：临床应用的严格要求**

   * 重建图像必须保持**诊断准确性**，不能引入虚假病灶或掩盖真实病变。
   * 算法需要满足**实时性或近实时性**要求，支持临床工作流。
   * 必须考虑**计算资源限制**，特别是在嵌入式医疗设备上的部署。

这些挑战使得医学图像重建成为理论深度与技术实用性并重的研究方向，非常适合作为新芽学子科研训练的起点。

***

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

***

### 2.1 基础教材与学习材料

在开始医学图像重建研究前，需要掌握相关领域的基础知识：

* **深度学习基础**：
  - 李沐[《动手学深度学习》](https://zh.d2l.ai/)——中文友好教材
  - [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow等）——经典教材

* **医学影像基础**：
  - [《Medical Image Processing, Reconstruction and Restoration》](https://www.taylorfrancis.com/books/mono/10.1201/9781420030679/medical-image-processing-reconstruction-restoration-jiri-jan-jiri-jan)（Jiri Jan）——医学图像处理基础
  - [《Principles of Magnetic Resonance Imaging》](https://www.mri-q.com/)——在线MRI原理教程

* **编程工具**：
  - [PyTorch官方教程](https://pytorch.org/tutorials)
  - [MONAI](https://monai.io/)——医学影像深度学习框架
  - [SigPy](https://sigpy.readthedocs.io/)——MRI重建Python库

* **实践平台**：
  - [fastMRI数据集](https://fastmri.med.nyu.edu/)——NYU提供的MRI重建基准数据集
  - [AAPM CT挑战赛数据](https://www.aapm.org/GrandChallenge/)——低剂量CT重建数据

***

### 2.2 入门文献（图像重建经典方法）

> 学生第一阶段的阅读训练，帮助理解图像重建的基本原理和方法。

* **[U-Net](https://arxiv.org/pdf/1505.04597): Convolutional Networks for Biomedical Image Segmentation (MICCAI 2015)** - 医学图像处理的基石网络

* **[Compressed Sensing MRI](https://doi.org/10.1109/MSP.2007.914728): Sparse MRI: The application of compressed sensing for rapid MR imaging (Magnetic Resonance in Medicine 2007)**

* **[V-Net](https://arxiv.org/pdf/1606.04797): V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation (3DV 2016)**

* **[Deep ADMM-Net](https://arxiv.org/pdf/1705.06869): Deep ADMM-Net for Compressive Sensing MRI (NeurIPS 2016)**

* **[ISTA-Net](https://arxiv.org/pdf/1706.07929): Learning a Deep Convolutional Network for Image Super-Resolution (ECCV 2018)** - 迭代收缩阈值算法的网络展开

* **[MoDL](https://arxiv.org/pdf/1712.02862): MoDL: Model-Based Deep Learning Architecture for Inverse Problems**

* **[GAN基础](https://arxiv.org/pdf/1406.2661): Generative Adversarial Networks (NeurIPS 2014)**

* **[DC-CNN](https://arxiv.org/pdf/1704.04044): A Deep Cascade of Convolutional Neural Networks for Dynamic MR Image Reconstruction (TIP 2017)**

* **[FBPConvNet](https://arxiv.org/pdf/1611.03679): A Deep Convolutional Neural Network for Tomographic Reconstruction (MIDL 2018)** - CT重建的经典方法

***

### 2.3 进阶文献（医学图像重建前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* **[VarNet](https://arxiv.org/pdf/2004.06688): Time‐optimized multi‐contrast 3D intracranial magnetic resonance angiography (Magnetic Resonance in Medicine 2020)**

* **[KIKI-net](https://arxiv.org/pdf/1910.02113): KIKI-net: cross-domain convolutional neural networks for reconstructing undersampled magnetic resonance images (Magnetic Resonance in Medicine 2018)**

* **[XPDNet](https://arxiv.org/pdf/2010.07290): XPDNet for MRI Reconstruction: an application to the 2020 fastMRI challenge (arXiv 2020)**

* **[Diffusion Models for MRI](https://arxiv.org/pdf/2111.08025): Measurement-conditioned Denoising Diffusion Probabilistic Model for Under-sampled Medical Image Reconstruction (MICCAI 2022)**

* **[Coil Compression](https://arxiv.org/pdf/2008.06559): Deep Learning for Coil Compression in Low-Field MRI (Magnetic Resonance in Medicine 2020)**

* **[UNFOLD-Net](https://arxiv.org/pdf/2103.15767): UNFOLD-Net: Unsupervised deep unfolding network for CS-MRI reconstruction (TMI 2021)**

* **[Recurrent Variational Network](https://arxiv.org/pdf/1907.09609): Recurrent Variational Network: A Deep Learning Inverse Problem Solver applied to the task of Accelerated MRI Reconstruction (CVPR 2020)**

* **[DuDoRNet](https://arxiv.org/pdf/2009.01899): DuDoRNet: Learning a Dual-Domain Recurrent Network for Fast MRI Reconstruction with Deep T1 Prior (CVPR 2020)**

* **[SLATER](https://arxiv.org/pdf/2203.10824): SLATER: Shadow-Layered Auto-Encoder-Tensor Reconstruction for accelerated MRI (TMI 2022)**

* **[SwinMR](https://arxiv.org/pdf/2205.05666): SwinMR: A Swin Transformer-based Multi-scale Refinement Network for MRI Reconstruction (TMI 2022)**

***

### 2.4 MRI/CT医学图像重建领域相关文献

> 结合本专题的研究背景，逐渐引导学生进入医学图像重建领域。学生可在此部分选择进阶文献进行专题汇报。

**MRI快速重建**

1. **[fastMRI挑战赛综述](https://arxiv.org/pdf/2109.03808)：The fastMRI Dataset: A Prospectively-Accelerated Knee MRI Dataset and Benchmark (NeurIPS 2021)**

2. **[E2E-VarNet](https://arxiv.org/pdf/2004.06688)：End-to-end variational networks for accelerated MRI reconstruction (Magnetic Resonance in Medicine 2020)**

3. **[K-band](https://arxiv.org/pdf/2105.04409)：K-band: Self-supervised MRI Reconstruction via Stochastic Gradient Descent over K-space subsets (Magnetic Resonance in Medicine 2021)**

4. **[DL-MRI](https://arxiv.org/pdf/2004.06688)：Deep Learning for Magnetic Resonance Image Reconstruction: A Survey (TMI 2020)**

5. **[SMS-Net](https://arxiv.org/pdf/2106.14242)：SMS-Net: A New Deep Learning Framework for Simultaneous Multi-Slice MRI Reconstruction (TMI 2021)**

**低剂量CT重建**

1. **[RED-CNN](https://arxiv.org/pdf/1703.00555)：Low-Dose CT with a Residual Encoder-Decoder Convolutional Neural Network (TMI 2017)**

2. **[WGAN-VGG](https://arxiv.org/pdf/1708.00961)：Low-Dose CT via Convolutional Neural Network with Wasserstein Distance and VGG Loss (TMI 2018)**

3. **[CTformer](https://arxiv.org/pdf/2203.09348)：CTformer: Convolution-free Token2Token Dilated Vision Transformer for Low-dose CT Denoising (TMI 2022)**

4. **[DuDoNet](https://arxiv.org/pdf/1905.00569)：DuDoNet: Dual Domain Network for CT Metal Artifact Reduction (CVPR 2019)**

5. **[FBP-Diffusion](https://arxiv.org/pdf/2209.14589)：FBP-Diffusion: Diffusion-based CT Reconstruction with Filtered Back Projection Prior (MICCAI 2022)**

**扩散模型在医学重建中的应用**

1. **[Score-based MRI](https://arxiv.org/pdf/2111.08025)：Score-based diffusion models for accelerated MRI (Medical Image Analysis 2022)**

2. **[Cold Diffusion](https://arxiv.org/pdf/2208.09392)：Cold Diffusion for MRI: Invertible and Robust Medical Image Reconstruction (MICCAI 2023)**

3. **[DDS-MRI](https://arxiv.org/pdf/2304.01108)：DDS-MRI: Deep Degradation-aware Stochastic MRI Reconstruction (TMI 2023)**

**物理引导的重建方法**

1. **[PD-DUN](https://arxiv.org/pdf/2203.13628)：Physics-driven Deep Unfolding Network for Sparse-view CT Reconstruction (TMI 2022)**

2. **[CG-DLR](https://arxiv.org/pdf/2103.06255)：Conjugate Gradient Method for Physics-driven Deep Learning Reconstruction (Magnetic Resonance in Medicine 2021)**

3. **[LPD-Net](https://arxiv.org/pdf/1910.00066)：Learned Primal-Dual Reconstruction (TMI 2018)**

**跨模态重建与超分辨率**

1. **[MM-GAN](https://arxiv.org/pdf/2103.16235)：Multi-modal GAN for Cross-modality MR Image Synthesis (TMI 2021)**

2. **[Cycle-MedGAN](https://arxiv.org/pdf/2007.09748)：Cycle-MedGAN: Simultaneous CT-MRI Synthesis and Segmentation (TMI 2020)**

3. **[SR-Diffusion](https://arxiv.org/pdf/2303.07034)：Diffusion Model for Medical Image Super-Resolution (TMI 2023)**

***

## 三、结语与期望

医学图像重建是人工智能与临床医学深度融合的典范领域，既需要扎实的理论基础，又要求对临床需求的深刻理解。通过这个专题，新芽学子将有机会接触从基础数学物理到前沿深度学习技术的完整知识体系，培养解决真实世界问题的能力。

我们期待看到新芽学子在这一充满挑战的领域中，不仅掌握先进的技术方法，更能培养出严谨的科研态度和跨学科思维，为未来的医学影像技术发展贡献智慧。