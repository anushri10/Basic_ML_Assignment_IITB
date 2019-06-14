
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
    	tokenized_text=sent_tokenize(data)
    	
    else:
    	temp_text = sent_tokenize(data)
    	tokenized_text+=temp_text
    	
    print(num,'\n',tokenized_text)
    
    num+=1
my_df = pd.DataFrame(tokenized_text)
my_df.to_csv('sentence.csv', index=False, header=False)    
