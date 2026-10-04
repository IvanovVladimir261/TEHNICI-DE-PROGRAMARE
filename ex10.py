#ex10.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests 
response=requests.get(BASE_URL, timeout=TIMEOUT)
print(response.status_code)

time.sleep(1)
try:
    response = requests.get(BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT)
    print(response.raise_for_status())
    print('Nu exista eroare')
except requests.HTTPError:
    print("Eroare HTTP:")

    # Codul cere o pagină care nu există, iar raise_for_status() aruncă HTTPError pentru codul 404, pe care try/except îl prinde și afișează mesajul de eroare în loc să oprească programul.