# AI-Assisted Bioinformatics Training Curriculum
## Intern Onboarding Program — SBML Lab, KAIST GSEB

**Prepared by:** SBML Lab  
**Submitted to:** Prof. Donghyuk Kim  
**Date:** May 2026  

---

## Executive Summary

This document describes a 6-week intern training curriculum designed to teach new SBML Lab members how to use Claude Code — an AI coding assistant — within the context of real bioinformatics workflows. The curriculum covers the full analysis pipeline that characterizes the lab's ChIP-exo research: reference data retrieval, read alignment, motif discovery, and biological interpretation. The final two weeks are dedicated to an independent mini-project in which each intern designs and executes an original analysis on published FUR ChIP-exo data.

The curriculum is delivered entirely through Jupyter notebooks running on GitHub Codespaces, requiring no local software installation. All bioinformatics tools used by the lab (bowtie2, samtools, MEME Suite, Biopython) are pre-installed in the cloud environment.

---

## Curriculum Structure

The curriculum consists of five modules delivered over six weeks:

| Week | Module | Topic |
|------|--------|-------|
| 1 | Module 1 | Introduction to Claude Code |
| 2 | Module 2 | File parsing and data processing with Claude Code |
| 3 | Module 3 | NGS alignment pipeline with Claude Code |
| 4 | Module 4 | Literature integration, Biopython, and motif analysis |
| 5–6 | Module 5 | Independent mini-project |

Each of Modules 1–4 is a self-contained Jupyter notebook with concept explanations, guided exercises, and conceptual check questions. All five notebooks reside in a shared `notebooks/` directory. Reference data and downloaded files are stored centrally in `data/reference/`.

Three lab-specific slash commands (`/log`, `/debug`, `/explain`) are provided as reusable tools that interns invoke throughout every module. These tools are defined as Markdown skill files in `.claude/skills/` and are used without modification until Module 1 Exercise 4, where interns extend one of them.

---

## Module 1 — Introduction to Claude Code (Week 1)

**Learning objectives:** Understand what Claude Code is and how it differs from a chatbot; learn to write effective prompts; develop a habit of critically evaluating Claude's output; use the three provided lab skills; make a first commit with Claude Code's assistance.

**Content:**

Module 1 establishes the conceptual foundation for all subsequent modules. Interns first learn the operational model of Claude Code: it runs in a terminal, reads and writes files, and executes commands — it is not a web interface. The concept section explains the three modes of use (write code, explain code, debug code) and the principle that specificity of input determines quality of output.

The prompting section closes with an explicit note on critical verification: Claude can be wrong — a flag slightly off, a parameter stated confidently that doesn't match the man page, a biological detail that sounds right but isn't. Interns are encouraged to develop the instinct of checking results when something surprises them or when a claim about the biology doesn't match what they read in a paper. This habit is introduced here and reinforced throughout subsequent modules through conceptual checks that ask interns to form their own understanding before consulting Claude Code.

The three lab-provided skills are introduced:

- `/log` — invoked at the end of every session to record what was accomplished, what broke, and what was learned. This builds a running lab notebook across all six weeks and is the deliverable for sessions that produce no runnable code.
- `/debug` — a structured debugging protocol (reproduce → localize → fix → verify → document) invoked whenever a command or script fails. Interns are required to complete this process before asking for help.
- `/explain` — explains any tool, algorithm, or concept anchored to the lab's context (organism, file formats, experimental technique). Used before resorting to external search.

**Exercises:**

1. *Write a Python script from natural language.* Interns describe a simple star-triangle pattern in plain English and ask Claude Code to produce the script. The goal is first contact with the write-code mode and iterative refinement through follow-up prompts.

2. *Debug a broken script.* A provided Python countdown script contains an intentional bug (incorrect `range()` arguments producing wrong output with no exception). Interns use `/debug` to identify the root cause and apply the minimal fix. This is the first structured use of the debug skill.

3. *Read and invoke the three skills.* Interns read all three skill files, invoke each one at least once, and answer questions about how they work and when to use them.

4. *Extend a skill with lab context.* Interns add one specific detail from `lab-context.md` to the `/explain` skill. This exercise teaches that skills are simply Markdown files — readable, modifiable, and extensible — and that customizing them for a specific context improves their output.

