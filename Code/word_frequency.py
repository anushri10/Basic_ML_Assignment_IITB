
import xml.etree.ElementTree as ET
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd 
import numpy as np
import csv

tree = ET.parse('7596.male.26.Internet.Scorpio.xml')
root = tree.getroot()
print(root, '\n')
num = 1

for post in root.iter('post'):
    data = post.text
    data = data.strip()
    if num==1:
    	tokenized_word=word_tokenize(data)	
    else:
    	temp_word = word_tokenize(data)
    	tokenized_word+=temp_word 	
    
    word_freq = FreqDist(tokenized_word)
    
    name ='para'+str(num)+'_'
    pd.DataFrame.from_dict(data=word_freq, orient='index').to_csv(name+'frequency.csv', header=False)
    num+=1
   
