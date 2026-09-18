---
layout: page
title: "研究经历"
permalink: /research/
lang: zh-CN
alternate_url: /en/research/
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/profile.css' | relative_url }}">
<div class="profile-content">
<section class="entry" id="expath"><h3>eXpath · 知识图谱链接预测解释</h3><div class="meta">2024.01–2025.01 · PVLDB / VLDB 2025 · 第一作者 · 已录用</div><ul class="project-points"><li><strong>项目描述：</strong> 融合本体闭环规则与关系路径证据，设计规则挖掘和路径搜索算法；两个解释质量指标约提升 20%，解释耗时减少 61.4%。</li><li><strong>主要贡献：</strong> 针对嵌入式链接预测缺乏可理解语义证据的问题，将关系路径与本体闭环规则结合，生成结构化解释；独立完成问题提出、方法设计、实现、实验分析与论文撰写；将规则挖掘和路径搜索落地为可评测的解释框架；在论文基准实验中，相比最佳对比方法，两个解释质量指标约提升 20%、解释耗时减少 61.4%；这些数字衡量解释质量与效率。</li></ul><div class="entry-links"><a href="https://github.com/cs-anonymous/eXpath">代码 ↗</a></div></section>
<section class="entry" id="ruledep"><h3>RuleDep · 依赖感知的规则聚合</h3><div class="meta">2025.08–2026.06 · ICDE 2027 · 第一作者 · 已录用</div><ul class="project-points"><li><strong>项目描述：</strong> 显式建模规则之间的互补与冗余，以稀疏二阶修正和两阶段训练改进聚合；七数据集平均 MRR 相比 LR-Agg 提升约 3.7%。</li><li><strong>主要贡献：</strong> 研究共同触发规则的依赖关系，在 log-failure evidence 空间引入带符号增益，区分互补证据与冗余证据；独立完成方法、算法实现与实验；以 Kotlin/JVM 编写核心实现，结合 CPU 多线程和原子操作管理共享状态；RuleDep-ens 的七数据集平均 MRR 从 0.382 提升至 0.396；在可解释方法比较中，21 项指标最佳或并列最佳。</li></ul><div class="entry-links"><a href="https://github.com/cs-anonymous/RuleDep">代码 ↗</a></div></section>
<section class="entry" id="geneticprism"><h3>GeneticPrism · 层次图设计与布局算法</h3><div class="meta">2023.09–2024.08 · IEEE TVCG · 第一作者 · 已录用</div><ul class="project-points"><li><strong>项目描述：</strong> 提出多主题研究演化的层次图表示与 IFHL 布局，联合组织主题内引用和跨主题影响；通过案例分析与 20 人用户研究评估。</li><li><strong>主要贡献：</strong> 设计 GeneticPrism 总览与 GeneticScroll 局部视图，支持主题重叠、时间演化及跨主题影响的多尺度分析；设计 Integrated Flow Hierarchical Layout（IFHL），将主题内部引用与跨主题流入／流出共同纳入分层布局，结合代理节点、加权交叉优化与边捆绑；独立完成研究设计、算法实现、实验和写作；采用三个案例及 20 人用户研究评估。问卷七个维度均报告 p &lt; .001，反映主观可用性与感知有效性。</li></ul><div class="entry-links"><a href="https://github.com/visdata/GeneticPrism">代码 ↗</a><a href="https://genetic-flow.com/">在线系统 ↗</a></div></section>
<section class="entry" id="inspire"><h3>INSPIRE · 表现力钢琴演奏生成</h3><div class="meta">2026.04–2026.08 · AAAI 2027 在投 · 第一作者</div><ul class="project-points"><li><strong>项目描述：</strong> 以音符级结构化表示、谱面相对时序建模和连续分布预测实现演奏生成，独立完成数据处理、模型、训练与评估。</li><li><strong>主要贡献：</strong> 将音符属性融合为单个 Transformer 时间步，以类型化编码和谱面相对时序偏差建模表现力控制；基于 PyTorch 与 Transformers 实现自定义模型组件和训练逻辑，贯通预处理、训练、推理及多粒度分布评估；ASAP 测试中，CINR-bounded 的 PP Human-Relative Wasserstein 相比 Pianist Transformer 下降 15.2%；指定测试任务推理成本由 126.4 降为 6.0 GPU-minutes。</li></ul></section>
<section class="entry" id="cueir"><h3>CueIR · Agent 长期记忆</h3><div class="meta">2026.08–至今 · 在研</div><ul class="project-points"><li><strong>项目描述：</strong> 研究可追溯的记忆组织与检索，已跑通记忆图构建及智能体工具，并在 LoCoMo 与 MemoryAgentBench 数据集上开展实验验证。</li></ul></section>

</div>
