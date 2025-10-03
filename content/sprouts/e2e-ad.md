---
title: 新芽专题介绍：端到端自动驾驶
date: 2025-09-17T01:19:00Z
draft: false
math: true
authors: 
---

<!-- > 此专题由非南开大学老师发布，选修南开大学 2025 秋《人工智能实践课-初级》课程的同学请勿选择此专题。非本课程选修同学可自由选择。 -->

> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。

## 一、专题介绍

### 1.1  研究背景

在现代军事与国防体系中，自动驾驶技术已成为推动智能化作战与无人化装备发展的核心支撑。依托先进的传感器、人工智能算法与高性能计算平台，自动驾驶能够在复杂、动态和高风险的战场环境中，实现无人平台的**自主感知、智能决策与稳定控制**。这不仅显著降低了人员伤亡风险，还极大提升了作战单元的机动性与执行效率。例如，在前沿侦察、后勤运输、危险区域补给以及高强度对抗场景中，具备自动驾驶能力的无人地面车辆、无人水下航行器和无人机集群，能够有效增强部队的战场覆盖能力和作战灵活性。

特别值得关注的是，**端到端自动驾驶**在现代军事和国防系统中展现出巨大的潜力。与传统的模块化方法不同，端到端架构通过统一的深度学习模型直接将多模态感知输入映射为控制指令或长时序轨迹，能够在信息受限、通信中断或干扰严重的条件下保持鲁棒性与实时性。其优势主要体现在以下几个方面：一是能够通过**长时序轨迹预测**实现对敌对威胁的规避与对复杂任务的提前规划；二是具备**多模态信息融合**能力，可在视觉受限或雷达干扰等极端条件下保持感知稳定；三是支持**分布式智能体的协同决策**，使无人作战单元能够在缺乏集中指挥的情况下仍然保持高效配合。

因此，端到端自动驾驶不仅是无人化装备智能化发展的前沿方向，更是实现未来战场“**无人作战、智能协同、快速反应**”的关键技术支撑，已成为各国国防科研机构与军工集团重点布局的战略领域。



### 1.2  研究意义

端到端自动驾驶是指通过深度学习模型将多模态传感器输入直接映射为车辆的**决策与控制输出**，省去传统模块化感知—预测—规划—控制链条中的繁杂接口。在这一模式下，系统能够**端到端学习驾驶策略**，从而在复杂交通环境中实现更高效、更鲁棒的智能驾驶。其研究意义主要体现在：

1. **军事与国防**：支持无人作战平台在战场上实现自主导航、规避威胁与协同作战，提升作战效能与生存能力。

2. **民用与社会**：推动智能交通与自动驾驶商业化落地，缓解交通压力，减少交通事故，提升出行效率与安全性。

3. **技术驱动**：促进多模态感知融合、长时序轨迹预测、强化学习与世界模型等前沿技术的发展，加速人工智能在真实物理环境中的应用探索。

因此，端到端自动驾驶不仅在军事与社会领域具有深远价值，同时也是人工智能、控制理论与自动化领域的前沿交叉课题，非常适合作为科研入门与高水平研究的关键方向。


### 1.3  当前主要挑战

尽管方向重要，但实现端到端自动驾驶仍然面临多重挑战：

1. **安全与可靠性**：在真实交通或战场环境中，极端天气、突发状况与未知场景都会导致模型的不确定性，如何保证系统在高风险条件下的稳定决策仍是难题。

2. **数据与泛化**：端到端模型高度依赖大规模多样化数据，但实际环境分布往往与训练数据存在偏差，如何提升跨域泛化能力和对未知情况的适应性是亟需解决的问题。

3. **可解释性与验证**：深度神经网络作为黑箱模型难以直观解释，缺乏系统化的安全验证手段，这对军事与民用场景下的部署均构成严峻挑战。

4. **实时性与算力**：端到端决策需要融合多模态感知信息并进行长时序推理，既要求高精度，又必须满足低延迟与轻量化部署，对算法设计和硬件平台均提出了更高要求。



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

> 学生第一阶段的阅读训练，可帮助理解目标检测/语义分割/关键点检测这一通用方向。

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

