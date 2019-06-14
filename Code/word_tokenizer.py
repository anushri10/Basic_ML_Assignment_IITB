
import xml.etree.ElementTree as ET
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import pandas as pd 
import numpy as np

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
    print(num,'\n',tokenized_word) 
    num+=1
my_df = pd.DataFrame(tokenized_word)
my_df.to_csv('word.csv', index=False, header=False)    
