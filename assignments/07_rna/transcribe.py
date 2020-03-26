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
        description='Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    num_files, num_seqs = 0, 0
# args.file is a bunch of open file handles
    for fh in args.file:
        num_files += 1
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')

# Here, DNA is equivalent to "line"
        for dna in fh:
            num_seqs += 1
            out_fh.write(dna.rstrip().replace('T', 'U') + '\n')

        out_fh.close()

    print(f'Done, wrote {num_seqs} '
          f'sequence{"" if num_seqs == 1 else "s"} in {num_files} '
          f'file{"" if num_files == 1 else "s"} to directory "{out_dir}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
