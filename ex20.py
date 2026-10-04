#ex20.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import requests
import time
session = requests.Session()
session.headers.update({"User-Agent": "WebLab-Ivanov-Vladimir"})

response = session.get(ECHO_URL + "/headers", timeout=TIMEOUT)

time.sleep(1)  

print(response.text)
print("User-Agent trimis:", response.json()["headers"]["User-Agent"])

# Codul creează o sesiune cu un antet User-Agent propriu, trimite cererea către /headers de la httpbin și afișează răspunsul, apoi extrage User-Agent-ul cu response.json(), care transformă textul JSON într-un dicționar.

# response.text este un atribut.
# response.json() este o metodă de a tranforma textul JSON și returnează un dicționar, deci se apelează cu paranteze.