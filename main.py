import argparse

import webtools
from webtools import get_title, security_headers, DEFAULT_HEADERS

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
url = args.url

print(webtools.get_title(webtools.fetch(url).text))

print(get_title(webtools.fetch(url).text))
print(security_headers(url))

print(DEFAULT_HEADERS)

rows = webtools.check_paths(url, ["/", "/robots.txt", "/sitemap.xml"])
webtools.save_csv(rows)

webtools.site_report(url)

# import webtools face funcțiile din webtools.py disponibile prin prefix (webtools.fetch, webtools.get_title); fișierul trebuie să fie în același folder cu main.py.
# Dacă main.py ar avea și o funcție proprie get_title, ar rămâne valabil numele definit ultimul: cea proprie ar înlocui funcția importată (sau invers, dacă importul vine după definiție), iar funcțiile din webtools.py nu ar fi afectate.
# argparse citește URL-ul din linia de comandă (python main.py https://cybercor.org), iar args.url înlocuiește BASE_URL în apelurile funcțiilor.
# check_paths returnează o listă de dicționare cu path, status și checked_at (ora din datetime.now().isoformat()), iar save_csv le scrie cu csv.DictWriter în report.csv.
# site_report apelează funcțiile din webtools pentru a colecta informațiile despre site, le afișează ca raport și salvează tot dicționarul în report.json.