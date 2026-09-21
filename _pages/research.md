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
<section class="entry" id="geneticprism"><h3>层次图布局算法与学术脉络可视分析 GeneticPrism (TVCG 2025, CCF-A)</h3><div class="meta">2023.09–2024.08 · 第一作者 · 已发表</div><ul class="project-points"><li>针对多主题研究演化中主题内引用与跨主题影响难以联合表征的问题，提出层次图表示方法并设计 IFHL（Integrated Flow Hierarchical Layout）布局，将两类关系纳入统一可视化框架，支撑复杂演化结构的表达。</li><li>主导设计 GeneticPrism 总览视图与 GeneticScroll 局部视图，覆盖主题重叠、时间演化及跨主题影响三类分析场景，实现多尺度联动探索，提升分析效率与洞察深度。</li></ul><div class="entry-links"><a href="https://github.com/visdata/GeneticPrism">代码 ↗</a><a href="https://genetic-flow.com/">在线系统 ↗</a></div></section>
<section class="entry" id="expath"><h3>知识图谱可解释推理框架 eXpath (VLDB 2025, CCF-A)</h3><div class="meta">2024.01–2025.01 · 第一作者 · 已发表</div><ul class="project-points"><li>针对嵌入式模型决策过程缺乏语义证据的黑盒难题，独立提出融合本体闭环规则与关系路径证据的解释框架。</li><li>设计规则挖掘与路径搜索协同的结构化解释生成机制，将本体闭环规则与关系路径证据有机整合，构建可量化评测的解释框架，有效弥补现有方法在语义可理解性方面的不足。</li><li>在标准基准实验中，相较最优对比方法，两项解释质量指标提升约 20%，解释生成耗时降低 61.4%，验证了框架在解释效果与计算效率上的双重优势。</li></ul><div class="entry-links"><a href="https://github.com/cs-anonymous/eXpath">代码 ↗</a></div></section>
<section class="entry" id="ruledep"><h3>依赖感知的规则聚合 RuleDep (ICDE 2027, CCF-A)</h3><div class="meta">2025.08–2026.06 · 第一作者 · 已录用</div><ul class="project-points"><li>针对规则聚合中互补与冗余关系未被显式建模的问题，主导设计稀疏二阶修正机制与两阶段训练框架，通过建模共同触发规则间的依赖结构，在 log-failure evidence 空间引入带符号增益以区分互补证据与冗余证据。</li><li>在七个数据集上实现平均 MRR 从 0.382 提升至 0.396，在可解释方法对比中取得 21 项指标最佳或并列最佳，并在依赖丰富子集上实现 MRR 约 10.7% 的提升。</li></ul><div class="entry-links"><a href="https://github.com/cs-anonymous/RuleDep">代码 ↗</a></div></section>
<section class="entry" id="inspire"><h3>表现力钢琴演奏生成 INSPIRE (AAAI 2027, CCF-A)</h3><div class="meta">2026.04–2026.06 · 第一作者 · 在投</div><ul class="project-points"><li>构建音符级结构化演奏生成框架，通过相对时序建模与连续分布预测，实现从离散符号到富有表现力演奏的生成。</li><li>设计类型化编码方案，将音高、时值、力度等多维音符属性融合为单一 Transformer 时间步输入，并引入谱面相对时序偏差建模，显著增强模型对演奏表现力的细粒度控制能力。</li><li>在 ASAP 基准测试中，PP HR 指标较 PianistTransformer 降低 15.2%，验证了生成演奏在表现力分布上的显著优势。通过架构与推理流程优化，将指定测试任务的推理成本降低达 95.3%，大幅提升方案的可部署性与迭代效率。</li></ul></section>
<section class="entry" id="cueir"><h3>CueIR · Agent 长期记忆</h3><div class="meta">2026.08–至今 · 在研</div><ul class="project-points"><li>研究可追溯的记忆组织与检索，已跑通记忆图构建及智能体工具，并在 LoCoMo 与 MemoryAgentBench 数据集上开展实验验证。</li></ul></section>

</div>
