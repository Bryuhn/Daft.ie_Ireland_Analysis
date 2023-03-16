import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from scipy.stats import norm
import datetime
import seaborn as sb

# Colours
font_colour = '#000000'
outline_colour = '#ffffff'
colours = ['#00589C', '#016FC4', '#1891C3', "#3AC0DA", '#3DC6C3', '#50E3C2']


# Create date
date = datetime.datetime.now().strftime("%d-%m-%Y")
print(date)
# Read SCV
df = pd.read_csv("Daft_rental_data_" + str(date) +".csv")

print(df)