---
title: 📄【ICCV 2025】DISTA-Net：首个远距离空间邻近红外小目标开源生态系统与动态解混框架
date: 2025-08-01
draft: false
math: true
authors: 
- Shengdong Han
---


![](https://fastly.jsdelivr.net/gh/bucketio/img2@main/2025/08/01/1754056371135-0448524b-2151-48fe-b47b-13bbf36abee0.PNG)

本文介绍了一种针对远距离空间邻近红外小目标解混的新方法DISTA-Net，利用动态迭代收缩阈值网络实现亚像素级检测精度，为红外小目标检测领域提供了首个专门的开源生态系统。

- **论文地址**：<https://arxiv.org/abs/2505.19148>
- **代码地址**：<https://github.com/GrokCV/GrokCSO/>
- **数据集开源地址**：<https://pan.baidu.com/s/1nuedV5Okng8rgFWKy_sMoA?pwd=Grok>

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2025/08/01/1754056456638-510d74f3-c7a5-4e58-b251-0d16ca3e6afb.JPEG)

<p align="center"><span style="color: #808080">图 1(a)</span></p>

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2025/08/02/1754114544183-785f334e-730b-47ce-afce-2195774f867b.png)

<p align="center"><span style="color: #808080">图 1(b)</span></p>

-------

在红外成像中，远距离密集成团的空间邻近小目标解混任务面临严峻的技术挑战，如图 1(b) 所示，信号混叠会严重影响目标数量统计、亚像素级定位以及辐射强度测定的准确性。为此，我们将空间邻近目标解混任务重新表述为一个可解释的深度展开问题，并提出了动态迭代收缩阈值网络 (*Dynamic Iterative Shrinkage Thresholding Network, DISTA-Net*)，该网络将传统稀疏重构方法重新概念化为动态框架，实现了卷积权重和阈值参数的自适应地生成，从而能够实时调整重建过程。据我们所知，*DISTA-Net* 是首个专门针对空间邻近红外小目标解混问题设计的深度学习模型，实现了卓越的亚像素检测精度。

为推动这一研究的发展，我们提供：
- **CSIST-100K**，一个公开的空间邻近红外小目标基准数据集；
- **CSO-mAP**，一个用于亚像素检测的自定义评估指标；
- **GrokCSO**，一个开源工具包，包含 DISTA-Net 和其他最先进的模型。

## 研究背景

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2025/08/02/1754127038701-e805c629-9e44-4d21-af10-f6a04afdaed2.png)

<p align="center"><span style="color: #808080">图 2 远距离空间邻近红外小目标成像及其解混过程示意图</span></p>

