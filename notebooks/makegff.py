#!/usr/bin/env python3
import sys

import pysam


def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: python {sys.argv[0]} <sorted.bam> <output.gff>")
    bam_path, gff_path = sys.argv[1], sys.argv[2]

    with pysam.AlignmentFile(bam_path, "rb") as bam, open(gff_path, "w") as gff:
        for read in bam.fetch(until_eof=True):
            if read.is_unmapped:
                continue
            strand = "-" if read.is_reverse else "+"
            start = read.reference_start + 1  # pysam is 0-based; GFF is 1-based
            end = read.reference_end  # already the correct 1-based inclusive end
            gff.write(
                f"{read.reference_name}\tmakegff\tread\t{start}\t{end}\t1\t{strand}\t.\tname={read.query_name}\n"
            )


if __name__ == "__main__":
    main()
