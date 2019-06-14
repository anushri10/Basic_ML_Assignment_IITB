from sklearn import preprocessing, linear_model
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
import pandas as pd 
import numpy as np

raw_data = pd.read_csv('Melbourne_housing_dataset_full.csv')
raw_data.drop(raw_data.select_dtypes(['object']), inplace=True, axis=1)
clean_data = raw_data.fillna(raw_data.mode().iloc[0])


new = clean_data[['Rooms', 'Bathroom', 'Car','BuildingArea']].copy()
array = clean_data.values
Y = array[:,4]
X = new.values
X_scaled = preprocessing.scale(X)
num =1

while num<=3:
	print('Iteration '+str(num),'\n')
	pft = PolynomialFeatures(degree = 1)  #polynomial regression using ridge linear model
	X_poly = pft.fit_transform(X_scaled)

	X_train, X_test, y_train, y_test = train_test_split(X_poly, Y,
	test_size = 0.30)

	model = linear_model.Ridge(alpha = 10000)
	model.fit(X_train, y_train)

	print('Poly ridge reg score: ',model.score(X_test,y_test),'\n')
	predicted = model.predict(X_test)
	pd.DataFrame(predicted).to_csv('Predcited_PolyRidgeReg'+str(num)+'.csv')
	pd.DataFrame(X_train).to_csv('x_train_poly_'+str(num)+'.csv', index = False, header= True)
	pd.DataFrame(y_train).to_csv('y_train_poly_'+str(num)+'.csv', index = False, header= True)
	pd.DataFrame(X_test).to_csv('x_test_poly_'+str(num)+'.csv', index = False, header= True)
	pd.DataFrame(y_train).to_csv('y_test_poly_'+str(num)+'.csv', index = False, header= True)
	

	#Decision Tree regressor 
	dtr = DecisionTreeRegressor(max_features=4, max_depth=10)
	X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y,
	test_size = 0.30)
	dtr.fit(X_scaled, Y)
	print('Decision Reg Tree score: ', cross_val_score(dtr, X_train, y_train, cv=5),'\n')

	predicted = dtr.predict(X_test)
	rmse = np.sqrt(mean_squared_error(y_test, predicted))
	print('\n','RMSE:')
	print(rmse,'\n')
	pd.DataFrame(predicted).to_csv('Predcited_DecisionTreeReg'+str(num)+'.csv')
	pd.DataFrame(X_train).to_csv('x_train_tree_'+str(num)+'.csv', index = False, header= True)
	pd.DataFrame(y_train).to_csv('y_train_tree_'+str(num)+'.csv', index = False, header= True)
	pd.DataFrame(X_test).to_csv('x_test_tree_'+str(num)+'.csv', index = False, header= True)
	pd.DataFrame(y_train).to_csv('x_test_tree_'+str(num)+'.csv', index = False, header= True)
	num +=1

'''
o/p seen - 
Iteration 1 

Poly ridge reg score:  0.6670612522934725 

Decision Reg Tree score:  [0.90754563 0.90315692 0.76221697 0.90789028 0.89697093] 


 RMSE:
0.23921638655612026 

Iteration 2 

Poly ridge reg score:  0.6220131908343427 

Decision Reg Tree score:  [0.90205279 0.81917256 0.89558807 0.90597745 0.89570183] 


 RMSE:
0.2917126523522837 

Iteration 3 

Poly ridge reg score:  0.707636494865928 

Decision Reg Tree score:  [0.72807982 0.89674648 0.90877317 0.89750151 0.89526562] 


 RMSE:
0.24188897561256847 

''''