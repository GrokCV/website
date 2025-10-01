---
title: 新芽专题介绍（6）：人体行为理解
date: 2025-09-17T01:45:00Z
draft: false
math: true
---

> 此专题由非南开大学老师发布，选修南开大学 2025 秋《人工智能实践课-初级》课程的同学请勿选择此专题。非本课程选修同学可自由选择。

## 一、专题介绍

### 1.1 研究背景

随着计算机视觉与人工智能技术的迅猛发展，人体行为理解逐渐成为**智能视频监控、人机交互、医疗康复、自动驾驶以及具身智能等领域的核心支撑技术**。其核心目标是通过分析与建模多源数据中的人体动作、姿态及其时序变化，实现对人类行为的自动分析与理解。凭借广泛的应用前景和重要的理论价值，人体行为理解已成为计算机视觉与人工智能领域的研究热点。

### 1.2 研究意义

人体行为理解技术旨在通过对多源数据中人体行为的自动感知与解析，为各类智能系统提供核心行为信息支撑。作为人工智能与计算机视觉领域的重要研究方向，该技术在**社会治理、具身智能、智慧医疗**等方面，具有广泛的应用价值和推动作用。典型应用领域例如：

1. **公共安全预警与事件检测**： 在机场、地铁站、商场及道路交通等公共场所，利用人体行为理解技术能够自动检测异常行为，例如：暴力行为、危险行为、违规行为以及异常行为。系统能够实时联动安防系统，实现自动报警和事件上报，有效提升安全事件的响应速度与处置能力，降低安全风险。

2. **具身智能与行为交互**： 人体行为理解技术为具身系统在动态开放环境中的多模态感知与运动控制提供核心支持，推动具身智能向更高层次的场景理解与行为协同方向发展。通过对人体姿态、手势及动作序列的实时感知与解析，具身智能体能够理解人类的交互意图和动作语义，并生成相应的响应行为。该能力广泛应用于服务机器人、康复辅助、智能陪伴等领域，实现自然、安全和协作式的人机交互。

3. **运动健康与精准医疗**： 在体育训练中，人体行为理解技术能够对运动员的技术动作进行精确捕捉与量化评估，为训练方案的制定与优化提供科学依据，提升训练效果。在医疗领域，该技术可应用于手术过程分析，评估手术操作的规范性和精准度；


因此，人体行为理解不仅在工业界与学术界长期受到关注，而且在开放数据资源与算法框架的推动下，拥有良好的研究与应用环境，亦为本科阶段科研训练与创新实践提供了理想的切入点。

