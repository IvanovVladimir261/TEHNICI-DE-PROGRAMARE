#ex38.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import re
import requests
from urllib.parse import urljoin, urlparse

BASE_URL = "https://cybercor.org"
TIMEOUT = 10  # secunde


def fetch(url: str):
    response = requests.get(url, timeout=TIMEOUT)
    return response


def extract_links(html: str) -> list[str]:
    links = re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(links))


def split_links(links: list[str], domain: str) -> tuple[list[str], list[str]]:
    site = urlparse(domain).netloc
    internal = []
    external = []
    for link in links:
        full = urljoin(domain, link)
        if urlparse(full).netloc == site:
            internal.append(full)
        else:
            external.append(full)
    return internal, external


response = fetch(BASE_URL)
links = extract_links(response.text)
internal, external = split_links(links, BASE_URL)

print("Interne:", len(internal))
for link in internal:
    print("  ", link)

print("Externe:", len(external))
for link in external:
    print("  ", link)

    # Funcția split_links transformă fiecare legătură în URL complet cu urljoin, apoi compară domeniul ei (urlparse().netloc) cu cel al site-ului și returnează două liste: interne și externe.

