#ex15.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
from pydoc import html
import requests

response = requests.get(BASE_URL, timeout=TIMEOUT)
lines=response.text.splitlines()
lines=max(lines, key=len)
print(lines)

# Codul împarte textul paginii în linii cu .splitlines() și găsește cea mai lungă linie cu max(lines, key=len), apoi o afișează.