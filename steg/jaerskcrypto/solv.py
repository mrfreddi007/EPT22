#!/usr/bin/env python3

with open("ppt/media/image4.jpeg","rb") as f:
    file = f.read()
    
mp3 = b""
for i in range(len(file)):
    if i >= 0x1736f7:
        mp3+=file[i].to_bytes()
        
with open("steg.mp3","wb") as f:
    f.write(mp3)