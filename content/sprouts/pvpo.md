---
title: 新芽专题介绍（25）：全景视频感知优化
date: 2025-09-17T01:26:00Z
draft: false
math: true
---

## 一、专题介绍
### 1.1 研究背景

近年来，全景（360°/VR）视频感知技术在虚拟现实、智慧监控、沉浸式娱乐以及自动驾驶等场景中得到了广泛关注。与传统平面视频相比，全景视频在提供完整视野和沉浸体验的同时，也带来了显著的计算与感知挑战：如球面几何畸变导致的特征提取偏差、超高分辨率带来的计算成本以及全局上下文建模的复杂性。现有方法通常基于平面视频进行优化，难以有效捕获跨区域的长程依赖或精细运动信息，导致检测、分类、分割等任务的表现与全景信息的潜在价值存在较大差距。因此，如何在**保持计算效率**的同时，**提升全景视频的空间感知精度、时序建模能力以及多模态对齐度**，成为当前研究的关键问题。

### 1.2 研究意义
在全景视频感知技术的发展背景下，提升全景视频的空间与时序理解能力，无疑是推动沉浸式应用与智能分析的关键突破。高精度的全景视频感知不仅是后续视频分析、增强现实与自动驾驶等任务的核心，还直接决定了多模态理解和决策的可靠性。这一提升的实现，将在多个层面产生深远而广泛的影响。
1. **增强全景视频理解能力，拓展多模态应用**：精细化的空间与时序感知能够更准确地捕捉全景场景中的对象位置、动作轨迹及跨视野关系，显著提升全景视频问答（VQA）、目标检测、行为分析和事件识别等任务的表现，使全景视频理解从“局部模糊”迈向“全局精准”。
2. **提升多模态对齐与语义一致性**：高精度的全景感知可为多模态分析（如 RGB、深度、光流）提供可靠的语义约束，减少因几何畸变或极区信息缺失导致的识别偏差，确保对象、动作及场景在时间和空间上的一致性，从而增强下游任务的可靠性与稳健性。
3. **推动全景视频感知技术赋能下游应用**：实例级、全局一致的全景感知能力可广泛应用于虚拟现实场景渲染、沉浸式教育、智能监控异常检测、自动驾驶环境感知及娱乐内容生成等领域。
因此，该研究主题不仅具有重要的学术价值，也将在沉浸式媒体、智慧监控及智能交通等行业中展现广阔的应用前景，是推动全景视频感知技术从理论探索走向实际落地的关键方向。

