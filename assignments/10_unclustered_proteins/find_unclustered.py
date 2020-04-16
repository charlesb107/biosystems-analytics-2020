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
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')



    args = parser.parse_args()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

## IN-CLASS EXAMPLES

    #Sets are lists with unique values, which are faster to parse through
    #Sets are not in a particular order
    clustered_ids = set()

    num_written = 0
    num_total = 0

    for line in args.cdhit:
        #These two lines will cause the program to ignore lines starting with '>'
        if line.startswith('>'):
            continue

        match = re.search('>(\d+)', line)
        if match: #Only prints matches
            prot_id = match.group(1)
            #Sets the dict values to 1
            #clustered_ids[prot_id] = 1



    for rec in SeqIO.parse(args.proteins, 'fasta'):
        num_total += 1
        # match = re.search('>(\d+)', rec.id)
        # if match:
        #     prot_id = match.group(1)

        #This replaces
        prot_id = re.sub('\|.*', '', rec.id)

        if prot_id not in clustered_ids:
            num_written += 1
            SeqIO.write(rec, args.outfile, 'fasta')


    print(f'Wrote {num_written:,} of {num_total:,} unclustered proteins to "{args.outfile.name}"')









    # out_fh = open(args.outfile, 'wt')

    #for line in args.cdhit:
        #print(line)
        # match = re.search(r'>(\d+)', line)
        # print(match)
        # id = match.group(1)
        # protein_ids = set()
        # protein_ids.add(id)
        # print(protein_ids)

    # for rec in SeqIO.parse(args.proteins, 'fasta'):
    #     protein_id = re.sub(r'\|.*', '', id)
    #     if protein_id not in protein_ids:
    #         SeqIO.write(rec, out_fh, 'fasta')
    #     #print(rec)
    #         break
    #
    #
    # plural = "" if unclust_total == 1 else 's'
    # print(f'Wote {unclust_num} of {unclust_total} unclustered protein{plural} to "{args.outfile}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
