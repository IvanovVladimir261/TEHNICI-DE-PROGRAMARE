#ex14.part2

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
from pydoc import html
import requests 

response = requests.get(BASE_URL, timeout=TIMEOUT)
titlu= response.text.strip().find("<title>") + len("<title>")
print(titlu)

# Codul caută poziția etichetei <title> în textul paginii cu .find() și adaugă len("<title>") ca să obțină indexul unde începe titlul.