#ex31.part3

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

def score_headers(results: dict[str, bool]) -> str:
    present = sum(results.values())
    total = len(results)
    return f"{present}/{total}"


print(security_headers(BASE_URL))
print(score_headers(security_headers(BASE_URL)))

# Funcția score_headers primește dicționarul din security_headers, adună valorile True cu sum() și returnează un șir precum "3/5"; cele două funcții se apelează una în alta.
