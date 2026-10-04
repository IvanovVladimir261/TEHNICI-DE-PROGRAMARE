#ex9.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import time
import requests
response=requests.get(BASE_URL, timeout=TIMEOUT)
print(response.status_code) #atribut
time.sleep(1)
print(response.ok) #atribut
time.sleep(1)
print(response.url) #atribut 
time.sleep(1)
print(response.encoding) #atribut

# Codul trimite o cerere GET către BASE_URL și afișează patru atribute ale răspunsului: codul de stare, ok (True dacă nu e eroare), URL-ul final și codificarea textului. Sunt atribute, deci se scriu fără paranteze.