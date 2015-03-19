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


##############################################
#TEST FOR MINIMUM NUMBER OF ROWS. SINCE WE ARE
#DEALING WITH STATE DATA THERE SHOULD BE AT
#LEAST 50 ROWS
##############################################
def test_getEiaData_for_number_of_rows():
    dfe = ep.getEiaData()
    assert len(dfe) >= 50


def test_getUscbData_for_number_of_rows():
    dfp = ep.getUscbData()
    assert len(dfp) >= 50


def test_getIncomeData_for_number_of_rows():
    dfi = ep.getIncomeData()
    assert len(dfi) >= 50


def test_getEiaRates_for_number_of_rows():
    dfr = ep.getEiaRates()
    assert len(dfr) >= 50


##############################################
#ENSURE EACH DATAFRAME HAS A "STATE" COLUMN
#SINCE DATAFRAMES WILL BE MERGED ON THIS
#COLUMN
##############################################
def test_EiaData_for_state_column():
    df = ep.getEiaData()
    assert 'State' in df.columns


def test_UscbData_for_state_column():
    df = ep.getUscbData()
    assert 'State' in df.columns


def test_IncomeData_for_state_column():
    df = ep.getIncomeData()
    assert 'State' in df.columns


def test_EiaRates_for_state_column():
    df = ep.getEiaRates()
    assert 'State' in df.columns


#############################################
#NOW TEST THE FUNCTION THAT DOES ALL THE WORK
#############################################
def test_electricPrice_frac_spent_col_exists():
    df = ep.electricPrice()
    assert 'FracSpent' in df.columns


def test_electricPrice_PerCap_col_exists():
    df = ep.electricPrice()
    assert 'PerCap' in df.columns


def test_electricPrice_FracSpent_lt_1():
    df = ep.electricPrice()
    assert df['FracSpent'].max() < 1


def test_electricPrice_for_number_of_rows():
    df = ep.electricPrice()
    assert len(df) >= 50