* **[Deformable DETR](https://arxiv.org/pdf/2010.04159): Deformable Transformers for End-to-End Object Detection (ICLR 2021)**

***


### 2.3 入门文献（端到端方法的综述）

> 学生第一阶段的**综述**阅读训练，可帮助理解端到端自动驾驶这一通用方向。

* **[Survey 1](https://arxiv.org/pdf/2307.04370): Recent Advancements in End-to-End Autonomous Driving using Deep Learning: A Survey (TIV 2024）**

* **[Survey 2](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10614862): End-to-End Autonomous Driving: Challenges and Frontiers (TPAMI 2024)**

***
### 2.4  入门数据集（端到端自驾经典数据集）

> 学生第二阶段需要熟悉的**数据集**，需要系统的学习评测指标以及数据集使用。

* **[NuScenes(必须掌握)](https://openaccess.thecvf.com/content_CVPR_2020/papers/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.pdf): nuScenes: A multimodal dataset for autonomous driving (CVPR 2020）**

* **[Bench2Drive(必须掌握)](https://proceedings.neurips.cc/paper_files/paper/2024/file/017761f94a1cd66d01c041aff85492c4-Paper-Datasets_and_Benchmarks_Track.pdf): Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving (TPAMI 2024)**

* **[NAVSIM(可选)](https://proceedings.neurips.cc/paper_files/paper/2024/file/017761f94a1cd66d01c041aff85492c4-Paper-Datasets_and_Benchmarks_Track.pdf): NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking (NIPS 2024)**

***

### 2.5  进阶文献（端到端经典方法）

> 学生可在此部分选择经典文献进行专题汇报。

* **[Uniad](https://openaccess.thecvf.com/content/CVPR2023/papers/Hu_Planning-Oriented_Autonomous_Driving_CVPR_2023_paper.pdf): Planning-oriented Autonomous Driving (CVPR 2022)**

* **[Think2Twice](https://arxiv.org/pdf/2010.04159): Think Twice before Driving:Towards Scalable Decoders for End-to-End Autonomous Driving (CVPR 2023)**

* **[SparseDrive](https://ieeexplore.ieee.org/abstract/document/11128800/): Sparsedrive: End-to-end autonomous driving via sparse scene representation (ICRA 2024)**

* **[MomAD](https://arxiv.org/abs/2503.03125): Don't Shake the Wheel: Momentum-Aware Planning in End-to-End Autonomous Driving (CVPR 2025)**

* **[ISEGO](http://openaccess.thecvf.com/content/CVPR2024/html/Li_Is_Ego_Status_All_You_Need_for_Open-Loop_End-to-End_Autonomous_CVPR_2024_paper.html): Is ego status all you need for open-loop end-to-end autonomous driving (CVPR 2024)**

* **[VAD](http://openaccess.thecvf.com/content/ICCV2023/html/Jiang_VAD_Vectorized_Scene_Representation_for_Efficient_Autonomous_Driving_ICCV_2023_paper.html): Vad: Vectorized scene representation for efficient autonomous driving (CVPR 2023)**

* **[GenAD](https://link.springer.com/chapter/10.1007/978-3-031-73650-6_6) Genad: Generative end-to-end autonomous driving(ECCV 2024)**

* **[Transfuser](http://openaccess.thecvf.com/content/CVPR2021/html/Prakash_Multi-Modal_Fusion_Transformer_for_End-to-End_Autonomous_Driving_CVPR_2021_paper.html): Multi-modal fusion transformer for end-to-end autonomous driving (CVPR 2021)**

* **[St-p3](https://link.springer.com/chapter/10.1007/978-3-031-19839-7_31): St-p3: End-to-end vision-based autonomous driving via spatial-temporal feature learning (ECCV 2022)**

* [EMMA](https://arxiv.org/abs/2410.23262): Emma: End-to-end multimodal model for autonomous drivin (ARXIV 2024)

* [Driveadapter](http://openaccess.thecvf.com/content/ICCV2023/html/Jia_DriveAdapter_Breaking_the_Coupling_Barrier_of_Perception_and_Planning_in_ICCV_2023_paper.html) Driveadapter: Breaking the coupling barrier of perception and planning in end-to-end autonomous driving

* [Vadv2](https://arxiv.org/abs/2402.13243) Vadv2: End-to-end vectorized autonomous driving via probabilistic planning(ICLR 2022)

* [Para-drive](http://openaccess.thecvf.com/content/CVPR2024/html/Weng_PARA-Drive_Parallelized_Architecture_for_Real-time_Autonomous_Driving_CVPR_2024_paper.html): Para-drive: Parallelized architecture for real-time autonomous driving (CVPR 2024)

* [Fusionad](https://arxiv.org/abs/2308.01006) Fusionad: Multi-modality fusion for prediction and planning tasks of autonomous driving

* [Driving into the future](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Driving_into_the_Future_Multiview_Visual_Forecasting_and_Planning_with_CVPR_2024_paper.html) Driving into the future: Multiview visual forecasting and planning with world model for autonomous driving (CVPR 2024)

***

### 2.6  业内前沿文献

> 结合本专题的研究背景，逐渐引导学生进入端到端自动驾驶的最新前沿。

**生成模型**

1. **[Diffusiondrive](https://arxiv.org/pdf/2106.00487)：Diffusiondrive: Truncated diffusion model for end-to-end autonomous driving（CVPR 2025）**

2. **[GoalFlow](http://openaccess.thecvf.com/content/CVPR2025/html/Xing_GoalFlow_Goal-Driven_Flow_Matching_for_Multimodal_Trajectories_Generation_in_End-to-End_CVPR_2025_paper.html)：Goalflow: Goal-driven flow matching for multimodal trajectories generation in end-to-end autonomous driving（CVPR 2025）**

3. **[DiffAD](https://arxiv.org/pdf/2503.12170) DiffAD: A Unified Diffusion Modeling Approach for Autonomous Driving（CVPR 2024）**

4. [DiffE2E](https://arxiv.org/abs/2505.19516) DiffE2E: Rethinking End-to-End Driving with a Hybrid Action Diffusion and Supervised Policy 

5. **[TransDiffuser](https://arxiv.org/pdf/2505.09315?) TransDiffuser: Diverse Trajectory Generation with Decorrelated Multi-modal Representation for End-to-end Autonomous Driving**


**Vision Language Action Model**

1. **[Covla](https://ieeexplore.ieee.org/abstract/document/10944039/) Covla: Comprehensive vision-language-action dataset for autonomous driving（CVPR 2025）**

2. **[AutoDrive-R](https://arxiv.org/pdf/2509.01944)：AutoDrive-R: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving（Arxiv 2025）**

3. **[AutoDrive-R](https://arxiv.org/abs/2506.05667)：DriveAction: A Benchmark for Exploring Human-like Driving Decisions in VLA Models（Arxiv 2025）**
4. **[Diffvla](https://arxiv.org/abs/2505.19381): Vision-language guided diffusion planning for autonomous driving（Arxiv 2025）**
5. **[Opendrivevla](https://arxiv.org/abs/2503.23463): Opendrivevla: Towards end-to-end autonomous driving with large vision language action model（Arxiv 2025）**
6. **[AutoVLA](https://arxiv.org/abs/2506.13757) AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning（Arxiv 2025）**
7. **[Impromptu VLA](https://arxiv.org/abs/2505.23757): Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models（Arxiv 2025）**
8. **[FastDriveVLA](https://arxiv.org/abs/2507.23318): FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning（Arxiv 2025）**
9. **[UPVLA](https://arxiv.org/abs/2507.23540): A Unified Perception-Language-Action Framework for Adaptive Autonomous Driving（Arxiv 2025）**
10. **[IRL-VLA](https://arxiv.org/abs/2508.06571): IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model（Arxiv 2025）**
11. **[AdaThinkDrive](https://arxiv.org/abs/2509.13769): AdaThinkDrive: Adaptive Thinking via Reinforcement Learning for Autonomous Driving（Arxiv 2025）**
12. **[TA-VLA](https://arxiv.org/abs/2509.07962): TA-VLA: Elucidating the Design Space of Torque-aware Vision-Language-Action Models（Arxiv 2025）**
13. **[OmniReason](https://arxiv.org/abs/2509.00789): OmniReason: A Temporal-Guided Vision-Language-Action Framework for Autonomous Driving（Arxiv 2025）**
14. **[Alphadrive](https://arxiv.org/abs/2503.07608): Alphadrive: Unleashing the power of vlms in autonomous driving via reinforcement learning and reasoning（Arxiv 2025）**


***

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。红外弱小目标检测是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
