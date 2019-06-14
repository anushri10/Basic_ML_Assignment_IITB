import pandas as pd 
import numpy as np
raw_data = pd.read_csv('Melbourne_housing_dataset_full.csv')
bool_list = []
new_list =[]
clean_data = raw_data.fillna(raw_data.mean())

#check if missing values are there in each row
bool_list = raw_data.isnull().sum(axis=1)
bool_list = bool_list.to_dict()
for k, v in bool_list.items():
	if v !=0:
		#print(clean_data.iloc[k].values.tolist())
		new_list.append(clean_data.iloc[k].values.tolist())

df = pd.DataFrame(new_list, columns=['Suburb','Address', 'Rooms','Type','Price', 'Method', 'SellerG', 'Date', 'Distance', 'Postcode',
'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'])
df.to_csv('extracted.csv', header = True)

