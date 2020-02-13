#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-02-10
Purpose: This is the 02_strings assignment
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():

    parser = argparse.ArgumentParser(
        description='My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('things',
                       metavar='str',
                       type=str,
                       nargs='+',
                       help='Some things')


    parser.add_argument('-s',
                        '--sep',
                        metavar='str',
                        type=str,
                        default=',',
                        help='A separator (default: , )')

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    things = args.things
    sep = args.sep

    faves = ''
    if len(things) == 1:
        print(f'{things[0]}\nThis is one of my favorite things.')

    elif len(things) == 2:
        print(f'{things[0]}{sep} {things[1]}\nThese are a few of my favorite things.')

#    else:
#         print(


#    faves = ''
#    if len(things) == 1:
#        print('{}\nThis is one of my favorite things.'.format(faves))

#    if len(things) == 2:

# --------------------------------------------------
if __name__ == '__main__':
    main()
