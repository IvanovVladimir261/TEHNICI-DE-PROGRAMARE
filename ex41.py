#ex41.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import json
import requests

BASE_URL = "https://cybercor.org"
TIMEOUT = 10  # secunde


def fetch(url: str):
    response = requests.get(url, timeout=TIMEOUT)
    return response


response = fetch(BASE_URL)

with open("headers.json", "w", encoding="utf-8") as file:
    json.dump(dict(response.headers), file, indent=2)

with open("headers.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded.get("Server", "lipsește"))

# Codul salvează antetele răspunsului în headers.json cu json.dump, apoi le încarcă înapoi cu json.load ca dicționar și afișează antetul Server.