---
title: 新芽专题介绍（49）：视频生成与质量评估
date: 2025-09-17T01:02:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1  研究背景

随着多模态大模型的发展，视频生成技术正从早期的低分辨率合成逐步迈向高质量、长时序和多条件可控的生成阶段。尤其是以**扩散模型和统一多模态预训练框架**为代表的方法，正在推动视频理解与生成的深度融合，使模型能够在同一参数体系下兼顾事件识别、语义解析与视频生成等任务。同时，**视频质量评估**是衡量数据可用性和驱动数据闭环迭代的核心环节。然而，现有主流方法多采用端到端回归框架，将复杂的质量感知任务简化为单一的分数预测，面临着可解释性、鲁棒性、扩展性 上的科学挑战。

### 1.2  研究意义

1.**提升跨任务泛化能力**：通过共享语义空间和模型参数，统一模型能够在理解和生成任务之间迁移知识，显著提升模型的适应性与鲁棒性。

2.**推动人工智能新范式**：实现视频理解与生成统一，有助于打破传统任务割裂的局限，推动多模态大模型在统一框架下完成识别、推理与生成任务。

3.**建立科学评价体系**：针对现有指标不足，研究视频质量评估有助于构建多维度、可量化的标准，为学术界和产业界提供统一参照。

4.**为模型优化提供反馈**：高效的评估指标可作为训练与推理过程中的优化信号，帮助生成模型在迭代中持续提升表现。

### 1.3  当前主要挑战

尽管方向重要，但实现理解与生成统一的视频生成模型和质量评估仍然面临多重挑战：
1. **挑战一：时序对齐不足：**

   * 文本往往来自字幕或整体描述，和视频关键帧/镜头缺乏精确的时间对应，导致训练时模态对齐噪声大；

2. **挑战二：语境碎片化**
   * 文本描述往往是孤立句子，不能体现跨句的语义连贯（例如动作的连续性、故事逻辑），导致模型生成的视频缺乏连贯性。

3. **挑战三：数据与标注问题**
   * 在原生多模态视频数据的采集与利用上，仍普遍面临“高冗余、低密度”的瓶颈——缺乏能高效提取跨模态语义信号的通用范式，导致数据规模虽大，信息增益却有限。
4. **挑战四：黑盒化输出**
   * 许多模型仅能给出单一质量分数，缺乏可解释性和证据支撑，难以为数据清洗、再采集或增强提供明确指引。

综上，理解与生成统一的视频生成模型和视频质量评估技术仍在探索突破阶段，这是一个很好的学习窗口：既能接触实际需求，又能跟随前沿研究。

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

### 2.2  入门文献

> 学生第一阶段的阅读训练，可帮助理解**理解与生成统一的视频生成模型和质量评估**这一通用方向。**仅用于入门，不可选择此部分文献汇报**。



