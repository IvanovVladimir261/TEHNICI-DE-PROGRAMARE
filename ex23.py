#ex23.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import time
import requests

BASE_URL = "https://adresa-reala-din-exercitii.ro"  # valoarea voastră reală
TIMEOUT = 10


def fetch(url, timeout=10):
    """Returnează obiectul răspuns pentru adresa url."""
    response = requests.get(url, timeout=timeout)
    return response


def get_status(url):
    """Returnează codul de stare HTTP pentru adresa url."""
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code



response = fetch(BASE_URL)
print("timeout implicit:", response.status_code)

response = fetch(BASE_URL, timeout=3)
print("timeout=3:", response.status_code)

# Parametrul timeout=10 din fetch este o valoare implicită: apelul fără argument o folosește, iar fetch(BASE_URL, timeout=3) o înlocuiește doar pentru acel apel.