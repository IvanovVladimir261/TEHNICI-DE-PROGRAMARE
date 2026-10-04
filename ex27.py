#ex27.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time
import requests

def fetch(url):
    response=requests.get(url, timeout=TIMEOUT)
    return response 

try:
    page_exists = fetch(BASE_URL)
    print("True")
except requests.exceptions.RequestException:
    print("False")

    # Codul încearcă să descarce pagina într-un try; dacă cererea reușește afișează True, iar dacă requests aruncă o excepție de rețea, o prinde cu except și afișează False.
