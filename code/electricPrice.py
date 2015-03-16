#!/usr/bin/env python

"""
Created on 2015-03-15T20:28:12
"""

from __future__ import division, print_function
import sys
import argparse
import pandas as pd

try:
    import numpy as np
except ImportError:
    print('You need numpy installed')
    sys.exit(1)

__author__ = "Matt Giguere (github: @mattgiguere)"
__maintainer__ = "Matt Giguere"
__email__ = "matthew.giguere@yale.edu"
__status__ = " Development NOT(Prototype or Production)"
__version__ = '0.0.1'


def electricPrice(arg1, arg2):
    """
    PURPOSE: A routine to combine data sets from the US Energy
    Information Agency and the US Census Bureau. The output
    are csvs showing the average energy use per resident by
    state and the fraction of income spent on electric annually
    by state.
    """

    #read in the US EIA Energy Use data:
    dfe = pd.read_excel('../january2015/Table_5_04_B.xlsx', skiprows=3, header=0)

    #now read in the US Census Population data:
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='argparse object.')
    parser.add_argument(
        'arg1',
        help='This argument does something.')
    parser.add_argument(
        'arg2',
        help='This argument does something else. By specifying ' +
             'the "nargs=>" makes this argument not required.',
             nargs='?')
    if len(sys.argv) > 3:
        print('use the command')
        print('python filename.py tablenum columnnum')
        sys.exit(2)

    args = parser.parse_args()

    electricPrice(int(args.arg1), args.arg2)
 