![](https://imgtu.com/uploads/pl1yum9n/file_1e1b1b.png)

▲ **典型的人体行为理解场景示例**

### 1.3 当前主要挑战

传统的人体行为理解研究多在数据和环境受控的条件下进行，而当前的应用需求正将其推向开放和动态的真实场景，现有研究主要面临以下挑战：

1.  **挑战一：开放场景下的数据漂移与类别失衡**
    * 模型在受控环境下训练的数据分布与真实开放场景中存在显著差异，由于光照、视角、背景及人体姿态的剧烈变化，导致模型面临严重的分布外泛化问题，性能显著退化。
    * 真实场景中行为类别呈现长尾分布，高频行为类别数据充足，而关键性异常行为或细微交互动作样本稀缺，导致模型对尾部类别识别能力不足，漏检误检现象突出。

2.  **挑战二：边云场景下的资源受限与隐私保护**
    * 行为理解模型通常具有较高的计算与存储复杂度，难以在资源受限的边缘设备中实现低延迟、高效率的部署，制约其在实时监控等场景中的应用。
    * 智能应用依赖持续收集用户数据进行迭代，但视频、音频等数据包含大量个人隐私。将原始数据上传至云端进行集中式训练，面临严峻的数据泄露风险，制约了可信AI发展。

3.  **挑战三：具身场景下的物理交互和场景推理**
    *  具身行为理解要求智能体必须作为一个与物理环境共存的实体，去推断其动作所产生的物理效应。然而，当前方法难以将这些物理先验与多模态感知信息有效融合，导致其对交互动态的预测与真实物理规律存在偏差。
    * 具身场景中的行为与场景高度耦合，智能体需同步感知自身状态与环境语义，并推理时空、功能等复杂关系，现有方法缺乏对场景语义、时空关系以及因果逻辑的深层建模。

综上所述，人体行为理解仍处于快速演进与持续突破的关键阶段，不仅蕴含着面向实际应用的巨大潜力，也为深入探索智能感知与交互的前沿理论提供了重要契机。因此，围绕上述挑战开展系统性研究，将为推动该领域向更高精度、更强鲁棒性与更广适应性的方向演进提供坚实基础。
***
## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下三部分：

***

### 2.1 基础教材与学习材料

在进入实践环节之前，夯实理论基础至关重要。以下**精选的学习资料**，将为您的研究之路提供必要的知识储备。：

* [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）：深度学习领域的经典教材，系统全面地介绍了深度学习的理论基础与实践方法。
* [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)：PyTorch官方提供的入门与进阶教程，内容丰富，示例详尽，是学习PyTorch框架的最佳起点。
* [《Machine Learning》](https://www.coursera.org/learn/machine-learning/)（Andrew Ng 等）：机器学习领域的经典入门课程，以浅显易懂的方式讲解了机器学习的基本概念和常用算法。
* [《deeplearning.ai》](https://www.deeplearning.ai/deep-learning-specialization/)（Andrew Ng 等）：深度学习专项课程，系统地介绍了深度学习的核心概念、模型与应用。

此外，你也可以使用一些**入门工具**：
*   [GitHub](https://github.com/)：全球代码托管平台，版本控制与协作开发利器，可查找学习开源代码。
*   [Hugging Face](https://huggingface.co/)：预训练模型中心，轻松获取并使用各类AI模型。
*   [Gitee](https://gitee.com/)：国内代码托管平台，高速稳定，支持开源协作。
*   [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑PyTorch代码。
*   [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛
*   [CSDN](https://www.csdn.net/)：中文IT技术社区，海量教程博客，问题交流平台。

Tips：**实践才是最好的老师**。在实战中学习，遇到瓶颈时再回头巩固基础知识，效率更高！

***

### 2.2 入门文献（计算机视觉经典方法）

> 学生第一阶段的阅读训练，可帮助理解计算机视觉的通用范式。**仅用于入门，不可选择此部分文献汇报**。
*  [AlexNet](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf): ImageNet Classification with Deep Convolutional Neural Networks (NeurIPS 2012)
*  [GAN](https://arxiv.org/pdf/1406.2661): Generative Adversarial Nets (NeurIPS 2014)
*   [Faster R-CNN](https://arxiv.org/pdf/1506.01497): Towards Real-Time Object Detection with Region Proposal Networks （NeurIPS 2015）
*  [FCN](https://arxiv.org/pdf/1411.4038): Fully Convolutional Networks for Semantic Segmentation (CVPR 2015)
*  [U-Net](https://arxiv.org/pdf/1505.04597): Convolutional Networks for Biomedical Image Segmentation (MICCAI 2015)
*  [ResNet](https://arxiv.org/pdf/1512.03385): Deep Residual Learning for Image Recognition (CVPR 2016)
*   [FPN](https://arxiv.org/pdf/1612.03144v2): Feature Pyramid Networks for Object Detection (CVPR 2017)
*   [Focal Loss](https://arxiv.org/pdf/1708.02002v2): Focal Loss for Dense Object Detection (ICCV 2017)
*   [DETR](https://arxiv.org/pdf/2005.12872): End-to-End Object Detection with Transformers (ECCV 2020)
*   [ViT](https://arxiv.org/pdf/2010.11929): An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ICLR 2021)
*  [Vision Mamba](https://arxiv.org/pdf/2401.09417): Efficient Visual Representation Learning with Bidirectional State Space Model (ICML 2024)

***

### 2.3 人体行为理解领域相关文献

> **学生可在此部分选择文献进行专题汇报，或自行查找最新的同类重要文献**。

**视频动作识别 (Video Action Recognition)**
> 人体行为理解中最基础和核心的任务，其目标是为一段已剪辑好的短视频分配一个预定义的动作类别（如“打篮球”、“弹吉他”）, 该领域的关键挑战在于如何有效地建模视频中的时空特征。

* [Two-Stream CNNs](https://arxiv.org/pdf/1406.2199): Two-Stream Convolutional Networks for Action Recognition in Videos (NeurIPS 2014)
* [C3D](https://arxiv.org/pdf/1412.0767): Learning Spatiotemporal Features with 3D Convolutional Networks (ICCV 2015)
* [TSN](https://arxiv.org/pdf/1608.00859): Temporal Segment Networks: Towards Good Practices for Deep Action Recognition (ECCV 2016)
* [I3D](https://arxiv.org/pdf/1705.07750): Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset (CVPR 2017)
* [SlowFast](https://arxiv.org/pdf/1812.03982): SlowFast Networks for Video Recognition (ICCV 2019)
* [CCG-LSTM](https://ieeexplore.ieee.org/abstract/document/8762119): Coherence Constrained Graph LSTM for Group Activity Recognition (TPAMI 2019)
* [Timesformer](https://arxiv.org/pdf/2102.05095): Is Space-Time Attention All You Need for Video Understanding? (ICML 2021)
* [MViT](https://arxiv.org/pdf/2104.11227): Multiscale Vision Transformers (CVPR 2021)
* [VideoMAE](https://arxiv.org/pdf/2203.12602): Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training (NeurIPS 2022)
* [X-CLIP](https://www3.cs.stonybrook.edu/~hling/publication/X-CLIP.pdf): Expanding Language-Image Pretrained Models for General Video Recognition (ECCV 2022)
* [Actionclip](https://ieeexplore.ieee.org/abstract/document/10323592): Actionclip: Adapting Language-Image Pretrained Models for Video Action Recognition (TNNLS 2023)
* [TC-CLIP](https://link.springer.com/chapter/10.1007/978-3-031-72664-4_5): Leveraging Temporal Contextualization for Video Action Recognition (ECCV 2024)
* [STPM](https://ieeexplore.ieee.org/abstract/document/10812838): STPM: Spatial-Temporal Token Pruning and Merging for Complex Activity Recognition (TCSVT 2025)
* [FocusVideo](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Action_Detail_Matters_Refining_Video_Recognition_with_Local_Action_Queries_CVPR_2025_paper.pdf): Action Detail Matters: Refining Video Recognition with Local Action Queries (CVPR 2025)

**时序动作定位 (Temporal Action Localization)**
> 相较于动作识别，该任务要求模型在一段未剪辑的长视频中，不仅要识别出发生了哪些动作，还要精确定位每个动作的起始和结束时间。此任务的挑战在于处理复杂的背景、多变的动作时长以及精确的边界预测。

* [BSN](https://arxiv.org/pdf/1806.02964): Boundary-Sensitive Network for Temporal Action Proposal Generation (ECCV 2018)
* [BMN](https://arxiv.org/pdf/1907.09702): BMN: Boundary-Matching Network for Temporal Action Proposal Generation (ICCV 2019)
* [TadTR](https://ieeexplore.ieee.org/abstract/document/9854104): End-to-End Video Temporal Action Detection with Transformer (TIP 2022)
* [ActionFormer](https://link.springer.com/chapter/10.1007/978-3-031-19772-7_29): Actionformer: Localizing Moments of Actions with Transformers (ECCV 2022)
* [DeTAL](https://ieeexplore.ieee.org/abstract/document/10517407): DeTAL: Open-Vocabulary Temporal Action Localization With Decoupled Networks（TPAMI 2024）

**骨骼点动作识别 (Skeleton-based Action Recognition)**
> 这一方向利用人体骨骼点坐标序列作为输入，而非原始的RGB像素。这种模态的优势在于数据量小、计算高效，并且能天然地抵抗背景、光照、衣着等无关因素的干扰，使模型专注于人体的运动本身。核心挑战在于如何对骨骼点这种非欧几里得的图结构（Graph）数据进行时空建模。

* [ST-GCN](https://arxiv.org/pdf/1801.07455): Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition (AAAI 2018)
* [2s-AGCN](https://openaccess.thecvf.com/content_CVPR_2019/papers/Shi_Two-Stream_Adaptive_Graph_Convolutional_Networks_for_Skeleton-Based_Action_Recognition_CVPR_2019_paper.pdf): Two-Stream Adaptive Graph Convolutional Networks for Skeleton-Based Action Recognition (CVPR 2019)
* [MS-G3D](https://openaccess.thecvf.com/content_CVPR_2020/papers/Liu_Disentangling_and_Unifying_Graph_Convolutions_for_Skeleton-Based_Action_Recognition_CVPR_2020_paper.pdf): Disentangling and Unifying Graph Convolutions for Skeleton-Based Action Recognition (CVPR 2020)
* [CTR-GCN](https://arxiv.org/pdf/2107.12213): Channel-wise Topology Refinement Graph Convolution for Skeleton-Based Action Recognition (ICCV 2021)
* [PoseConv3D](https://openaccess.thecvf.com/content/CVPR2022/papers/Duan_Revisiting_Skeleton-Based_Action_Recognition_CVPR_2022_paper.pdf): Revisiting Skeleton-based Action Recognition (CVPR 2022)
* [MAC-Learning](https://ieeexplore.ieee.org/abstract/document/9954217): Multi-Granularity Anchor-Contrastive Representation Learning for Semi-Supervised Skeleton-Based Action Recognition (TPAMI 2022)
* [FR Head](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhou_Learning_Discriminative_Representations_for_Skeleton_Based_Action_Recognition_CVPR_2023_paper.pdf): Learning Discriminative Representations for Skeleton Based Action Recognition (CVPR 2023)
* [BlockGCN](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhou_BlockGCN_Redefine_Topology_Awareness_for_Skeleton-Based_Action_Recognition_CVPR_2024_paper.pdf): BlockGCN: Redefine Topology Awareness for Skeleton-Based Action Recognition (CVPR 2024)
* [PP-CDL](https://ieeexplore.ieee.org/abstract/document/11086379): Prompt-Guided Prototype-Aware Commonality and Discrimination Learning for Zero-Shot Skeleton-Based Action Recognition (TMM 2025)

**具身智能与行为理解 (Embodied AI & Action Understanding)**
> 具身智能旨在让AI智能体（如机器人）在物理或虚拟环境中，通过感知、理解并与环境交互来完成任务。在这个领域，行为理解不再是旁观者视角的被动分析，而是第一人称视角的主动学习。智能体需要理解视频中的人类行为，以便进行模仿学习，或者理解人类的指令来执行相应的物理操作。这使得行为理解与决策、规划和控制紧密结合。

* [Ego4D](https://arxiv.org/pdf/2110.07058): Ego4D: Around the World in 3,000 Hours of Egocentric Video (CVPR 2022)
* [VIMA](https://arxiv.org/pdf/2210.03094): VIMA: General Robot Manipulation with Multimodal Prompts (ICML 2023)
* [RT-2](https://arxiv.org/pdf/2307.15818): RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (CoRL 2023)
* [BSG](https://openaccess.thecvf.com/content/ICCV2023/papers/Liu_Birds-Eye-View_Scene_Graph_for_Vision-Language_Navigation_ICCV_2023_paper.pdf): Bird's-Eye-View Scene Graph for Vision-Language Navigation (ICCV 2023)
* [GPT4Ego](https://ieeexplore.ieee.org/abstract/document/10817586): NavGPT-2: Unleashing the Potential of Pre-Trained Models for Zero-Shot Egocentric Action Recognition (TMM 2024)
* [NavGPT-2](https://link.springer.com/chapter/10.1007/978-3-031-72667-5_15): NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models (ECCV 2024)
* [LHPR-VLN](https://openaccess.thecvf.com/content/CVPR2025/papers/Song_Towards_Long-Horizon_Vision-Language_Navigation_Platform_Benchmark_and_Method_CVPR_2025_paper.pdf): Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method (CVPR 2025)
* [OpenVLA](https://arxiv.org/abs/2406.09246): OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2025)
* [Hi Robot](https://arxiv.org/abs/2502.19417): Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models (ICML 2025)

***

## 三、结语与期望

怀揣着对未知的渴望，“新芽计划”愿做各位同学扬帆起航的港湾，助力你们在知识的海洋中茁壮成长。人体行为理解，一个连接通用人工智能未来与学术创新前沿的领域，既是挑战，更是机遇。我们衷心希望，本次专题学习不仅能让同学们领略AI的魅力，更能激发你们的内在潜能，在独立思考中碰撞灵感，在实践探索中提升技能，在解决难题中收获成长。期待你们在最终汇报中，以充满创见的解读，展现新芽学子的智慧与风采！