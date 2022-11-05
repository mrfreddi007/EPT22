#!/usr/bin/env python3
from pwn import *
import base64

r = remote("io.ept.gg", 30047)
print(r.recvuntil(b"ready?\n"))
r.sendline(b"\n")
flag = b""

# while b"EPT{" not in flag:
print(r.recvuntil(b"'se'])?\n"))
print(r.recv(4096))