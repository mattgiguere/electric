#!/usr/bin/env python

"""
Created on 2015-03-18T21:59:12
"""

from __future__ import division, print_function
import sys
import argparse
import pandas as pd
import re

__author__ = "Matt Giguere (github: @mattgiguere)"
__maintainer__ = "Matt Giguere"
__email__ = "matthew.giguere@yale.edu"
__status__ = " Development NOT(Prototype or Production)"
__version__ = '0.0.1'

from electric.code import electricPrice as ep

def test_getEiaData_for_number_of_columns():
	dfe = ep.getEiaData()
	dfe_coln = len(dfe.columns.values)
	assert dfe_coln == 11






	
