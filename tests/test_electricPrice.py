#!/usr/bin/env python

"""
Created on 2015-03-18T21:59:12
"""

from __future__ import division, print_function
import sys
import argparse
import pandas as pd
import re
from electric.code import electricPrice as ep

__author__ = "Matt Giguere (github: @mattgiguere)"
__maintainer__ = "Matt Giguere"
__email__ = "matthew.giguere@yale.edu"
__status__ = " Development NOT(Prototype or Production)"
__version__ = '0.0.1'


#############################################
#TEST NUMBER OF COLUMNS FOR ALL 4 DATA SETS
#############################################
def test_getEiaData_for_number_of_columns():
    dfe = ep.getEiaData()
    dfe_coln = len(dfe.columns.values)
    assert dfe_coln == 11


def test_getUscbData_for_number_of_columns():
    dfp = ep.getUscbData()
    dfp_coln = len(dfp.columns.values)
    assert dfp_coln == 8


def test_getIncomeData_for_number_of_columns():
    dfi = ep.getIncomeData()
    dfi_coln = len(dfi.columns.values)
    assert dfi_coln == 11


def test_getEiaRates_for_number_of_columns():
    dfr = ep.getEiaRates()
    dfr_coln = len(dfr.columns.values)
    assert dfr_coln == 11
