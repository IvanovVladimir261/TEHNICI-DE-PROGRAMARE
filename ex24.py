#ex24.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import requests 

def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

# Funcția get_title primește un șir HTML, găsește cu .find() pozițiile lui <title> și </title> și returnează textul dintre ele, curățat cu .strip(), fără nicio operație de rețea.