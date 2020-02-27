#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-02-23
Purpose: Rock the Casbah
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""
from typing import Any

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
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default='10')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    line_num=0

    for line in args.file:
        print(line, end='')
        line_num += 1

        if line_num == args.num:
            break


# --------------------------------------------------
if __name__ == '__main__':
    main()
