#ex7.part1

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


import requests 
import time
start=time.perf_counter()
response=requests.get(BASE_URL,timeout=TIMEOUT)
finish=time.perf_counter()
responsetime=finish-start

time.sleep(1)

print("perf_counter:", responsetime)
print("response.elapsed:", response.elapsed.total_seconds())


# Codul măsoară durata cererii în două moduri: manual, cu time.perf_counter() înainte și după cerere, și direct din response.elapsed, apoi afișează ambele valori pentru comparație.

#comparand rezultatele, am observat ca perf_counter este mai precis, deoarece returneaza timpul in secunde mai exact
#in timp ce repsonse.elapse cu o precizie mai mica. Totodata, am observat ca perf_counter este doar un nr 
#al functiei responsetime=finish-start, in timp ce response.elapsed este atributul la requests.get()


