import pandas as pd
import re
dicto={'Mandarin':[],'PinYin':[],'English':[]}
lines=open('/home/dhanraj/Documents/cedict_ts.txt').readlines()
for line in lines:
    k=re.split('\/',line)
    l=re.split('\[',k[0])

    dicto['Mandarin'].append(l[0])
    dicto['PinYin'].append(re.sub('\]','',l[1]))
    dicto['English'].append(k[1].lower().strip())

df=pd.DataFrame(dicto,columns=['Mandarin','PinYin','English'])
df.to_excel('out.xlsx')

