import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# %matplotlib inline


data = pd.read_csv("Melbourne_housing_dataset_full.csv")

#print(data.head())

#print(data.describe())

data.drop(data.select_dtypes(['object']), inplace=True, axis=1)
data = data[data.Price != 0]
data = data.fillna(data.mean())
#print(data.info())
#print(data.isnull().sum(axis=0))

'''
#explore attribute relationship to target price

data['Rooms'].value_counts().plot(kind='bar')
plt.title('number of rooms')
plt.xlabel('rooms')
plt.ylabel('Count')
sns.despine

plt.figure(figsize=(10,10))
sns.jointplot(x=data.Lattitude.values, y=data.Longtitude.values, size=10)
plt.ylabel('Longtitude', fontsize=12)
plt.xlabel('Lattitude', fontsize=12)
plt.show()
plt1 = plt()
sns.despine

plt.scatter(data.Price,data.Landsize)
plt.title("Price vs Landsize")

plt.scatter(data.Price,data.Longtitude)
plt.title("Price vs Location of the area")

plt.scatter(data.Lattitude, data.Price)
plt.ylabel("Price")
plt.xlabel('Latitude')
plt.title("Latitude vs Price")

plt.scatter(data.Rooms,data.Price)
plt.title("rooms and Price ")
plt.xlabel("rooms")
plt.ylabel("Price")
plt.show()
sns.despine

plt.scatter(data.Bathroom,data.Price)
plt.title("bathrooms and Price ")
plt.xlabel("bathrooms")
plt.ylabel("Price")
plt.show()
sns.despine

plt.scatter(data.Car,data.Price)
plt.title("car and Price ")
plt.xlabel("car")
plt.ylabel("Price")
plt.show()
sns.despine

plt.scatter(data.Postcode,data.Price)
plt.title("Postcode and Price ")
plt.xlabel("Postcode")
plt.ylabel("Price")
plt.show()
sns.despine

plt.scatter((data['Rooms']+data['Bathroom']+ data['Car']),data['Price'])

plt.scatter(data.Distance,data.Price)
plt.title("Distance and Price ")
plt.xlabel("Distance")
plt.ylabel("Price")
plt.show()
sns.despine

'''
#train1 = data.drop(['Bedroom2','BuildingArea', 'YearBuilt', 'Propertycount', 'Distance','Postcode' ],axis=1)
#train1 = train1[train1.Landsize >200]
#train1 = train1.drop(['Landsize'],axis=1)
#print(train1.shape)
#print(train1.head())
num=1

while num<=3:
  train1 = data.drop(['Bedroom2','BuildingArea', 'YearBuilt', 'Propertycount', 'Distance','Postcode' ],axis=1)
  train1 = train1[train1.Landsize >200]
  #train1 = train1.drop(['Landsize'],axis=1)
  #print(train1.shape)
  #print(train1.head())
  reg = LinearRegression()

  labels = train1.drop(['Rooms','Bathroom','Car', 'Lattitude','Longtitude','Landsize'], axis=1)
  #print(labels.shape)
  train1 = train1.drop(['Price'],axis=1)

  x_train , x_test , y_train , y_test = train_test_split(train1 , labels , test_size = 0.30)

  reg.fit(x_train,y_train)
  predicted = reg.predict(x_test)
  print(reg.score(x_test,y_test))

  pd.DataFrame(predicted).to_csv('Predicted_LinReg'+str(num)+'.csv')
  pd.DataFrame(x_train).to_csv('x_train_lr_'+str(num)+'.csv', index = False, header= True)
  pd.DataFrame(y_train).to_csv('y_train_lr_'+str(num)+'.csv', index = False, header= True)
  pd.DataFrame(x_test).to_csv('x_test_lr_'+str(num)+'.csv', index = False, header= True)
  pd.DataFrame(y_train).to_csv('y_test_lr_'+str(num)+'.csv', index = False, header= True)

  num+=1

# o/p seen - 
#0.185624528446977
#0.18958262280861485
#0.1906722566939235
