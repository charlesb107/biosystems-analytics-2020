#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-04-12
Purpose: Rock the Casbah
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)



    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        #type=argparse.FileType('wt'),
                        default='unclustered.fa')



    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    out_fh = open(out_file, 'wt')

    for line in args.cdhit:
        match = re.search(r'>(\d+)', line)
        #print(match.group(1))
        id = match.group(1)
        protein_ids = set()
        protein_ids.add(id)

    for rec in SeqIO.parse(args.proteins, 'fasta'):
        protein_id = re.sub(r'\|.*', '', id)
        if protein_id not in protein_ids:
            SeqIO.write(rec, out_fh, 'fasta')
        #print(rec)
            break


    # plural = "" if unclust_total == 1 else 's'
    # print(f'Wote {unclust_num} of {unclust_total} unclustered protein{plural} to "{args.outfile}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
