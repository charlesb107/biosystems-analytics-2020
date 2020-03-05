#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-03-01
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

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-m',
                        '--min',
                        help='The minimum Hamming distance',
                        metavar='int',
                        type=int)


    args = parser.parse_args()

    return args

    #return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
#    int_arg = args.int


# Attempt #?

    total_diff = ''
    for line in args.file:
        line_list = line.split()
        len_w0, len_w1 = len(line_list[0]), len(line_list[1])
        len_diff = abs(len_w0 - len_w1)

        w0 = line_list[0]
        w1 = line_list[1]
        zip_list = list(zip(w0, w1))


        diff_num = 0
        for item in zip_list:
            if item[0] != item[1]:
                diff_num += 1
        total_diff = len_diff + diff_num

    if total_diff >= args.min:
            print(f'       {total_diff}:{w0}                 {w1}')


   # print(f'       {total_diff}:{w0}                 {w1}')

## Class Notes

 #   for line in args.file:
 #       word1 = 'foo'
 #       word2 = 'bar'
  #      word1, word2 = line.split()
 #       test_list = line.split()
 #       dist = abs(len(word1)-len(word2))
 #       print(test_list)
 #       print(f'Length Diff: {dist}')
  #       = line.split()
  #      print(testo)
    # Zip will compare the elements PAIRWISE, of the same length
    # Iterate over these indices, comparing them
    # Add diff output from len and from zip to get total # of diffs
#    test_list = list(zip(word1, word2))
#    print(test_list)

  #  for item in test_list:




# --------------------------------------------------
if __name__ == '__main__':
    main()
