import numpy as np
import pandas as pd
try:
    url = 'https://raw.githubusercontent.com/SJ-Kumar/datasets/main/bank_marketing_dataset.csv?token=GHSAT0AAAAAABWK2JBOOD2QVORNP6SNJTSSYYBBO2Q'

    df = pd.read_csv(url)
    print(df.describe())
    print(df.shape)
    
except:
    print("The dataset could not be loaded.")

