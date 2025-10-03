---
title: 新芽专题介绍：多目标跟踪
date: 2025-09-17T01:27:00Z
draft: false
math: true
---

> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。

## 一、专题介绍

### 1.1  研究背景

在现代计算机视觉与智能感知系统中，多目标跟踪（Multi-Object Tracking, MOT）是核心研究任务之一。它旨在在视频序列中同时检测并持续跟踪多个目标的空间位置与运动轨迹。该技术广泛应用于**无人机航拍、智能交通、安防监控、自动驾驶以及军事防御等领域**，能够提供动态环境下的实时目标行为信息，是态势感知与智能决策的重要支撑。与单目标跟踪不同，多目标跟踪面对的是一个高度动态与复杂的场景：目标数量不确定，运动轨迹多样，遮挡、交互和丢失问题频繁发生。这使得MOT成为计算机视觉研究中的一个长期难题，也是算法创新与应用落地的试金石。

### 1.2  研究意义

多目标跟踪通常指在连续视频序列中，**同时检测并持续跟踪多个目标的空间位置与轨迹**。与单目标跟踪相比，它不仅要解决单个对象的定位问题，还要处理目标之间的交互、遮挡与身份保持等复杂挑战。然而，能否在动态场景中对多个目标实现稳定、准确的跟踪，直接关系到：

1. **军事防御与战场感知**：在复杂战场环境中，多目标跟踪可用于敌方无人机、导弹与地面目标的实时监测与轨迹预测，直接影响防御系统的反应速度与有效性。

2. **公共安全与社会治理**：在智慧城市与公共安防中，多目标跟踪能够实时监控人群与车辆动态，提升事故预警与治安防控能力。

3. **智能交通与无人系统**：在自动驾驶与无人机系统中，持续跟踪多类目标是安全避障、路径规划与协同控制的核心前提。

因此，多目标跟踪既有现实紧迫性，又是前沿方法学的重要突破口。

