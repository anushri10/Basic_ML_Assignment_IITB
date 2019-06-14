
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
stop_words=set(stopwords.words("english"))
#print('stopwords are: ','\n',stop_words,'\n')
para_sw=[]
para_nsw=[]
num = 1
for post in root.iter('post'):
    data = post.text
    data = data.strip()
    tokenized_word=word_tokenize(data)
    name = 'para'+str(num)
    para_sw.append(name)
    para_nsw.append(name)
    for w in tokenized_word:
    	if w in stop_words:
        	para_sw.append(w)
    	else:
    		para_nsw.append(w)
    num+=1

my_df = pd.DataFrame(para_sw)
my_df.to_csv('stopwords.csv', index=False, header=False)    
my_df = pd.DataFrame(para_nsw)
my_df.to_csv('nonstopwords.csv', index=False, header=False)