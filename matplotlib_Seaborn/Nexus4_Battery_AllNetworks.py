#!/usr/bin/python3
import matplotlib.pyplot as plt
import matplotlib as mpl

# For LaTeX Text Rendering
from matplotlib import rc, rcParams

import pandas as pd
import numpy as np

# activate latex text rendering
rc('text', usetex=True)
rc('font', weight='bold')
rcParams['text.latex.preamble'] = [r'\usepackage{sfmath} \boldmath']

# General Settings for matplotlib
mpl.rcParams['figure.titlesize'] = 'large'

# Reading data from Excel sheet 1
df = pd.read_excel('datasets/Nexus4BatteryAllNetworks.xlsx', sheetname='Sheet1', header=None)
print(df)

# Setting Columns
ModelName = df[0]
Device = df[1]
AllNetworks = df[2]
ModelsFetched = df[3]
IDTHannibal = df[4]
# IDTNoHannibal = df[5]

# Setting the Lists for annotations of the points on the graph accordingly
Annotations_WithHannibal = ['360 Sprite', '360 Sprite', '100K', '200K', '200K']
# Annotations_WithNoHannibal = ['', '', '1.5M', '1.5M', '1.5M']

fig, ax = plt.subplots()
# Adjusting margins around the figure
# Original: left: 0.12, bottom: 0.11, right:0.90, top: 0.88, wspace: 0.20, hspace: 0.20
# To tweak that use IDLE (Python 3.6) installed - there is a GUI customizer
plt.subplots_adjust(left=0.12, right=0.90, top=0.88, bottom=0.15)

# set size of figure in inches (for the LaTeX Thesis)
# Get current size
fig_size = plt.rcParams["figure.figsize"]

# Prints: [8.0, 6.0]
print("Current size:", fig_size)

# Set figure width to 8 and height to 8
fig_size[0] = 8
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size

# Set invisible the spline of right side and top side
#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)

# Plot the lines
plt.plot(AllNetworks, IDTHannibal, label="With Hannibal", marker='x')
# plt.plot(AllNetworks, IDTNoHannibal, label="No Hannibal", marker='o')

# Plot Title (notice using LaTeX)
plt.title(r'\textbf{Download \& Processing Times - Battery Model' + '\n' + r'\textbf{On Nexus 4 Across All Networks}')

# Customising ticks labels on X-Axis so they do not look like what is in Excel
plt.xticks(np.arange(5), (
    r'\textbf{GPRS}' + '\n' + r'\textbf{(Simulated)}', r'\textbf{2G}' + '\n' + r'\textbf{Simulated)}',
    r'\textbf{3G}' + '\n' + r'\textbf{(Simulated)}',
    r'\textbf{4G}', r'\textbf{CS WiFi}'))

# X-Axis Label (with LaTeX)
plt.xlabel(r'\textbf{Network Regimes}', fontsize=12)

# create a padding space between Axes and titles in points
# mpl.rcParams['axes.labelpad'] = 30

# Y-Axis Label (With LaTeX)
plt.ylabel(r'\textbf{Download \& Processing Times (s)')

# Change the xtick/yticks Labels (meaning the text) size
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16

# Generating the Legend (legend is fine as is)
plt.legend()

# Enabling Grid
plt.grid(True)

# Looping to Annotate the points from Lists
for i, txt in enumerate(Annotations_WithHannibal):
    Annotation = ax.annotate(txt, (AllNetworks[i], IDTHannibal[i]))

# for j, txt2 in enumerate(Annotations_WithNoHannibal):
#     Annotation2 = ax.annotate(txt2, (AllNetworks[j], IDTNoHannibal[j]))

# Changing the position of last Annotation (since part of it is outside right spine)
# Luckily it is still saved in Annotation variable
New_position_Annotation_X = 3.9     # Moving on X-Axis
New_position_Annotation_Y = IDTHannibal[4] + 0.2  #Just lille nudge on Y-Axis
print(New_position_Annotation_X)
print(New_position_Annotation_Y)
Annotation.set_position((New_position_Annotation_X, New_position_Annotation_Y))


# Changing the position of last Annotation (since part of it is outside right spine)
# Luckily it is still saved in Annotation2 variable
# New_position_Annotation2_X = 3.9    # Moving on X-Axis
# New_position_Annotation2_Y = IDTNoHannibal[4] + 0.2  #Just lille nudge on Y-Axis
# print(New_position_Annotation2_X)
# print(New_position_Annotation2_Y)
# Annotation2.set_position((New_position_Annotation2_X, New_position_Annotation2_Y))

# saving the plot in different formats (could not save PDF with LaTeX) - 600 DPI is too much for LaTeX
# 300 DPI is too much also (getting TeX Capacity Exceeded error)
plt.savefig('datasets/plots/Nexus4BatteryAllNetworks.png')
plt.savefig('datasets/plots/Nexus4BatteryAllNetworks_HighDPI.png', dpi=200)

plt.show()
