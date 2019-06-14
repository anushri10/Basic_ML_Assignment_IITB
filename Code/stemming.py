from nltk.stem import PorterStemmer
import xml.etree.ElementTree as ET
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd 
import numpy as np
import csv

tree = ET.parse('7596.male.26.Internet.Scorpio.xml')
root = tree.getroot()
print(root, '\n')


ps = PorterStemmer()
stems=[]
num = 1

for post in root.iter('post'):
    data = post.text
    data = data.strip()
    tokenized_word=word_tokenize(data)
    name = 'para'+str(num)
    stems.append(name)
    for w in tokenized_word:
    	stems.append(ps.stem(w))

my_df = pd.DataFrame(stems)
my_df.to_csv('stems.csv', index=False, header=False)