#ex39.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir


import requests
from html.parser import HTMLParser

BASE_URL = "https://cybercor.org"
TIMEOUT = 10  # secunde


def fetch(url: str):
    response = requests.get(url, timeout=TIMEOUT)
    return response


class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            src = dict(attrs).get("src")
            if src:
                self.images.append(src)

response = fetch(BASE_URL)

finder = ImageFinder()
finder.feed(response.text)

print(len(finder.images), "imagini")
for src in finder.images:
    print(src)

    # Clasa ImageFinder moștenește HTMLParser și suprascrie handle_starttag, pe care parserul o apelează singur din feed() pentru fiecare tag; la tag-urile img, ea salvează atributul src în lista images.