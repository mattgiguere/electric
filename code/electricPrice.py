#!/usr/bin/env python

"""
Created on 2015-03-15T20:28:12
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


def getEiaData():
    """
    PURPOSE: Restore the EIA data to DataFrame
    """
    #read in the US EIA Energy Use data:
    dfe = pd.read_excel('../data/january2015/Table_5_04_B.xlsx', skiprows=3, header=0)

    #rename columns. (R)esidential, (C)ommercial, (I)ndustrial
    #(T)ransportation, and (A)ll:
    dfe.columns = ['State',
                   '201411YTDR', '201311YTDR',
                   '201411YTDC', '201311YTDC',
                   '201411YTDI', '201311YTDI',
                   '201411YTDT', '201311YTDT',
                   '201411YTDA', '201311YTDA']
    return dfe


def getUscbData():
    """
    PURPOSE: Restore the census data
    """
    #now read in the US Census Population data. Skip the first 3 rows,
    #which have details about the data, and the last 5 rows, which
    #have more details about the data. The python engine needs to be
    #specified when using `skipfooter`. See docs for details.
    dfp = pd.read_csv('../data/NST-EST2014-01.csv', skiprows=3, header=0,
                      skipfooter=5, engine='python', thousands=',')

    #now change the column name of the first column to state:
    colnms = dfp.columns.values
    colnms[0] = 'State'
    dfp.columns = colnms

    #for some f'ed up reason, the US CB decided to put a dot in front
    #of every state name. I will use a regex to get rid of it:
    dfp['State'] = [re.search('[^\.](.*)', str(dfp.loc[idx, 'State'])).group(0) for idx in range(len(dfp))]
    return dfp


def saveDataToCsv(df):
    """PURPOSE:
    A routine to save the data.
    """
    df.to_csv('../data/2014PerCapitaUsage.csv', columns=['State', '201411YTDR', '2014', 'PerCap'])


def electricPrice():
    """
    PURPOSE: A routine to combine data sets from the US Energy
    Information Agency and the US Census Bureau. The output
    are csvs showing the average energy use per resident by
    state and the fraction of income spent on electric annually
    by state.
    """

    #retrieve EIA data:
    dfe = getEiaData()

    #retrieve Census data:
    dfp = getUscbData()

    #merge the two:
    df = pd.merge(dfe, dfp, on='State')

    #now calculate the per capita usage:
    df['PerCap'] = df['201411YTDR']*1e6 / df['2014']
    return df


def electricPriceDrive():
    """
    PURPOSE:
    A routine to do all of the above
    """
    df = electricPrice()
    saveDataToCsv(df)
