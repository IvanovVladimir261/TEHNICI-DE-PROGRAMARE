#ex28.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time
import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def get_status(url: str) -> int:
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code


def check_paths(base: str, paths: list[str]) -> dict[str, int]:
    results = {}
    for path in paths:
        results[path] = get_status(base + path)
        time.sleep(1)
    return results


rezultate = check_paths(BASE_URL, ["/", "/robots.txt", "/sitemap.xml"])
print(rezultate)


# Funcția check_paths apelează get_status pentru fiecare cale din listă și returnează un dicționar {cale: cod_de_stare}, cu pauză de o secundă între cereri.