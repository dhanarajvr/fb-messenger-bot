import json
dic={}
with open('input.json','r') as f:
    dic=json.load(f)
class Mandrains():
    def eng2pyin(self, sentence):
        if sentence.strip() in dic:
            return dic[sentence.strip()]


