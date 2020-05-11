#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-05-05
Purpose: Rock the Casbah
"""

import argparse
import os
import collections
import sys
import csv
###
from collections import defaultdict
import re
from pprint import pprint



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    search_word = f'{args.val.lower()}'
    num_match = 0


    if args.col:
        if args.col not in reader.fieldnames:
            print(f'--col "{args.col}" not a valid column!', file=sys.stderr)
            sys.exit(1)

        for row in reader:
            col_val = row.get(args.col)
            if re.search(args.val, col_val, re.IGNORECASE):
                num_match += 1
                writer.writerow(row)


    if not args.col:
        for row in reader:
            if re.search(args.val, f'{row.values()}', re.IGNORECASE):
                num_match += 1
                writer.writerow(row)


    print(f'Done, wrote {num_match} to "{args.outfile.name}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
