---
title: 新芽专题介绍（7）：智能软件漏洞挖掘
date: 2025-09-07
draft: false
math: true
authors:
- admin
---

## 一、专题介绍

### 1.1 研究背景

在数字化浪潮席卷全球的当下，软件已然成为现代社会运转的基石。从日常使用的移动应用、办公软件，到关乎国家安全的关键信息基础设施，软件无处不在。然而，随着软件规模的持续膨胀以及功能的日益复杂，其内部潜藏的安全隐患也呈爆发式增长。据安全数据库网站 CVE Details 报告显示，2016 - 2019 年间，**披露的安全漏洞数量从 6447 个攀升至 16556 个，而 2019 年前 10 个月便已达 12174 个，其中 8.7% 的漏洞 CVSS 得分超 9.0**。这些漏洞一旦被不法分子利用，将对个人隐私、企业经济利益乃至国家安全构成严重威胁。​
传统的软件漏洞挖掘手段，如静态分析与动态分析方法，在面对如今海量、复杂的软件代码时，**逐渐暴露出高误报率、高漏报率等弊端**，难以满足保障软件安全的需求。在此背景下，智能软件漏洞挖掘技术应运而生。它借助人工智能、机器学习、深度学习等前沿技术，能够更高效、精准地在软件代码中探寻潜藏的安全漏洞，为软件安全保驾护航，已成为当前网络安全领域炙手可热的研究方向。

### 1.2 研究意义

智能软件漏洞挖掘技术的研究具有多方面的意义：

1. **保障信息安全，维护社会稳定**：在金融领域，智能软件漏洞挖掘技术可提前检测银行核心系统、支付软件的漏洞，防止黑客窃取资金、篡改交易记录，避免引发金融秩序混乱。在医疗行业，能够确保医疗设备控制软件、电子病历管理系统的安全，防止患者隐私泄露，保障患者生命安全。

2. **助力企业发展，提升竞争力**：企业若能借助该技术及时发现并修复软件产品中的漏洞，不仅可减少因安全事件导致的经济损失，如赔偿用户损失、支付罚款、品牌形象受损等，还能提升产品质量与用户信任度，增强市场竞争力。

3. **推动技术创新，促进产业升级**：智能软件漏洞挖掘技术的研究，促使机器学习算法优化、数据表征形式创新、模型学习效率提升等关键技术的发展，进而带动整个网络安全产业的升级，为相关领域培养专业人才，促进学科交叉融合。

4. **学术价值与科研启蒙**：作为计算机科学、网络安全、人工智能等多学科交叉的典型研究案例，为本科生开启科研大门提供绝佳契机，帮助其理解前沿技术在实际问题中的应用，培养科研思维与实践能力。

因此，漏洞挖掘作为网络安全与深度学习的前沿交叉领域中的核心任务，非常适合作为本科生进入相关科研领域的启蒙训练。

### 1.3 当前主要挑战

尽管方向重要，但实现智能应用软件的漏洞挖掘工作仍然面临多重挑战：

1. **挑战一：软件复杂性高，漏洞模式难捕捉**

   - 现代软件系统规模庞大，代码行数动辄数百万甚至数千万，不同模块间交互错综复杂。

   - 漏洞表现形式多样，新的漏洞类型不断涌现，传统基于规则的检测方法难以全面覆盖。

例如，复杂的面向对象编程结构、动态链接库调用，使得漏洞隐藏在多层次的代码逻辑中，难以被精准识别。

2. **挑战二：数据获取与标注困难**

   - 获取大规模、多样化且涵盖各类漏洞场景的代码数据集困难。

   - 人工标注代码中的漏洞标签，需耗费大量专业人力与时间成本，且标注准确性易受主观因素影响。

   - 开源数据集中可能本身就包含漏洞，以此训练模型，会影响模型对漏洞的识别能力。

3. **挑战三：模型泛化能力不足**

   - 目前基于深度学习的漏洞检测模型，面对不同来源、不同类型的软件代码，泛化能力欠佳。

   - 不同企业、不同项目的代码风格、编程习惯、业务逻辑差异较大，导致模型在新环境下检测准确率大幅下降，难以满足实际软件安全检测需求。

