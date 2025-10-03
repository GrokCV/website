---
title: 新芽专题介绍：事件相机目标检测
date: 2025-09-17T01:25:00Z
draft: false
math: true
---

> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。

## 一、专题介绍

### 1.1 研究背景

在新型视觉传感技术中，事件相机（Event Camera）作为一种**高时间分辨率（低延迟）、宽动态范围、低功耗**的传感器，正逐渐受到学术界与工业界的广泛关注。与传统帧式相机不同，事件相机通过捕捉**像素亮度变化**来生成异步事件流，从而实现**微秒级响应**与**稀疏数据输出**。这种特性使其在高速运动、极端光照、强对比度环境下，依旧能够稳定工作。

事件目标检测作为事件视觉的重要研究方向，旨在从**非冗余、异步的事件流**中提取目标信息，实现对快速移动或弱小目标的实时识别与定位。由于其独特的传感机制，该技术在国防预警、无人系统、智能交通以及空天探测等领域，均具有潜在的颠覆性应用价值。

### 1.2 研究意义

事件目标检测的核心难点在于事件数据的**稀疏性、非结构化与高噪声**特性。尽管如此，它所能带来的突破性能力，使其成为前沿研究的关键方向：

1. **军事防御与安全预警**  
   能够在高速飞行器、隐身目标或复杂干扰环境中快速识别目标，为新一代空天防御与导弹拦截系统提供坚实支撑。

2. **民用与交通安全**  
   应用于自动驾驶中的高速动态目标识别、无人机规避障碍、轨道交通监控等场景，有助于提升复杂环境下的安全性与鲁棒性。

3. **科学探索与空间探测**  
   在卫星监视、空间碎片探测、深空目标识别等极端条件下，事件相机独特的感知特性可实现传统传感器无法完成的探测任务。

4. **技术推动与交叉创新**  
   推动事件驱动神经网络、事件表示学习、跨模态融合等新型算法的发展，促进计算机视觉、神经形态计算与人工智能的深度融合。

因此，事件目标检测不仅是事件视觉领域的核心应用问题，也是当前智能感知技术的前沿探索主题，非常适合作为科研训练与技术攻关的重要方向。

