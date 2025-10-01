---
title: 新芽专题介绍（25）：目标轨迹预测
date: 2025-09-17T01:26:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1  研究背景
“轨迹预测”旨在依据历史状态与环境约束，推断行人、车辆、船舶、飞行器等未来一段时间的位置/速度序列，是自动驾驶安全决策、群体行为理解、海事交通管控与空管四维航迹（4D Trajectory）等系统的关键环节。近年，向多智能体交互、矢量化地图表示、Transformer/扩散模型与语言/视觉-语言模型融合加速演进，形成系统性的任务管线与评测生态。最新综述对预测任务的输入/输出模态、特征建模与范式作了系统梳理，并讨论与大模型结合的趋势。

***

### 1.2  研究意义

“轨迹预测”指在给定历史运动与环境信息的条件下，提前推断行人、车辆、船舶、飞行器等对象未来一段时间的位置和速度变化。它看似只是**往前多看几秒，却直接关系到**:

1. **安全与决策**：为自动驾驶、无人机与机器人提供提前量，及时避让、减速或变道，降低碰撞与连锁风险；在人群疏导、公共安全场景中，帮助预判拥堵与异常行为。

2. **管控与运营**：在空管与航运中提升到达时间预测（ETA）与冲突检测能力；在城市交通中辅助信号控制与路径规划；在物流与仓储中优化调度与成本。

2. **技术推动**：倒逼多智能体交互建模、时空序列学习、概率不确定性与校准、闭环评测与高效推理等关键技术发展，并促进与地图先验、传感融合以及大模型的深度结合与落地。

***

### 1.3  当前主要挑战

尽管方向重要，但要把轨迹预测做**准、稳、快**，仍然面临这些现实难题：

1. **挑战一：未来不止一条：多模态、不确定**

   * 同样的历史轨迹，可能出现多种“合理的未来”（比如直行、变道、刹停），如何选择。

   * 模型容易只学到最常见的一条，忽略其他安全可行的可能性。

2. **挑战二：彼此会影响：多智能体交互很复杂**

   * 人与人、车与车会让行、别车、结伴、博弈，不是独立运动，而是相互联系。

   * 如何既抓住关键互动，又不把模型做得笨重，是难点。

3. **挑战三：地图很香，也会“绑架”模型：场景与先验依赖**

   * 有高清地图时容易“过度依赖”，换城市/国家/施工路段就掉分。

   * 没地图（如船舶/航空/室内）又缺先验，更考验动力学与环境建模。

4. **挑战四：要看得远，还要稳：长时预测与稀有事件**

   * 预测时间一长，误差会像滚雪球一样迅速累积。

   * 危险工况、极端动作样本很少，模型往往学不会、猜不准。

5. **挑战五：更要靠谱：概率与鲁棒校准**

   * 面对传感缺失、定位抖动、雨夜眩光、遮挡等扰动，如何保持稳健。
   
   * 预测不仅要“给位置”，还要给置信度，且要校准（别过度自信或过度保守）。

***

## 二、学习资料与参考文献

建议“边做边学”：先用简洁基线跑通，再逐步引入稳像、异方差预测、动作多任务学习与物理先验.

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

