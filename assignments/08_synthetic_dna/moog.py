#!/usr/bin/env python3
"""
Author : charlesb107
Date   : 2020-03-31
Purpose: Rock the Casbah
Reference: Tiny Python Projects (Book)/Biosystems Analytics (BE534), Spring 2020
"""

import argparse
import os
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        #type=argparse.FileType('wt'),
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        choices=['dna', 'rna'],
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='The number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_file = args.outfile
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for i in range(1, args.numseqs+1):
        #out_file = os.path.join(os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        seq_len = random.choice(range(args.minlen, args.maxlen))
        seq = ''.join(random.sample(pool, seq_len))
        out_fh.write(seq + '\n')

        # For quickly testing output, compare to outfile text
        #print(seq)

    out_fh.close()

    print(f'Done, wrote {args.numseqs} sequence{"" if args.numseqs == 1 else "s"} to "{args.outfile}"')

# -------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    # pctgc = args.pctgc
    # max_len = args.maxlen
    # seq_type = args.seqtype

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))

# --------------------------------------------------
if __name__ == '__main__':
    main()
