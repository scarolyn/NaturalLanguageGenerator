# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library:
##from (library) import (specific library function)
from docutils.nodes import inline
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting

Location = r'C:\Users\Carolyn\workspace\NaturalLanguageGenerator\locus_data_12years.csv'
df = pd.read_csv(Location)

firstDate = ""
secondDate = ""
ticker = ""



print(df.all)
print(df.icol(3))
print(df.irow(df,5,copy=False))
# %matplotlib inline
# class NLG(object):
#     primary = {}
#     def __init__(self, filename):
#         with open(filename, r) as f:
#             f.readLine();

