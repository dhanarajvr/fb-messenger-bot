import json
import pandas as pd
from unidecode import unidecode
df=pd.read_excel('Mandarin_Sentences.xlsx',encoidng='utf-8')
dic={}
for index, row in df.iterrows():
    k=row['English']
    dic[k]=unidecode(row['PinYin'])

with open('input.json','w+') as f:
    f.write(json.dumps(dic))
dic1={}
with open('input.json','r') as f:
    dic1=json.load(f)
print dic1


