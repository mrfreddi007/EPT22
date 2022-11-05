#!/usr/bin/env python3
import requests

#while True:
print(requests.post("http://127.0.0.1:5000",data={'name':'admin'}).cookies)