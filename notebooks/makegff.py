#!/usr/bin/env python3
import math
import sys
from collections import Counter

import pysam

TARGET_MAX_SCORE = 10


# Pileup counts span a huge range (1 to several thousand in this dataset), so a
# raw count would let a handful of outlier positions dominate the GFF score
# column and flatten every real (but smaller) peak to invisible near MetaScope's
# axis. Log-scaling and normalizing against this run's own max count spreads
# the common low counts across the 1..TARGET_MAX_SCORE range instead.
def compute_score(count, max_count, target_max=TARGET_MAX_SCORE):
    if max_count <= 1:
        return 1
    score = 1 + (target_max - 1) * math.log(count) / math.log(max_count)
    return round(score)


def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: python {sys.argv[0]} <sorted.bam> <output.gff>")
    bam_path, gff_path = sys.argv[1], sys.argv[2]

    # counts[(chrom, strand)][position] = number of reads whose 5' end falls on that position
    counts = {}

    with pysam.AlignmentFile(bam_path, "rb") as bam:
        for read in bam.fetch(until_eof=True):
            if read.is_unmapped:
                continue
            strand = "-" if read.is_reverse else "+"
            # ChIP-exo signal is the read's 5' end: start if '+', end if '-'.
            pos = read.reference_start + 1 if strand == "+" else read.reference_end
            # Strip the FASTA accession version (e.g. NC_000913.3 -> NC_000913) so this
            # track's chromosome ID matches the lab annotation's in MetaScope.
            chrom = read.reference_name.split(".")[0]
            key = (chrom, strand)
            counts.setdefault(key, Counter())[pos] += 1

    max_count = max(
        (c for positions in counts.values() for c in positions.values()), default=1
    )

    with open(gff_path, "w") as gff:
        for (chrom, strand), positions in sorted(counts.items()):
            for pos, count in sorted(positions.items()):
                score = compute_score(count, max_count)
                # MetaScope reads the SIGN of the score (not column 7) to tell + from -
                # strand apart when drawing a track, so encode strand here too.
                if strand == "-":
                    score = -score
                gff.write(
                    f"{chrom}\tmakegff\tfiveprime\t{pos}\t{pos}\t{score}\t{strand}\t.\tdepth={count}\n"
                )


if __name__ == "__main__":
    main()

# terminal 에서 수행할 땐
# cd /workspaces/intern-claude-training/notebooks
# python3 makegff.py ../SRR1168121_sorted.bam chipexo.gff
