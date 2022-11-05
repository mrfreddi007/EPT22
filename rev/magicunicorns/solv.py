#!/usr/bin/env python3
from pwn import *
#Navnet er max 39 karakterer
#Reg-key er 

#r = process("./magic")
r = remote("io.ept.gg",30050)
print(r.recv())
r.sendline(b"jegheterfredrikogerikkealtforflinkireve\x00") #10361 base10
print(r.recv())

send = [1480, 1500, 1400, 1450, 1460, 1761, 1310,
        1400, 1450, 1460, 1761, 1310, 1480, 1500,
        1460, 1761, 1310, 1480, 1500, 1400, 1450,
        1310, 1480, 1500, 1400, 1450, 1460, 1761,
        1500, 1400, 1450, 1460, 1761, 1310, 1480,
        1450, 1460, 1761, 1310, 1480, 1500, 1400,
        1761, 1310, 1480, 1500, 1400, 1450, 1460
]
j = 0
for i in send:
    print(j)
    j+=1
    r.send(p64(i) + b"\r")
    
print(r.recv())

    
r.close()