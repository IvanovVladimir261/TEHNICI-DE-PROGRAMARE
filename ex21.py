#ex21.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
import requests


BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response

response = fetch(BASE_URL)
print(response.status_code)

# Funcția fetch trimite o cerere GET către adresa primită și returnează întregul obiect răspuns; apelul pentru BASE_URL salvează răspunsul și afișează codul de stare.