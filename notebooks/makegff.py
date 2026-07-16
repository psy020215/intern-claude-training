#!/usr/bin/env python3
import argparse
import math
from collections import Counter

import pysam


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert a sorted BAM into a 5'-end pile-up GFF (ChIP-exo signal) for MetaScope."
    )
    parser.add_argument("bam", help="sorted BAM file")
    parser.add_argument("gff", help="output GFF path")
    parser.add_argument(
        "--log_scale",
        action="store_true",
        help="write log2(count+1) in the score column instead of the raw read count",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # counts[(chrom, strand)][position] = number of reads whose 5' end falls on that position
    counts = {}

    with pysam.AlignmentFile(args.bam, "rb") as bam:
        for read in bam.fetch(until_eof=True):
            if read.is_unmapped:
                continue
            strand = "-" if read.is_reverse else "+"
            # ChIP-exo signal is the read's 5' end: start if '+', end if '-'.
            pos = read.reference_start + 1 if strand == "+" else read.reference_end
            key = (read.reference_name, strand)
            counts.setdefault(key, Counter())[pos] += 1

    with open(args.gff, "w") as gff:
        for (chrom, strand), positions in sorted(counts.items()):
            for pos, count in sorted(positions.items()):
                score = f"{math.log2(count + 1):.3f}" if args.log_scale else str(count)
                gff.write(
                    f"{chrom}\tmakegff\tfiveprime\t{pos}\t{pos}\t{score}\t{strand}\t.\tdepth={count}\n"
                )


if __name__ == "__main__":
    main()

# terminal 에서 수행할 땐
# cd /workspaces/intern-claude-training/notebooks
# python3 makegff.py ../SRR1168121_sorted.bam chipexo.gff
# (log-scale로 score를 눌러서 보고 싶으면 --log_scale 옵션 추가)