[![MOT.gif](https://imgtu.com/uploads/s75y2804/t-mot.webp)](https://imgtu.com/upload/s75y2804/mot)

▲一个典型的多目标跟踪场景：复杂环境下的车辆与行人跟踪。

### 1.3  当前主要挑战

尽管多目标跟踪在智能感知和应用系统中具有重要地位，但其实现过程仍然面临多重挑战：

1. **挑战一：目标动态复杂，身份保持困难**

   * 多目标在视频序列中存在尺度变化、光照差异、运动模式多样等问题，检测结果往往不够稳定。

   * 当多个目标发生遮挡或交互时，极易出现轨迹丢失和ID切换，难以保证长时间跟踪的一致性。

   * 特别是在密集人群或车辆场景中，身份保持成为精度提升的主要瓶颈。

2. **挑战二：数据关联脆弱，特征建模不足**

   * 多目标跟踪的核心在于跨帧的匹配与关联，但传统的几何距离或外观相似性度量在复杂场景下可靠性不足。

   * 背景干扰、外观相似目标的存在，都会导致错误关联。

   * 如何在时序维度融合外观特征、运动信息和上下文关系，建立更加鲁棒的特征表征与匹配机制，是研究的关键。

3. **挑战三：计算压力巨大，实时性难以兼顾**

   * 多目标跟踪通常处理高分辨率视频，目标数量众多，导致算法计算量庞大。

   * 在无人机、自动驾驶等资源受限的边缘平台上，算力和功耗限制更加突出。

   * 如何在有限资源下保持高效处理，实现实时且稳定的跟踪，是工程化落地的最大难点。

综上，多目标跟踪技术仍处于不断突破的阶段，既面临实际应用的紧迫需求，也孕育着前沿研究的广阔空间。

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

> 这一类是MOT研究的起点，方法简洁高效，主要解决基本的检测与数据关联问题，同时建立了标准评测体系。

* **[DeepSORT](https://arxiv.org/pdf/1703.07402): Simple Online and Realtime Tracking with a Deep Association Metric (ICIP 2017)**

* **[SORT](https://arxiv.org/pdf/1602.00763): Simple Online and Realtime Tracking (ICIP 2016)**

* **[MOTChallenge Benchmark](https://motchallenge.net/): A Benchmark for Multiple Object Tracking (ECCV 2016)**

* **[FairMOT](https://arxiv.org/pdf/2004.01888): FairMOT : On the Fairness of Detection and Re-Identification in Multiple Object Tracking (IJCV 2021)**

* [HOTA](https://link.springer.com/article/10.1007/s11263-020-01375-2): HOTA: A Higher Order Metric for Evaluating Multi-object Tracking (International Journal of Computer Vision 2021)

* [JDE](https://link.springer.com/chapter/10.1007/978-3-030-58621-8_7): Towards Real-Time Multi-Object Tracking (ECCV 2020)

* [DanceTrack](https://arxiv.org/abs/2111.14690): DanceTrack: A Challenging Benchmark for Multi-Object Tracking  (CVPR 2022)

* [BoT-SORT](https://www.arxiv.org/abs/2206.14651): BoT-SORT: Robust Associations Multi-Pedestrian Tracking (Arxiv 2022)

* [ByteTrack](https://arxiv.org/pdf/2110.06864): ByteTrack: Multi-Object Tracking by Associating Every Detection Box (ECCV 2022)

### 2.3 进阶方法

这一类方法在基础框架上加入ReID、运动建模、图匹配或记忆机制，显著提升了复杂场景下的鲁棒性和精度。

* **[OC-SORT](https://arxiv.org/pdf/2203.14360): Observation-Centric SORT : Rethinking SORT for Robust Multi-Object Tracking (CVPR 2023)**

* **[CenterTrack](https://link.springer.com/chapter/10.1007/978-3-030-58548-8_28): Tracking Objects as Points  (ECCV 2020)**

* **[MotionTrack](https://arxiv.org/abs/2303.10404): MotionTrack: Learning Robust Short-Term and Long-Term Motions for Multi-Object Tracking (CVPR 2023)**

* [SOTMOT](https://ieeexplore.ieee.org/document/9578284): Improving Multiple Object Tracking With Single Object Tracking  (CVPR 2021)

* [MO3TR](https://www.arxiv.org/abs/2103.14829): Looking Beyond Two Frames: End-to-End Multi-Object Tracking Using Spatial and Temporal Transformers (TPAMI 2022)

* [Chained-Tracker](https://www.arxiv.org/abs/2007.14557): Chained-Tracker: Chaining Paired Attentive Regression Results for End-to-End Joint Multiple-Object Detection and Tracking (ECCV 2020)

* [MeMOT](https://arxiv.org/abs/2203.16761): MeMOT: Multi-Object Tracking With Memory  (CVPR 2022)

* [SiamMOT](https://arxiv.org/abs/2105.11595): SiamMOT: Siamese Multi-Object Tracking (CVPR 2021)

* [MAT](https://www.sciencedirect.com/science/article/abs/pii/S0925231221019627): MAT: Motion-aware multi-object tracking (Neurocomputing 2022)

* [QDTrack](https://www.arxiv.org/abs/2006.06664): Quasi-Dense Similarity Learning for Multiple Object Tracking (CVPR 2021)

* [SUSHI](https://www.arxiv.org/pdf/2212.03038): Unifying Short and Long-Term Tracking with Graph Hierarchies (CVPR 2023)

* [UMA](https://www.arxiv.org/abs/2003.11291): A Unified Object Motion and Affinity Model for Online Multi-Object Tracking (CVPR 2020)

* [Siamese Track-RCNN](https://www.arxiv.org/abs/2004.07786): Multi-Object Tracking with Siamese Track-RCNN (Arxiv 2020)

* [CSTrack](https://www.arxiv.org/abs/2010.12138): Rethinking the competition between detection and ReID in Multi-Object Tracking (TIP 2020)

* [SMILEtrack](https://www.arxiv.org/abs/2211.08824): SMILEtrack: SiMIlarity LEarning for Occlusion-Aware Multiple Object Tracking (AAAI 2024)

### 2.4 基于Transformer方法（端到端与时空建模）

该类方法利用Transformer的全局建模能力，统一检测与跟踪，实现跨帧时空特征的高效建模，是当前研究热点。

* **[DETR](https://arxiv.org/pdf/2005.12872): End-to-End Object Detection with Transformers (ECCV 2020)**

* **[MOTR](https://link.springer.com/chapter/10.1007/978-3-031-19812-0_38): MOTR: End-to-End Multiple-Object Tracking with Transformers (ECCV 2022)**

* **[TransTrack](https://arxiv.org/pdf/2012.15460): TransTrack: Multiple Object Tracking with Transformer (CVPR 2021)**

* **[TrackFormer](https://arxiv.org/pdf/2101.02702): TrackFormer: Multi-Object Tracking with Transformers (CVPR 2022)**

* [TransMOT](https://www.arxiv.org/abs/2104.00194): TransMOT: Spatial-Temporal Graph Transformer for Multiple Object Tracking (WACV 2023)

* [GTR](https://www.arxiv.org/abs/2203.13250Global): Global Tracking Transformers (CVPR 2022)

* [MOTRv2](https://arxiv.org/abs/2211.09791): MOTRv2: Bootstrapping End-to-End Multi-Object Tracking by Pretrained Object Detectors  (CVPR 2023)

### 2.5 扩展与特殊场景

这些研究聚焦在细分领域或扩展任务，如MOT+分割、无人机航拍、体育比赛和分割驱动的MOT，推动MOT走向更复杂应用。

* [SAM2MOT](https://www.arxiv.org/abs/2504.04519): SAM2MOT: A Novel Paradigm of Multi-Object Tracking by Segmentation (Arxiv 2025)

* [MOTS](https://ieeexplore.ieee.org/document/8953401): MOTS: Multi-Object Tracking and Segmentation (CVPR 2019)

* [SportsMOT](https://www.arxiv.org/abs/2304.05170): SportsMOT: A Large Multi-Object Tracking Dataset in Multiple Sports Scenes (ICCV 2023)

* [UAVMOT](https://ieeexplore.ieee.org/document/9878576): Multi-Object Tracking Meets Moving UAV  (CVPR 2022)

* [3D MOT](https://ieeexplore.ieee.org/abstract/document/9341164): 3D Multi-Object Tracking: A Baseline and New Evaluation Metrics (IROS 2020)

* [SimpleTrack](https://link.springer.com/chapter/10.1007/978-3-031-25056-9_43): SimpleTrack: Understanding and Rethinking 3D Multi-object Tracking (ECCV 2022)

* [YOLO11-JDE](https://www.arxiv.org/abs/2501.13710): YOLO11-JDE: Fast and Accurate Multi-Object Tracking with Self-Supervised Re-ID (WACV 2025)

* [SparseTrack](https://www.arxiv.org/abs/2306.05238): SparseTrack: Multi-Object Tracking by Performing Scene Decomposition based on Pseudo-Depth (TCSVT 2025)

***

## 三、结语与期望

多目标跟踪是一个理论与实践高度结合的方向，它要求研究者同时具备检测、关联、时序建模与系统部署的能力。对于初入科研的学生而言，MOT不仅能快速锻炼编程与算法能力，还能培养解决实际问题的综合思维。

我们期待通过本专题，能够让新芽学子在阅读经典文献与实践前沿算法的过程中，逐步理解这一领域的内在逻辑，并在最终的专题汇报中展现自己的深度思考与创新见解。
