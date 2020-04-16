#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-04-05
Purpose: Rock the Casbah
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys
import random
from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input FASTA file(s)')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not 0 <= args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    out_dir = args.outdir

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)


    file_num = 0
    num_seq = 0
    for fh in args.file:
        file_num += 1
        basename = os.path.basename(fh.name)
        out_file = os.path.join(args.outdir, basename)
        print(f'{file_num:3}: {basename}')



        out_fh = open(out_file, 'wt')

        for rec in SeqIO.parse(fh, 'fasta'):

            if random.random() <= args.pct:
                num_seq += 1
                SeqIO.write(rec, out_fh, 'fasta')

        out_fh.close()


    print(f'Wrote {num_seq:,} sequence{"" if num_seq == 1 else "s"} from {file_num}'
           f' file{"" if file_num == 1 else "s"} to directory "{out_dir}"')

# # IN-CLASS EXAMPLES
#     if not os.path.isdir(out_dir):
#         os.makedir(out_dir)
#
#     out_dir = args.outdir
#
#     for i, fh in enumerate(args.file, start=1):
#         basename = os.path.basename(fh.name)
#         out_file = os.path.join(out_dir, basename)
#         out_fh = open(out_file, 'wt')
#         print(f'{i:3}: {basename}')
#
#         for rec in SeqIO.parse(fh, 'fasta'):
#             if random.random() <= args.pct:
#             SeqIO.write(rec, out_fh, 'fasta')


# --------------------------------------------------
if __name__ == '__main__':
    main()
