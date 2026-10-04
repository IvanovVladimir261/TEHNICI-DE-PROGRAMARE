#ex26.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time
import requests



def fetch(url: str, timeout: int = 10) -> requests.Response:

    response = requests.get(url, timeout=timeout)
    return response


def get_status(url: str) -> int:
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code


def get_title(html: str) -> str | None:
   
    start = html.find("<title>")
    if start == -1:
        return None
    start += len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

print(get_status(123))

# Adnotările (url: str, -> int) arată ce tipuri se așteaptă, dar Python nu le verifică la rulare: get_status(123) a eșuat în requests cu MissingSchema, nu din cauza adnotărilor.