import pandas as pd 
import numpy as np
raw_data = pd.read_csv('Melbourne_housing_dataset_full.csv')
encoded_df = raw_data[['CouncilArea','Regionname']]
#print(encoded_df['CouncilArea'].unique(),'\n')
#print(encoded_df['Regionname'].unique(),'\n')
print(encoded_df.isnull().sum())

#Label Encoding on CouncilArea and Regionname
encoded_df['CouncilArea']=encoded_df['CouncilArea'].astype('category')
encoded_df['Regionname']=encoded_df['Regionname'].astype('category')
print(encoded_df.dtypes)
encoded_df['CouncilArea']=encoded_df['CouncilArea'].cat.codes
encoded_df['Regionname']=encoded_df['Regionname'].cat.codes

#Populate missing values
encoded_df = encoded_df.fillna(encoded_df.mean())
print(encoded_df.isnull().sum(),'\n')
print(encoded_df.head())

#save to csv
#my_df = pd.DataFrame(tokenized_word)
encoded_df.to_csv('encoded.csv', index=False, header=True)  
