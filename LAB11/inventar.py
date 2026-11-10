from dataclasses import dataclass, asdict
import json

@dataclass
class Proces:
    pid: int
    nume: str
    user: str
    cale: str

p=Proces(3120, "update.exe", "ana", r"C:\Users\ana\AppData\Local\Temp\update.exe")
print(p.pid, p.nume)
print(p)

CAI_SUSPECTE=("\\Temp\\", "\\Roaming\\")
@dataclass
class Proces:
    pid: int; nume: str; user: str; cale: str
    def e_suspect(self):
        for cai in CAI_SUSPECTE:
            if cai in self.cale:
                return True
        return False
p = Proces(1234, "update.exe", "ivano", "C:\\Users\\ivano\\AppData\\Local\\Temp\\update.exe")
print(p.e_suspect())


SUSPECTE_ID={4625,1102,7045}
@dataclass
class Eveniment:
    id: int; nivel: str; sursa: str; cont: str; mesaj: str
    def e_suspect(self):
        for self.id in SUSPECTE_ID:
            return True 
        return False

e = Eveniment(4625, "High", "Security", "ivano", "Failed login attempt")
print(e.e_suspect())


def procese_din_json(cale):
    with open(cale, encoding="utf-8") as f:
        date = json.load(f)
    return [Proces(**p) for p in date]

procese=procese_din_json("arsenal/windows/start/procese.json")
print("procese:", len(procese))
print("suspecte:", sum(1 for p in procese if p.e_suspect()))


from datetime import date
@dataclass
class Inventar:
    procese: list
    @classmethod
    def din_json(cls, cale):
        with open(cale, encoding="utf-8") as f:
            date = json.load(f)
            return cls([Proces(**p) for p in date])
    def __len__(self):
        return len(self.procese)
inv=Inventar.din_json("arsenal/windows/start/procese.json")
print("procese:", len(inv))

@dataclass
class Inventar:
    procese: list

    @classmethod
    def din_json(cls, cale):
        with open(cale, encoding="utf-8") as f:
            return cls([Proces(**d) for d in json.load(f)])

    def __len__(self):
        return len(self.procese)

    def suspecte(self):
        return [p for p in self.procese if p.e_suspect()]

    def pe_user(self):
        rez = {}
        for p in self.procese:
            rez.setdefault(p.user, []).append(p.nume)
        return rez

inv = Inventar.din_json("arsenal/windows/start/procese.json")
print("procese:", len(inv))

for p in inv.suspecte():
    print(f"  [{p.pid}] {p.nume}  {p.cale}")
print(inv.pe_user())



def evenimente_din_json(cale):
      with open(cale, encoding="utf-8") as f:
        return [Eveniment(**d) for d in json.load(f)]

from dataclasses import asdict

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("capturi")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    inv = Inventar.din_json(a.capturi + "/procese.json")
    ev = evenimente_din_json(a.capturi + "/evenimente.json")
    suspecte = inv.suspecte()
    alarma = [e for e in ev if e.e_suspect()]

    if a.json:
        raport = {
            "procese_suspecte": [asdict(x) for x in suspecte],
            "evenimente_alarma": [asdict(e) for e in alarma],
        }
        print(json.dumps(raport, indent=2, ensure_ascii=False))
    else:
        print(f"Procese: {len(inv)} | suspecte: {len(suspecte)}")
        for x in suspecte:
            print(f"  [{x.pid}] {x.nume}  ({x.user})  {x.cale}")
        print(f"Evenimente: {len(ev)} | alarma: {len(alarma)}")
        for e in alarma:
            print(f"  {e.id} [{e.nivel}] {e.cont}: {e.mesaj}")

if __name__ == "__main__":
    main()