1. * **[GAN](https://arxiv.org/abs/1406.2661):Generative Adversarial Nets (NeurIPS 2014)**

2. * **[Mocogan](http://openaccess.thecvf.com/content_cvpr_2018/papers/Tulyakov_MoCoGAN_Decomposing_Motion_CVPR_2018_paper.pdf): Mocogan: Decomposing motion and content for video generation (CVPR 2018）**

3. * **[VAE](https://indico.math.cnrs.fr/event/11377/attachments/4589/6915/18012024_Kingma-and-Welling-2022%20Auto-Encoding%20Variational%20Bayes.pdf): Auto-Encoding Variational Bayes (ICLR 2014)**

4. * **[Transformer](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf): Attention is all you need (NeurIPS 2017)**

5. * [Make-a-video](https://arxiv.org/pdf/2209.14792): Make-a-video: Text-to-video generation without text-video data (ICLR 2023)**

6. * [LPIPS](http://openaccess.thecvf.com/content_cvpr_2018/papers/Zhang_The_Unreasonable_Effectiveness_CVPR_2018_paper.pdf): The Unreasonable Effectiveness of Deep Features as a Perceptual Metric (CVPR 2018)

7. * [FVD](https://arxiv.org/pdf/1812.01717): Towards Accurate Generative Models of Video: A New Metric & Challenges(Arxiv 2018)

8. * [Stable diffusion](http://openaccess.thecvf.com/content/CVPR2022/papers/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.pdf): High-Resolution Image Synthesis with Latent Diffusion Models (CVPR 2022)

9. * [ControlNet](https://arxiv.org/abs/2302.05543): Adding Conditional Control to Text-to-Image Diffusion Models (ICCV 2023) 

***

### 2.3  进阶文献（视频生成前沿方法）

> 学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。

1. * **[Phenaki](https://arxiv.org/pdf/2210.02399): Phenaki: Variable length video generation from open domain textual description (ECCV 2022 )**

2. * **[Cogvideo](https://arxiv.org/pdf/2205.15868): Cogvideo: Large-scale pretraining for text-to-video generation via transformers (Arxiv 2022)**

3. * **[Imagen video](https://arxiv.org/pdf/2210.02303):Imagen video: High definition video generation with diffusion models (Arxiv 2022)**

4. * **[Stable Video Diffusion](https://arxiv.org/pdf/2311.15127): Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets (Arxiv 2023)**

5. * **[Text2video-zero](http://openaccess.thecvf.com/content/ICCV2023/papers/Khachatryan_Text2Video-Zero_Text-to-Image_Diffusion_Models_are_Zero-Shot_Video_Generators_ICCV_2023_paper.pdf): Text2video-zero: Text-to-image diffusion models are zero-shot video generators(ICCV  2023)**

6. * **[MetaQueries](https://arxiv.org/abs/2504.06256): Transfer between Modalities with MetaQueries (Arxiv 2025)**

7. * **[Unitoken](https://openaccess.thecvf.com/content/CVPR2025W/MMFM/papers/Jiao_UniToken_Harmonizing_Multimodal_Understanding_and_Generation_through_Unified_Visual_Encoding_CVPRW_2025_paper.pdf): Unitoken: Harmonizing multimodal understanding and generation through unified visual encoding(CVPR 2025)**

8. * **[ UniFluid](https://arxiv.org/pdf/2503.13436): Unified autoregressive visual generation and understanding with continuous tokens (Arxiv 2025)**

9. * **[Visual Planning](https://arxiv.org/pdf/2505.11409): Visual Planning: Let's Think Only with Images. (Arxiv 2025)**


***

### 2.4  理解生成统一的视频生成和视频质量评估领域相关文献

> 结合本专题的研究背景，逐渐引导学生进入理解生成统一的多模态模型和视频质量评估研究领域。学生可在此部分选择进阶文献进行专题汇报，或自行查找最新的同类重要文献。
>
1. * **[Begal](https://arxiv.org/pdf/2505.14683?): Emerging properties in unified multimodal pretraining (Arxiv 2025)**

2. * **[Show-o](https://arxiv.org/pdf/2408.12528?): Show-o: One single transformer to unify multimodal understanding and generation (ICLR 2025)**

3. * **[Show-o2](https://arxiv.org/pdf/2506.15564?): Show-o2: Improved Native Unified Multimodal Models (Arxiv 2025)**

4. * **[Janusflow](https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_JanusFlow_Harmonizing_Autoregression_and_Rectified_Flow_for_Unified_Multimodal_Understanding_CVPR_2025_paper.pdf):Janusflow: Harmonizing autoregression and rectified flow for unified multimodal understanding and generation (CVPR 2025)**

5. * **[Janus-pro](https://arxiv.org/pdf/2501.17811): Janus-pro: Unified multimodal understanding and generation with data and model scaling (Arxiv 2025)**

6. * **[Visual sketchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf): Visual sketchpad: Sketching as a visual chain of thought for multimodal language models.(NeurIPS 2024)**

7. * **[DeepEyes](https://arxiv.org/pdf/2505.14362): DeepEyes: Incentivizing" Thinking with Images" via Reinforcement Learning (Arxiv 2025)**

8. * **[DyFo ](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_DyFo_A_Training-Free_Dynamic_Focus_Visual_Search_for_Enhancing_LMMs_CVPR_2025_paper.pdf): DyFo: A Training-Free Dynamic Focus Visual Search for Enhancing LMMs in Fine-Grained Visual Understanding (CVPR 2025)**

9. * **[Finevq](https://openaccess.thecvf.com/content/CVPR2025/papers/Duan_FineVQ_Fine-Grained_User_Generated_Content_Video_Quality_Assessment_CVPR_2025_paper.pdf): Finevq: Fine-grained user generated content video quality assessment. (CVPR 2025)**

***

## 三、结语与期望

“新芽计划”的初衷是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。海报生成是一个充满挑战与机遇的领域，它既是国家需求的“硬骨头”，也是学术创新的“试金石”。希望通过这个专题，新芽学子不仅能学到前沿的 AI 知识，更能培养出独立思考、动手实践和解决复杂问题的能力。

我们热切期待，在最终的汇报中，能看到大家闪耀着智慧火花的解读与创见！
