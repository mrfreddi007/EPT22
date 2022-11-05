# from tensorflow import keras 
# import numpy as np 
# from keras.utils.vis_utils import plot_model
from pwn import *

# # Should probably install tensorflow for this to work, you can skip GPU as any CPU should do

# def map_pins(digit):
#     pin = [0]*20
#     pin[digit] = 1
#     return tuple(pin)

# with open("pincodes.txt","r") as f:
#     firstpins = f.read().split("\n")



# pinlist = []

# for i in range(20):
#     pinlist.append(map_pins(i))
# # for i in temp:
# #     temp1 = []
# #     a = i.split(" ")
# #     for j in a:
# #         temp1.append(map_pins(int(j)))
# #     pinlist.append(tuple(temp1))
# pinlist = tuple(pinlist)
# print(pinlist)

# my_model = keras.models.load_model('model.h5')

# print(my_model.get_config())
# print(my_model.summary())

# for i in pinlist:
#     output = list(my_model.predict(pinlist))
    
# map = dict()
# for i in range(20):
#     temp = list(output[i])
#     map[str(i)] = temp.index(max(temp))
    
# print(map)

# with open("newpins.txt","w") as f:
#     pins = []
#     for i in firstpins:
#         temp = i.split(" ")
#         print(temp)
#         temp1 = []
#         for i in temp:
#             temp1.append(str(map[i]))
#         pins.append(temp + temp1)
#         # pins.append(temp1)
        
#     for i in pins:
#         f.write(" ".join(i) + "\n")

with open("newpins.txt","r") as f:
    possiblepins = f.read().split("\n")
    
for pin in possiblepins:
    firstset = pin.split(" ")[0:5]
    secondset = pin.split(" ")[5:]
    r = remote("io.ept.gg",30921)
    print(r.recvuntil(b"1510432\n>"))
    r.sendline("".join(firstset))
    print(r.recv())
    r.sendline("".join(secondset))
    print(r.recv())