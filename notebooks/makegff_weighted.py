#!/usr/bin/env python3
import sys
from collections import Counter
import pysam

# ChIP-exo reads pile up at the same 5' boundary when they hit a true binding
# site, so read weight is based on how many reads share the same 5' end.
# BAM always stores the leftmost (reference_start) coordinate regardless of
# strand, but the biological 5' end is reference_start for + strand reads and
# reference_end for - strand reads (exonuclease stops at the crosslink site
# from the other direction) - so the pileup key must branch on strand rather
# than reusing reference_start for both. Thresholds were picked from this
# dataset's count distribution (median=1, p99=4).
def weight_for_count(count):
    if count >= 5:
        return 5
    if count >= 2:
        return 3
    return 1

def pileup_key(read):
    five_prime = read.reference_end if read.is_reverse else read.reference_start
    return (read.reference_name, five_prime, read.is_reverse)

def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: python {sys.argv[0]} <sorted.bam> <output.gff>")
    bam_path, gff_path = sys.argv[1], sys.argv[2]

    with pysam.AlignmentFile(bam_path, "rb") as bam:
        counts = Counter()
        for read in bam.fetch(until_eof=True):
            if read.is_unmapped:
                continue
            counts[pileup_key(read)] += 1

    with pysam.AlignmentFile(bam_path, "rb") as bam, open(gff_path, "w") as gff:
        for read in bam.fetch(until_eof=True):
            if read.is_unmapped:
                continue
            strand = "-" if read.is_reverse else "+"
            start = read.reference_start + 1  # pysam is 0-based; GFF is 1-based
            end = read.reference_end # already the correct 1-based inclusive end
            # Strip the FASTA accession version (e.g. NC_000913.3 -> NC_000913) so
            # this track's chromosome ID matches the lab annotation's in MetaScope.
            chrom = read.reference_name.split(".")[0]
            count = counts[pileup_key(read)]
            score = weight_for_count(count)
            gff.write(
                f"{chrom}\tmakegff\tread\t{start}\t{end}\t{score}\t{strand}\t.\tname={read.query_name}\n"
            )

if __name__ == "__main__":
    main()
