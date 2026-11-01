import re
import base64
from urllib.parse import unquote
import hashlib
import argparse, json


s = "Salut"
b = s.encode()
print(b, b[0])

h = b.hex()
print(h)

print(bytes.fromhex(h))

def ghici_strat(s):
    if re.search(r"%[0-9a-fA-F]{2}", s):
        return "url"
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/]+=*", s):
        return "base64"
    return "necunoscut"

print(ghici_strat("%2Fetc"))
print(ghici_strat("48656c6c6f"))
print(ghici_strat("U2FsdXQ="))
print(ghici_strat("salut lume!"))


def desfa(s):
    strat = ghici_strat(s)
    if strat == "base64":
        return strat, base64.b64decode(s)
    if strat == "hex":
        return strat, bytes.fromhex(s)
    if strat == "url":
        return strat, unquote(s).encode()
    return strat, s.encode()

print(desfa("U2FsdXQ="))
print(desfa("48656c6c6f"))
print(desfa("%2Fetc"))


def citibil(b):
    return all(32 <= c < 127 for c in b)

val = "NTM1OTU3NTk="
for _ in range(8):
    strat, b = desfa(val)
    if strat == "necunoscut" or not citibil(b):
        break
    print(strat, b)
    val = b.decode()
print("rezultat:", val)



date = open("probe/xor.bin", "rb").read()
for k in range(256):
    clar = bytes(b ^ k for b in date)
    if citibil(clar):
        print("cheie:", k, clar.decode())


tinta = open("probe/hashuri.txt").readline().strip()
print(len(tinta))

alg = {32: "md5", 40: "sha1", 64: "sha256"}[len(tinta)]
for cuv in open("probe/wordlist.txt", encoding="latin1"):
    cuv = cuv.strip()
    if hashlib.new(alg, cuv.encode()).hexdigest() == tinta:
        print("gasit:", cuv)
        break



p = argparse.ArgumentParser()
p.add_argument("intrare")
p.add_argument("--fisier", action="store_true")
a = p.parse_args()

if a.fisier:
    sir = open(a.intrare).read().strip()
else:
    sir = a.intrare

val = sir
for _ in range(8):
    strat, b = desfa(val)
    if strat == "necunoscut" or not citibil(b):
        break
    val = b.decode()

print(val)
json.dump({"strat": strat, "rezultat": val},
          open("arsenal/forensics/fisa.json", "w"))

