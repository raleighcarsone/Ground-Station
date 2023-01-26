# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 01:36:27 2022

@author: 15129
"""

import matplotlib.pyplot as plt
import pandas as pd

data = load_my_data()
fig, ax = plt.subplots()
data['Points'].value_counts().plot(ax=ax, kind='bar')