#ex29.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

from os import name

from socket import timeout
import time
from urllib import response
import requests

def fetch(url):
    response=requests.get(url, timeout=TIMEOUT)
    return response

def get_header(url: str, name: str, default: str = "lipsește"):
  response = fetch(url)
  return response.headers.get(name, default)

print(get_header(BASE_URL, name="Server"))
print(get_header(BASE_URL, name="X-Inexistent"))               
print(get_header(BASE_URL, name="X-Inexistent", default="N/A"))  
# Funcția get_header returnează valoarea unui singur antet cu headers.get(name, default), iar apelurile cu argumente cu nume (name=, default=) arată clar ce reprezintă fiecare valoare.