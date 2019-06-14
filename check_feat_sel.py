
# Feature Extraction with RFE
import pandas as pd 
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.decomposition import PCA
# load data and clean
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

raw_data = pd.read_csv('Melbourne_housing_dataset_full.csv')
raw_data.drop(raw_data.select_dtypes(['object']), inplace=True, axis=1)
clean_data = raw_data.fillna(raw_data.mode().iloc[0])
print(clean_data.dtypes.index,'\n')

array = clean_data.values
selector = [x for x in range(array.shape[1]) if x != 4]
X = array[:,selector]
Y = array[:,4]

# feature extraction using RFE 
print('\n',"LOGISTIC REGRESSION",'\n')
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print(("Num Features: %d") % (fit.n_features_, ))
print(("Selected Features: %s") % (fit.support_, ))
print(("Feature Ranking: %s") % (fit.ranking_, ))

#feature extraction using Extra Tree
print('\n',"EXTRA TREEE",'\n')
model2 = ExtraTreesClassifier()
model2.fit(X, Y)
print(model2.feature_importances_)

'''
# feature extraction using PCA
pca = PCA(n_components=3)
fit = pca.fit(X)
# summarize components
print(("Explained Variance: %s") % (fit.explained_variance_ratio_, ))
print(fit.components_)
'''