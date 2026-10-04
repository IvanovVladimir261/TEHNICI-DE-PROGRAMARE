#ex4.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time
import urllib.request
a=urllib.request.urlopen(BASE_URL,timeout=TIMEOUT)
print(a.status)
time.sleep(1)
answer=a.read().decode('utf-8', timeout=TIMEOUT)
print(answer[:200], timeout=5)

# Codul deschide BASE_URL cu urllib.request.urlopen, afișează codul de stare, citește conținutul paginii și afișează primele 200 de caractere decodate din bytes în text.


