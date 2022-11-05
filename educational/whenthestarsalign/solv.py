#!/usr/bin/env python3
from PIL import Image

img = Image.open("./stars.png")

coords = []

with open("pixels","w") as f:
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x,y)) != (0, 0, 0):
                coords.append((x,y))
                f.write("1")
            else:
                f.write("0")

flag = ""    
for y in coords:
    flag +=chr(y[1])
    
print(flag)