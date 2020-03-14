# Python 3 venv for Fifa 19 Statistics
#
# Docker image used: http://github.com/kaggle/docker-python
#
# Author: Arthur Bowers
#[1]
#import streamlit
#import numpy as np   # Linear Algebra
import pandas as pd  # Data processing/dataframes
import seaborn as sb # Any results written to currDir are saved as output.
import matplotlib.pyplot as plt
import re # regex
import os

# Input data files available in the "./input/" directory.

print(os.listdir("./input"))

# If gridlines aren't needed, comment out this line.
sb.set(style="ticks")

flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
flatui = sb.color_palette(flatui)

#[2]
data = pd.read_csv('./input/fifa19data.csv', index_col = 'Unnamed: 0')


#[3] Cleaning wage and value columns from currency to real numbers
data['Wage'] = data['Wage'].apply(lambda x: int(re.findall('\d+', x)[0] + '000'))
data['Value'] = data['Value'].apply(lambda x: 'M' in x and int((re.findall('\d+\.*\d*', x)[0] + '000000').replace('.','')) or int((re.findall('\d+\.*\d*', x)[0] + '000').replace('.', '')))

# Getting top ten most popular countries
top_ten_countries = data['Nationality'].value_counts().head(10).index.values
top_ten_countries_data = data.loc[data['Nationality'].isin(top_ten_countries), :]

# How does the distribution of players overall score
# differ from country to country?

sb.set(style='white')
plt.figure(figsize=(11, 0))
p = sb.boxplot(x = 'Nationality', y = 'Overall', data = top_ten_countries_data)


