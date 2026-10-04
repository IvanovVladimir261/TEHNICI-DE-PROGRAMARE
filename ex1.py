#ex1.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import requests
print(requests.__version__)

import urllib.request

# Codul importă biblioteca requests și afișează versiunea ei cu requests.__version__, apoi importă și urllib.request pentru comparație.
#urllib este o biblioteca "oficiala" de la python, iar requests ese facuta de o echipa aparte