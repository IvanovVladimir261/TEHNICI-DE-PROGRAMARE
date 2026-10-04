#ex32.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir


import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response


def fetch_robots(base: str) -> str | None:
    response = fetch(base + "/robots.txt")
    if response.status_code == 200:
        return response.text
    return None


def disallowed_paths(robots_text: str | None) -> list[str]:
    if robots_text is None:
        return []
    paths = []
    for line in robots_text.splitlines():
        line = line.strip()
        if line.lower().startswith("disallow:"):
            value = line[len("disallow:"):].strip()
            if value:
                paths.append(value)
    return paths


robots = fetch_robots(BASE_URL)
print(disallowed_paths(robots))
print(disallowed_paths(None))   

# fetch_robots returnează textul lui /robots.txt sau None dacă lipsește, iar disallowed_paths extrage valorile Disallow: într-o listă și returnează listă goală dacă primește None.