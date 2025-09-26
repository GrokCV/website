---
title: 新芽专题介绍（46）：高性能向量检索系统
date: 2025-09-17T01:05:00Z
draft: false
math: true
---

## 一、专题介绍

### 1.1  研究背景

随着人工智能和大数据技术的快速发展，海量高维数据的快速检索与匹配已成为推荐系统、多模态搜索、大模型增强等众多应用的核心需求。向量检索系统通过将数据转化为高维向量并借助近似最近邻搜索（ANNS）技术，实现高效相似性匹配，是当前工业界与学术界的研究热点。


### 1.2  研究意义

向量检索已经成为搜索引擎和大模型系统的基础设备，具体的应用方向包括但不限于：

1. **检索增强生成（RAG）**：使用向量检索得到相关文档增强大模型的生成质量。

2. **搜索引擎**：根据用户输入得到更准备的搜索结果，应用于电商平台、短视频平台等。

这一研究主题是智能时代数据管理的核心问题，也适合作为本科生进入科研领域的尝试方向。

### 1.3  当前主要挑战

然而，面对数据规模的不断膨胀和应用场景的日益复杂，现有向量检索系统在精度、效率、可扩展性以及硬件适配方面仍面临诸多挑战。

1. **挑战一：精度和效率难以平衡**

   * 为了提升速度，向量检索系统通常采用近似搜索。

   * 另一方面，系统对检索结构精度也有极高的要求。

   * 只能时代巨大的数据规模进一步加剧了这一挑战。

2. **挑战三：难以充分利用底层硬件能力**

   * 数据量的爆炸使得向量索引需要大量存储空间，但向量索引在廉价的SSD等设备上性能较差。

   * 向量索引的计算需求较大，但经典的索引结构难以使用GPU等进行加速。

2. **挑战三：与大模型推理服务欠缺适配**

   * 向量检索+大模型共同组成的RAG系统愈发火爆，但二者只是**浅耦合**，欠缺统一系统优化。

   * 多模态大模型的发展需要支持多模态数据的向量检索系统。

本课题聚焦于向量检索系统的核心算法优化与架构创新，涵盖索引结构设计、查询加速、硬件协同等多个前沿方向。学生将深入理解向量检索的技术原理与系统实现，结合新型存储技术和机器学习技术，探索下一代向量检索系统的实现路径，并有机会在高水平会议或期刊中发表研究成果。

***

## 二、学习资料与参考文献

为了引导新芽学子逐步进入研究，本专题结构分为以下四部分：

***

### 2.1  基础教材与学习材料

在开始探险之前，你需要掌握一些基础的“内功心法”，这些是后续一切学习的基石。

先从向量的相似度和ANN问题了解起：
* [向量的相似度-【余弦相似度，点积，L1，L2】](https://zhuanlan.zhihu.com/p/660426812)——了解如何衡量向量之间的相关性
* [什么是向量的KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)——维基百科介绍
* [从KNN到ANN](https://sefiks.com/2023/07/27/k-nn-vs-approximate-nearest-neighbors/)——ANN算法存在的意义
* [ANN算法性能的评估维度](https://apxml.com/zh/courses/vector-databases-semantic-search/chapter-3-approximate-nearest-neighbor-search/evaluating-ann-performance)——如何衡量一个ANN算法的好坏

你需要了解的编程知识：
* [树、图](https://zhuanlan.zhihu.com/p/622191693)，[堆](https://zhuanlan.zhihu.com/p/615541177)，[聚类(KMeans)](https://zhuanlan.zhihu.com/p/391877604)——数据结构&算法基础
* [用邻接矩阵存储图结构](https://www.cnblogs.com/helloylh/p/17209626.html)
* C++ STL中的[vector](https://www.runoob.com/cplusplus/cpp-vector.html)、[priority queue](https://www.runoob.com/cplusplus/cpp-libs-priority_queue.html)

初步了解以上之后，可以先通过以下几个综合性博客对ANN算法的分类有初步了解：
* [理解近似最近邻 (ANN) 算法](https://www.elastic.co/cn/blog/understanding-ann)
* [Nearest Neighbor Indexes for Similarity Search](https://www.pinecone.io/learn/series/faiss/vector-indexes/)——经典算法全解析
* [经典向量索引](https://yongyuan.name/blog/vector-ann-search.html)——一篇广度深度兼顾的中文博客

一些主流开源**工具**：
* [Faiss](https://github.com/facebookresearch/faiss)：最主流的ANN算法库，可以参考这个[个人开发者的入门指导](https://github.com/LandonZhang/FAISS-Tutorial)，学习如何调用Faiss提供的算法。
* [ann-benchmarks](https://github.com/erikbern/ann-benchmarks)：现有算法的性能基准测试平台，也可以在这里下载常用数据集。

Tips：务必**摆脱所有基础都打好后，再进行下一阶段学习的心态**，在干中学，遇到不明白的再回溯补基础。

***

### 2.2  入门文献/资料（向量检索经典算法）

> 学生第一阶段的阅读训练，可帮助理解向量检索这一通用方向，研究主流为**基于倒排（聚类）的索引和图索引**。**仅用于入门，不可选择此部分文献汇报**。

* **[ANNS综述](https://www.vldb.org/pvldb/vol14/p1964-wang.pdf): A Comprehensive Survey and Experimental Comparison of Graph-Based Approximate Nearest Neighbor Search (VLDB 2021)**

* **[IVFPQ](https://zhuanlan.zhihu.com/p/378725270): Inverted File with Product Quantization——工业界常见选择，[Milvus文档-IVFPQ](https://milvus.io/docs/zh/ivf-pq.md)(对倒排结构描述更加简洁)**



* **[Graph-based ANNS综述](https://dl.acm.org/doi/abs/10.1145/3709693): Graph-Based Vector Search: An Experimental Evaluation of the State-of-the-Art (SIGMOD 2025）**

* **[DiskANN](https://proceedings.neurips.cc/paper_files/paper/2019/file/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Paper.pdf): DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node (NeurIPS 2019）**

* **[NSW](https://www.hse.ru/data/2015/03/13/1325528089/Approximate%20nearest%20neighbor%20algorithm%20b..navigable%20(Information%20Systems).pdf): Approximate nearest neighbor algorithm based on navigable small world graphs (IS 2014）**

* **[HNSW](https://proceedings.neurips.cc/paper_files/paper/2019/file/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Paper.pdf): Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs  (TPAMI 2018）**

* **图索引相关的辅助阅读资料：[理解近似最近邻 (ANN) 问题中的图算法](https://zhuanlan.zhihu.com/p/610454162)，[从Delaunay graph到HNSW Graph](https://hustai.github.io/zh/posts/rag/HNSW.html)**

***