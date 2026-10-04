#ex16.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
from pydoc import html
import requests

response = requests.get(BASE_URL, timeout=TIMEOUT)
if(response.url.startswith("https")):
    print("Conexiune securizata.")
else:
    print("Conexiune nesecurizata.")

    # Codul verifică cu .startswith("https") dacă URL-ul final al răspunsului începe cu https și afișează dacă conexiunea este securizată sau nu.