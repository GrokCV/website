---
title: 新芽专题介绍（X）：多模态基础模型
date: 2025-09-18T01:00:00Z
draft: false
math: true
---
> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。


## 一、专题介绍

### 1.1  研究背景

传统视觉模型通常围绕预先设定的类别和任务训练，经典的视觉检测模型（如 [Faster R-CNN](https://arxiv.org/abs/1506.01497)、[FCOS](https://arxiv.org/abs/1904.01355)、[YOLO26](https://arxiv.org/abs/2606.03748) 等）已经能够很好地检测出物品。而现实中的感知需求更加开放：除了识别具体的物品（比如“汽车”、“鸟”），我们还希望通过一句自然语言，找到“左侧穿红衣服的人”，甚至理解更复杂的属性与关系，现有的小模型很难完成这样的任务。**多模态基础模型**通过大规模图像、文本等数据的联合学习，为这种灵活的视觉感知需求提供了新的途径。

从 [CLIP](https://proceedings.mlr.press/v139/radford21a.html) 的图文语义对齐，到 [Grounding DINO](https://arxiv.org/abs/2303.05499) 的语言引导检测，再到 [Qwen-VL](https://arxiv.org/abs/2308.12966)、[Youtu-VL](https://arxiv.org/abs/2601.19798) 等多模态大语言模型（MLLM）的视觉能力增强，研究正由图像级语义理解向实例级空间定位与细粒度描述演进。本专题以**视觉—语言**两种模态的表征学习为起点，梳理从图文语义对齐到多模态大语言模型的技术演进，重点关注跨模态理解与细粒度视觉感知能力的构建，以及其在目标检测、视觉定位与分割等任务中的应用。

![Grounding DINO展示从固定类别检测到开放类别与指代表达定位的变化](https://arxiv.org/html/2303.05499v5/hero_image.png)

▲从固定类别检测到语言引导的目标定位：模型既可以接收类别名称，也可以理解“左边的狮子”等复杂指代描述。图源：[Grounding DINO](https://github.com/IDEA-Research/GroundingDINO)。

### 1.2  研究意义

视觉信息提供了理解场景的直观依据，而自然语言能够表达目标属性、空间关系与任务需求。将二者结合，有助于感知系统根据不同任务识别和定位目标，并对视觉内容进行语义解释。如何让机器具备同样的能力，是计算机视觉与自然语言处理交叉领域最核心的挑战之一。图像—语言建模的研究意义，正体现在它所打通的三个层面：
1. **感知层面**：传统目标检测依赖固定类别标签，难以应对真实世界中开放、多变的任务需求。引入语言后，模型可以通过自然语言描述定位任意目标，使视觉感知从“封闭世界假设”走向开放场景。
2. **智能层面**：多模态大语言模型的出现，使机器能够将视觉感知与语义推理统一在同一个框架下，为视觉问答、图像检索、人机交互等高层智能任务奠定基础。
3. **应用层面**：从自动驾驶的场景理解，到医疗影像的辅助诊断，再到具身智能的语言指令执行等等，多模态大模型正在成为新一代智能系统的共同底座。

这一专题涉及当前人工智能的多个前沿方向，围绕其技术演进脉络展开学习，有助于逐步建立对多模态学习的系统认知。


### 1.3  当前主要挑战
尽管多模态基础模型已展现出较强的视觉语言理解能力，但在迈向真实场景应用的过程中，仍面临以下几个关键挑战：


1. **挑战一：通用视觉能力强 ≠ 天然适合检测**
    * 特征抽象的侧重不同：多模态大模型擅长提取高层级的抽象语义，而目标检测依赖低层级的边缘、纹理与空间相对位置。模型能够生成详尽的图像描述，但因特征层层抽象易丢失局部细节，模型难以准确输出目标的空间坐标。
    * 语义理解与几何定位之间存在范式冲突：多模态基础模型主要通过大规模图文数据学习视觉语义，而目标检测要求模型完整发现实例并预测精确边界，两者的学习目标并不完全一致。图像级描述能够提供丰富语义，却难以直接教会模型如何区分多个相似实例、处理漏检，并生成稳定的边界框。
    * 任务迁移依赖后训练： 如何通过指令微调、检测数据和空间监督，将通用视觉语言能力有效转化为可靠的检测能力，是模型应用于实际检测任务时必须解决的问题。
    ![同一场景中，模型可以找到一个指定目标，却可能漏掉同类的其他目标、框出不存在的目标，或无法完整检测多个类别。](https://arxiv.org/html/2311.14552v3/comparison.png)
    ▲从单目标指认到完整检测：模型不仅需要找到指定对象，还需要处理同类多实例、不存在的目标及多类别检测。图源：[Griffon](https://arxiv.org/abs/2311.14552)。

2. **挑战二：模型需要适应不断扩展的模态**
    * 不同模态的数据表征差异显著： RGB 图像、红外、事件流、深度与雷达等传感器具有不同的数据结构、成像机理和信息分布，已有视觉编码器往往难以直接迁移到新的感知模态。
    * 跨模态对齐成本较高： 多模态基础模型依赖大规模数据建立视觉与语言之间的语义对应关系，而新模态通常缺乏与文本或其他模态成规模配对的数据，重新进行大规模预训练代价高昂。
    * 统一模型需要兼顾共享与特有信息： 不同模态之间既存在可共享的目标语义与空间信息，也包含各自独有的观测特征。如何在统一模型中实现有效融合，同时避免模态间相互干扰，是扩展多模态基础模型的重要问题。
    ![不同模态](https://arxiv.org/html/2604.03685v1/data_strength_v5.png)
    ▲多模态模型需要在统一表示中协调利用这些信息。图源：[DSERT-RoLL](https://arxiv.org/html/2604.03685v1)。

3. **挑战三：空间定位能力对通用模型压缩算法极其敏感**

    * 坐标预测对量化噪声容忍度低：低比特量化（如 AWQ、4-bit 量化）在语言生成任务中表现优异，但极小的权重偏差就会导致边界框坐标大幅漂移，造成定位精度断崖式下跌。
    * 理论压缩与端侧协同落差：轻量化手段带来的理论推理成本降低，在真实硬件上未必能转化为等比例的端侧延迟缩减。


综上，多模态基础模型的工作仍在快速突破阶段，这恰好是一个学习窗口：既能建立“模型-算力-精度”的全局工程视角，又能紧跟多模态感知与高效部署的前沿研究。


## 二、学习资料与参考文献

为了引导同学们逐步进入研究，本专题按**基础知识 → 通用视觉-语言建模 → 面向检测的多模态模型 → 细粒度感知与领域适配 → 轻量化部署**组织阅读。加粗文献可优先阅读，无需一次性读完全部论文。

***

### 2.1  基础教材与学习材料

* [《动手学深度学习》](https://zh.d2l.ai/)：重点学习注意力机制、Transformer、目标检测与预训练，可参考其[课程系列视频](https://space.bilibili.com/1567748478/lists/358497?type=series)。
* [PyTorch 官方教程](https://docs.pytorch.org/tutorials/)：掌握模型训练、推理与性能分析的基本流程。
* [Hugging Face LLM 课程](https://huggingface.co/learn/llm-course/zh-CN/chapter1/1)：了解分词、预训练模型与微调，为使用多模态大模型做准备。
* [Transformer](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)：Attention is all you need（NIPS 2017）——理解注意力机制。
* [ViT](https://arxiv.org/abs/2010.11929)：An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale（ICLR 2021）——理解图像如何转化为 token 序列。
* [DETR](https://arxiv.org/abs/2005.12872)：End-to-End Object Detection with Transformers（ECCV 2020）——理解目标查询、集合预测与边界框匹配。

Tips：**在实践中补基础**。或许可以先尝试跑通一个图文匹配或检测样例 demo，感受效果，再带着问题读论文。务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在实践中学，遇到不明白的再回溯补基础。

***

### 2.2  入门文献（从图文对齐到多模态大模型）

> 本阶段回答：图像与语言如何建立联系？模型如何获得视觉-语言能力？

1. **[CLIP](https://proceedings.mlr.press/v139/radford21a.html)：Learning Transferable Visual Models From Natural Language Supervision（ICML 2021）**
    通过图文对比学习建立共享语义空间，是理解开放词汇识别的基础；原始 CLIP 主要进行图像级匹配，并不直接输出检测框。
2. **[Flamingo](https://arxiv.org/abs/2204.14198): Flamingo: a Visual Language Model for Few-Shot Learning (NeurIPS 2022)**
   通过将预训练视觉编码器与大型语言模型连接起来，实现图像与文本交错输入下的少样本学习，是现代多模态大语言模型的重要奠基性工作之一。其核心思想是保留已有视觉与语言模型能力，再通过跨模态连接模块实现统一建模。
3. **[LLaVA](https://papers.nips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html)：Visual Instruction Tuning（NeurIPS 2023）**
    通过视觉指令微调构建图像问答与对话能力，帮助理解“视觉编码器—连接模块—大语言模型”的典型结构，是后续几乎所有 MLLM 的共同起点。

***

### 2.3  进阶文献（从通用理解到目标检测）

> 本阶段围绕“如何把语言对应到图像中的具体目标”展开，比较语言条件检测器与生成式多模态模型两条路线。

**传统目标检测：从视觉特征到类别与边界框**

> 先了解以 CNN 为骨干的传统检测器如何提取视觉特征、判断目标类别并预测边界框。

1. **[Faster R-CNN](https://arxiv.org/abs/1506.01497)：Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks（NIPS 2015）**
    通过区域建议网络生成候选区域，再对候选区域进行分类与边界框回归，是两阶段目标检测的经典代表。
2. **[FCOS](https://arxiv.org/abs/1904.01355)：FCOS: Fully Convolutional One-Stage Object Detection（ICCV 2019）**
    将目标检测转化为特征图上的逐位置预测，通过预测目标类别及当前位置到边界框四条边的距离完成检测，无需预设锚框，单阶段完成。
3. [YOLO26](https://arxiv.org/abs/2606.03748)：Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models（arXiv 2026，补充阅读）
    作为实时检测的近期实例，关注其端到端检测与部署设计，并与前两篇比较精度、速度和推理流程。可结合实际训练与预测，理解检测模型如何从论文方法走向可部署系统。

> **阅读衔接：** 这些检测器通常围绕训练时设定的类别进行预测。接下来关注：当类别标签被替换为开放的自然语言描述时，模型需要如何改变特征交互、训练目标与输出方式？

**开放词汇检测：将图文对齐落实到目标区域**
1. **[GLIP](https://arxiv.org/abs/2112.03857)：Grounded Language-Image Pre-training（CVPR 2022）**
   将目标检测与短语定位统一为同一个预训练任务，学习目标区域与文本的对应关系，是从 CLIP 的全图对齐走向局部感知的重要一环。
2. **[Grounding DINO](https://arxiv.org/abs/2303.05499)：Marrying DINO with Grounded Pre-Training for Open-Set Object Detection（ECCV 2024）**
   将语言信息融入特征提取、目标查询与解码过程，支持类别名称及指代表达输入，是语言引导检测的代表性基线。
3. **[YOLO-World](https://arxiv.org/abs/2401.17270)：Real-Time Open-Vocabulary Object Detection（CVPR 2024）**
将区域—文本对齐引入 YOLO 系列，通过预先编码词汇嵌入和重参数化结构，把开放词汇能力压缩进实时检测框架。

**生成式多模态模型：在语言模型中强化视觉定位与分割**

1. [Griffon](https://arxiv.org/abs/2311.14552)：Spelling Out All Object Locations at Any Granularity with Large Language Models（**ECCV 2024**）
   将不同粒度的语言定位数据统一为生成式训练任务，不引入额外检测模块或特殊坐标 token，探索 MLLM 直接输出目标位置的能力。除指代表达理解与短语定位外，也在 COCO 上评估目标检测。
2. **[Qwen2.5-VL](https://arxiv.org/abs/2502.13923)：Qwen2.5-VL Technical Report（arXiv 2025，技术报告）**
   引入动态分辨率视觉编码与专门的框、点定位训练，显著强化开放词汇检测与结构化坐标输出能力；应注意区分其定位能力与原生像素级分割能力。
3. **[Youtu-VL](https://arxiv.org/abs/2601.19798)：Unleashing Visual Potential via Unified Vision-Language Supervision（arXiv 2026，技术报告）**
   提出 VLUAS（视觉—语言统一自回归监督）范式，将视觉信号从“被动输入”变为与文本同等的“监督目标”，使标准 VLM 架构无需额外任务头即可原生完成目标检测、指代分割、语义分割等视觉中心任务，代表了 MLLM 从“看懂”走向“看准”的近期探索。
   ![Youtu-VL的视觉编码、统一视觉语言监督和密集预测机制](https://arxiv.org/html/2601.19798v1/pipeline.png)
   ▲Youtu-VL 将视觉编码器与语言模型通过统一自回归目标连接，使检测、分割等任务共享同一套生成机制。图源：[Youtu-VL 论文](https://arxiv.org/abs/2601.19798)。


***

### 2.4  应用领域文献（细粒度感知与领域适配）

> 本阶段回答：如何围绕检测、定位与计数等具体任务，以及遥感等专业场景，设计多模态模型的训练与适配方法？

**一、细粒度感知：目标检测、指代定位与计数**


1. **[Griffon v2](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhan_Griffon_v2_Advancing_Multimodal_Perception_with_High-Resolution_Scaling_and_Visual-Language_ICCV_2025_paper.pdf)：Advancing Multimodal Perception with High-Resolution Scaling and Visual-Language Co-Referring（ICCV 2025）**
   通过高分辨率视觉编码与轻量下采样连接模块控制视觉 token 数量，并结合文本、局部图像等提示强化通用 MLLM 检测、指代定位与计数能力。

**二、领域适配：遥感目标检测与视觉定位**

2. **[OpenRSD](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_OpenRSD_Towards_Open-prompts_for_Object_Detection_in_Remote_Sensing_Images_ICCV_2025_paper.pdf)：Towards Open-prompts for Object Detection in Remote Sensing Images（ICCV 2025）**
   面向遥感图像构建开放提示检测框架，支持文本与图像提示，以及水平框和旋转框检测；通过不同检测头兼顾精度与实时性。它展示了语言条件检测路线如何适配遥感任务的提示形式、目标方向和效率要求。
3. **[GeoChat](https://openaccess.thecvf.com/content/CVPR2024/html/Kuckreja_GeoChat_Grounded_Large_Vision-Language_Model_for_Remote_Sensing_CVPR_2024_paper.html)：Grounded Large Vision-Language Model for Remote Sensing（CVPR 2024）**
   基于 LLaVA-1.5，利用遥感多模态指令数据进行领域适配，支持区域描述、视觉问答、带坐标的对话和指代检测。它将遥感场景理解与区域级定位结合起来，适合学习如何从已有领域数据构造指令，并训练 MLLM 输出空间信息。

**三、扩展阅读：目标跟踪与大幅遥感图像理解**

4. [JTD-UAV](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_JTD-UAV_MLLM-Enhanced_Joint_Tracking_and_Description_Framework_for_Anti-UAV_Systems_CVPR_2025_paper.html)：MLLM-Enhanced Joint Tracking and Description Framework for Anti-UAV Systems（**CVPR 2025**）
   面向反无人机系统，将目标跟踪与运动意图描述结合，研究 MLLM 如何参与具体视觉应用中的定位与语义理解。
5. [When Large Vision-Language Model Meets Large Remote Sensing Imagery: Coarse-to-Fine Text-Guided Token Pruning](https://openaccess.thecvf.com/content/ICCV2025/html/Luo_When_Large_Vision-Language_Model_Meets_Large_Remote_Sensing_Imagery_Coarse-to-Fine_ICCV_2025_paper.html)（**ICCV 2025**）
针对大幅遥感图像整体缩放易丢失细节、密集切块又增加计算的问题，结合动态图像金字塔、文本引导的区域聚焦与由粗到细的图块选择和 token 裁剪。
6. [LinkS²Bench](https://arxiv.org/abs/2604.02020)：Are VLMs Lost Between Sky and Space? LinkS²Bench for UAV-Satellite Dynamic Cross-View Spatial Intelligence（arXiv 2026）
    面向无人机视频与卫星图像之间的动态跨视角空间理解，构建涵盖感知、定位、关系与推理四个维度的评测基准，并通过跨视角对齐适配器改善模型表现，显式对齐增强空间定位与推理能力，是多模态模型用于遥感空间智能的任务研究实例。


***
### 2.5  专题文献（轻量化与高效部署）

> 本阶段回答：如何保留多模态感知能力，同时减少存储、计算和响应时间？

**知识蒸馏与轻量模型**
1. [Knowledge Distillation](https://arxiv.org/abs/1503.02531)：Distilling the Knowledge in a Neural Network（NIPS 2014 Deep Learning Workshop）
通过教师模型的软目标训练学生模型，是理解知识迁移与模型压缩的经典起点。
2. **[AWQ](https://arxiv.org/abs/2306.00978)：Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration（MLSys 2024）**
   利用激活分布信息降低低比特权重量化误差，是压缩 MLLM 语言骨干最常用的方法之一；检测与坐标输出的精度需要单独检验。
3. **[FastV](https://arxiv.org/abs/2403.06764)：An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models（ECCV 2024）**
   按注意力权重筛选视觉 token 并在浅层之后剪除，减少后续计算。可进一步思考：为图像问答设计的 token 筛选，能否保留检测所需的小目标与局部信息？
4. **[FlashAttention](https://arxiv.org/abs/2205.14135): Fast and Memory-Efficient Exact Attention with IO-Awareness (NeurIPS 2022)**
   通过优化 GPU 中 Attention 的内存访问方式，在不近似、不裁剪 token 的情况下减少数据搬运和显存占用。它说明高效部署不仅要减少 FLOPs，还需要考虑计算与硬件之间的实际执行效率。
5. **[PagedAttention](https://arxiv.org/abs/2309.06180): Efficient Memory Management for Large Language Model Serving with PagedAttention (SOSP 2023)**
   采用分页式 KV Cache 管理减少显存浪费，并支持更高效的批处理与并发推理，是 vLLM 推理系统的核心技术。可进一步理解：模型压缩解决“模型能否放得下”，而推理系统优化决定“模型能否真正跑得快”。


## 三、结语与期望
专题设计的初衷是点燃同学们对未知探索的热情，并为大家提供一片成长的沃土。希望通过这个专题，同学们能从阅读经典论文出发，逐步熟悉提出问题、设计解决方案、验证想法与解释结果的流程，培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！