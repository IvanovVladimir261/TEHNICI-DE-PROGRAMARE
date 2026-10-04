#ex18.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests

response_head = requests.head(BASE_URL, timeout=TIMEOUT)

time.sleep(1)  

response_get = requests.get(BASE_URL, timeout=TIMEOUT)

print("HEAD:", len(response_head.content))
print("GET: ", len(response_get.content))

# Codul trimite o cerere HEAD (doar antete) și una GET (pagina completă), apoi compară lungimea conținutului: la HEAD este 0, la GET este dimensiunea paginii.
