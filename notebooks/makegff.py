#이거는 start, end point만을 기점으로 카운트함. 원래는 read
"""처음엔 strand의 end point 만을 기준으로 겹치는 지점만을 count해서 피크로 구현했고,
그러다보니 strand 방향에 따라 전사 시작 부분이 달라진다고 생각.
-> 이렇게 할 경우, FUR결합부위로부터 조금 떨어진 곳에서 peak가 만들어짐
-> point를 기준으로 하고싶으면, Strand에서 위치별 endpoint를 따로 카운트하고 피크 사이에 결합위치가 존재한다고 판단
근데 그렇게 접근하는 것보다 strand position별로 쌓인 read를 +/-별로 count하여 통합시켜서 접근하는게 올바름"""

#!/usr/bin/env python3
import math
import sys
from collections import Counter

import pysam

TARGET_MAX_SCORE = 10

# 피크 구별이 쉽도록 count의 범위를 1~10 사이로 압축하는 log 스케일링을 적용.

def compute_score(count, max_count, target_max=TARGET_MAX_SCORE):
    if max_count <= 1:
        return 1
    score = 1 + (target_max - 1) * math.log(count) / math.log(max_count)
    return round(score)


def main():
    if len(sys.argv) != 3:# 터미널에서 스크립트 실행 시 입력한 인자들이 입력(BAM file), 출력(GFF file), 스크립트 이름까지 해서 총 3개인지 검증
        sys.exit(f"Usage: python {sys.argv[0]} <sorted.bam> <output.gff>")
    bam_path, gff_path = sys.argv[1], sys.argv[2]

    # counts[chrom][(pos, strand)] = 해당 (위치, strand)에 5' end가 몰린 read 개수
    counts = {}

    with pysam.AlignmentFile(bam_path, "rb") as bam:#bam 파일 열고 모든 read 순회
        for read in bam.fetch(until_eof=True):
            if read.is_unmapped:
                continue 
            strand = "-"if read.is_reverse else "+"
            # ChIP-exo 시그널은 read의 5' end: +가닥은 start, -가닥은 end를 기준으로
            pos = read.reference_start + 1 if strand == "+" else read.reference_end
            # FASTA accession 버전(.3)을 떼어 lab annotation의 chromosome ID(NC_000913)와 맞춤
            chrom = read.reference_name.split(".")[0]
            counts.setdefault(chrom, Counter())[(pos, strand)] += 1

    max_count = max((c for positions in counts.values() for c in positions.values()), default=1)

    with open(gff_path, "w") as gff:
        # (pos, strand) 순으로 정렬하면 -> 파일 전체가 좌표 기준으로 단조 증가하는 coordinate-sorted GFF가 된다 
        # (strand별로 통째로 묶어서 쓰면 좌표가 중간에 처음으로 되돌아가서, 좌표 정렬을 기대하는 뷰어에서 뒤쪽 strand의 데이터가 로드되지 않는 문제 발생)
        for chrom, positions in sorted(counts.items()):
            for (pos, strand), count in sorted(positions.items()):
                score = compute_score(count, max_count)
                # 부호로 strand를 한 번 더 표시(컬럼7의 +/-와 중복되지만, MetaScope에서
                # 두 strand 트랙을 score 축 위아래로 갈라 보기 위해 유지한다).
                if strand == "-":#strand가 -이면 score를 음수로 시각화
                    score = -score
                gff.write(f"{chrom}\tmakegff\tfiveprime\t{pos}\t{pos}\t{score}\t{strand}\t.\tdepth={count}\n")


if __name__ == "__main__":
    main()
