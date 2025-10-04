---
title: 新芽专题介绍：AI对抗攻击与防御
date: 2025-09-17T01:07:00Z
draft: false
math: true
---

> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。

## 一、专题介绍

### 1.1  研究背景

随着大模型的发展，人们已经清晰地认识到人工智能会在生活的各个方面发挥重要作用，例如自动驾驶，医疗诊断，工业制造，娱乐服务等。然而，当将AI模型应用于真实世界时，开发者和使用者都会有疑问：部署的AI模型是否足够可靠，是否会在某些情况下失效而造成不可估量的损失，例如自动驾驶可能会造成人员伤亡。AI对抗攻击与防御就是在此背景下形成的相对新颖的研究方向，属于人工智能安全的核心和重点之一。AI对抗攻击与防御的核心目的是：
1. **发现AI模型在潜在部署环境中的脆弱性：** 在AI模型真实部署之前，通过对抗攻击生成对抗样本来误导AI模型，从而主动挖掘AI模型难以处理，例如识别失败，但是真实世界中可能出现的样本（人为恶意或自然存在）。
2. **主动提升AI模型的可靠性和安全性：** AI对抗防御是指通过模型更新或数据净化能有效地抵抗输入的对抗样本而不出现错误。

### 1.2  研究意义

研究AI对抗攻击与防御，在AI模型部署和能力提升方面都有重要意义：

1. **AI模型鲁棒性评估：** 区别于传统的基于标准数据集的评估方法，AI对抗攻击提供了主动式的评估方式，其本质是挖掘困难且可能出现的样本使的AI模型失败。对于一个AI模型，越难发现对抗样本表示其越鲁棒。

2. **AI模型可靠和安全性提升：**利用找到的对抗样本，可以指导模型提升其可靠性和安全性，避免在类似的样本上出现错误。

3. **AI模型的可解释性：** 通过对抗样本，能够探索AI模型是如何实现准确预测的，以及为什么在某些情况下会失败。

4. **互为对手，交互提升：**对抗攻击与防御是一个问题的两个相反面，通过各自提升，最终推进AI模型实现高可靠和高安全性。

区别于传统研究方向关注于AI模型的功能性创新，这一研究主题往往另辟蹊径，提供了新的研究思路和思维方式，非常适合作为本科生进入科研领域的创新启蒙训练。

▲一个典型的对抗攻击场景：人脸识别，光照影响大，哪个光照条件影响最大？

### 1.3  当前主要挑战

尽管方向重要，但实现AI对抗攻击与防御仍然面临多重挑战：

1. **挑战一：对抗攻击需满足自然性和攻击性两个矛盾的性质**

  - 对抗攻击目标生成自然的对抗样本，例如微小加性噪声，真实可能出现的自然干扰包括模糊、光照、光晕等。
  
  - 对抗攻击目标是能误导AI模型，这往往要求对抗样本有较大的扰动，从而能显著降低目标模型的性能。
  
  - 上述两个目标形成了相互矛盾的两个方面。
  
2. **挑战二：对抗样本在跨模型攻击的时候攻击能力急剧下降**
  - 同一任务可以通过不同训练数据或不同模型架构来实现。
  
  - 对一个模型生成的对抗样本在其他模型上有效性降低。
  
  - 对抗样本的低迁移能力极大影响了对抗攻击的实用意义。
  
3. **挑战三：对抗防御会降低模型在干净数据的精度也需要额外的计算开销**

  - 对抗训练通过对抗样本提升模型的对抗鲁棒性，也会影响模型在干净数据上的精度。
  
  - 通过数据净化实现模型鲁棒性提升，也会造成模型推理阶段计算耗时提升。
  
  - 如何提升模型对抗鲁棒性同时，维持干净数据上的精度和推理效率，是个极具挑战的任务。
  
综上，随着大模型的发展，对抗攻击与防御技术仍在探索突破阶段，可以将其扩展到所有AI相关领域，这是一个很好的学习窗口：既能接触实际需求，又能跟随前沿研究。

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

如果你学有余力，可以尝试下列进阶的专题教程：
* 计算机视觉：斯坦福 CS231n —— Deep Learning for Computer Vision*
* 自然语言处理：斯坦福 CS224N —— Natural Language Processing with Deep Learning*
* 生成式学习：斯坦福 CS236 —— Deep Generative Models*
* 大语言模型：李宏毅 —— 《Machine Learning》课程，以及斯坦福 CS324 —— Large Language Models *

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

***

### 2.3  进阶文献（目标检测前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报。


  下面这篇论文首次提出了对抗攻击和防御这一课题，揭示了神经网络天然地容易被干扰的特性：

