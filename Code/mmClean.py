import pandas as pd 
import numpy as np
raw_data = pd.read_csv('Melbourne_housing_dataset_full.csv')
clean_data = raw_data.fillna(raw_data.mode().iloc[0])
#clean_data = raw_data.fillna(raw_data.mean())
#clean_data = raw_data.fillna(raw_data.median())
clean_data.to_csv('mmClean.csv')
print(clean_data.isnull().sum())

''' 
The last two comments can be used inplace of the mode statement to find mean/median of columns. 
However dtype = object is not numerical and hence missing values are not imputed.
In that case such columns can be dropped.
Or can be encoded to numerical values and then mean/median can be applied. 
This is done in the cat_encoding script ahead.

''' 