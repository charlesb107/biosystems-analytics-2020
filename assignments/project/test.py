#!/usr/bin/env python3
"""Test for the QFilter program"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './qfilter.py'

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_usage():
    """Checks for usage statement"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

# -------------------------------------------------------
def test_small_input():
    """Tests program on a smaller FASTQ file"""

    qual_val_s = round(random.uniform(.85, .9), 2)
    num_reads_s = random.randint(100, 110)
    qual_pct_s = round(qual_val_s * 100, 2)

    inp_small = 'HBR_Rep1_ERCC-Mix2_Build37-ErccTranscripts-chr22.read1.fastq'
    out_small = 'test_out_small.txt'


    rv, out = getstatusoutput(f'{prg} -q {qual_val_s} -n {num_reads_s} -o {out_small} {inp_small}')
    assert re.search(f'Done. {num_reads_s} sequences had an average quality of {qual_pct_s}% or greater. \n'
          f'Please see the file "{out_small}"', out)

# ------------------------------------------------------------
def test_file_exist_s():
    """Checks to see if the output file of the previous test exists"""

    out_small = 'test_out_small.txt'

    assert os.path.isfile(out_small)


# --------------------------------------------------
def test_large_input():
    """Tests program on a larger FASTQ file"""

    qual_val_l = round(random.uniform(.3, .8), 2)
    num_reads_l = random.randint(25, 100)
    qual_pct_l = round(qual_val_l * 100, 2)

    inp_large = 'SRR396636.sra_1.fastq'
    out_large = 'test_out_large.txt'


    rv, out = getstatusoutput(f'{prg} -q {qual_val_l} -n {num_reads_l} -o {out_large} {inp_large}')
    assert re.search(f'Done. {num_reads_l} sequences had an average quality of {qual_pct_l}% or greater. \n'
          f'Please see the file "{out_large}"', out)



# ------------------------------------------------------------
def test_file_exist_l():
    """Checks to see if the output file of the previous test exists"""

    out_large = 'test_out_large.txt'

    assert os.path.isfile(out_large)
