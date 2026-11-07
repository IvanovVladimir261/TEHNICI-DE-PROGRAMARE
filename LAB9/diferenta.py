import os, sys
AICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AICI, "..", ".."))

from arsenal.privesc.enum import citeste_linii, nume, GTFO

START = AICI



def cai(fisier):
    return set(citeste_linii(fisier))


def main():
    baza = cai(os.path.join(START, "baza_suid.txt"))
    acum = cai(os.path.join(START, "suid.txt"))
    print("baza:", len(baza), " acum:", len(acum))

    
    noi = acum - baza
    print(len(noi), "SUID noi fata de sistemul curat")
    for c in sorted(noi):
        print(" ", c)

    risc = {nume(c): ("mare" if nume(c) in GTFO else "normal") for c in noi}
    periculoase = [c for c in sorted(noi) if nume(c) in GTFO]
    print("periculoase NOI:", periculoase)


if __name__ == "__main__":
    main()