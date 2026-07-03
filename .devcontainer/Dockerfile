FROM mcr.microsoft.com/devcontainers/miniconda:3

# Configure channels
RUN conda config --add channels defaults && \
    conda config --add channels bioconda && \
    conda config --add channels conda-forge && \
    conda config --set channel_priority strict

# Install mamba and create sbml env at IMAGE BUILD TIME
RUN conda install -n base -c conda-forge mamba -y && \
    mamba create -n sbml -y python=3.11 \
      ipykernel jupyter notebook \
      bowtie2 samtools bedtools sra-tools meme \
      biopython pysam scipy pandas matplotlib seaborn entrez-direct && \
    conda clean -afy

# Set sbml env as default in PATH — no conda activation needed
ENV PATH="/opt/conda/envs/sbml/bin:/opt/conda/bin:${PATH}"

# Install Node.js 20 and Claude Code CLI at image build time
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @anthropic-ai/claude-code && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
