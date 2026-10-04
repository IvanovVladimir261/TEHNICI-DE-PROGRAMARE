#ex19.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import requests

response = requests.get(BASE_URL, timeout=TIMEOUT)

if len(response.cookies) == 0:
    print("Niciun cookie setat")
else:
    for cookie in response.cookies:
        print(cookie.name, cookie.secure)

        # Codul verifică dacă serverul a setat cookie-uri în response.cookies; dacă nu, afișează un mesaj, iar dacă da, afișează numele fiecărui cookie și dacă are atributul secure.