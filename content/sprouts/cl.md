---
title: 新芽专题介绍（26）：持续学习
date: 2025-09-17T01:25:00Z
draft: false
math: true
---



### 1.1  研究背景

在现代人工智能的发展中，深度学习模型展现了强大的表征与推理能力。然而，传统训练范式普遍假设**数据分布固定**，模型一次性学习完所有任务即可。这种静态模式在动态环境下难以适用。
在实际应用场景中，智能体往往需要**持续不断地接收新任务、新类别和新知识**，例如：智能助手需要理解不断扩展的指令库，自动驾驶系统需要适应不同天气和交通状况，医疗诊断模型需要逐步学习新的疾病类型。这种需求催生了一个关键方向——**持续学习（Continual Learning, CL）**，旨在让模型具备“像人一样不断学习”的能力。

在持续学习场景中，模型需要逐步接收一系列任务，并在学习新任务时**避免遗忘旧知识**。如何在**高效适配新知识**与**保持已有能力**之间找到平衡，成为推动智能体长期自主运行的关键环节。因此，持续学习已经成为机器学习领域的前沿研究方向。

---

### 1.2  研究意义

持续学习的提出，不仅是对人工智能模型“可扩展性”的需求，更是迈向\*\*通用人工智能（AGI）\*\*的重要一步。其研究价值主要体现在以下几个方面：

1. **现实需求**：

   * 面对动态环境（如无人驾驶、机器人、医疗诊断），模型无法一次性收集所有数据，而是需要随着时间逐步学习。

2. **科学价值**：

   * 持续学习为探索“机器是否能像人类一样具备长期学习与记忆能力”提供了研究窗口，推动对智能本质的理解。

3. **技术推动**：

   * 推动**灾难性遗忘抑制**、**知识迁移与共享**、**高效参数利用**等关键技术发展。
   * 促进模型在资源受限设备（边缘计算、嵌入式系统等）上的落地应用。

因此，持续学习不仅是一个重要的研究方向，也是人工智能跨越“实验室模型”到“长期应用系统”的必经之路，非常适合作为人工智能学习者进入科研的启蒙主题。



### 持续学习 vs. 常规训练

---
| 对比维度       | 常规训练（Conventional Training） | 持续学习（Continual Learning）    |
| ---------- | --------------------------- | --------------------------- |
| **数据获取方式** | 一次性获取完整数据集，数据分布固定           | 数据按时间序列逐步到达，分布不断变化          |
| **训练流程**   | 单次训练完成，模型固定                 | 多阶段持续训练，模型不断更新              |
| **任务场景**   | 单任务或多任务一次性学习                | 新任务持续到来，需动态适应               |
| **数据存储**   | 可无限保存所有训练数据                 | 历史数据有限存储或无法保存               |
| **计算环境**   | 假设资源充足、算力集中                 | 需在受限算力/存储下高效运行              |
| **目标**     | 在固定数据集上取得最优性能               | 在长期动态环境中保持**学习能力**和**已有知识** |
---

▲ 持续学习的特点。

---

### 1.3  当前主要挑战

尽管持续学习方向重要，但要实现真正的“不断学习”仍面临多重挑战：

1. **挑战一：灾难性遗忘（Catastrophic Forgetting）**

   * 模型在学习新任务时往往会严重丧失旧任务的能力。
   * 缺乏稳定的“记忆机制”，导致知识难以长期保存。

2. **挑战二：知识迁移与共享不足**

   * 新旧任务间的数据分布差异大，导致迁移学习困难。
   * 部分任务之间甚至存在冲突，模型容易“学了新的忘了旧的”。

3. **挑战三：计算与存储资源有限**

   * 真实应用中，数据量庞大但存储能力有限，不可能无限保留历史数据。
   * 持续学习算法需要在**有限算力与存储**条件下运行，如何做到参数高效成为瓶颈。

4. **挑战四：评估体系不完善**

   * 持续学习涉及动态过程，不同任务的相对重要性、时间顺序和数据条件不同，统一的评测基准仍在探索。

综上，持续学习既是人工智能走向真实场景应用的必然需求，又是深度学习亟需突破的核心难题。这一领域兼具理论价值与工程挑战，为科研训练与方法创新提供了极佳的切入点。


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

**接下来是论文的阅读，在所列的论文外，一个可供参考阅读更多论文的列表：**