4. **挑战四：对抗攻击与误报漏报问题**

   - 智能漏洞挖掘模型的检测结果可能会受恶意构造的对抗样本影响，使其漏检真实漏洞或产生大量误报。

   - 现有模型自身也难以精准区分真实漏洞与代码中的正常异常情况，高误报率会消耗安全人员大量精力排查，而高漏报率则使软件安全留下隐患。

综上，智能软件漏洞挖掘技术的研究与应用，不仅需要解决上述挑战，还需不断探索创新，以实现软件安全检测的智能化、高效化。

***

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下三个部分：

***

### 2.1 基础教材与学习材料

在开始探险之前，你需要掌握一些基础的“内功心法”，这些是后续一切学习的基石。以下是你可以使用的一些**书籍/教程**：

- 李沐[《动手学深度学习》](https://zh.d2l.ai/)——适合中文初学者的深度学习教材，以及[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)

- [《Deep Learning》](https://www.deeplearningbook.org/)（Ian Goodfellow 等）——深度学习入门经典教材

- [PyTorch 官方教程](https://pytorch.org/tutorials)，也可以使用 [PyTorch 中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

- [《Pattern Recognition and Machine Learning》](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)（Christopher M. Bishop）——机器学习原理入门（难度不小）

- [《漏洞战争：软件漏洞分析精要（修订版）》](https://github.com/riusksk/vul_war)————系统地讲解了软件漏洞分析与利用所需的各类工具、理论技术和实战方法

- [《网络攻防技术与实战————软件漏洞挖掘与利用》](https://www.tup.tsinghua.edu.cn/booksCenter/book_09589801.html)————通过实践提高读者对软件漏洞的分析和利用能力及针对各种破解手段的防范能力

- [《二进制分析实战》](http://product.m.dangdang.com/11957103633.html?t=1758094803)————基于攻防对抗实战经验，针对二进制分析领域动态检测与自动化漏洞利用的技术空白，系统构建了该领域的知识体系 

此外，你也可以使用一些**入门工具**：

- [Google Colab](https://colab.research.google.com/)：免费云平台，不用安装软件，就能跑 PyTorch 代码

- [NVD（National Vulnerability Database）](https://nvd.nist.gov/)：美国国家标准与技术研究院(NIST)维护的国家漏洞数据库，包含大量CVE（公共漏洞披露）条目 

- [SARD（Software Assurance Reference Dataset）](https://samate.nist.gov/SRD/index.php)：包含漏洞代码、无漏洞代码和元数据，支持多种漏洞类型的静态分析和深度学习模型训练

- [Kaggle平台](https://www.kaggle.com/)：免费数据集和竞赛

Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2 入门文献

> 学生第一阶段的阅读训练，可帮助理解软件源码漏洞挖掘这一通用方向。**仅用于入门，不可选择此部分文献汇报**。

* **[Vuldeepecker](https://arxiv.org/abs/1801.01681): Vuldeepecker: A deep learning-based system for vulnerability detection (NDSS, 2018) (https://github.com/CGCL-codes/VulDeePecker)([johnb110/VDPython: VulDeePecker 算法用 Python 实现 --- johnb110/VDPython: VulDeePecker algorithm implemented in Python](https://github.com/johnb110/VDPython))**

* **[CVD](https://ieeexplore.ieee.org/abstract/document/9293321): Combining Graph-Based Learning With Automated Data Collection for Code Vulnerability Detection (TIFS 2020)([HuantWang/FUNDED_NISL: FUNDED is a novel learning framework for building vulnerability detection models.](https://github.com/HuantWang/FUNDED_NISL/tree/main))**

* **[DLDSV](https://ieeexplore.ieee.org/document/9321538): A Framework for Using Deep Learning to Detect Software Vulnerabilities (TDSC 2022)**

* [SVCE](https://arxiv.org/pdf/1808.04673):  Mining Threat Intelligence about Open-Source Projects and Libraries from Code Repository Issues and Bug Reports (arXiv, 2018)

* [SeRules](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9903259): Software Security Testing Model Based on Data Mining (IHMSC 2022)

* **[ITS](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9671757): Mining Learner-friendly Security Patterns from Huge Published Histories of Software Applications for an Intelligent Tutoring System in Secure Coding (IEEE 2021)**

* **[CVSS](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5260472): Security Data Mining in an Ontology for Vulnerability Management (IEEE 2009)**

* **[RPC](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7009365): Vulnerability mining for network protocols based on fuzzing (ICSAI 2014)**

* **[CNN-LSTM](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8322752): Vulnerability detection with deep learning (ICCC 2017)**

* **[Botnet](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8935236): Botnet Vulnerability Intelligence Clustering Classification Mining and Countermeasure Algorithm Based on Machine Learning (IEEE 2019)**

* **[Improved Fuzz-SOA](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10748312): Research on Open Source Software Vulnerability Mining Based on Improved Fuzz-SOA (AIoTC 2024)**

***

### 2.3 进阶文献（近三年较前沿的软件漏洞挖掘技术）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

* **[SySeVR](https://ieeexplore.ieee.org/document/9321538): SySeVR: A Framework for Using Deep Learning to Detect Software Vulnerabilities (IEEE 2022)([SySeVR/SySeVR](https://github.com/SySeVR/SySeVR))**

* **[SCVDM](https://ieeexplore.ieee.org/document/10911761): A Source Code Vulnerability Detection Method Based on Positive-Unlabeled Learning (RICAI 2024)**

* **[VulChecker](https://ieeexplore.ieee.org/document/9724335): A Deep Learning Approach for Vulnerability Detection in Software (USENIX Security, 2022) (https://github.com/ymirsky/VulChecker)**

* **[SHAP](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11088900): Leveraging Explainable AI for Pointer Usage-based Software Vulnerability Analysis (RAIT, 2025)**

* **[DeepVulGuard](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11029760): Closing the Gap: A User Study on the Real-world Usefulness of AI-powered Vulnerability Detection & Repair in the IDE (ICSE, 2025)**

* **[BiLSTMs](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11021147): Enhancing Smart Contract Security with Explainable AI: A Framework for Re-entrancy Vulnerability Detection and Explanation (SIEDS, 2025)**

* [VulZoo](https://arxiv.org/pdf/2406.16347): A Comprehensive Vulnerability Intelligence Dataset (ASE, 2024)(https://github.com/NUS-Curiosity/VulZoo)

* [ACFIX](https://arxiv.org/pdf/2403.06838): Guiding LLMs with Mined Common RBAC Practices for Context-Aware Repair of Access Control Vulnerabilities in Smart Contracts (arXiv, 2025)(https://github.com/zly123987/Repair-Access-Control-C)

* [GAIL-PT](https://arxiv.org/pdf/2204.01975): A Generic Intelligent Penetration Testing Framework with Generative Adversarial Imitation Learning (arXiv, 2022)(https://github.com/Shulong98/GAIL-PT)

* [Forensics_LLMs](https://arxiv.org/pdf/2508.20643):  CyberSleuth: Autonomous Blue-Team LLM Agent for Web Attack Forensics(arXiv, 2025)(https://github.com/AnonUsenix/LLM_Agent_Cybersecurity_Forensic)

* [RL](https://arxiv.org/pdf/2508.03783):  Probing and Enhancing the Robustness of GNN-based QEC Decoders with Reinforcement Learning(arXiv, 2025)

* [LIFT](https://arxiv.org/pdf/2507.04931):  LIFT: Automating Symbolic Execution Optimization with Large Language Models for AI Networks(ACM, 2025)

* [QLPro](https://arxiv.org/pdf/2506.23644):  QLPro: Automated Code Vulnerability Discovery via LLM and Static Code Analysis Integration(arXiv, 2025)

***

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。软件漏洞挖掘是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
