#ex6.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
import time
import requests 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde



#print(help(requests.get(BASE_URL)))
A=requests.get(BASE_URL,timeout=TIMEOUT)
print(A.status_code)

# Codul trimite o cerere GET către BASE_URL, salvează răspunsul în variabila A și afișează codul de stare din A.status_code (de exemplu 200).