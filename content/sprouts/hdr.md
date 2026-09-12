---
title: 新芽专题介绍（20）：超高动态范围与广色域显示适配
date: 2025-09-18T01:40:00Z
draft: false
math: true
---

> 选择此专题并在新芽系列课程中获得优秀的同学，可以免去前期筛选考核流程，直接进入南开大学媒体计算团队以及国家人工智能学院等合作院校团队推免生招收面试的最后一轮。

## 一、专题介绍

### 1.1 研究背景

随着显示硬件（如Mini-LED、OLED）的飞速发展，显示器的峰值亮度已从传统的100cd/m2(SDR)跨越至1000cd/m2甚至4000cd/m2以上(HDR)，色域也从Rec.709演进至近乎覆盖Rec.2020。然而，内容创作与终端显示之间存在严重的不对等现象：高质量的HDR原始素材往往承载了远超普通显示器物理极限的信息量；同时，现存的大量SDR内容亦无法充分体现先进硬件的效果优势。

色调映射与色域转换不再仅仅是一个简单的线性缩放过程，而是一门平衡物理亮度限制与人类视觉感知（HVS）的艺术。如何在高动态范围、广色域的信息流中，精准地将“导演意图”适配到千差万别的显示终端上，是当前计算摄像学与显示工程领域的核心课题。

### 1.2 研究意义

本研究旨在构建从“高位深物理亮度”到“感知一致性显示”的桥梁，具有深厚的学术价值与工业应用意义：

捍卫创作者意图：通过显式适配算法，确保同一部HDR影片在2000nits的专业监视器和400nits的移动设备上都能保持一致的氛围感与暗部细节，避免出现“死黑”或“过曝”。

突破感知极限：利用视觉模型优化量化曲线，在有限的带宽和位深下消除色彩断层，实现肉眼不可分辨的平滑过渡。

软硬结合的实时管线：结合现代图形API与异构计算，探索高性能的实时色调映射算子，为8K/120fps等极端性能场景提供低延迟的处理方案。

### 1.3 当前主要挑战

理解HDR适配的复杂性，需要深入探讨以下三个维度：

**挑战1：艺术意图与物理约束的非线性对齐**

当面临从4,000nits（理想母版）到500nits（主流显示器）的剧烈压缩时，算法必须在保留高光纹理与维持中灰度亮度之间做出抉择。如何定义一个“感知上正确”的映射方式，并将其参数化，使之既符合物理定律又符合人眼感知，是适配算法的首要难题。

**挑战2：视频流的时间相干性与闪烁抑制**

在动态场景下，两帧之间的亮度分布可能会剧烈变化。如果逐帧独立应用色调映射，会导致画面出现明显的亮度跳变或呼吸感。研究如何在保持艺术意图的同时，利用时域滤波或记忆机制实现平滑的曝光补偿，是确保视频观看舒适度的技术关键。

**挑战3：色域压缩中的色相恒常性**

在广色域转换过程中，单纯的亮度压缩往往伴随着饱和度的丢失或色相的偏移。如何在Rec.2020到Rec.709的映射中保持色貌的稳定性，确保肤色、天空等记忆色在不同显示基准下的一致性，需要复杂的3D-LUT优化或基于感知空间的数学建模。

张茂军《计算摄影学基础》

***

## 二、学习资料与参考文献

***

### 2.1 基础教材与学习材料

* 张茂军《计算摄影学基础》——适合中文初学者的HDR与色彩科学入门教材（资料链接：自行搜索）
* Fairchild, Mark D., Color Appearance Models——经典的色貌模型教材，译本可见https://shuwei666.github.io/Color-appearance-models/（资料链接：自行搜索）
* 李沐《动手学深度学习》——适合中文初学者的深度学习教材（资料链接：自行搜索）
* HDR10+ Technologies, LLC, Understanding the HDR10 Ecosystem——适合了解HDR产业的入门资料（资料链接：自行搜索）

***

### 2.2 入门文献

* High Dynamic Range Image Tone Mapping: Literature review and performance benchmark（Digital Signal Processing 2023）——自行搜索
* Photographic Tone Reproduction for Digital Images（TOG2002）——自行搜索
* Fast Bilateral Filtering for the Display of High-Dynamic-Range Images（SIGGRAPH2002）——自行搜索
* Objective Quality Assessment of Tone-Mapped Images（TIP2012FovVideoVDP: A visible difference predictor for wide field-of-view video）——自行搜索

***

### 2.3 进阶文献

* FovVideoVDP: A visible difference predictor for wide field-of-view video（TOG2021）——自行搜索
* Zero-Shot Structure-Preserving Diffusion Model for High Dynamic Range Tone MappingCVPR2024（CVPR2024）——自行搜索
* Perceptually Adaptive Real-Time Tone Mapping:（SIGGRAPH ASIA 2023）——自行搜索
* Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement（CVPR2020）——自行搜索

***

### 2.4 领域相关文献

* BT.2100-3-2025（2025）——Image parameter values for high dynamic range television for use in production and international programme exchange
* BT.2390-12-2025（2025）—— High dynamic range television for production and international programme exchange
* T/UWA 005.1-2024（2024）——高动态范围（HDR）视频技术 第1部分:元数据及适配

***

## 三、结语与期望

“新芽计划”的初心，是点燃新芽学子对未知探索的热情，并为大家提供一片成长的沃土。面向超高动态范围与广色域的显式适配是一个兼具底层科学探索与尖端工程实践的跨学科研究方向，它不仅要求我们透彻理解色度学、物理光学与人眼视觉系统的生理逻辑，更要求我们将这些复杂的色调映射算法实装到实时显示管线与异构计算框架中，去解决真实硬件环境下对比度受限、色相漂移与跨设备显示一致性的核心难题，并最终引领数字影像步入“所见即所得”的高保真感知显示新纪元。

<!-- 来源：减论 Reduct 已发布专题 超高动态范围与广色域显示适配；文件头日期为导出时间。 -->
