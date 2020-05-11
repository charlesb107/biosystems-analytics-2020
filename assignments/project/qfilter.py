#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-04-20
Purpose: Filters FASTQ ID's based on average quality
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Returns a list of reads exceeding given quality threshold',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input FASTQ file(s)')

    parser.add_argument('-q',
                        '--qual',
                        help='Average read-quality threshold value',
                        metavar='quality value',
                        type=float,
                        default=.8)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        default='goodreads.txt')

    parser.add_argument('-n',
                        '--num',
                        help='Number of acceptable reads to produce',
                        metavar='int',
                        type=int,
                        default=10)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Skeebidee beep bop!"""

    args = get_args()
    num_seq, tot_reads = 0, 0
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    qual_pct = args.qual * 100

    for fh in args.file:
        for i in range(1, args.num + 1):
            for rec in SeqIO.parse(fh, 'fastq'):
                tot_reads += 1
                perf_score = len(rec.letter_annotations["phred_quality"]) * 40
                tot_score = sum(rec.letter_annotations["phred_quality"])
                dec_score = tot_score / perf_score

                if args.num > num_seq:
                    if args.qual <= dec_score:
                        num_seq += 1
                        pct_score = round(dec_score * 100, 1)
                        out_fh.write(f'ID: {rec.id} = {pct_score}%' + '\n')

                        #For testing purposes only
                        # out_fh.write(f'Total Score = {tot_score}' + '\n'
                        #              f'Perfect Score = {perf_score}' + '\n'
                        #              f'{rec.letter_annotations["phred_quality"]}' + '\n' + '\n')




    out_fh.close()
    print(f'Done. {num_seq:,} sequence{"" if num_seq == 1 else "s"} had an average quality of {qual_pct}% or greater. \n'
          f'Please see the file "{args.outfile}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
