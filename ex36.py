#ex36.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir


from urllib.parse import urljoin

BASE_URL = "https://cybercor.org"

links = ["/about", "contact.html", "../index.html"]

for link in links:
    print(link, "->", urljoin(BASE_URL, link))

    # Funcția urljoin combină BASE_URL cu fiecare legătură relativă din listă și returnează URL-ul complet; ../ nu poate urca mai sus de rădăcina site-ului.