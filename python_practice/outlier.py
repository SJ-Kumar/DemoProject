import numpy as np
import pandas as pd
try:
    url = 'https://raw.githubusercontent.com/SJ-Kumar/datasets/main/aqi.csv?token=GHSAT0AAAAAABWK2JBOOYPG7YZ4TYWJSGGGYYBBXUA'

    df = pd.read_csv(url)
    print(df.describe())
    print(df.shape)
    
except:
    print("The dataset could not be loaded.")

