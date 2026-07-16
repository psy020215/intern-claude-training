#!/usr/bin/env python3
import math
import sys
from collections import Counter

import pysam

TARGET_MAX_SCORE = 10


# Pileup counts span a huge range (1 to several thousand, and occasional
# artifact positions much higher), so a raw or log2(count+1) score still lets
# a handful of outlier positions dominate the GFF score axis and flatten every
# other real peak near zero. Normalizing this run's own counts onto a fixed
# 1..TARGET_MAX_SCORE range guarantees the tallest peak is always exactly
# TARGET_MAX_SCORE, so weaker (but still real) peaks stay visible.
def compute_score(count, max_count, target_max=TARGET_MAX_SCORE):
    if max_count <= 1:
        return 1
    score = 1 + (target_max - 1) * math.log(count) / math.log(max_count)
    return round(score)


def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: python {sys.argv[0]} <sorted.bam> <output.gff>")
    bam_path, gff_path = sys.argv[1], sys.argv[2]

    # counts[chrom][(pos, strand)] = 해당 (위치, strand)에 5' end가 몰린 read 개수
    counts = {}

    with pysam.AlignmentFile(bam_path, "rb") as bam:
        for read in bam.fetch(until_eof=True):
            if read.is_unmapped:
                continue
            strand = "-" if read.is_reverse else "+"
            # ChIP-exo 시그널은 read의 5' end: +가닥은 시작, -가닥은 끝
            pos = read.reference_start + 1 if strand == "+" else read.reference_end
            # FASTA accession 버전(.3)을 떼어 lab annotation의 chromosome ID(NC_000913)와 맞춤
            chrom = read.reference_name.split(".")[0]
            counts.setdefault(chrom, Counter())[(pos, strand)] += 1

    max_count = max(
        (c for positions in counts.values() for c in positions.values()), default=1
    )

    with open(gff_path, "w") as gff:
        # (pos, strand) 순으로 정렬 -> 파일 전체가 좌표 기준으로 단조 증가하는
        # coordinate-sorted GFF가 된다 (strand별로 통째로 묶어서 쓰면 좌표가
        # 중간에 처음으로 되돌아가서, 좌표 정렬을 기대하는 뷰어에서 뒤쪽 strand의
        # 뒷부분 데이터가 로드되지 않는 문제가 있었다).
        for chrom, positions in sorted(counts.items()):
            for (pos, strand), count in sorted(positions.items()):
                score = compute_score(count, max_count)
                # 부호로 strand를 한 번 더 표시(컬럼7의 +/-와 중복되지만, MetaScope에서
                # 두 strand 트랙을 score 축 위아래로 갈라 보기 위해 유지한다).
                if strand == "-":
                    score = -score
                gff.write(
                    f"{chrom}\tmakegff\tfiveprime\t{pos}\t{pos}\t{score}\t{strand}\t.\tdepth={count}\n"
                )


if __name__ == "__main__":
    main()