A final session log entry written with `/log` is the required deliverable for Week 1.

---

## Module 2 — File Parsing and Data Processing with Claude Code (Week 2)

**Learning objectives:** Use Claude Code to generate and refine GFF parsing scripts from natural language descriptions; diagnose and fix pandas errors; understand the pandas loading and indexing model.

**Content:**

Module 2 introduces the GFF file format — the lab's primary data representation for genomic features — and the pandas library for structured data processing. The concept section explains GFF column structure (9 tab-delimited columns, 1-based coordinates, attribute field syntax) and how it maps onto a pandas DataFrame.

All exercises use the lab's internal *E. coli* K-12 MG1655 annotation file (`ec_annotation_20100903_DHK_cSRNA_with_ortho.gff`), which contains TSS positions, sRNA annotations, and gene features derived from the lab's published work. This is the same annotation file used in Module 4 and the mini-project.

**Exercises:**

1. *Natural language → GFF parsing script.* Interns describe a filtering task in plain English and ask Claude Code to generate the script. The exercise requires at least two follow-up refinement prompts to teach iterative collaboration.

2. *Debug a broken pandas script.* A provided script contains two bugs: the GFF file is loaded without `header=None`, causing the first data row to be misinterpreted as column names; and column access uses a string name rather than an integer index. Interns use `/debug` to reproduce the `KeyError`, identify both root causes, and apply fixes.

3. *When to use iterrows().* Interns ask Claude Code to explain when `iterrows()` is appropriate and when vectorized operations are preferred. The conceptual check requires writing a one-sentence rule before verifying it with Claude Code.

---

## Module 3 — NGS Alignment Pipeline with Claude Code (Week 3)

**Learning objectives:** Understand the bowtie2 alignment algorithm and samtools post-processing steps at a conceptual level; use plan mode to generate and review a full pipeline before execution; write a custom BAM-to-GFF conversion script using pysam.

**Content:**

Module 3 is the most technically substantial module. It covers the complete single-end ChIP-exo alignment workflow that the lab uses for transcription factor binding site mapping: reference indexing, read alignment with bowtie2, coordinate-sorted BAM generation with samtools, and conversion to GFF format for MetaScope visualization.

The module opens with a file format reference table (FASTQ, FASTA, SAM, BAM, GFF) and asks interns to use Claude Code to identify which format each step of the pipeline produces. This grounds subsequent exercises in the actual data flow.

The concept section explains bowtie2's FM-index and seed-and-extend model without requiring interns to know alignment theory in advance — Claude Code is used as the explanation tool. Similarly, samtools' use of coordinate sorting for efficient random access and the role of the `.bai` index file are explained through directed prompts.

**Exercises:**

1. *Understand bowtie2.* Before running any command, interns use Claude Code to understand how bowtie2 finds alignments and what the key flags control. A 3-sentence summary in the intern's own words is required.

2. *Sort-before-index reasoning.* Without asking Claude Code first, interns write an explanation of why BAM files must be sorted before indexing. This is a conceptual check verified afterward with Claude Code.

3. *Plan mode pipeline.* Using plan mode (Shift+Tab, requires Pro plan), interns generate the full pipeline from reference indexing through sorted BAM. They are required to review every proposed step before approving and to identify at least one thing they would change. This is the first formal use of plan mode.

4. *Find and download ChIP-exo reads.* Interns navigate to GEO series GSE54901, identify an appropriate single-end ChIP-exo SRR accession themselves, and use Claude Code to download it. No command is provided in advance. This mirrors the real workflow of retrieving data for a new project.

5. *Decode a SAM FLAG value.* Interns choose a FLAG value they have not previously looked up and use Claude Code to decode its bitwise components. This introduces the SAM specification and binary encoding.

6. *Write makegff.py.* Interns write the lab's custom BAM-to-GFF conversion script using pysam. The script reads a sorted, indexed BAM file and outputs one GFF line per aligned read, with 1-based coordinates and strand information. The expected output format is specified:

   ```
   NC_000913.3  makegff  read  <start>  <end>  1  <strand>  .  name=<read_name>
   ```

   This exercise integrates all preceding knowledge — BAM format, GFF column structure, pysam API, and coordinate conventions — into a single deliverable.

The reference genome (NC_000913.3) is also retrieved by interns using Claude Code, with only the NCBI accession provided as a starting point.

