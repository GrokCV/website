---
title: 新芽专题介绍（2）：辅助信息/辅助任务驱动的视觉感知
date: 2025-09-17T01:49:00Z
draft: false
math: true
authors: 
- admin
---

## 一、专题介绍

### 1.1  研究背景

随着各项视觉任务如目标检测、图像分割、图像复原等在实际应用场景中的落地，研究者逐渐意识到，单一模态数据和单一任务驱动的模型虽然在标准数据集上能够取得优异表现，但在**复杂场景**下往往难以保持稳定的性能。这种局限性一方面源于单一任务对特征挖掘的不完全，另一方面源于单一模态数据本身的信息缺失。

在此背景下，**引入辅助信息与辅助任务**成为提升视觉任务性能的重要思路。通过在输入层注入额外模态数据，或在训练阶段融入合理的辅助任务联合学习，模型能够学习到更全面、更鲁棒的特征表示，从而在主任务上实现性能提升，并进一步增强跨域泛化能力。

### 1.2  研究意义

在视觉任务中，辅助信息与辅助任务的引入价值主要体现在以下几个方面：

1. **缓解主任务数据稀缺与高成本问题**：在许多应用中，主任务数据标注昂贵且有限。通过辅助信息或辅助任务的引入，能够提供额外判别依据并提升有限数据的利用效率，缓解过拟合风险，降低对大规模标注的依赖。
2. **提升主任务表征学习的鲁棒性**：辅助任务通过多目标联合优化为特征空间施加结构性约束。例如，在检测任务中引入边缘检测或属性预测，可促使模型学习到更具判别力和可迁移性的特征表达。
3. **促进跨模态与跨任务融合**：辅助信息与任务天然推动多模态、多任务的协同学习，使模型能够在异质场景中更好地适应与泛化。这对自动驾驶、医学影像、遥感监测等复杂应用场景尤为关键。

下图展示了辅助信息/辅助任务赋能视觉任务的经典工作：

