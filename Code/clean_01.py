import pandas as pd 
import numpy as np
raw_data = pd.read_csv('Melbourne_housing_dataset_full.csv')
print(raw_data.isnull().sum())
clean_data = raw_data.dropna(axis=1)
clean_data.to_csv('drop.csv')

