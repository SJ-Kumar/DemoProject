import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

t = sns.load_dataset('tips') 

print(t.head(10))

print (t.tail(5))

print (t.shape)

sns.scatterplot (x='total_bill', y='tip', data=t, hue='day')

