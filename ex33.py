#ex33.part3

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

def response_times(*urls) -> dict[str, float]:
    results={}
    for url in urls:
        start_time=time.time()
        response = fetch(url)
        end_time=time.time()
        results[url] = end_time - start_time
    return results

results=response_times(BASE_URL, ECHO_URL)
print(results)

# Prin *urls funcția response_times primește oricâte adrese, măsoară cu time.time() durata fiecărei cereri și returnează un dicționar {url: secunde}.