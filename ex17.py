#ex17.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import requests

response = requests.get("http://cybercor.org", timeout=TIMEOUT)

for redirect in response.history:
    print(redirect.status_code, redirect.url)

print("URL final:", response.url)

# Codul cere varianta http:// a site-ului, parcurge lista response.history cu redirecționările intermediare (cod de stare și URL) și afișează la final URL-ul la care s-a ajuns.