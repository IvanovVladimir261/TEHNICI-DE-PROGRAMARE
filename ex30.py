#ex30.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 

from urllib import response

import requests


BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]

def fetch(url):
   response=requests.get(url, timeout=TIMEOUT)
   return response

def security_headers(url: str) -> dict[str, bool]:
    response = fetch(url)
    results = {}
    for name in SECURITY_HEADERS:
      results[name] = name in response.headers
    return results

print(security_headers(BASE_URL))

# Funcția security_headers parcurge lista celor cinci antete de securitate și returnează un dicționar {antet: True/False}, după cum antetul există sau nu în răspuns.
