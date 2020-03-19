#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-03-15
Purpose: Translates DNA codons to amino acids
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        type=str,
                       # nargs='+',
                        help='Input sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

#     args = get_args()
# #    args_file = args.file()
#
#
#     codons = {'AAA': 'K', 'AAG': 'K', 'AAU': 'N', 'ACC': 'T', 'ACG': 'T',
#               'ACU': 'T', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I',
#               'AUG': 'M', 'AUU': 'I', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
#               'CCC': 'P', 'CCU': 'P', 'CGA': 'R', 'CGC': 'R', 'CGU': 'R',
#               'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'GAA': 'E',
#               'AAC': 'N', 'AAT': 'N', 'ACA': 'T', 'UGG': "L",
#               'ACT': 'T', 'AGA': 'R',  'AGC':'S', 'AGT':'S',  'ATA':'I',  'ATC':'I',
#               'ATG': 'M', 'ATT': 'I', 'CAA': 'Q', 'CAT':'H', 'CCA':'P',
#               'CCG':'P', 'CCT':'P', 'CGG':'R', 'CGT':'R',
#               'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'GAC':'D', 'GAG':'E',
#               'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G',
#               'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'TAA':'Stop',
#               'TAC':'Y', 'TAG':'Stop', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
#               'TGA':'Stop', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'}
#
#     n = 3
#     input_text = [args.text[i:i+n] for i in range(0, len(args.text), n)]
#
#     for codon in input_text:
#         outfile_handle = open(args.outfile, 'wt')
#         outfile_handle.write(codons.get(codon, '-'))
#         print(codons.get(codons.get(codon, '-'), file=outfile_handle, end='')
#         outfile_handle.close()
#
#     print(f'Output written to "{args.outfile}".')

    # CLASS SOLUTION
    args = get_args()
    seq = args.seq.upper()

    codons = {}

    for line in args.codons:
        #Similar to the "Hamming" assignment
        codon, protein = line.upper().split()
        codons[codon] = protein

        k = 3
        proteins = []
        for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:
            proteins.append(codons.get(codon, '-'))

    print(''.join(proteins), file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')

    # --------------------------------------------------
if __name__ == '__main__':
    main()
