#!/usr/bin/env python3
with open("strenger.txt","r") as f:
    lines = f.read().split("\n")

with open("classesnames","w") as f:
    for line in lines:
        if " div " in line:
            f.write(line.replace(".","").split(" ")[0])