![](https://imgtu.com/uploads/s9rxb5ji/r-right_top.webp)

▲ 事件相机与传统相机对比：得益于事件相机的高动态范围等优势，其能在各种光照（过曝、正常、欠曝）条件下，以微秒级响应，输出稀疏数据。传统相机在极端光照环境中，几乎完全失效。


### 1.3 当前主要挑战

在事件小目标检测（如无人机探测）中，主要面临以下几个关键问题：

1. **目标特征稀缺与噪声抑制**  
   无人机在事件流中通常只产生稀疏且弱小的事件点，极易与大量随机噪点或自然干扰（昆虫、鸟类等）混淆。如何在低信噪比条件下提取稳定、可分辨的目标特征，是最突出的挑战。

2. **真实场景建模与数据集不足**  
   现有事件检测数据集多依赖简化假设（如目标居中、环境单一），缺乏复杂飞行模式和极端环境条件的覆盖。这与实际应用差距明显，限制了算法的泛化性与实用性。

3. **高速机动目标的实时检测**  
   无人机具有高速、高机动性和不可预测的轨迹，要求检测算法在有限算力下实现毫秒级响应。如何兼顾检测精度与实时性，是算法设计的核心难点。

4. **跨模态感知与多源融合**  
   单一事件相机在某些场景下仍存在感知不足的问题。如何与RGB、红外、雷达等传感器进行有效互补与融合，从而增强系统鲁棒性，是未来的重要发展方向。


综上，事件小目标检测仍处于快速发展阶段，其方法体系和性能指标尚不成熟，但在应对高速、低光和复杂环境目标探测方面展现出独特优势。这不仅凸显了其应用潜力，也为算法创新与跨模态感知研究提供了广阔空间。
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

* [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑 PyTorch 代码。

* [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

>Tips：不要等到 “把所有基础都打好” 后再进入下一阶段学习，而是要在实践中学习，在探索中不断补充和完善基础。遇到不理解的地方，再回过头去查漏补缺，这样才能更高效地成长。


***

### 2.2  入门文献（事件目标检测方法等）

> 本阶段文献主要用于学生的初步阅读训练，旨在帮助理解事件数据的基本特性、常见的数据表达方式，以及事件目标检测（含语义分割方法）在内的相关算法与研究思路。
> 注意，本专题不推荐脉冲神经网络 (Spiking Neural Network, SNN) 相关文献。

**事件表达**

1. [End-to-End Learning of Representations for Asynchronous Event-Based Data](https://openaccess.thecvf.com/content_ICCV_2019/papers/Gehrig_End-to-End_Learning_of_Representations_for_Asynchronous_Event-Based_Data_ICCV_2019_paper.pdf) (CVPR 2019)

2. [From Chaos Comes Order:  Ordering Event Representations for Object Recognition and Detection](https://openaccess.thecvf.com/content/ICCV2023/papers/Zubic_From_Chaos_Comes_Order_Ordering_Event_Representations_for_Object_Recognition_ICCV_2023_paper.pdf) (ICCV 2023)

**事件目标检测**

1. [RVTs](https://openaccess.thecvf.com/content/CVPR2023/papers/Gehrig_Recurrent_Vision_Transformers_for_Object_Detection_With_Event_Cameras_CVPR_2023_paper.pdf): Recurrent Vision Transformers for Object Detection with Event Cameras (CVPR 2023)

2. [SAST](https://openaccess.thecvf.com/content/CVPR2024/papers/Peng_Scene_Adaptive_Sparse_Transformer_for_Event-based_Object_Detection_CVPR_2024_paper.pdf): Scene Adaptive Sparse Transformer for Event-based Object Detection (CVPR 2024)

3. [ASTMNet](https://ieeexplore.ieee.org/document/9749022): Asynchronous Spatio-Temporal Memory Network for Continuous Event-Based Object Detection (TIP 2022)



**事件语义分割**

1. [EV-SpSegNet](https://arxiv.org/abs/2506.23575): Event-based Tiny Object Detection: A Benchmark Dataset and Baseline (ICCV 2025)

2. [SSCNs](https://openaccess.thecvf.com/content_cvpr_2018/papers/Graham_3D_Semantic_Segmentation_CVPR_2018_paper.pdf): 3D Semantic Segmentation with Submanifold Sparse Convolutional Networks (CVPR 2018)

3. [EV-SegNet](https://openaccess.thecvf.com/content_CVPRW_2019/papers/EventVision/Alonso_EV-SegNet_Semantic_Segmentation_for_Event-Based_Cameras_CVPRW_2019_paper.pdf): EV-SegNet: Semantic Segmentation for Event-based Cameras (CVPRW 2019)



**事件 GitHub 资源**

1. [Event-based Vision Resources](https://github.com/uzh-rpg/event-based_vision_resources) (持续更新 | Stars 3.3k)

2. [Deep-Learning-for-Event-based-Vision](https://github.com/vlislab22/Deep-Learning-for-Event-based-Vision) (上年 | Stars 63)

3. [Awesome-Deep-Learning](https://github.com/yunfanLu/Awesome-Events-Deep-Learning) (三年前 | Stars 44)

4. [event_representation](https://github.com/LarryDong/event_representation) (两年前 | Stars 150)



***

### 2.3  进阶文献（前沿方法）

> 本部分聚焦事件目标检测的前沿研究与最新方法，旨在引导学生深入理解先进算法的设计理念、关键技术和实际应用。


**事件表达 (进阶)**

1. [Making Every Event Count:  Balancing Data Efficiency and Accuracy in Event Camera Subsampling](https://arxiv.org/abs/2505.21187) (arXiv 2025)

2. [Point-Voxel Absorbing Graph Representation Learning for Event Stream based Recognition](https://arxiv.org/abs/2306.05239) (arXiv 2023)

3. [Event2Vec: Processing neuromorphic events  directly by representations in vector space](https://arxiv.org/abs/2504.15371) (arXiv 2025)

4. [Event-based Graph Representation with Spatial and Motion Vectors  for Asynchronous Object Detection](https://arxiv.org/abs/2507.15150) (arXiv 2025)

5. [OmniEvent: Unified Event Representation Learning](https://arxiv.org/abs/2508.01842) (arXiv 2025)


**事件目标检测 (进阶)**

1. [CvHeat-DET](https://arxiv.org/abs/2505.12908): Dynamic Graph Induced Contour-aware Heat Conduction Network for Event-based Object Detection (arXiv 2025)

2. [MvHeat-DET](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Object_Detection_using_Event_Camera_A_MoE_Heat_Conduction_based_CVPR_2025_paper.pdf): Object Detection using Event Camera: A MoE Heat Conduction based Detector  and A New Benchmark Dataset (CVPR 2025)

3. [SODFormer](https://ieeexplore.ieee.org/document/10195232): SODFormer: Streaming Object Detection With Transformer Using Events and Frames (TPAMI 2023)

4. [NeRDD](https://arxiv.org/abs/2409.16099v1): Neuromorphic Drone Detection: an Event-RGB Multimodal Approach (ECCVW 2024)

5. [AEGNN](https://openaccess.thecvf.com/content/CVPR2022/papers/Schaefer_AEGNN_Asynchronous_Event-Based_Graph_Neural_Networks_CVPR_2022_paper.pdf): AEGNN: Asynchronous Event-based Graph Neural Networks (CVPR 2022)



**事件语义分割 (进阶)**


1. [EvSegFormer](https://ieeexplore.ieee.org/document/10058930): Event-Based Semantic Segmentation With Posterior Attention (TIP 2023)

2. [HMNet](https://openaccess.thecvf.com/content/CVPR2023/papers/Hamaguchi_Hierarchical_Neural_Memory_Network_for_Low_Latency_Event_Processing_CVPR_2023_paper.pdf): Hierarchical Neural Memory Network for Low Latency Event Processing (CVPR 2023)

3. [EIFNet](https://arxiv.org/abs/2507.21971): EIFNet: Leveraging Event-Image Fusion for Robust Semantic Segmentation (arXiv 2025)

4. [BRENet](https://arxiv.org/abs/2505.01548): Rethinking RGB-Event Semantic Segmentation with a Novel Bidirectional Motion-enhanced Event Representation (arXiv 2025)


***

### 2.4 事件综述及其他前沿方向

> 本部分提供关于事件视觉的综述文献及事件前沿研究方向的参考资料，包括事件目标追踪、事件多模态大模型、姿态估计等（主要提供最新的文献资料）。旨在为学生系统了解事件视觉领域全貌，并为进阶文献选择和专题汇报提供可靠、可操作的参考。


**事件综述**

1. [Drone Detection with Event Cameras](https://arxiv.org/abs/2508.04564) (arXiv 2025)

2. [Event-based Vision: A Survey](https://ieeexplore.ieee.org/document/9138762) (TPAMI 2020)

3. [Deep Learning for Event-based Vision:  A Comprehensive Survey and Benchmarks](https://arxiv.org/abs/2302.08890) (arXiv 2023)

4. [基于事件相机的目标检测与跟踪算法综述](https://researching.cn/ArticlePdf/m00002/2025/62/4/0400004.pdf) (激光与光电子学进展 2025)

5. [From Events to Enhancement: A Survey on Event-Based  Imaging Technologies](https://arxiv.org/abs/2505.05488) (arXiv 2025)

6. [Recent Event Camera Innovations: A Survey](https://link.springer.com/chapter/10.1007/978-3-031-92460-6_21) (ECCVW 2024)


**事件目标追踪**

1. [Object Tracking by Jointly Exploiting Frame and Event Domain](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Object_Tracking_by_Jointly_Exploiting_Frame_and_Event_Domain_ICCV_2021_paper.pdf)：Object Tracking by Jointly Exploiting Frame and Event Domain (ICCV 2021)

2. [AFNet](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_Frame-Event_Alignment_and_Fusion_Network_for_High_Frame_Rate_Tracking_CVPR_2023_paper.pdf)：Frame-Event Alignment and Fusion Network for High Frame Rate Tracking (CVPR 2023)

3. [EventVOT](https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_Event_Stream-based_Visual_Object_Tracking_A_High-Resolution_Benchmark_Dataset_and_CVPR_2024_paper.pdf)：Event Stream-based Visual Object Tracking: A High-Resolution Benchmark  Dataset and A Novel Baseline (CVPR 2024)

4. [SFTrack](https://arxiv.org/abs/2505.12903)：Towards Low-Latency Event Stream-based Visual Object Tracking: A Slow-Fast  Approach(arXiv 2025)

5. [Adversarial Attack and Defense](https://arxiv.org/abs/2504.14423)：Adversarial Attack for RGB-Event based Visual  Object Tracking (arXiv 2025)

6. [Mamba-FETrack V2](https://arxiv.org/abs/2506.23783)：Mamba-FETrack V2: Revisiting State Space Model  for Frame-Event based Visual Object Tracking (arXiv 2025)

7. [HDETrack V2](https://arxiv.org/abs/2502.05574)：Event Stream-based Visual Object Tracking: HDETrack V2 and A High-Definition Benchmark (arXiv 2025)

**事件多模态大模型**

1. [CM3AE](https://arxiv.org/abs/2504.12576): CM3AE: A Unified RGB Frame and Event-Voxel/-Frame Pre-training Framework (arXiv 2025)

2. [EventPretrain](https://arxiv.org/abs/2508.05507): Revealing Latent Information: A Physics-inspired Self-supervised Pre-training Framework for Noisy and Sparse Events (arXiv 2025)

3. [Event Camera Data Pre-training](https://openaccess.thecvf.com/content/ICCV2023/papers/Yang_Event_Camera_Data_Pre-training_ICCV_2023_paper.pdf): Event Camera Data Pre-training (ICCV 2023)

**姿态估计/行为识别**

1.  [EventCrab](https://arxiv.org/abs/2411.18328): EventCrab: Harnessing Frame and Point Synergy for Event-based Action Recognition and Beyond (CoRR 2024)

2. [EVT](https://openaccess.thecvf.com/content/WACV2025/papers/Lang_Event-Guided_Video_Transformer_for_End-to-End_3D_Human_Pose_Estimation_WACV_2025_paper.pdf): Event-guided Video Transformer for End-to-end 3D Human Pose Estimation (WACV 2025)

3. [MTevent](https://arxiv.org/abs/2505.11282): MTevent: A Multi-Task Event Camera Dataset for 6D Pose Estimation and Moving Object Detection (CVPRW 2025)

4. [EvSharp2Blur](https://arxiv.org/abs/2507.22438): From Sharp to Blur: Unsupervised Domain Adaptation for 2D Human Pose Estimation Under Extreme Motion Blur Using Event Cameras (ICCV 2025)

5. [MMHCO-HAR](https://arxiv.org/abs/2504.05830): Human Activity Recognition using RGBEvent based Sensors: A Multi-modal Heat  Conduction Model and A Benchmark Dataset (arXiv 2025)

6. [CA-MambaPose](https://openaccess.thecvf.com/content/WACV2025/papers/Lang_Event-Guided_Fusion-Mamba_for_Context-Aware_3D_Human_Pose_Estimation_WACV_2025_paper.pdf): Event-guided Fusion-Mamba for Context-aware 3D Human Pose Estimation (WACV 2025)



> 注意：建议仍以事件（小）目标检测为核心研究方向，但可根据个人兴趣探索相关或交叉领域。除事件目标追踪、事件多模态大模型、姿态估计/行为识别等方向外，还有事件视频去模糊、视频帧插值、事件图像增强、事件深度补全、事件超分辨率、自动驾驶、关键点检测等前沿研究方向可以自行深入探索。

***



## 三、结语与期望

“新芽计划”的初衷是激发学子对未知探索的热情，并为大家营造成长与实践的土壤。事件小目标检测是一个兼具挑战与机遇的前沿方向，它既关乎国家安全需求，也代表着学术创新的前沿阵地。希望通过本专题，大家不仅能够掌握前沿的智能感知知识，更能培养独立思考、动手实践与解决复杂问题的能力。  

我们期待在最终的汇报中，见证大家以智慧和创造力带来的独到见解与创新成果。
