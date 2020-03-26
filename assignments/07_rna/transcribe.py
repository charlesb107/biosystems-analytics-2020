#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-03-23
Purpose: Rock the Casbah
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=dir,
                        default='out')

    args = parser.parse_args()


    base = os.path.basename(args.file)
    out_dir = 'out'
    os.path.join(out_dir, base)

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for char in args.file:
        trans_seq = char.replace('T', 'U')
        print(trans_seq)

    for fh in args.file:
        for char in fh:
            trans_seq = char.replace('T', 'U')

        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        out_fh.write(trans_seq)
        out_fh.close()

        num_lines = 0
        for line in fh:
            num_lines += 1

    #print(f'Done, wrote {num_lines} sequences in {num_file} to directory "{out_dir}.')

# # From Howler
#     out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
#     out_fh.write(args.text.upper() + '\n')
#     out_fh.close()




# --------------------------------------------------
if __name__ == '__main__':
    main()