- [Intriguing properties of neural networks](https://arxiv.org/pdf/1312.6199)

  当然，你还可以通过阅读经典的survey来了解对抗攻击与防御：

- [Adversarial Machine Learning at Scale](https://arxiv.org/pdf/1611.01236)
- [Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey](https://arxiv.org/pdf/1801.00553)

  接下来的论文提出了领域内最为经典，被广泛应用的攻击方法：

- [FGSM: Explaining and Harnessing Adversarial Examples ](https://arxiv.org/pdf/1412.6572)
- [I-FGSM: ](https://arxiv.org/pdf/1607.02533)[Adversarial Examples in the Physical World](https://arxiv.org/pdf/1607.02533)
- [PGD: ](https://arxiv.org/pdf/1706.06083)[Towards Deep Learning Models Resistant to Adversarial Attacks](https://arxiv.org/pdf/1706.06083)
- [C&W: Towards Evaluating the Robustness of Neural Networks](https://arxiv.org/pdf/1608.04644)
- [JSMA: The Limitations of Deep Learning in Adversarial Settings](https://arxiv.org/pdf/1511.07528)
- [Practical Black-Box Attacks against Deep Learning Systems](https://arxiv.org/pdf/1602.02697)
- [ZOO: Zeroth Order Optimization Based Black-box Attacks](https://arxiv.org/pdf/1708.03999)

  相对应的，下面的论文提出了早期的防御方法：

- [Towards Deep Learning Models Resistant to Adversarial Attacks](https://arxiv.org/pdf/1706.06083)
- [Ensemble Adversarial Training: Attacks and Defenses](https://arxiv.org/abs/1705.07204)
- [Distillation as a Defense to Adversarial Perturbations](https://arxiv.org/pdf/1511.04508)
- [Certified Robustness to Adversarial Examples with Differential Privacy](https://arxiv.org/pdf/1802.03471)
- [Provable Defenses against Adversarial Examples via the Convex Outer Adversarial Polytope](https://arxiv.org/pdf/1711.00851)
- [Certified Adversarial Robustness via Randomized Smoothing](https://arxiv.org/pdf/1902.02918)

***

### 2.3 进阶文献（前沿方法）

  *学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。*

  前沿对抗攻击研究：

- [Towards Practical Deployment-Stage Backdoor Attack on Deep Neural Networks](https://openaccess.thecvf.com/content/CVPR2022/papers/Qi_Towards_Practical_Deployment-Stage_Backdoor_Attack_on_Deep_Neural_Networks_CVPR_2022_paper.pdf)
- [AdvDiff: Generating Unrestricted Adversarial Examples using Diffusion Models](https://arxiv.org/pdf/2307.12499)
- [Magic: Mastering physical adversarial generation in context through collaborative llm agents](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=MgdM9n0AAAAJ&citation_for_view=MgdM9n0AAAAJ:zYLM7Y9cAGgC)
- [DepthVanish: Optimizing Adversarial Interval Structures for Stereo-Depth-Invisible Patches](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=MgdM9n0AAAAJ&citation_for_view=MgdM9n0AAAAJ:Tyk-4Ss8FVUC)
- [Coljailbreak: Collaborative generation and editing for jailbreaking text-to-image deep generation](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Rj2x4QUAAAAJ&sortby=pubdate&citation_for_view=Rj2x4QUAAAAJ:WbkHhVStYXYC)

  前沿对抗防御研究

- [Fast Adversarial Training with Adaptive Step Size](https://arxiv.org/pdf/2206.02417)
- [Adversarial Masking for Self-Supervised Learning](https://arxiv.org/pdf/2201.13100)
- [Raising the Bar for Certified Adversarial Robustness with Diffusion Models](https://arxiv.org/pdf/2305.10388)
- [Guided Diffusion Model for Adversarial Purification](https://arxiv.org/pdf/2205.14969)
- [IRAD: Implicit Representation-driven Image Resampling against Adversarial Attacks](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Rj2x4QUAAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=Rj2x4QUAAAAJ:cFHS6HbyZ2cC)

  <a name="heading_8"></a>**2.4 大模型对抗攻击与防御领域相关文献**

  *结合本专题的研究背景，逐渐引导学生进入前沿大模型对抗攻击与防御。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。*

  **通用大模型对抗攻击与防御**

- [Scenetap: Scene-coherent typographic adversarial planner against vision-language models in real-world environments](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Rj2x4QUAAAAJ&sortby=pubdate&citation_for_view=Rj2x4QUAAAAJ:08ZZubdj9fEC)
- [Semantic-aligned adversarial evolution triangle for high-transferability vision-language attack](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Rj2x4QUAAAAJ&sortby=pubdate&citation_for_view=Rj2x4QUAAAAJ:5Ul4iDaHHb8C)
- [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/pdf/2307.15043)
- [Jailbreaking Black Box Large Language Models in Twenty Queries](https://arxiv.org/pdf/2310.08419)
- [A Watermark for Large Language Models](https://arxiv.org/pdf/2301.10226)
- [Visual Adversarial Examples Jailbreak Aligned Large Language Models](https://arxiv.org/pdf/2306.13213)

  **具身大模型对抗攻击与防御**

- [Towards transferable attacks against vision-llms in autonomous driving with typography](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Rj2x4QUAAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=Rj2x4QUAAAAJ:f2IySw72cVMC)
- [Advgps: Adversarial gps for multi-agent perception attack](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Rj2x4QUAAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=Rj2x4QUAAAAJ:yD5IFk8b50cC)
- [Everyday Object Meets Vision-and-Language Navigation Agent via Backdoor](https://proceedings.neurips.cc/paper_files/paper/2024/file/58e6c003c9fb3992265005ff6aef1913-Paper-Conference.pdf) 
- [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/pdf/2411.13587)
- [Jailbreaking LLM-controlled Robots](https://arxiv.org/pdf/2410.13691)

***

## 三、结语与期望


  “新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。对抗攻击与防御是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

  我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
