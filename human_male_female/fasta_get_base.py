#!/usr/bin/env python3

# Copyright (c) 2020 Leiden University Medical Center
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse

from Bio.SeqIO.FastaIO import FastaIterator


def argument_parser() -> argparse.ArgumentParser():
    parser = argparse.ArgumentParser(
        description="Get the nucleotide at a given position in a fasta")
    parser.add_argument("fasta", type=str, help="the fasta file")
    parser.add_argument("chromosome", type=str, help="chromosome")
    parser.add_argument("position", type=int, help="1-based position")
    return parser


def get_base(fasta: str, chromosome: str, position: int):
    with open(fasta, "rt") as fasta_handle:
        records = FastaIterator(fasta_handle)
        for record in records:
            print(len(record))
            if record.id == chromosome:
                return record[position - 1]
        # If we have not returned the chromosome was not there.
        raise ValueError(f"{chromosome} not found in {fasta}")


def main():
    args = argument_parser().parse_args()
    print(get_base(args.fasta, args.chromosome, args.position))


if __name__ == "__main__":
    main()
