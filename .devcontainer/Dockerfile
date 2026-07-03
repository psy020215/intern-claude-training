# Stage 1: Official MEME Suite image — get pre-compiled binaries
FROM memesuite/memesuite:5.5.9 AS meme-stage

# Stage 2: Main devcontainer
FROM mcr.microsoft.com/devcontainers/miniconda:3

# Copy MEME Suite binaries from official image (bypasses bioconda Perl version conflicts entirely)
COPY --from=meme-stage /usr/local/bin/meme /usr/local/bin/meme
COPY --from=meme-stage /usr/local/bin/fimo /usr/local/bin/fimo
COPY --from=meme-stage /usr/local/bin/ame /usr/local/bin/ame
COPY --from=meme-stage /usr/local/bin/sea /usr/local/bin/sea
COPY --from=meme-stage /usr/local/bin/meme-chip /usr/local/bin/meme-chip
# Copy MEME data files (path varies by version: meme-5.5.9 or meme)
COPY --from=meme-stage /usr/local/share/ /tmp/meme-share-src/
RUN find /tmp/meme-share-src -maxdepth 1 -name 'meme*' -exec cp -r {} /usr/local/share/ \; && \
    rm -rf /tmp/meme-share-src

# Install Perl + libs needed for meme-chip Perl scripts at runtime
RUN apt-get update && apt-get install -y perl libexpat1 zlib1g && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Configure conda channels (bioconda last added = highest priority)
RUN conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda config --set channel_priority flexible

# Create sbml env — python=3.11, all tools EXCEPT meme (no Perl conflict now)
RUN conda install -n base -c conda-forge mamba -y && \
    mamba create -n sbml -y python=3.11 \
      ipykernel jupyter notebook \
      bowtie2 samtools bedtools sra-tools \
      biopython pysam scipy pandas matplotlib seaborn entrez-direct && \
    conda clean -afy

# Make sbml env active by default — no conda activate needed
ENV PATH="/opt/conda/envs/sbml/bin:/opt/conda/bin:${PATH}"

# Install Node.js 20 and Claude Code CLI
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @anthropic-ai/claude-code && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
