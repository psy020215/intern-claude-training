# Reference Data

All data used across modules lives here. Notebooks reference files as `../data/reference/<filename>`.

---

## Pre-provided (instructor copies before distributing)

| File | Description | Used in |
|------|-------------|---------|
| `ec_annotation_20100903_DHK_cSRNA_with_ortho.gff` | *E. coli* K-12 MG1655 annotation with TSS positions and sRNA annotations | M2, M4 Exercise 7, Mini-project |

---

## Module 3 — Downloads

No files are pre-loaded. Download as part of the exercises.

**Reference genome** — *E. coli* K-12 MG1655, accession **NC_000913.3**:
```bash
efetch -db nucleotide -id NC_000913.3 -format fasta > data/reference/NC_000913.fasta
```

**ChIP-exo reads** — use the SRR accession your instructor provided:
```bash
fastq-dump [SRR_ACCESSION] --outdir data/reference/ --skip-technical
mv data/reference/[SRR_ACCESSION].fastq data/reference/reads.fastq
```

After downloading, this directory should contain:
```
data/reference/
├── NC_000913.fasta
└── reads.fastq
```

---

## Module 4 — Downloads

Use Claude Code to fetch these. Give it the GEO series URL and ask it to download to `data/reference/`:
```
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE54901
```

- Fur ChIP-exo peak GFF (iron-replete condition)
- `NC_000913.fasta` (same file as Module 3 — skip if already downloaded)

---

## Mini-project — Cohort dataset

Added by the instructor before distributing. See `instructor/BEFORE_DISTRIBUTING.md`.
