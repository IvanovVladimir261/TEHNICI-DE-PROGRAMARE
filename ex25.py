#ex25.part3

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

def get_title(html):
    start = html.find("<title>")
    if start == -1:
        return None
    start += len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

help(get_title)

# Funcția get_title returnează None dacă pagina nu are <title>, iar help(get_title) afișează în consolă semnătura și docstring-ul funcției.