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

    parser.add_argument('things'
                       metavar='str',
                       type=str,
                       nargs='+'
                       help='Some things')


    parser.add_argument('-s',
                        '--sep',
                        action='

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    things = args.things

    if len(things) == 1:
        print(f'{arg}\n This is one of my favorite things')

    if len(things) == 2:
        print(f'
# --------------------------------------------------
if __name__ == '__main__':
    main()
