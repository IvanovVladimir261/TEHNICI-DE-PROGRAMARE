#ex8.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
 
try:
   import bs4
except ImportError:
   print("Instalați modulul cu: pip install beautifulsoup4")

# Codul încearcă să importe modulul bs4 și, dacă nu este instalat (ImportError), afișează un mesaj cu comanda de instalare, în loc să se oprească cu eroare.

# Modul = un singur fișier .py cu cod.
# Pachet = un folder cu mai multe module și un fișier __init__.py (urllib, requests).
# Bibliotecă = termen general pentru o colecție de cod reutilizabil,
# poate fi un modul sau un pachet (biblioteca standard, biblioteca requests).