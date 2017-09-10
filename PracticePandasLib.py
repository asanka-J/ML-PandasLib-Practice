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

