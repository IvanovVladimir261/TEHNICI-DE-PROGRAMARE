#ex37.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import re
import requests

BASE_URL = "https://cybercor.org"
TIMEOUT = 10  # secunde


def fetch(url: str):
    response = requests.get(url, timeout=TIMEOUT)
    return response


def extract_links(html: str) -> list[str]:

    links = re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(links))


response = fetch(BASE_URL)
links = extract_links(response.text)
print(len(links), "legături unice")
for link in links:
    print(link)

    # Funcția extract_links caută cu re.findall toate valorile href="..." din HTML și elimină duplicatele cu dict.fromkeys, păstrând ordinea apariției.