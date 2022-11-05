#!/usr/bin/env python3
import json

with open("tst.txt","r") as f:
    a = f.read().split("\n")

lit = []
for i in a:
    lit.append(i.split(" = ")[1])
    
counts = {}
for item in lit:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
        
print(counts)