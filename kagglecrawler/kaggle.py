import json
import pandas as pd 
import datadotworld as dw
import os
import pandas as pd 
f = open('link.txt','r')
Lines = f.readlines()
link = []

for i in range(len(Lines)):
    if i%2 == 0:
        link.append((Lines[i])[1:].replace('\n', ''))

os.system('kaggle datasets download akshaydattatraykhare/diabetes-dataset -p kaggle')
# for i in range(len(link)):
    
#     command = 'kaggle datasets download {} -p kaggle'.format(link[i])
#     print(command)
#     os.system(command)