#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-02-23
Purpose: Rock the Casbah
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('r'),
                        default=[sys.stdin],
                        help='Input file')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default='10')

    args = parser.parse_args()

# You might want to change these back to "args.text" if this isn't working
    if os.path.isfile(args.file):
        args.file=open(args.file).read().rstrip()

    if args.int <= 0:
        parser.error(f'--num "{args.int}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file



#    if args.int <= 0:
#        parser.error(f'--num "{args.int}" must be greater than 0')





# --------------------------------------------------
if __name__ == '__main__':
    main()