![](https://imgtu.com/uploads/32ky56l8/r-1280x1280_1.webp)
▲ 全景图像的ERP投影。

### 1.3 当前主要挑战
优化全景视频感知，仍存在以下挑战：
1. **全景视频数据集匮乏**：与平面视频相比，可用于全景视频感知训练和评测的高质量公开数据集数量有限，且大多数数据集在分辨率、标注精细度、场景多样性或时序长度上存在局限。这严重制约了算法的泛化能力、模型训练效率以及跨场景应用的可靠性。
2. **几何畸变与特征提取困难**：全景视频采用 ERP 或球面投影方式呈现，极区存在明显拉伸，而常规卷积或局部特征提取方法难以适应球面几何，导致目标识别、分割和跟踪精度下降，同时超高分辨率视频增加了计算成本，精度与效率难以兼顾。
3. **多模态能力不足**：全景视野可达 360°，对象可能跨越多个视角或极区。结合多模态统一建模能力不足，影响动态场景理解和事件分析。
### 1.4 研究目标
要求模型在传统平面图像感知的基础上，基于ERP格式的全景视频特性进行算法优化，完成子任务，包含理解、检测、分割、追踪任务等.

## 二、学习资料与参考文献
### 2.1 基础教材与学习材料
> 在开始探险之前，你需要掌握一些基础的“内功心法”，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：

* 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)
* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材
* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)
* [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门（难度不小）

> 此外，你也可以使用一些**入门工具**：

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。
* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛
* [FFmpeg 音视频处理教程](https://zhuanlan.zhihu.com/p/15849180981)：FFmpeg帮助掌握音视频编解码、帧提取、多轨道合成等基础操作。

> Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

### 2.2 入门文献（图像视觉感知）
> 学生第一阶段的阅读训练，可帮助理解视觉感知这一通用算法。**仅用于入门，不可选择此部分文献汇报**。
* **[ResNet](https://arxiv.org/pdf/1512.03385): Deep Residual Learning for Image Recognition (CVPR 2016)**
* **[YOLO](https://arxiv.org/pdf/1506.02640): You Only Look Once: Unified, Real-Time Object Detection (CVPR 2016)**
* **[Faster R-CNN](https://arxiv.org/pdf/1506.01497): Towards Real-Time Object Detection with Region Proposal Networks (NeurIPS 2015)**
* **[DETR](https://arxiv.org/pdf/2005.12872): End-to-End Object Detection with Transformers (ECCV 2020)**
* **[Mask R-CNN](https://arxiv.org/pdf/1703.06870): Mask R-CNN (ICCV 2017)**
* **[MaskFormer](https://arxiv.org/pdf/2107.06278): Per-Pixel Classification is Not All You Need for Semantic Segmentation (NeurIPS 2021)**
* DenseNet: Densely Connected Convolutional Networks (CVPR 2017)
* R-CNN: Rich feature hierarchies for accurate object detection and semantic segmentation (CVPR 2014)
* Fast R-CNN: Fast R-CNN (ICCV 2015)
* SSD: Single Shot MultiBox Detector (ECCV 2016)
* RetinaNet: Focal Loss for Dense Object Detection (ICCV 2017)
* FCOS: Fully Convolutional One-Stage Object Detection (ICCV 2019)
* FCN: Fully Convolutional Networks for Semantic Segmentation (CVPR 2015)
* U-Net: Convolutional Networks for Biomedical Image Segmentation (MICCAI 2015)
* DeepLab v3+: Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation (ECCV 2018)
### 2.3 进阶文献（平面视频感知）
> 学生可在此部分选择进阶文献进行课题汇报，或自行查找最新的同类重要文献。
* **[SAM 2](https://arxiv.org/pdf/2408.00714): Segment Anything in Images and Videos (ArXiv 2024)**
* **[MOTR](https://arxiv.org/pdf/2105.03247): End-to-End Multiple-Object Tracking with Transformer (ECCV 2022)**
* **[SlowFast](https://arxiv.org/pdf/1812.03982): SlowFast Networks for Video Recognition (ICCV 2019)**
* MaskTrack R-CNN: Video Instance Segmentation (CVPR 2019)
* X3D: Expanding Architectures for Efficient Video Recognition (CVPR 2020)
* STM: Video Object Segmentation using Space-Time Memory Networks (ICCV 2019)
* All in One: Exploring Unified Video-Language Pre-training (CVPR 2023)
### 2.4 全景图像与视频感知
> 结合本课题的研究背景，逐渐引导学生进入全景视频感知领域。学生可在此部分选择进阶文献进行课题汇报，或自行查找最新的同类重要文献。
* **[OmniTrack](https://arxiv.org/pdf/2503.04565): Omnidirectional Multi-Object Tracking (CVPR 2025)**
* **[PanoVOS](https://arxiv.org/pdf/2309.12303): Bridging non-panoramic and panoramic views with transformer for video segmentation (ECCV 2024)**
* **[360VOTS](https://openaccess.thecvf.com/content/ICCV2023/papers/Huang_360VOT_A_New_Benchmark_Dataset_for_Omnidirectional_Visual_Object_Tracking_ICCV_2023_paper.pdf): Visual Object Tracking and Segmentation in Omnidirectional Videos (Arxiv 2025)**
* 360VOT: A New Benchmark Dataset for Omnidirectional Visual Object Tracking (ICCV 2023)
* Im2Pano3D: From a Single Image to a 3D Semantic Panorama (CVPR 2018)
* Pano2Vid: Automatic Cinematography for 360° Video (ACCV 2016)
* OmniDet: Omnidirectional Vision: Saliency and Object Detection in 360° Images (CVPR 2019)
* FoV-IoU: Field-of-view IoU for object detection in 360° images (Arxiv 2023)
* MPFR-Net: Multi-projection fusion and refinement network for salient object detection in 360 omnidirectional image (TNNLS 2023)
* Waymo-PVPS: Panoramic video panoptic segmentation (ECCV 2022)
### 2.5 其他代码基础或demo
> 可以用作基线（baseline）的代码参考与demo参考帮助理解
* [OmniTrack Github](https://github.com/xifen523/OmniTrack) (2025)


## 三、结语与期望
“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。红外弱小目标检测是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
