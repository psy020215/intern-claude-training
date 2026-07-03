FROM mcr.microsoft.com/devcontainers/miniconda:3

# Configure channels (bioconda last = highest priority for bioinformatics tools)
RUN conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda config --set channel_priority flexible

# Install mamba and create sbml env (meme excluded — 5.5.x Perl deps removed from bioconda)
RUN conda install -n base -c conda-forge mamba -y && \
    mamba create -n sbml -y python=3.11 \
      ipykernel jupyter notebook \
      bowtie2 samtools bedtools sra-tools \
      biopython pysam scipy pandas matplotlib seaborn entrez-direct && \
    conda clean -afy

# Install meme in a separate layer pinned to 5.4.1 (predates perl-sys-info dep chain)
RUN /opt/conda/bin/mamba install -n sbml -y -c bioconda -c conda-forge "meme=5.4.1" && \
    conda clean -afy

# Set sbml env as default in PATH — no conda activation needed
ENV PATH="/opt/conda/envs/sbml/bin:/opt/conda/bin:${PATH}"

# Install Node.js 20 and Claude Code CLI at image build time
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @anthropic-ai/claude-code && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
