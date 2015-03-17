# electric

**electric activity by US state**

[![MIT-Lic](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/mattgiguere/electric/blob/master/LICENSE)

This repository contains all the code and data that went into an analysis of the electric usage in the United States by state.

###Directory Descriptions

- **code** All of the python code used in the analysis
- **data** All of the data sources used in the analysis
- **tableau** the tableau workbooks used in the analysis. The workbooks and resulting dashboards can also be viewed on my Tableau Public page: https://public.tableau.com/profile/mattgiguere

###File Descriptions
---------------------------------------

 - ####code
  - **electricPrice.py**: The main routine for combining and cleaning the data sets used in this analysis. There are no input arguments, and it contains just a few simple commands using the pandas and re libraries. Some examples are shown below.
    - To extract the data from the US Energy Information Agency used in the creation of the `electricRatesByState201411.twb` Tableau workbook:
   ```python
   import electricPrice as ep
   dfr = ep.getEiaRates()
   ```
   where `dfe` is a pandas DataFrame containing the entirety of the Table 5.06 B excel spreadsheet from the US EIA monthly reports.

    - To read in the population data from the US Census Bureau that is in csv format as a pandas DataFrame:
    ```python
    import electricPrice as ep
    dfp = ep.getUscbData()
    ```

    - To calculate the average fraction of income spent on electric and save the results as a csv file to be imported into Tableau:
    ```python
    import electricPrice as ep
    ep.electricPriceDrive()
    ```

 - ####data
  - see data/README.md for file descriptions.
