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
                        help='Input file(s)')


    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=dir,
                        default='out',
                        required=True)

    args = parser.parse_args()

    base = os.path.basename(args.text)
    out_dir = 'out'
    os.path.join(out_dir, base)
    
    # Makes an output directory if one doesn't exist
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    #args.file = open(args.file).read()


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()



    for fh in args.file:
        num_seq = 0
        for line in fh:
            num_seq += 1
        for char in fh:
            trans_seq = char.replace('T', 'U')


        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        out_fh.write(trans_seq)
        out_fh.close()


    print(f'Done, wrote {num_lines} sequences in {num_file} to directory "{out_dir}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
