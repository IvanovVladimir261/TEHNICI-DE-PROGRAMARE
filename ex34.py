#ex34.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir


import time
from urllib import response

import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response

def log(message, **details):
    parts = [message]
    for key, value in details.items():
        parts.append(f"{key}={value}")
    print(" | ".join(parts))


log("verificat", url=BASE_URL, status=200)

# Prin **details funcția log primește orice argumente cu nume într-un dicționar și afișează mesajul urmat de fiecare pereche cheie=valoare, separate prin " | ".

#print() afișează o valoare pe ecran, pentru ochii omului. După afișare, valoarea se pierde: programul nu o mai poate folosi.
#return trimite valoarea înapoi către codul care a apelat funcția, ca aceasta să fie salvată într-o variabilă, trecută la altă funcție sau testată. Nu afișează nimic de la sine.