* **[Awesome-Incremental-Learning](https://github.com/xialeiliu/Awesome-Incremental-Learning)**

***
### 2.2  基础文献（持续学习经典方法）

> 学生第一阶段的阅读训练，可帮助理解持续学习的基础方法和经典场景。**仅用于入门**


* **[Learning without Forgetting (ECCV 2016)](https://arxiv.org/pdf/1606.09282)**
* **[Overcoming Catastrophic Forgetting in Neural Networks (PNAS 2017)](https://arxiv.org/abs/1612.00796)**
* **[Continual Learning through Synaptic Intelligence (ICML 2017)](https://arxiv.org/abs/1703.04200)**
* **[Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference (ICLR 2019)](https://arxiv.org/abs/1810.11910)** 


* **[iCaRL: Incremental Classifier and Representation Learning (CVPR 2017)](https://arxiv.org/abs/1611.07725)** 
* **[Gradient Episodic Memory for Continual Learning (NeurIPS 2017)](https://arxiv.org/abs/1706.08840)**
* **[Experience Replay for Continual Learning (NeurIPS 2019)](https://arxiv.org/abs/1811.11682)**
* **[Dark Experience for General Continual Learning: a Strong, Simple Baseline (NeurIPS 2020)](https://arxiv.org/abs/2004.07211)**

* **[Learn to Grow: A Continual Structure Learning Framework (ICML 2019)](https://arxiv.org/abs/1904.00310)**
* **[Lifelong Learning with Dynamically Expandable Networks (ICLR 2018)](https://arxiv.org/abs/1708.01547)**
* **[DER: Dynamically Expandable Representation for Class Incremental Learning (CVPR 2021)](https://arxiv.org/abs/2103.16788)**



***

### 2.3  进阶文献（持续学习的前沿方向）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。以下不同方向为并行方向无顺序要求。


***
#### 2.3.1  经典分类持续学习
> 在学习新类别时，模型容易覆盖旧类别的表征，导致旧类别性能迅速下降。 特别是在类增量场景中，模型需要同时在所有已学类别上分类，遗忘问题比更严重。分类器作为瓶颈更新更加困难。

* **[L2P](https://arxiv.org/abs/2112.08654) Learning to Prompt for Continual Learning (CVPR 2022)**

* **[DyTox](https://arxiv.org/abs/2112.08654) DyTox: Transformers for Continual Learning with DYnamic TOken eXpansion (CVPR 2022)**

* **[SSRE](https://arxiv.org/abs/2203.06359) Self-Sustaining Representation Expansion for Non-Exemplar Class-Incremental Learning (CVPR 2022)**

* **[cassle](https://arxiv.org/abs/2112.04215) Self-Supervised Models are Continual Learners (CVPR 2022)**

* **[RanPAC](https://arxiv.org/pdf/2307.02251.pdf) RanPAC: Random Projections and Pre-trained Models for Continual Learning (NeurIPS 2023)**

* **[HiDe-Prompt](https://arxiv.org/abs/2310.07234) Hierarchical Decomposition of Prompt-Based Continual Learning: Rethinking Obscured Sub-optimality (NeurIPS 2023)**

* **[InfLoRA](https://arxiv.org/abs/2404.00228) InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning (CVPR 2024)**

* **[CoFiMA](https://arxiv.org/pdf/2312.08977) Weighted Ensemble Models Are Strong Continual Learners (ECCV 2024)**

* **[C-Flat](https://openreview.net/pdf/be179393fb5b55da27facef791300b7cea7f22b0.pdf) Make Continual Learning Stronger via C-Flat (NeurIPS 2024)**

#### 2.3.2  多模态持续学习
> 随着多模态预训练模型不断发展，多模态的持续学习也成为重要方向。不仅要避免单一模态的遗忘，还要维持模态间对齐关系。不同数据来源导致的异质性带来的不同遗忘问题和表现。

* **[ZSCL](https://arxiv.org/pdf/2303.06628.pdf) Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models (ICCV 2023)**

* **[RAPF](https://arxiv.org/abs/2407.14143) Class-Incremental Learning with CLIP: Adaptive Representation Adjustment and Parameter Fusion (ECCV24)**

* **[ViLCo](https://arxiv.org/pdf/2406.13123) ViLCo-Bench: VIdeo Language COntinual learning Benchmark (NeurIPS 2024)**

* **[MG-CLIP](https://arxiv.org/abs/2507.09118) Mind the Gap: Preserving and Compensating for the Modality Gap in CLIP-Based Continual Learning (ICCV 2025)**

* **[GMM](https://arxiv.org/abs/2403.18383.pdf) Generative Multi-modal Models are Good Class Incremental Learners (CVPR 2024)**

* **[HiDe-LLaVA](https://arxiv.org/abs/2503.12941) HiDe-LLaVA: Hierarchical Decoupling for Continual Instruction Tuning of Multimodal Large Language Model (ACL 2025)**

* **[Spurious Forgetting](https://link.springer.com/chapter/10.1007/978-3-031-72652-1_15) Spurious Forgetting in Continual Learning of Language Models (ICLR 2025) (ICLR 2025)**

* **[KG-GMM](https://arxiv.org/abs/2503.18403) Knowledge Graph Enhanced Generative Multi-modal Models for Class-Incremental Learning (NeruIPS 2025)**

* **[C-CLIP](https://openreview.net/forum?id=sb7qHFYwBc) C-CLIP: Multimodal Continual Learning for Vision-Language Model (ICLR 2025)**

#### 2.3.3  分割任务的持续学习
> 连续分割任务不仅需要应对持续训练过程中的灾难性遗忘和背景语义偏移，还面临新的挑战。例如，当静态图像数据扩展为视频流时，现有方法的性能往往急剧下降。如何有效克服这些问题，是未来亟待深入研究的重要方向。

* **[MiB](http://openaccess.thecvf.com/content_CVPR_2020/html/Cermelli_Modeling_the_Background_for_Incremental_Learning_in_Semantic_Segmentation_CVPR_2020_paper.html): Modeling the Background for Incremental Learning in Semantic Segmentation (CVPR 2020)**

* **[PLOP](https://openaccess.thecvf.com/content/CVPR2021/html/Douillard_PLOP_Learning_Without_Forgetting_for_Continual_Semantic_Segmentation_CVPR_2021_paper.html) : PLOP: Learning Without Forgetting for Continual Semantic Segmentation (CVPR 2021)**

* **[EWF](https://openaccess.thecvf.com/content/CVPR2023/html/Xiao_Endpoints_Weight_Fusion_for_Class_Incremental_Semantic_Segmentation_CVPR_2023_paper.html) Endpoints Weight Fusion for Class Incremental Semantic Segmentation (CVPR 2023)**

* **[ECLIPSE](https://arxiv.org/abs/2403.20126) ECLIPSE: Efficient Continual Learning in Panoptic Segmentation  with Visual Prompt Tuning (CVPR 2024)**

* **[NeST](https://link.springer.com/chapter/10.1007/978-3-031-73347-5_11) Early preparation pays off: New classifier pre-tuning for class incremental semantic segmentation (ECCV 2024)**

* **[Cs2k](https://link.springer.com/chapter/10.1007/978-3-031-72652-1_15) Cs2K: Class-Specific and Class-Shared Knowledge Guidance for Incremental Semantic Segmentation (ECCV 2024)**

* **[SimCIS](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Rethinking_Query-based_Transformer_for_Continual_Image_Segmentation_CVPR_2025_paper.html) Rethinking Query-based Transformer for Continual Image Segmentation (CVPR 2025)**

* **[FALCON](https://openaccess.thecvf.com/content/CVPR2025/html/Truong_FALCON_Fairness_Learning_via_Contrastive_Attention_Approach_to_Continual_Semantic_CVPR_2025_paper.html) FALCON: Fairness Learning via Contrastive Attention Approach to Continual Semantic Scene Understanding (CVPR 2025)**

* **[COMBO](https://openaccess.thecvf.com/content/CVPR2025/html/Fang_CoMBO_Conflict_Mitigation_via_Branched_Optimization_for_Class_Incremental_Segmentation_CVPR_2025_paper.html) CoMBO: Conflict Mitigation via Branched Optimization for Class Incremental Segmentation (CVPR 2025)**

#### 2.3.4  持续的生成、压缩、推荐、检测和大语言模型等方向
> 持续学习在多个方向展现出独特价值，对于模型的个性化有很大用途。这是一节拓展阅读。

* **[IMSR](https://cloudcatcher888.github.io/files/icde.pdf) Incremental Learning for Multi-Interest Sequential Recommendation (ICDE 2023)**

* **[INFER](https://ojs.aaai.org/index.php/AAAI/article/view/28790)  Influential Exemplar Replay for Incremental Learning in Recommender Systems (AAAI 2024)**

* **[L $^2$ DM](https://arxiv.org/pdf/2309.04430) Create Your World: Lifelong Text-to-Image Diffusion (TPAMI 2024)**

* **[C-C](https://arxiv.org/abs/2402.18862) Towards Backward-Compatible Continual Learning of Image Compression (CVPR2024)**

* **[LLaMA-MoE](https://arxiv.org/abs/2406.16554) LLaMA-MoE: Building Mixture-of-Experts from LLaMA with Continual Pre-training (EMNLP 2024)**

* **[DuET](https://arxiv.org/pdf/2506.21260) DuET: Dual Incremental Object Detection via Exemplar-Free Task Arithmetic (ICCV 2025)**

* **[NSE](https://aclanthology.org/2025.acl-long.815.pdf) Neuron-Level Sequential Editing for Large Language Models (ACL 2025)**

* **[RLEdit](https://arxiv.org/pdf/2502.05759) Reinforced Lifelong Editing for Language Models (ICML 2025)**

* **[RePRE](https://arxiv.org/pdf/2502.05540) Demystifying Catastrophic Forgetting in Two-Stage Incremental Object Detector (ICML 2025)**

* **[ASAL](https://arxiv.org/abs/2502.19644) Adaptive Score Alignment Learning for Continual Perceptual Quality Assessment of 360-Degree Videos in Virtual Reality (VR-TVCG 2025)**

## 三、结语与期望

新芽计划”的初心，是引领同学们走向科研的第一步，去感受未知领域的魅力与挑战。持续学习作为人工智能的关键问题，不仅关乎模型如何像人类一样不断学习新知识，更是未来智能系统走向真正自主进化的必由之路。

希望通过这个专题，同学们能够深入理解持续学习的本质困难，掌握应对遗忘与适应的核心方法，逐步培养出面向未来智能系统的科研眼光和创新思维。

我们热切期待，在最终的汇报中，能看到大家以独立的视角，呈现出对持续学习问题的深刻思考与独到见解，让思想的火花照亮科研探索的道路！