#ex12.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests 

response = requests.get(BASE_URL, timeout=TIMEOUT)
print(response.headers.get("Server", "lipseste"))
print(response.headers.get("Content-Type", " lipseste"))
time.sleep(1)
print(response.headers.get("content-type" , 'lispseste'))


# Codul citește antete individuale cu headers.get(nume, valoare_implicită), care returnează valoarea sau textul implicit dacă antetul lipsește; căutarea nu ține cont de majuscule, deci Content-Type și content-type dau același rezultat.

#am observat ca response.headers.get este un case insensitive, ceea ce inseamna ca nu conteaza daca scriem
#cu litera mica sau mare si va afisa la ecran acelasi raspuns
