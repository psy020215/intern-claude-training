#!/usr/bin/env python3
import sys
from collections import Counter

import pysam


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
            key = (read.reference_name, strand)
            counts.setdefault(key, Counter())[pos] += 1

    with open(gff_path, "w") as gff:
        for (chrom, strand), positions in sorted(counts.items()):
            for pos, count in sorted(positions.items()):
                gff.write(
                    f"{chrom}\tmakegff\tfiveprime\t{pos}\t{pos}\t{count}\t{strand}\t.\tdepth={count}\n"
                )


if __name__ == "__main__":
    main()

# terminal 에서 수행할 땐
# cd /workspaces/intern-claude-training/notebooks
# python3 makegff.py ../SRR1168121_sorted.bam chipexo.gff
