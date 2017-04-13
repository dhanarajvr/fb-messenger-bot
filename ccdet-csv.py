import pandas as pd
import re
dicto={'mandrain':[],'pynin':[],'english':[]}
lines=open('/home/dhanraj/Documents/cedict_ts.txt').readlines()
for line in lines:
    k=re.split('\/',line)
    l=re.split('\[',k[0])

    dicto['mandrain'].append(l[0])
    dicto['pynin'].append(re.sub('\]','',l[1]))
    dicto['english'].append(k[1])

df=pd.DataFrame(dicto,columns=['mandrain','pynin','english'])
df.to_excel('out.xlsx')

