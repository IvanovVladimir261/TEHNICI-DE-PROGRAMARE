#ex2.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time

import requests
print(requests.get(BASE_URL, timeout=5))
time.sleep(1)
from requests import get
print(get(BASE_URL, timeout=5))


# Codul trimite aceeași cerere GET către BASE_URL în două moduri: cu import requests (requests.get) și cu from requests import get (get direct), cu o pauză de o secundă între ele.

# Avantaj import requests: se vede clar de unde vine funcția (requests.get),
# deci codul e mai ușor de citit și nu apar conflicte cu alte funcții "get".

# Avantaj from requests import get: codul e mai scurt,
# pentru că se scrie direct get(...), fără prefixul requests.