红外成像凭借其出色的热辐射感知能力，不受光照条件限制，在远距离探测与监视中至关重要<sup>[[1]](#ref1)</sup>。然而，远距离目标的辐射强度极弱<sup>[[2]](#ref2)</sup>。当远距离目标密集聚集时，多个目标在成像平面重叠，形成团块状光斑<sup>[[3]](#ref3)</sup>（如图 2），导致难以分辨目标的数量、位置和辐射强度<sup>[[4]](#ref4)</sup>。这种光学扩散模糊现象严重阻碍了红外搜索与跟踪 (*Infrared Search and Tracking, IRST*) 系统后续的探测、跟踪和识别阶段。因此， 作为红外目标检测任务的后续任务，探索针对此类空间邻近红外小目标 (*Closely-Spaced Infrared Small Targets, **CSIST***) 的有效的解混和重建技术，以准确辨别其确切位置和辐射强度，具有重要意义。

本研究与传统红外小目标检测研究虽均聚焦红外小目标，但在以下两个关键维度存在本质区别：
1. **处理流程的阶段差异**：CSIST解混是传统红外小目标检测的后置任务，核心研究目标在于远距离空间邻近红外小目标的精确解混。其中，重叠目标的准确检测是实现亚像元级定位和辐射强度预测的重要基础。
2. **预测目标的本质差异**：区别于传统二值化（存在/不存在）检测范式，本研究通过亚像元位置测定和辐射强度估算，实现了多维度目标特性解析，为红外目标特征认知提供了更深入的解决方案。

为促进该领域持续发展，本研究同时致力于构建完整的空间邻近红外小目标研究生态系统，涵盖从数据集、评价指标到工具包的全套解决方案。

## CSIST-100K 数据集

![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/08/02/1754127103282-bc077718-25dd-4351-8826-ad708830af3a.png)

<p align="center"><span style="color: #808080">图 3 多目标成像与解混示意图</span></p>

当单一点光源通过透镜成像时，在焦点处会出现一种称为 "艾里斑 (*Airy disk*) " 的衍射图案，其特征为中央呈现明亮圆斑，周围环绕着多个明暗相间的同心环状条纹。这种衍射效应通常通过点扩散函数 (*Point Spread Function, PSF*) 进行近似，其标准差取决于传感器焦比 (F值) 和检测带宽，用于量化能量扩散程度。在多目标成像中，每个像素捕获的辐射强度是多点源的累积响应（如图 **3**）。特别是对于遥远物体，每个物体都被视为点光源，其产生的艾里斑半径为$1.22\lambda/D$（$\lambda$为探测波长，$D$为透镜直径），也就是二维高斯 PSF 的$1.9$倍标准差，是传感器对两个点源目标的物理分辨极限，称为**瑞利依据**($1R$, Rayleigh criterion)。依据光学模型原理我们设计了如下仿真，仿真图像见图 **4**。

![](https://fastly.jsdelivr.net/gh/bucketio/img15@main/2025/08/02/1754127151763-baac3c7e-1dcf-4c80-b1b0-9c6a26855b90.png)

<p align="center"><span style="color: #808080"> 图 4 CSIST-100K 数据集：首行分别是含 1 到 5 个目标的混叠情况，下三行是不同倍率分割的解混结果</span></p>

仿真参数：
- 模拟真实光学系统（σPSF =0.5像素）
- 包含 1-5 个目标的混叠场景
- 成像中心约束在单像素内
- 辐射强度：220-250（8bit 量化）
- 目标间距 ≥ 0.52 R
- 随机分布在11×11像空间
- 10 万样本（8 万训练+ 1 万验证/测试）

## CSO-mAP评价指标

![](https://fastly.jsdelivr.net/gh/bucketio/img14@main/2025/08/02/1754127230843-9ea3a58a-09a2-4c0b-9547-f8ed071ad19d.png)
<p align="center"><span style="color: #808080">图 5 小于距离阈值</span><span style="color: #A5A5A5">（灰色虚线）</span><span style="color: #808080">并且未匹配过的最近预测目标</span><span style="color: #A5A5A5">（灰色实线所指）</span><span style="color: #808080">视为该真实目标</span><span style="color: #C00000">（红点）</span><span style="color: #808080">的预测</span></p>

受通用目标检测中广泛采用的平均精度 (*Mean Average Precision, mAP*) 指标的启发，本文提出一种特定的评估指标，即**空间邻近目标平均精度** (*Closely-spaced Object Mean Average Precision, CSO-mAP*) ，用于评估 *CSIST* 检测的准确性。该指标通过设定一系列距离阈值（0.05到0.25像素）来控制所需的定位精度，当预测点与真实目标之间的距离小于设定阈值时，匹配成功，否则匹配失败。通过动态调整检测亮度阈值，可获得一系列精确度和召回率值，从而形成 *PR* 曲线。计算 PR 曲线下的面积获得平均精确度（*AP*），对模型在不同灰度阈值下的性能进行综合评估，有效总结了精确度与召回率之间的权衡关系。最后，我们引入指标 (*CSO-mAP*)，其通过对不同距离阈值下的 *AP* 取平均值，为 *CSIST* 解混任务中模型性能的比较提供了一个标准化指标。

## 焦平面成像模型
鉴于目标和红外探测器之间的显著距离，远距离目标可以视为点源目标。光学系统的衍射效应导致点目标的能量分布在几个相邻像素之间，这种现象通常使用**二维高斯点扩散函数** (*PSF*) 来描述。该函数描述了目标在焦平面上的能量分布模式，其中扩散程度由参数σ控制。

在红外成像系统中，由于光学系统的点扩散函数的影响，远距离空间邻近红外小目标发出的红外辐射在焦平面上的像素之间发生了扩散。每个像素对混叠目标的入射辐射进行积分，产生响应。像素对目标的响应会线性叠加，从而形成线性焦平面成像模型。该积分表示像素对目标响应的累积效应，反映了目标能量在像素边界内的分布情况。

进一步地，假设一个红外焦平面由多个像素构成，并且有多个亚像素级目标。通过将焦平面矩阵重新排列为向量形式，可以得到焦平面测量模型。该模型将多个目标的响应组合成一个向量形式，其中包含了所有目标的贡献和噪声成分。导向矩阵由 *CSIST* 的位置唯一确定，表示了各个目标对像平面各像元响应的贡献。目标的峰值强度用向量表示，而噪声则代表具有特定方差的高斯白噪声，在各像元中独立分布。

## 基于稀疏重构的解混框架

**在允许一定量化误差的前提下**，图像平面上紧密分布的红外弱小目标的可能位置是有限的。基于这一特性，可以穷举所有亚像素位置，构建一个完备的可能目标位置集合。这样可以确保 *CSIST* 中的实际目标位置必定是的一个小子集。

![](https://fastly.jsdelivr.net/gh/bucketio/img13@main/2025/08/02/1754127265985-95b17e47-c822-4c45-bf7a-3ca5ed38bc44.png)

<p align="center"><span style="color: #808080">图 6 亚像素划分</span></p>

**将每个像素划分为多个亚像素网格**的过程，总共得到大量亚像素。假设网格划分足够精细，每个亚像素最多包含一个目标，且目标位置与最近的亚像素中心的最大偏差不超过设定阈值。如图 **6** 反映了像素划分为亚像素网格的过程，得到测量模型的超完备表示。该超完备表示将测量问题转化为稀疏信号重构的形式。

式中导向矩阵是一个以位置集中的导向矢量为列的矩阵。当网格划分精细时，矩阵的列数显然多于行数，扩展后的稀疏信号矢量进行了零填充，仅在网格内的目标位置处取非零值。这一测量模型被重新表述为稀疏表示，本研究将远距离 *CSIST* 解混任务转化为一个稀疏信号重构问题。这需要从中选择多个基函数，并优化信号强度，以最佳拟合观测到的信号。这种稀疏恢复问题可以通过最小化重构误差和稀疏性约束来求解目标位置和强度。

其中正则化参数是一个通常预先确定的正则化参数。一旦获得重构结果，则非零元素个数对应了 CSIST 中目标的个数，与非零元素对应的基函数的位置集为 *CSIST* 中各个目标的位置。

![](https://fastly.jsdelivr.net/gh/bucketio/img0@main/2025/08/02/1754127485665-07ac29d5-b4a9-4920-9a52-517886a9a91e.png)
<p align="center"><span style="color: #808080">算法 1 DISTA</span></p>

亚像素划分的方法将CSIST解混问题转化为稀疏信号恢复问题。基于传统迭代收缩阈值算法（*ISTA*），*ISTA-Net* 通过引入可学习的非线性变换替代固定变换，提升了稀疏重建性能。然而，其网络权重在训练后固定不变，在面对复杂多变的CSIST解混场景时，难以自适应调整特征提取策略。

本研究突破静态网络限制，提出动态迭代收缩阈值框架。通过实时调整网络参数响应输入特征变化，提升模型对密集目标混叠模式的适应能力。（具体实现流程详见**算法 1**）

## DISTA-Net： 一个全新的动态框架

为了将 *ISTA* 与基于网络的稀疏表示相结合，*DISTA-Net* 将每个 *ISTA* 迭代步骤映射到网络层中，通过串联这些层并通过端到端的训练，网络能够自动优化参数，相较于传统 *ISTA* 中手动设计的参数，既提升了性能又保持了可解释性。基于 *ISTA-Net* 的压缩感知框架，**我们引入了两项关键改进**：
![](https://fastly.jsdelivr.net/gh/bucketio/img8@main/2025/08/02/1754127406676-be7934bb-6c57-440d-806c-7cbb4fd4e115.png)
<p align="center"><span style="color: #808080">图 7 DISTA-Net 网络结构图</span></p>

1. **动态变换模块**，采用双分支结构设计，通过动态卷积核实现对特征表示的自适应调整，增强网络的特征表达能力；
2. **动态阈值模块**，引入双卷积层结构捕获多尺度特征，改善图像重建过程中对稀疏向量扰动的鲁棒性。

## 实验
为了全面评估 DISTA-Net 的性能，我们在 **CSIST-100K** 数据集上与传统优化 (*ISTA*) 、图像超分辨率和深度展开方法进行了比较。计算效率 (*#P/FLOPs*)、定位精度 (*CSO-mAP*) 和图像质量 (*PSNR/SSIM*) 结果如下：

![](https://fastly.jsdelivr.net/gh/bucketio/img14@main/2025/08/02/1754128472894-5586e8dd-0d39-4095-b6b5-1564088e73a3.png)
<p align="center"><span style="color: #808080">表1 3× 亚像素划分下DISTA在 CSIST-100K 上的表现</span></p>

如**表 1** 所示，我们在 **CSIST-100K** 这一基准数据集上对 *DISTA-Net* 进行了全面的性能比较和评估，**实验结果证明了 DISTA-Net 的 SOTA 性能**。

![](https://fastly.jsdelivr.net/gh/bucketio/img0@main/2025/08/02/1754128591586-928db7e2-b7c0-42da-bbc8-32c042ba5c2f.png)
<p align="center"><span style="color: #808080">图 8  DISTA-Net CSIST-100K 上解混效果可视化对比</span></p>

**图 8** 直观展示了我们方法与部分前沿方法的解混效果对比。可以看出，*DISTA-Net* 不同数量的 *CSIST* 解混中均表现出明显优势，检测结果更加精准可靠。

## 总结
在本研究中，我们针对空间邻近红外小目标解混问题，提出动态迭代收缩阈值网络。通过将传统稀疏重构转化为动态深度展开框架，*DISTA-Net* 自适应生成卷积、阈值参数，显著提升亚像素检测精度。为推动该领域研究，我们引入了**CSIST-100K** 数据集、**CSO-mAP** 评估指标和 **GrokCSO** 工具包，为后续研究提供支持。

## 致谢

本研究由国家自然科学基金（项目编号：*62206133、62301261、62206134、U24A20330、62361166670、62225604*）和深圳科技计划（*JCYJ20240813114237048*）资助。计算资源由南开大学超级计算中心提供。

### 参考文献
<a name="ref1">[1]</a> Sobrino J A, Del Frate F, Drusch M, et al. **Review of thermal infrared applications and requirements for future high-resolution sensors[J].** IEEE Transactions on Geoscience and Remote Sensing, 2016, 54(5): 2963-2972.

<a name="ref2">[2]</a> Kou R, Wang C, Peng Z, et al. **Infrared small target segmentation networks: A survey[J].** Pattern Recognition, 2023, 143: 109788. Pruett K, McNaughton N, Schneider M. **Closely-Spaced Object Classification Using MuyGPyS[J].** arXiv preprint arXiv:2311.10904, 2023.

<a name="ref3">[3]</a> Pruett K, McNaughton N, Schneider M. **Closely-Spaced Object Classification Using MuyGPyS[J].** arXiv preprint arXiv:2311.10904, 2023.

<a name="ref4">[4]</a> Zhao M, Li W, Li L, et al. **Single-frame infrared small-target detection: A survey[J].** IEEE Geoscience and Remote Sensing Magazine, 2022, 10(2): 87-119.

<a name="ref5">[5]</a> Meyer F, Williams J L. **Scalable detection and tracking of geometric extended objects[J].** IEEE Transactions on Signal Processing, 2021, 69: 6283-6298.

<a name="ref6">[6]</a> Hui X U, Liangkui L I N. **Super-resolution method of closely spaced objects based on sparse reconstruction using single frame infrared data[J].** Acta Optica Sinica, 2013, 33(4): 0411001.

<a name="ref7">[7]</a> Chen X, Liu J, Wang Z, et al. **Hyperparameter tuning is all you need for LISTA[J].** Advances in Neural Information Processing Systems, 2021, 34: 11678-11689.

<a name="ref8">[8]</a> Wan Z, He H, Tang B. **A generative model for sparse hyperparameter determination[J].** IEEE Transactions on Big Data, 2017, 4(1): 2-10.

<a name="ref9">[9]</a> Li X, Dong W, Wu J, et al. **Superresolution Image Reconstruction: Selective milestones and open problems[J].** IEEE Signal Processing Magazine, 2023, 40(5): 54-66.

<a name="ref10">[10]</a> Dai Y, Wu Y, Zhou F, et al. **Attentional local contrast networks for infrared small target detection[J].** IEEE transactions on geoscience and remote sensing, 2021, 59(11): 9813-9824.

<a name="ref11">[11]</a> Dai Y, Li X, Zhou F, et al. **One-stage cascade refinement networks for infrared small target detection[J].** IEEE Transactions on Geoscience and Remote Sensing, 2023, 61: 1-17.

<a name="ref12">[12]</a> Gao C, Meng D, Yang Y, et al. **Infrared patch-image model for small target detection in a single image[J].** IEEE transactions on image processing, 2013, 22(12): 4996-5009.

<a name="ref13">[13]</a> Wang H, Zhou L, Wang L. **Miss detection vs. false alarm: Adversarial learning for small object segmentation in infrared images[C]//**Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019: 8509-8518.

<a name="ref14">[14]</a> Dai Y, Wu Y. **Reweighted infrared patch-tensor model with both nonlocal and local priors for single-frame small target detection[J].** IEEE journal of selected topics in applied earth observations and remote sensing, 2017, 10(8): 3752-3767.

<a name="ref15">[15]</a> Vaswani N, Narayanamurthy P. **Static and dynamic robust PCA and matrix completion: A review[J].** Proceedings of the IEEE, 2018, 106(8): 1359-1379.

<a name="ref16">[16]</a> Dai Y, Wu Y, Song Y. **Infrared small target and background separation via column-wise weighted robust principal component analysis[J].** Infrared Physics & Technology, 2016, 77: 421-430.
