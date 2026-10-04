#ex22.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import time
import requests

BASE_URL = "https://exemplu.com"  # păstrați valoarea din exercițiile anterioare
TIMEOUT = 10


def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response


def get_status(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code


for path in ["/", "/robots.txt", "/sitemap.xml"]:
    status = get_status(BASE_URL + path)
    print(path, status)
    time.sleep(1)

    # Funcția get_status returnează doar codul de stare al unei adrese, iar bucla o apelează pentru /, /robots.txt și /sitemap.xml, cu pauză de o secundă între apeluri.