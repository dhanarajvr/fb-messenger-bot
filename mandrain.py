import json
dic={}
with open('input.json','r') as f:
    dic=json.load(f)
class Mandrains():
    def eng2pyin(self, sentence):
        if sentence.lower().strip() in dic:
            return dic[sentence.lower().strip()][0]


