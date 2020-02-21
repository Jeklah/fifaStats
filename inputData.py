# Python 3 venv for Fifa 19 Statistics
#
# Docker image used: http://github.com/kaggle/docker-python
#
# Author: Arthur Bowers
#[1]
import numpy as np   # Linear Algebra
import pandas as pd  # Data processing/dataframes
import seaborn as sb # Any results written to currDir are saved as output.
import matplotlib.pyplot as plt
#matplotlib inline
import os

# Input data files available in the "./input/" directory.

print(os.listdir("./input"))

# If gridlines aren't needed, comment out this line.
sns.set(style="ticks")

flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
flatui = sns.color_palette(flatui)

#[2]

