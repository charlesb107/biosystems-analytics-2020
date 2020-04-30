#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-04-27
Purpose: Rock the Casbah
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        #required=True,
                        default=None)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='[taxa [taxa ...]]',
                        type=str,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=None)



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    #taxa = set(map(str.lower, ))


    # for rec in SeqIO.parse(args.file, "swiss"):
    #     print(rec.annotations['taxonomy'])
         #if rec.annotations['taxonomy'] == args.taxa:
            #skip

    skip = set(map(str.lower, args.skiptaxa))
    print(skip)


   # print(f'Done, skipped {num_skip} and took {num_took}. See output in "{args.outfile}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
