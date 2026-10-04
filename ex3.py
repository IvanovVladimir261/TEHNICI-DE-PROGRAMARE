#ex3.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

from time import time
import requests as rq
print(rq.get(BASE_URL,timeout=5))


# Codul importă requests sub aliasul rq și trimite o cerere GET către BASE_URL prin rq.get(), apoi afișează răspunsul (de exemplu <Response [200]>).

#Alias face codul mai usor de citit deoarece ne permite sa citim o conventie mai usosr (requsts - rq)
#Alias face codul mai greu de citit deoarece cuvantul se face mai scurt si nu intotdeauna se primeste 
#sa iti aduci aminte ce biblioteca se afla in spatele lui