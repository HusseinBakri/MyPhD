#!/usr/bin/python3
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# For LaTeX Text Rendering
from matplotlib import rc, rcParams

import pandas as pd
import numpy as np

'''
Side by Side graphs via Seaborn
'''

# activate latex text rendering
rc('text', usetex=True)
rc('font', weight='bold')
rcParams['text.latex.preamble'] = [r'\usepackage{sfmath} \boldmath']

# General Settings for matplotlib
mpl.rcParams['figure.titlesize'] = 'large'

# Reading data from Excel sheet 1
df = pd.read_excel('datasets/AllForLight.xlsx', sheetname='Sheet1')
print(df)
print("Header of df: ")
print(df.head())

#Spaces in string in column causes problems
df.columns = df.columns.str.strip()
print(df.columns.tolist())
#sns.lmplot(x='Device', y='With Hannibal', data=df)
g = sns.FacetGrid(df, row="Device", col="Network", hue="Model")
g.map(plt.scatter, "With Hannibal", "Without Hannibal")
g.add_legend()

#sns.regplot(x='Without Hannibal', y='With Hannibal', data=df)

# dataset = sns.load_dataset("datasets/AllForLight.xlsx")
# sns.set(style="ticks", color_codes=True)
# g = sns.FacetGrid(dataset, col="Model", row="With Hannibal")

plt.show()
