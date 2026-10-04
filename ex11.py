#ex11.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests 

response = requests.get(BASE_URL, timeout=TIMEOUT)
#print(response.headers.items())
for name, value in response.headers.items():
    print(f"{name}: {value}")

    # Codul parcurge cu un for toate antetele răspunsului, folosind response.headers.items() care dă perechi (nume, valoare), și le afișează câte unul pe rând sub forma nume: valoare.