#ex43.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import socket
import ssl
import time

TIMEOUT = 10  # secunde


def cert_days_left(hostname: str) -> int:
    """Returnează câte zile mai sunt până la expirarea certificatului."""
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure:
            cert = secure.getpeercert()
    expires = ssl.cert_time_to_seconds(cert["notAfter"])
    return int((expires - time.time()) // 86400)


print(cert_days_left("cybercor.org"), "zile rămase")

# Funcția cert_days_left se conectează la portul 443, citește certificatul cu getpeercert(), convertește data notAfter în secunde cu ssl.cert_time_to_seconds și returnează câte zile au rămas până la expirare.

#handle_starttag() este apelată de parserul însuși, adică de metoda feed() a clasei HTMLParser. Voi apelați doar finder.feed(html). 
# În timp ce parcurge textul HTML, parserul recunoaște fiecare tag de deschidere
#  și apelează automat self.handle_starttag(tag, attrs), transmițând numele tagului și lista de atribute.