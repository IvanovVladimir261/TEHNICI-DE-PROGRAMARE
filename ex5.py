#ex5.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


from time import time

import requests 
print(dir(requests))
print(type(requests.session))     # <class 'function'>
print(type(requests.Response))    #<class 'type'>
print(type(requests.exceptions))  #<class 'module'>

# Codul afișează cu dir() toate numele din modulul requests și verifică cu type() natura a trei dintre ele: session este o funcție, Response este o clasă, iar exceptions este un modul.