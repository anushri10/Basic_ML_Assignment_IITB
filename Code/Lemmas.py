from nltk.stem.wordnet import WordNetLemmatizer
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


lem = WordNetLemmatizer()
lemmas=[]
num = 1

for post in root.iter('post'):
    data = post.text
    data = data.strip()
    tokenized_word=word_tokenize(data)
    name = 'para'+str(num)
    lemmas.append(name)
    for w in tokenized_word:
    	lemmas.append(lem.lemmatize(w))

my_df = pd.DataFrame(lemmas)
my_df.to_csv('lemmas.csv', index=False, header=False)