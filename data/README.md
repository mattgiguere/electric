#Data Sources

Below is a description of the data sources contained within this directory.

- **january2015**: All tables in xlsx format from the Energy Information Adminstration's January 2015 Electric Power Monthly Report. This can be downloaded from the US EIA's website [here][UsEiaEpm].

- **2014EnergyDataFull.csv**: The output from the `electricPrice.py` `electricPriceDrive` function. Included is the calculated fraction of income spent on electric by state. Columns are
 - *unnamed*: The pandas index
 - *State*: The name of the state or district
 - *201411YTDR*: The Year to date (as of Nov 2014) average residential electric usage in Million kWh. This is the "Residential November 2014 YTD" column in the January 2015 US EIA EPM Report.
 - *2014*: The estimated 2014 US population by state. This is from `statemhi2_13.xls` (see below).
 - *PerCap*: The calculated per capita energy usage by state in annual kWh used.
 - *1411RateYTDR*: The year to date (as of November 2014) average electric rate by state (in cents per kWh).
 - *MedianIncome12-13*: The 2 year average (from 2012-2013) annual median household income by state in US Dollars. The data in this column are from `statemhi2_13.xls`
 - *FracSpent*: The fraction of income spent on electric in US by State.


- **2014EnergyDataFull.tde**: The Tableau Data Extract of `2014EnergyDataFull.csv`. This file is needed to save Tableau workbooks to Tableau public.

- **2014PerCapitaUsage.csv**: The electric usage per capita by state. Columns are
  - *unnamed*: The pandas index
  - *State*: The name of the state or district
  - *201411YTDR*: The Year to date (as of Nov 2014) average residential electric usage in Million kWh. This is the "Residential November 2014 YTD" column in the January 2015 US EIA EPM Report.
  - *2014*: The estimated 2014 US population by state. This is from `statemhi2_13.xls` (see below).
  - *PerCap*: The calculated per capita energy usage by state in annual kWh used.


- **statemhi2_13.xls**: The Annual Social and Economic Supplement Current
Income of Households by State

[UsEiaEpm]: http://www.eia.gov/electricity/monthly/index.cfm