![](https://imgtu.com/uploads/od8uhlnj/xinya.png)

因此，引入辅助信息或辅助任务不仅是一种性能优化的有效策略，更是推动通用视觉智能持续演进的重要途径。

### 1.3  当前主要挑战

尽管该方向潜力巨大，但在具体落地过程中依然存在诸多亟待突破的瓶颈：

1. **挑战一：辅助信息与辅助任务的有效性与相关性**
   - 辅助信息在真实场景中可能存在**缺失、噪声或不一致性**，若缺乏稳健机制加以甄别与利用，反而可能对模型产生误导。
   - 辅助任务若与主任务**相关性不足**，甚至存在目标冲突，容易削弱特征学习效果，导致负迁移。如何科学选择并设计与主任务高度协同的辅助信息和任务，是亟需解决的关键问题。
2. **挑战二：多模态与多任务的融合与协同**
   - 不同模态数据（如 RGB 图像、红外图像、深度图、文本、点云、事件等）在**表征形式、信息密度和噪声特性**上差异显著，直接拼接或简单融合往往会造成特征空间不对齐、信息冗余甚至互相干扰。
   - 多任务联合优化过程中，由于任务间**难度差异与优化目标差异**，常常引发梯度冲突与收敛速率不一致，从而影响整体性能提升。如何实现高效的特征对齐与任务协同，是模型设计的核心挑战之一。
3. **挑战三：性能提升与计算开销的平衡**
   - 引入辅助信息与任务虽然能够增强模型表征能力，但不可避免地增加了**参数规模与计算复杂度**，在训练与推理阶段均带来额外开销。
   - 在资源受限的应用场景（如移动端、无人机、边缘计算设备）中，算力、存储与功耗约束尤为突出，复杂模型难以直接部署。如何在保证性能提升的同时兼顾**轻量化与实时性**，是落地应用面临的重要瓶颈。

综上，对于本科生而言，对该方向的理解意味着不仅要掌握单一算法，更要具备跨模态、跨任务的思维与实践能力，从而在科研起点上拓展更广阔的视野。

***

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

### 2.2  入门文献
> 学生第一阶段的阅读训练，可帮助初步了解辅助信息和辅助任务驱动的各种经典任务。**仅用于入门，不可选择此部分文献汇报**。

* [ConcatNet](https://arxiv.org/abs/1505.03873): Improving image classification with location context (ICCV 2015)

* [PriorsNet](https://arxiv.org/pdf/1906.05272): Presence-Only Geographical Priors for Fine-Grained Image Classification (ICCV 2019)

* [GeoNet](https://arxiv.org/abs/1906.01737): Geo-aware networks for fine-grained recognition (ICCVW 2019)

* [Dynamic MLP](https://arxiv.org/abs/2203.03253): Dynamic MLP for Fine-Grained Image Classification by Leveraging Geographical and Temporal Information (CVPR2022)

* [RGBD-SOD](https://ieeexplore.ieee.org/abstract/document/10897410): RGB-D salient object detection: A survey (CVMJ 2021)

* [Indoor Segmentation and Support Inference from RGBD Images](https://link.springer.com/chapter/10.1007/978-3-642-33715-4_54) (ECCV 2012)

* [xMUDA](https://arxiv.org/abs/1911.12676): xMUDA: Cross-Modal Unsupervised Domain Adaptation for 3D Semantic Segmentation (CVPR 2020)

* [D4](https://ieeexplore.ieee.org/document/9878571): Self-Augmented Unpaired Image Dehazing via Density and Depth Decomposition (CVPR 2022)

* [EFNet](https://arxiv.org/abs/2112.00167): Event-Based Fusion for Motion Deblurring with Cross-modal Attention (ECCV 2020)

* [AuxSegNet](https://arxiv.org/abs/2107.11787): Leveraging Auxiliary Tasks with Affinity Learning for Weakly Supervised Semantic Segmentation (ICCV 2021) 

* [Image Change Captioning by Learning From an Auxiliary Task](https://ieeexplore.ieee.org/document/9577664)
(CVPR 2021)

* [ObjectNav](https://arxiv.org/abs/2104.04112): Auxiliary Tasks and Exploration Enable ObjectGoal Navigation (ICCV 2021)

***

### 2.3 进阶文献
> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

辅助信息
* [SAMLP](https://ieeexplore.ieee.org/document/10172029/): Improving Fine-Grained Image Classification With Multimodal Information (TMM 2024)

* [MetaSegNet](https://arxiv.org/abs/2312.12735): MetaSegNet: Metadata-collaborative Vision-Language Representation Learning for Semantic Segmentation of Remote Sensing Images (TGRS 2024)

* [DMM](https://arxiv.org/abs/2407.08132): DMM: Disparity-Guided Multispectral Mamba for Oriented Object Detection in Remote Sensing (TGRS 2025)

* [LightDiff](https://arxiv.org/abs/2404.04804): Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving (CVPR 2024)

* [PUGAN](https://arxiv.org/abs/2306.08918): PUGAN: Physical Model-Guided Underwater Image Enhancement Using GAN with Dual-Discriminators (TIP 2023) 

* [Dformer](https://arxiv.org/abs/2309.09668): DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation (ICLR 2024)

* [DFormerv2](https://arxiv.org/abs/2504.04701): DFormerv2: Geometry Self-Attention for RGBD Semantic Segmentation (CVPR 2025)

* [EventAid](https://arxiv.org/abs/2312.08220): EventAid: Benchmarking Event-Aided Image/Video Enhancement Algorithms With Real-Captured Hybrid Dataset (TPAMI 2025)

* [EvDeblurNeRF](https://arxiv.org/abs/2403.19780): Mitigating Motion Blur in Neural Radiance Fields with Events and Frames (CVPR 2024)

* [EvaGaussians](https://arxiv.org/abs/2405.20224): EvaGaussians: Event Stream Assisted Gaussian Splatting from Blurry Images (arxiv 2024)

* [TransFusion](https://ieeexplore.ieee.org/document/10208592): TransFusion: Multi-modal Fusion Network for Semantic Segmentation (CVPRW 2023)

* [MSALNet](https://ieeexplore.ieee.org/document/10589918): Multi-Stage Auxiliary Learning for Visible-Infrared Person Re-Identification (TCSVT 2024)

* [AuxDet](https://arxiv.org/pdf/2505.15184): Auxiliary Metadata Matters for Omni-Domain Infrared Small Target Detection (arXiv 2025)

辅助任务：
* [Rethinking Image Restoration for Object Detection](https://proceedings.neurips.cc/paper_files/paper/2022/file/1cac8326ce3fbe79171db9754211530c-Paper-Conference.pdf) (NeurIPS 2022)

* [AuxFormer](https://arxiv.org/abs/2308.08942): Auxiliary Tasks Benefit 3D Skeleton-based Human Motion Prediction (ICCV 2023)

* [CI-DGA](https://link.springer.com/article/10.1007/s11263-025-02529-w): A Causal Intervention Method for Domain Generalization with a Self-Supervised Auxiliary Task (IJCV 2025)

* [SMG-LLIE](https://arxiv.org/abs/2305.05839): Low-Light Image Enhancement via Structure Modeling and Guidance (CVPR 2023)

* [GG-LLERF](https://arxiv.org/abs/2312.15855): Geometric-Aware Low-Light Image and Video Enhancement via Depth Guidance (TIP 2025)

* [SKF](https://arxiv.org/abs/2304.07039): Learning semantic-aware knowledge guidance for low-light image enhancement (CVPR 2023)

* [DCMPNet](https://arxiv.org/abs/2403.01105): Depth information assisted collaborative mutual promotion network for single image dehazing (CVPR 2024)

* [Osmosis](https://arxiv.org/abs/2403.14837): Osmosis: RGBD Diffusion Prior for Underwater Image Restoration (ECCV 2024)

* [PDHAT](https://ieeexplore.ieee.org/document/10403902): Perceptual Decoupling With Heterogeneous Auxiliary Tasks for Joint Low-Light Image Enhancement and Deblurring (TMM 2024)

* [S2Gaussian](https://openaccess.thecvf.com/content/CVPR2025/papers/Wan_S2Gaussian_Sparse-View_Super-Resolution_3D_Gaussian_Splatting_CVPR_2025_paper.pdf): S2Gaussian: Sparse-View Super-Resolution 3D Gaussian Splatting (CVPR 2025)

* [DMM](https://arxiv.org/abs/2407.08132): DMM: Disparity-Guided Multispectral Mamba for Oriented Object Detection in Remote Sensing (TGRS 2025)

* [MSALNet](https://ieeexplore.ieee.org/document/10589918): Multi-Stage Auxiliary Learning for Visible-Infrared Person Re-Identification (TCSVT 2024)

* [BAFE-Net](https://arxiv.org/pdf/2407.20078): Background Semantics Matter: Cross-Task Feature Exchange Network for Clustered Infrared Small Target Detection With Sky-Annotated Dataset (arXiv 2024)

* [HazyDet](https://arxiv.org/abs/2409.19833): HazyDet: Open-Source Benchmark for Drone-View Object Detection with Depth-Cues in Hazy Scenes (arxiv 2024)

* [A Simple Detector with Frame Dynamics is a Strong Tracker](https://arxiv.org/abs/2505.04917) (CVPRW 2025)

***

## 三、结语与期望

利用辅助信息与辅助任务提升视觉任务性能，不仅是视觉智能研究的重要前沿，更承载着应对复杂现实场景的技术使命。希望通过这一专题，新芽学子能够超越单一任务的局限，学会从多模态、多任务的视角审视问题，培养独立思考、系统分析与创新实践的能力。

我们期望，在最终的汇报中，每位同学都能将所学知识转化为独立见解与创新成果，让科研不仅成为探索的过程，更成为塑造未来视觉智能发展的力量源泉。让“新芽”在实践中扎根，在思考中生长，成为推动学术前沿和技术创新的新生力量。