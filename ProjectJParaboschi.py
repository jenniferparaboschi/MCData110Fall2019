# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:38:13 2020

@author: Jennifer

Data 205 - Capstone in Data Science
Jennifer Paraboschi
Fall 2020
Inputs: datasets from dataMontgomery

"""


# Import packages. The data comes from an API on dataMontgomery as json.
import json
import numpy as np
import pandas as pd
import re
import requests
import seaborn as sns
import matplotlib as plt
violations_data = pd.DataFrame(requests.get("https://data.montgomerycountymd.gov/resource/4tja-rkhg.json").json())
violations_data.head()
print (violations_data)
violations_data.shape
violations_data.dtypes
violations_data.describe(include="all")
type(violations_data)
len(violations_data)
pd.set_option("display.max.columns", None)
violations_data.info()
violations_data.describe(include=np.object)
 
violations_data.disposition

violations_data.axes
# =============================================================================
# The dataframe has over 937 rows and 6 columns.
# The data types for the variables are all objects.
#the dataframe needs cleaning to convert the objects and extract the information into new columns.  =============================================================================
# Clean variables with missing values. 
# Replace missing Disposition values with "No Violation".
violations_data["disposition"]=violations_data["disposition"].fillna(value="No Violation", inplace=True)

# Create a variable that contains the penalty dollar amount from the Disposition var; disregard rest of Disposition info
# Pull the characters before the $ into the status var; put the penalty amount into penalty var; drop Disposition column
# Not all rows have a $ amount; not all rows have a value (blank); 
#cleaning_data=requests.get(violations_data)


violations_data["status"]=violations_data["disposition"].apply(lambda x: x.split("$")[0])
violations_data["penalty"]=violations_data["disposition"].apply(lambda x: x.split("$")[1])
violations_data.drop("disposition", axis=1, inplace=True)
# Now penalty var contains the penalty plus other characters. Need to clean this and change to numeric for computation. And some will be blank
#violations_data['penalty'].fillna(0, inplace=True)


# 