* [MotionCNN on WOMD](https://github.com/stepankonev/MotionCNN-Waymo-Open-Motion-Dataset?utm_source=chatgpt.com): （强基线、数据管线清晰）

Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2 入门综述/全景导航

* [Survey](https://arxiv.org/abs/2503.03262): Trajectory Prediction for Autonomous Driving: Progress, Limitations, and Future Directions (arXiv 2025)

* [Survey](https://arxiv.org/abs/2506.03408): Trajectory Prediction Meets Large Language Models: A Survey (arXiv 2025)

* [Survey](https://arxiv.org/abs/2402.01397): A survey on robustness in trajectory prediction for autonomous vehicles(arXiv 2024)

***

### 2.3  经典入门论文（轨迹预测经典方法）

>快速把握任务定义、主流范式、数据与评测全貌，建立术语与认知框架，为后续复现与阅读奠定基础。

* [Social LSTM](https://cvgl.stanford.edu/papers/CVPR16_Social_LSTM.pdf?utm_source=chatgpt.com): Social LSTM: HumanTrajectory Prediction in Crowded Spaces (CVPR 2016)

* [Social GAN](https://arxiv.org/pdf/1803.10892): Social GAN: Socially Acceptable Trajectories with Generative Adversarial Networks (CVPR 2018)

* [SoPhie](https://arxiv.org/pdf/1806.01482): SoPhie: An Attentive GAN for Predicting Paths Compliant to Social and Physical Constraintsn (CVPR 2019)

* [PECNet](https://arxiv.org/pdf/2004.02025): It is not the Journey but the Destination: Endpoint Conditioned Trajectory Prediction (ECCV 2020)

* [Trajectron++](https://arxiv.org/pdf/2001.03093): Trajectron++: Dynamically-Feasible Trajectory Forecasting With Heterogeneous Data (ECCV 2020)

* [ISA](https://arxiv.org/pdf/2105.03136): Interpretable Social Anchors for Human Trajectory Forecasting in Crowds (CVPR 2021)

* [TrajNet++](https://arxiv.org/pdf/2007.03639): Human Trajectory Forecasting in Crowds: A Deep Learning Perspective (TPAMI 2022)

***

### 2.4  无车道/无地图/无交互”场景(船舶 & 航空)

>船/航任务弱地图先验、强动力学与环境约束，能锻炼纯时间序列与动力学先验结合的建模能力，是上手的良好补充方向。


* [TrAISformer](https://arxiv.org/pdf/2108.10015): A Transformer-based Model for Vessel Trajectory Prediction (arXiv 2021) 

* [PECNet](https://arxiv.org/pdf/2310.18948): Multi-Path Long-Term Vessel Trajectories Forecasting with Probabilistic Feature Fusion for Problem Shifting (arXiv 2024)

* [AIS](https://arxiv.org/pdf/2505.07374): AIS Data-Driven Maritime Monitoring Based on Transformer: A Comprehensive Review (arXiv 2025)

* [PECNet](https://arxiv.org/pdf/2506.12029): Physics-Informed Neural Networks for Vessel Trajectory Prediction: Learning Time-Discretized Kinematic Dynamics via Finite Differences (arXiv 2025)

* [PECNet](https://arxiv.org/pdf/2505.00599): Visual Trajectory Prediction of Vessels for Inland Navigation (arXiv 2025)

***

### 2.5  地图/环境交互场景（自动驾驶 & 行人）

>学强地图与矢量表示，掌握车道/交规先验/行人避让融合与工业级评测流程，体会性能与泛化之间的取舍。

* [DenseTNT](https://arxiv.org/pdf/2108.09640): End-to-end Trajectory Prediction from Dense Goal Sets (ICCV 2021)

* [MTR](https://arxiv.org/pdf/2207.05844): Motion Forecasting via Simple & Efficient Attention Networks (arXiv 2022)

* [MTR++](https://arxiv.org/pdf/2307.14187): Multi-Agent Motion Prediction with Symmetric Scene Modeling and Guided Intention Querying (TPAMI 2024)

* [ADAPT](https://arxiv.org/pdf/2307.14187): ADAPT: Efficient Multi-Agent Trajectory Prediction with Adaptation (ICCV 2023)

* [STR](https://arxiv.org/pdf/2310.19620): Large Trajectory Models are Scalable Motion Predictors and Planners (arXiv 2023)

* [EqDrive](https://arxiv.org/pdf/2310.17540): EqDrive:Efficient Equivariant Motion Forecasting with Multi-Modality for Autonomous Driving (arXiv 2023)

* [ControlMTR](https://arxiv.org/pdf/2404.10295): Control-Guided Motion Transformer with Scene-Compliant Intention Points for Feasible Motion Prediction (arXiv 2024)

* [PPT](https://arxiv.org/pdf/2407.11588): Progressive Pretext Task Learning for Human Trajectory Prediction (ECCV 2024)

* [IA-LSTM](https://arxiv.org/pdf/2311.15193): Interaction-Aware LSTM for Pedestrian Trajectory Prediction ( IEEE-TC 2024)

* [RealMotion](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ec078518dcce6be1324cfd3de11ed24-Paper-Conference.pdf?utm_source=chatgpt.com): Motion Forecasting in Continuous Driving (NeurIPS 2024)

* [DenseTNT](https://arxiv.org/pdf/2405.01266): MFTraj:Map-Free, Behavior-Driven Trajectory Prediction for Autonomous Driving (IJCAI 2024)

* [Co-mtp](https://arxiv.org/pdf/2502.16589): Co-MTP:A Cooperative Trajectory Prediction Framework with Multi-Temporal Fusion for Autonomous Driving (ICRA 2025)

* [DSTIGCN](https://ieeexplore.ieee.org/abstract/document/10843981): Deformable Spatial-Temporal Interaction Graph Convolution Network for Pedestrian Trajectory Prediction( IEEE-TITS 2025)

* [IGGCN](https://www.sciencedirect.com/science/article/abs/pii/S105120042400486X): Individual-guided graph convolution network for pedestrian trajectory prediction ( Digital Signal Processing 2025)

***

### 2.6  生成式/扩散与大模型趋势（多模态、多代理）

>了解扩散与LLM/VLM融合的思路与利弊，提升多样性、可控性与知识注入能力，探索面向落地的生成范式。

* [MID](https://arxiv.org/pdf/2203.13777): Stochastic Trajectory Prediction via Motion Indeterminacy Diffusion (CVPR 2022)

* [LED](https://arxiv.org/pdf/2303.10895): Leapfrog Diffusion Model for Stochastic Trajectory Prediction (CVPR 2023)

* [MotionDiffuser](https://arxiv.org/pdf/2306.03083): MotionDiffuser:Controllable Multi-Agent Motion Prediction using Diffusion (CVPR 2023).

* [MotionLM](https://arxiv.org/pdf/2309.16534): MotionLM:Multi-Agent Motion Forecasting as Language Modeling (ICCV 2023)

* [SceneDM](https://arxiv.org/pdf/2311.15736): SceneDM:Scene-level Multi-agent Trajectory Generation with Consistent Diffusion Models (arXiv 2023)

* [SMART](https://arxiv.org/pdf/2405.15677): SMART:Scalable Multi-agent Real-time Motion Generation via Next-token Prediction (NeurIPS 2024)

* [UniTraj](https://arxiv.org/pdf/2405.17680): A Unified Trajectory Generation Model for Multi-Scenario Sports Analytics (arXiv 2024)

* [Diffusion Planner](https://arxiv.org/pdf/2501.15564): Diffusion-Based Planning for Autonomous Driving with Flexible Guidance (ICLR 2025)

* [U2Diff](https://arxiv.org/pdf/2503.18589): Unified Uncertainty-Aware Diffusion for Multi-Agent Trajectory Modeling (CVPR 2025)

***

## 三、结语与期望

“新芽计划”的初衷，是点燃新芽学子对未知的好奇心，并为成长提供一片可实践、可复现的沃土。轨迹预测既服务于自动驾驶、机器人与智慧交通等国家与产业需求，也是多智能体交互、时空建模与不确定性学习的学术前沿，充满挑战与机会。