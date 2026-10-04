#ex40.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import hashlib
import requests

BASE_URL = "https://cybercor.org"
TIMEOUT = 10  # secunde


def fetch(url: str):
    response = requests.get(url, timeout=TIMEOUT)
    return response


def page_fingerprint(url: str) -> str:
    """Returnează amprenta SHA-256 a conținutului paginii."""
    response = fetch(url)
    return hashlib.sha256(response.content).hexdigest()


h1 = page_fingerprint(BASE_URL)
h2 = page_fingerprint(BASE_URL)
print(h1)
print(h2)
print("Identice:", h1 == h2)

# Funcția page_fingerprint calculează cu hashlib.sha256 amprenta conținutului paginii; amprentele diferă doar dacă pagina se schimbă între cereri (conținut dinamic, token, actualizare).
