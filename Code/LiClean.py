import pandas as pd 
import numpy as np
raw_data = pd.read_csv('Melbourne_housing_dataset_full.csv')
clean_data = raw_data.interpolate(method = 'linear', limit_direction = 'backward')
clean_data['CouncilArea'] = raw_data.fillna(raw_data.mode().iloc[0])
clean_data['Regionname'] = raw_data.fillna(raw_data.mode().iloc[0])
clean_data.to_csv('LiClean.csv')
print(clean_data.isnull().sum())

'''
cant use linear interpolation on dtype = object. hence have used mode

'''