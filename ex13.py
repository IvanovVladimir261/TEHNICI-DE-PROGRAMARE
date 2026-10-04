#ex13.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests 

response = requests.get(BASE_URL, timeout=TIMEOUT)

numar = response.text.lower().count("cyber")
print("Cuvântul 'cyber' apare de", numar, "ori")

# Codul transformă textul paginii în litere mici cu .lower() și numără apariția cuvântului „cyber” cu .count(); metodele se pot înlănțui pentru că .lower() returnează un șir nou.

# Se pot înlănțui .lower() și .count() deoarece .lower() returnează un șir nou
# , iar orice șir are metoda .count(). Rezultatul unei metode devine
# obiectul pe care se apelează următoarea metodă.