---

## Module 4 — Literature Integration, Biopython, and Motif Analysis (Week 4)

**Learning objectives:** Extract structured information from published papers using Claude Code; retrieve public ChIP-exo data from GEO; write Biopython scripts for sequence extraction; run MEME Suite for motif discovery; interpret motif results biologically.

**Content:**

Module 4 brings all preceding skills together around a real published dataset: the FUR (Ferric Uptake Regulator) ChIP-exo study in *E. coli* by Seo et al. (2014), available from GEO accession GSE54901. FUR is a global iron-responsive transcription factor in *E. coli* that represses iron acquisition genes under iron-replete conditions — a well-characterized system suitable as a training case because the expected motif (the Fur box) is known from literature.

The concept section introduces the MEME algorithm (expectation-maximization over sequence windows) and explains E-value interpretation. The `-mod zoops` model (zero or one occurrence per sequence) is used, appropriate for ChIP-exo data where each peak may or may not contain the canonical binding motif. Interns are asked to reason about which flag accounts for FUR binding to double-stranded DNA before consulting Claude Code.

**Exercises:**

1. *Read Seo et al. 2014.* Interns read the paper and write a 3-sentence summary: what the experiment measured, what organism and condition were used, and what the main finding was. The concept cell does not pre-state the results.

2. *Cross-check the FUR regulon.* Using Claude Code, interns identify what other published reference gene sets exist for the FUR regulon and how they were determined. This contextualizes the Seo et al. dataset within the broader literature.

3. *Understand MEME.* Before running any command, interns write a 3-sentence explanation of how MEME works and what E-value means. This is verified against Claude Code's explanation after writing.

4. *Download data from GEO using Claude Code.* Interns provide the GEO series URL to Claude Code and ask it to download the FUR ChIP-exo peak GFF file and the reference genome FASTA. This exercise practices the real workflow of retrieving public data for analysis.

5. *Write a Biopython sequence extraction script.* Using the downloaded peak coordinates and reference genome, interns write a Biopython script to extract ±50 bp windows around each peak summit and write them to a multi-FASTA file for MEME input.

6. *Run MEME and interpret the output.* Interns construct the MEME command with Claude Code's help and run it on the extracted sequences. They then interpret the output file and assess whether the top motif is biologically meaningful, with written justification.

7. *TSS distance analysis.* Using the lab's annotation GFF, interns write a Python script to compute the distance between each FUR binding site and the nearest annotated TSS. This connects the binding site coordinates to a biological question about regulatory proximity.

---

## Module 5 — Independent Mini-Project (Weeks 5–6)

**Learning objectives:** Formulate an original biological question from a real dataset; design and execute a complete analysis pipeline with Claude Code assistance; interpret results in the context of published literature; write a reproducible analysis report.

**Content:**

The mini-project is an open-ended independent analysis on the same FUR ChIP-exo dataset used in Module 4. No new dataset is introduced. Interns have access to all tools installed in the Codespace environment and may use Claude Code to acquire additional tools or datasets if their question requires them.

The project spans six days with defined milestones:

| Day | Milestone |
|-----|-----------|
| 1 | Literature review complete; biological question drafted |
| 2 | Question refined and approved (instructor check-in) |
| 3 | Analysis plan written and plan-mode pipeline generated |
| 4 | Pipeline executing; at least one result figure produced |
| 5 | Analysis complete; all figures finalized |
| 6 | Report written and notebook submitted |

**Structure:**

*Part 1 — Literature context.* Interns use Claude Code to survey what is known about FUR beyond Seo et al. 2014: other ChIP studies, the known Fur box consensus, genes in the FUR regulon, and condition-dependent binding. This grounds the subsequent question in existing knowledge.

*Part 2 — Biological question.* Interns propose one specific, biologically motivated question answerable from the FUR ChIP-exo data. Examples of acceptable questions include: "Do FUR binding sites with higher peak scores show stronger motif matches?", "Which genes in the lab annotation have a FUR binding site upstream, and what functions do those genes serve?", "Are FUR binding sites enriched near sRNA genes compared to protein-coding genes?", or "How does GC content at FUR sites compare to random genomic windows?" Vague questions ("What genes does FUR regulate?") are not accepted. An instructor check-in is required before proceeding.

