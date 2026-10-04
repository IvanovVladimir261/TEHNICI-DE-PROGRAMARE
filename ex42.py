#ex42.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import socket


def resolve(hostname: str) -> str:
    """Returnează adresa IP a unui domeniu."""
    return socket.gethostbyname(hostname)


print(resolve("cybercor.org"))

# Funcția resolve folosește socket.gethostbyname pentru a transforma numele domeniului (fără https://) în adresa lui IP, pe care codul o afișează.