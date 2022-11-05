#!/usr/bin/env python3
import json

messages = []
with open("messages.json","r") as f:
    js = json.loads(f.read())
    for i in range(1,6):
        o = js[str(i)]['content'].split(" ")
        messages.append(o) 
        
with open("tst.txt","r") as f:
    a = f.read().split("\n")
    
dic = dict()
for i in a:
    i = i.split(" = ")
    dic[i[1]] = i[0]
    
translated = []
for i in messages:
    temp = []
    for j in i:
        try:
            temp.append(dic[j])
        except:
            pass
    translated.append(temp)
    
print(translated)