*Part 3 — Analysis plan.* Interns write a plain-English analysis plan independently. Plan mode is then used to ask Claude Code to draft the full pipeline; interns must annotate each proposed step with their own understanding before approving.

*Part 4 — Pipeline execution.* Interns execute the analysis with Claude Code assistance. All errors are handled via `/debug`. All sessions are logged via `/log`.

*Part 5 — Results.* Interns produce at least one figure and write an interpretation of their findings — what the result means biologically, whether it is novel, confirmatory, or unexpected relative to the literature.

*Part 6 — Report.* A written report in Markdown cells covers: biological question and motivation, methods (reproducible step-by-step), results (with figures), and interpretation. Claude Code may be used for writing assistance but is not required.

---

## Assessment

The mini-project is assessed on five criteria totaling 100 points:

| Criterion | Weight | What is Assessed |
|-----------|--------|-----------------|
| Question quality | 20% | Specificity, biological motivation, literature grounding |
| Claude Code usage | 20% | Thoughtful use throughout the pipeline; ability to explain all generated code; evidence of `/debug` and `/log` usage; plan mode for pipeline generation |
| Analysis correctness | 30% | End-to-end execution without errors; reproducibility; biologically plausible outputs |
| Biological interpretation | 20% | Explanation of what results mean, relation to literature, characterization as novel / confirmatory / unexpected |
| Report clarity | 10% | Reproducible methods, results matching figures, clear writing |

Modules 1–4 are not formally graded. Progress is assessed through the presence of session `/log` entries and completion of exercises within each notebook.

---

## Technical Environment

All tools are pre-installed via GitHub Codespaces using a conda environment (`sbml`) built during Codespace initialization. Interns authenticate Claude Code with a personal Claude Pro plan account after launch.

**Installed tools:**

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11 | Primary programming language |
| bowtie2 | latest | Short-read alignment |
| samtools | latest | BAM processing |
| bedtools | latest | Genomic interval operations |
| sra-tools | latest | SRA/GEO data download |
| MEME Suite | latest | Motif discovery |
| Biopython | latest | FASTA parsing and sequence manipulation |
| pysam | latest | BAM file parsing (Python) |
| pandas | latest | Tabular data processing |
| matplotlib / seaborn | latest | Visualization |
| scipy | latest | Statistical analysis |
| entrez-direct | latest | NCBI data retrieval via command line |
| Claude Code CLI | latest | AI coding assistant |

**Reference data provided by instructor before distribution:**

- `ec_annotation_20100903_DHK_cSRNA_with_ortho.gff` — lab's internal *E. coli* K-12 MG1655 annotation with TSS positions and sRNA annotations (used in Modules 2, 4, and the mini-project)

All other data (reference genome, ChIP-exo reads, ChIP-exo peak GFF) is retrieved by interns as part of the exercises.

---

## Design Principles

The curriculum was designed around four principles:

**1. Interns discover answers through Claude Code, not from pre-filled cells.** No exercise answer is provided in advance. All code cells start empty. Even data retrieval commands (SRA accession lookup, reference genome download) are not given — interns use Claude Code to figure out what to run and navigate public databases themselves.

**2. Every module uses real lab data and real tools.** Module 2 uses the actual lab annotation GFF. Module 3 uses a real ChIP-exo FASTQ from NCBI SRA. Module 4 uses the published Seo et al. 2014 FUR dataset from GEO. The mini-project is an original analysis on the same data. Interns complete the training having run the same tools on the same data types they will encounter in lab work.

**3. Claude Code is a tool to understand, not a shortcut to avoid understanding.** Each module includes at least one conceptual check where interns must write their own explanation before consulting Claude Code. Plan mode is required for all pipeline-generating prompts, forcing review and approval of every proposed step. The assessment criterion for Claude Code usage explicitly rewards the ability to explain generated code, not simply the ability to generate it.

**4. Critical verification is a habit, not a step.** Interns are introduced in Module 1 to the idea that Claude can be wrong — a flag slightly off, a biological claim that doesn't match the paper. Rather than enforcing formal cross-check steps, the curriculum builds this as instinct: conceptual checks run in both directions (write before you ask, verify after you receive), and interns are expected to notice when a result or explanation doesn't feel right and investigate it.
