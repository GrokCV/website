---
title: 🎯 AuxDet：辅助元数据驱动的广域红外小目标检测方法
date: 2025-06-20
math: true
# image:
#   placement: 2
#   caption: 'Image credit: [**John Moeses Bauan**](https://unsplash.com/photos/OGZtQF8iC0g)'
---

![](https://github.com/GrokCV/imgbed/blob/master/blog/AuxDet/author.png?raw=true)

**arXiv 地址**：https://arxiv.org/abs/2505.15184

**开源地址**：https://github.com/GrokCV/AuxDet

**一句话概括：** 

本文介绍了一种引入图像元数据（成像平台、成像波段、图像分辨率）的多模态红外小目标检测新范式 AuxDet，利用元数据隐含的物理先验实现图像特征的样本级动态调制，增强模型在广域检测中的泛化能力。

------

## 研究背景  

红外成像凭借其在恶劣天气和低能见度条件下捕获目标信息的独特优势，在海洋资源开发、精准制导和生态监测等领域得到广泛应用。然而，远距离成像导致目标不仅纹理结构信息匮乏，还易受复杂背景干扰，使得目标信号常被环境噪声所淹没。这种特性使得红外小目标检测（Infrared Small Target Detection, IRSTD）成为计算机视觉领域的重大技术挑战。

当前主流方法聚焦于图像内部特征的深度挖掘，旨在建立弱小目标与复杂背景的差异化表征。随着深度学习技术的发展，研究者尝试通过强调鲁棒特征提取和精细化注意力机制的神经网络架构来解决 IRSTD 问题。代表性工作如 ALCNet<sup>[[1]](#ref1)</sup> 引入注意力引导的局部对比机制放大目标-背景差异，ISNet<sup>[[2]](#ref2)</sup> 则开发了红外专用空间变换器实现抗噪特征学习。

尽管取得了一定进展，但现有方法在扩展到实际应用时仍存在**两大关键缺陷**：

1. **过度专精化**：多数方法聚焦窄域优化（如长波红外的陆基成像或短波红外的天基成像），难以适应广域应用中固有的传感器-平台-频谱连续体变化；
2. **过度工程化**：研究者日益依赖域专用技术提升检测精度，例如通过背景分解来预识别海域以有效检测海上目标。这些方法虽然降低了窄域任务的复杂度，但本质上削弱了跨域泛化能力。

![图 1：WideIRSTD-Full 数据集部分特性分析示意图。](https://github.com/GrokCV/imgbed/blob/master/blog/AuxDet/dataset.jpg?raw=true)

**为满足日益增长的大规模、多平台、可部署检测系统的实际需求，我们锚定了广域红外小目标检测（Omni-IRSTD）这个新任务。** 如图 1 所示，该任务通过解决四个核心维度来统一异构传感域的 IRSTD 范式：(1) 多平台观测（陆基、空基、天基）；(2) 多目标类型（点状、斑状、扩展目标）；(3) 多光谱波段（如 LWIR、NIR、SWIR）；(4) 多分辨率成像（256×256 至 6000×6000）<sup>[[3]](#ref3)</sup>。**相比传统单域检测，Omni-IRSTD 因环境背景、目标外观分布的明显差异面临重大挑战。** 实验结果（见表 1）表明，前沿方法在广域基准上出现性能大幅下降，这种性能差距揭示了应对广域复杂性的范式革新需求。

------

## 研究动机

我们认为现有方法的根本性局限源于对物理特性差异显著的成像域强行追求统一特征表示的内在矛盾。简单聚合多域数据时，不同域的梯度方向在参数空间产生对抗性冲突，导致网络陷入次优平衡。也就是说，理想特征在不同域间存在本质差异，统一策略既不实际也损害表达有效性。更合理的解决路径应是使模型具备领域感知能力，即根据输入数据的成像条件动态调整表征策略。然而，经典单模态视觉架构存在本质缺陷——其难以仅凭原始像素数据有效推断特定成像域的物理条件。这引出了核心研究命题：**模型是否具备预先识别输入样本所属成像域的能力，从而实现这种自适应调整机制？**

我们的答案是肯定的。在实际红外传感系统中，每张捕获的图像天然附带一组辅助元数据，记录图像采集时的物理条件，如传感器平台、光谱带、空间分辨率和观测角度。**这些通常被忽视的元数据，实际上编码了驱动特定域特征分布和外观模式的关键因素，可以作为紧凑且语义丰富的表征，提供低维却高度信息丰富的成像域抽象。通过将这些元数据显式地纳入学习过程，检测范式可以从单纯依赖视觉的被动建模方式，转变为基于情境感知的主动框架，使得模型能够根据每个输入样本的领域特性，动态调整其表征策略。**

基于以上见解，我们提出了**辅助元数据驱动的 IRSTD 新范式 AuxDet**，该框架突破传统单一视觉依赖范式，依赖多模态辅助元数据实现动态场景感知优化，构建了面向真实应用场景的 Omni-IRSTD 解决方案。

------

## AuxDet

如图 2 所示，我们提出的 AuxDet 构建了一种面向 Omni-IRSTD 的新颖多模态架构，以 Cascade RPN<sup>[[4]](#ref4)</sup> 作为基础网络，并引入三个专门设计的组件，协同应对跨域泛化挑战：

1. 一个辅助元数据处理流，将异构传感器参数转换为潜在语义表示；
2. 一种层次融合机制，实现视觉-元数据协同适应与样本级动态调制；
3. 一个轻量级边缘感知细化组件，用于平衡红外小目标的细节恢复。

![图 2：AuxDet 网络结构。](https://github.com/GrokCV/imgbed/blob/master/blog/AuxDet/AuxDet.png?raw=true)

该方法以并行的特征提取路径开始——一条是通过传统的 CNN 主干网络进行视觉模式挖掘，另一条是通过元数据预编码器，将物理传感器特性通过可学习的张量层嵌入结构化的高维特征空间。这两种互补表征在多模态动态调制模块（Multi-modal Dynamic Modulation Module, M2DM）中逐步对齐、交互并进行样本级的定制化通道-空间并行特征调制，从而在复杂背景中增强目标的可区分性。调制后的特征随后被送入轻量级的边缘增强模块（Lightweight Edge Enhancement Module, LEEM），该模块沿空间维度顺序施加方向分离的相位感知一维卷积块，利用局部差异先验进行初始化以放大高频目标特征。

> 总的来说，AuxDet 针对广域红外小目标检测中的实际挑战，将图像元数据（如平台类型、波段信息、分辨率等）深度融入检测模型，实现对跨域图像的成像条件先验注入与自适应感知调节。

## 实验 

为了全面评估所提出的 AuxDet 框架的有效性，我们采用了公开可用的 [WideIRSTD-Full 数据集](https://github.com/XinyiYing/WideIRSTD-Dataset)作为评估基准，该数据集整合了七个主要的公共数据集：SIRST-V2<sup>[[5]](#ref5)</sup>、IRSTD-1K<sup>[[2]](#ref2)</sup>、IRDST<sup>[[6]](#ref6)</sup>、NUDT-SIRST<sup>[[7]](#ref7)</sup>、NUDT-SIRST-Sea<sup>[[8]](#ref8)</sup>、NUDT-MIRSDT<sup>[[9]](#ref9)</sup>、Anti-UAV<sup>[[10]](#ref10)</sup> 和一个国防科技大学团队开发的数据集。

如图 1 所示，WideIRSTD-Full 涵盖了多种成像平台、光谱波段和目标类型，具有显著的变化性。该数据集包含 9000 张具有相应辅助信息的图像，我们根据官方提供的[可参考划分标准](https://github.com/YeRen123455/ICPR-Track2-LightWeight/tree/main/dataset/ICPR_Track2/70_20)，使用其中 7000 张图像作为训练集，2000 张图像用于验证。丰富的元数据信息和大规模图像样本使其特别适合评估 AuxDet 在广域场景中的泛化能力。

![表 1：AuxDet 在 WideIRSTD-Full 数据集上的表现。](https://github.com/GrokCV/imgbed/blob/master/blog/AuxDet/comparision.png?raw=true)

如表 1 所示，我们在 WideIRSTD-Full 这一基准数据集上对 AuxDet 进行了全面的性能比较和评估，**实验结果证明了 AuxDet 的 SOTA 性能**。

![图 3：AuxDet 在 WideIRSTD-Full 数据集上的检测效果可视化对比。](https://github.com/GrokCV/imgbed/blob/master/blog/AuxDet/bbox.jpg?raw=true)

图 3 直观展示了我们方法与部分前沿方法的检测效果对比。可以看出，AuxDet 在漏检和虚警方面均表现出明显优势，检测结果更加精准可靠。

## 结论和未来工作的讨论

我们的工作首次在 IRSTD 领域引入并系统性建模辅助元数据，重新定义了传统仅依赖视觉信息的检测范式。在 WideIRSTD-Full 基准测试中，AuxDet 显著超越了现有最先进方法，验证了辅助元数据在提升鲁棒性与准确性方面的不可或缺性，展现出在 Omni-IRSTD 场景下的广泛适应性。

尽管取得了初步成果，目前的探索仍存在诸多局限，包括元数据呈现形式较为简单，以及元数据融合策略仍有待深入研究。未来，我们希望这一元数据辅助策略能够激发相关领域在数据存储方式上的进一步丰富，从而基于更丰富的元数据信息探索并实现更高效的检测指导。同时，视觉-语言模型在元数据理解与扩展方面的潜力也值得进一步探索。

## 致谢  

我们感谢天津视觉计算与智能感知重点实验室（VCIP）提供的宝贵资源。  

## 参考文献  

<a name="ref1">[1]</a>: Yimian Dai, Yiquan Wu, Fei Zhou, and Kobus Barnard. **Attentional Local Contrast Networks for Infrared Small Target Detection.** *IEEE Transactions on Geoscience and Remote Sensing* 59 (2021), 9813–9824.

<a name="ref2">[2]</a>: Mingjin Zhang, Rui Zhang, Yuxiang Yang, Haichen Bai, Jing Zhang, and Jie Guo. **ISNet: Shape Matters for Infrared Small Target Detection.** *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (2022), 877–886.

<a name="ref3">[3]</a>: Boyang Li, Xinyi Ying, Ruojing Li, Yongxian Liu, Yangsi Shi, and Miao Li. **The First Competition on Resource-Limited Infrared Small Target Detection Challenge: Methods and Results.** *arXiv preprint* arXiv:2408.09615 (2024).

<a name="ref4">[4]</a>: Thang Vu, Hyunjun Jang, Trung X. Pham, and Chang Yoo. **Cascade RPN: Delving into High-Quality Region Proposal Network with Adaptive Convolution.** *Advances in Neural Information Processing Systems* 32 (2019).

<a name="ref5">[5]</a>: Yimian Dai, Xiang Li, Fei Zhou, Yulei Qian, Yaohong Chen, and Jian Yang. **One-Stage Cascade Refinement Networks for Infrared Small Target Detection.** *IEEE Transactions on Geoscience and Remote Sensing* 61 (2023), 1–17.

<a name="ref6">[6]</a>: Heng Sun, Junxiang Bai, Fan Yang, and Xiangzhi Bai. **Receptive-Field and Direction Induced Attention Network for Infrared Dim Small Target Detection With a Large-Scale Dataset IRDST.** *IEEE Transactions on Geoscience and Remote Sensing* 61 (2023), 1–13.

<a name="ref7">[7]</a>: Boyang Li, Chao Xiao, Longguang Wang, Yingqian Wang, Zaiping Lin, Miao Li, Wei An, and Yulan Guo. **Dense Nested Attention Network for Infrared Small Target Detection.** *IEEE Transactions on Image Processing* 32 (2023), 1745–1758.

<a name="ref8">[8]</a>: Tianhao Wu, Boyang Li, Yihang Luo, Yingqian Wang, Chao Xiao, Ting Liu, Jungang Yang, Wei An, and Yulan Guo. **MTU-Net: Multilevel TransUNet for Space-Based Infrared Tiny Ship Detection.** *IEEE Transactions on Geoscience and Remote Sensing* 61 (2023), 1–15.

<a name="ref9">[9]</a>: Ruojing Li, Wei An, Chao Xiao, Boyang Li, Yingqian Wang, Miao Li, and Yulan Guo. **Direction-Coded Temporal U-Shape Module for Multiframe Infrared Small Target Detection.** *IEEE Transactions on Neural Networks and Learning Systems* 36 (2025), 555–568.

<a name="ref10">[10]</a>: Nan Jiang, Kuiran Wang, Xiaoke Peng, Xuehui Yu, Qiang Wang, Junliang Xing, Guorong Li, Guodong Guo, Qixiang Ye, Jianbin Jiao, Jian Zhao, and Zhenjun Han. **Anti-UAV: A Large-Scale Benchmark for Vision-Based UAV Tracking.** *IEEE Transactions on Multimedia* 25 (2023), 486–500.