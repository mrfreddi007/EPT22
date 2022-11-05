#!/usr/bin/env python3
import h5py
from keras.models import load_model
from keras.preprocessing import image
from keras.utils.vis_utils import plot_model
import numpy as np
import json
import string

ascii = dict()
asciiinv = []
with open("ascii.txt","r") as f:
    a = f.read().split("\n")
    for line in a:
        l = line.split("\t")
        ascii[l[0]] = l[1]
        asciiinv.append(l[0])

messages = []
with open("messages.json","r") as f:
    js = json.loads(f.read())
    for i in range(1,6):
        o = js[str(i)]['content'].split(" ")
        temp = []
        for j in o:
            temp1 = []
            for k in j:
                temp1.append(int(k))
            temp.append(tuple(temp1))
        temp = tuple(temp)
        messages.append(temp)    
            



model = load_model('secret.h5')
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
model.summary()
# for message in messages:
#     print(message)
#     output = model.predict(message)
#     print(output)

testset = []
for i in asciiinv:
    temp = []
    for j in i:
        temp.append(int(j))
    testset.append(tuple(temp))
testset = tuple(testset)

print(a[0])

output = model.predict(testset)
with open("tst.txt","w") as f:
    k = 0
    for i in output:
        
        line = []
        for j in i:
            line.append(str(round(j)))
        f.write(a[k].split("\t")[1] + " = " + "".join(line) + "\n")
        k+=1
     
        
