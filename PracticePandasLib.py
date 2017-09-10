# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 00:19:41 2017

@author: Asanka
"""
#Importing Libraries
import pandas as pd
import numpy as np


# ## Exploring a Dataset

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')


# Read in data into a dataframe
dataFrame = pd.read_csv('GlobalTemperatures.csv')

# Select the LandAverageTemperature
dataFrame = dataFrame.ix[:,0:2]
dataFrame.head()


#plot
plt.figure(figsize = (15, 5))
plt.scatter(x = dataFrame['LandAverageTemperature'].index, y = dataFrame['LandAverageTemperature'])
plt.title("Average Land Temperature 1750-2015")
plt.xlabel("Year")
plt.ylabel("Average Land Temperature")
plt.show()


# check date column value types
print(type(dataFrame['dt'][0]))

# Convert to date time value format in Pandas
times = pd.DatetimeIndex(dataFrame['dt'])

# Group by year
grouped = dataFrame.groupby([times.year]).mean()


# Plot
plt.figure(figsize = (15, 5))
plt.plot(grouped['LandAverageTemperature'])

# Name axis
plt.title("Yearly Average Land Temperature 1750-2015")
plt.xlabel("Year")
plt.ylabel("Yearly Average Land Temperature")
plt.show()

print(dataFrame['LandAverageTemperature'].isnull().sum())


