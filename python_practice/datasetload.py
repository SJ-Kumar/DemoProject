import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#df = pd.read_csv(r'C:\10-Practice\DemoProject\ds_salaries.csv')
df = pd.read_csv('https://raw.githubusercontent.com/SJ-Kumar/datasets/main/ds_salaries.csv?token=GHSAT0AAAAAABWK2JBPHZOSPY6DMP4MUCFYYYBB23Q')
print(df.head(10))
print(df.shape)
print(df.job_title.value_counts())