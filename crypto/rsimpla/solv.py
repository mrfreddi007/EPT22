from Crypto.Util.number import bytes_to_long, getPrime
from sympy import nextprime
from decimal import *


with open("output.txt","r") as f:
    temp = f.read().split("\n")
    
e = int(temp[0].replace("e: ",""))
n = int(temp[1].replace("n: ",""))
c = int(temp[2].replace("c: ",""))
print(e)
print(n)
print(c)

# https://docs.python.org/3/library/decimal.html
c = Decimal(c)
e = Decimal(e)

getcontext().prec = 500 # Set a big enough precision
root = pow(c, 1/e) # Calculate c^(1/e) = m^(e * 1/e) = m
print(root)

# Decode with no padding
m = hex(int(root))[2:-1] # Number to hex
m = ''.join(chr(int(m[i:i+2], 16)) for i in range(0, len(m), 2)) # Hex to Ascii
print(m)

# a_prime = getPrime(2048)
# b_prime = getPrime(2048)
# p = nextprime(a_prime)
# q = nextprime(b_prime)
# n = p * q
# e = 3
# flag = open("flag.txt", "r").read().encode("utf-8")
# assert flag.startswith(b"EPT{")
# assert flag.endswith(b"}")
# assert len(flag) == 51
# c = pow(bytes_to_long(flag), e, n)

# with open('output.txt', 'w') as f:
#     f.write(f"e: {e}\n")
#     f.write(f"n: {n}\n")
#     f.write(f"c: {c}\n")