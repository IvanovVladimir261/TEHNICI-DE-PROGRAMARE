import code

import requests
import time

BASE = "https://httpbin.org"
PATHS = ["/get", "/redirect/2", "/delay/1", "/status/404", "/delay/5"]
TIMEOUT = 3


# Partea 1: parametri în URL
def search(params):
    r = requests.get(f"{BASE}/get", params=params, timeout=TIMEOUT)
    return r.json()["args"]


def search_url(params):
    r = requests.get(f"{BASE}/get", params=params, timeout=TIMEOUT)
    return r.url


# Partea 2: anteturi
def fetch_with_agent(agent):
    r = requests.get(BASE + "/headers", headers={"User-Agent": agent}, timeout=TIMEOUT)
    return r.json()["headers"]["User-Agent"]


def default_agent():
    r = requests.get(BASE + "/headers", timeout=TIMEOUT)
    return r.json()["headers"]["User-Agent"]


# Partea 3: trimiterea datelor
def post_json(data):
    """POST cu datele ca JSON pe /post; returnează JSON-ul primit de
    server."""
    r = requests.post(BASE + "/post", json=data, timeout=TIMEOUT)
    return r.json()["json"]


def post_form(data):
    """POST cu datele ca formular pe /post; returnează formularul primit de
    server."""
    r = requests.post(BASE + "/post", data=data, timeout=TIMEOUT)
    return r.json()["form"]


# Partea 4: coduri de stare
def describe_status(code):
    """GET pe /status/<code>; returnează 'succes', 'eroare client' sau
    'eroare server'."""
    r = requests.get(BASE + f"/status/{code}", timeout=TIMEOUT)
    try:
        r.raise_for_status()
        return "succes"
    except requests.HTTPError:
        if 400 <= code < 500:
            return "eroare client"
        if 500 <= code < 600:
            return "eroare server"
        return "eroare"


def is_ok(code):
    """GET pe /status/<code>; returnează True dacă cererea a reușit, altfel
    False."""
    try:
        r = requests.get(f"{BASE}/status/{code}", timeout=TIMEOUT)
        r.raise_for_status()
        return True
    except requests.RequestException:
        return False


# Partea 5: redirecționări
def count_redirects(n):
    """GET pe /redirect/<n>; returnează câte redirecționări au fost urmate."""
    r = requests.get(f"{BASE}/redirect/{n}", timeout=TIMEOUT)
    return len(r.history)


def final_url(n):
    """GET pe /redirect/<n>; returnează adresa la care ai ajuns."""
    r = requests.get(f"{BASE}/redirect/{n}", timeout=TIMEOUT)
    return r.url


def first_hop(n):
    """GET pe /redirect/<n> FĂRĂ a urma redirecționarea; returnează antetul Location."""
    r = requests.get(f"{BASE}/redirect/{n}", allow_redirects=False, timeout=TIMEOUT)
    return r.headers["Location"]

#Partea 6: cookie-uri
def cookie_demo(name, value):
    """Setează un cookie, apoi citește cookie-urile înapoi folosind O SINGURĂ
    sesiune."""
    s = requests.Session()
    s.get(f"{BASE}/cookies/set", params={name: value}, timeout=TIMEOUT)
    r = s.get(f"{BASE}/cookies", timeout=TIMEOUT)
    return r.json()["cookies"]
    pass

def no_session_demo(name, value):
    requests.get(f"{BASE}/cookies/set", params={name: value}, timeout=TIMEOUT)
    r = requests.get(f"{BASE}/cookies", timeout=TIMEOUT)
    return r.json()["cookies"]


# Partea 7: raportul final
def report(path):
    """Returnează un dicționar care descrie pagina de la BASE + path."""
    try:
        r = requests.get(BASE + path, timeout=TIMEOUT)
        content_type = r.headers.get("Content-Type", "")
        return {
            "status": r.status_code,
            "final_url": r.url,
            "redirects": len(r.history),
            "seconds": round(r.elapsed.total_seconds(), 2),
            "content_type": content_type.split(";")[0],
        }
    except requests.RequestException as e:
       return {"status": None, "error": type(e).__name__}
 
 
def main():
    results = []
    for path in PATHS:
        data = report(path)
        data["path"] = path
        results.append(data)
 
    ok = [d for d in results if d["status"] == 200]
    ok.sort(key=lambda d: d["seconds"], reverse=True)
 
    for d in ok:
        print(f"{d['path']} -> {d['status']}, {d['seconds']} secunde")
 
    failed = len(results) - len(ok)
    print(f"Reușite: {len(ok)} | Eșuate: {failed}")
 
 
# Bonus: autentificare
def check_login(user, password):
    """Returnează True dacă serverul acceptă datele de autentificare, altfel False."""
    try:
        r = requests.get(
            BASE + "/basic-auth/admin/secret",
            auth=(user, password),
            timeout=TIMEOUT,
        )
        return r.status_code == 200
    except requests.RequestException:
        return False


if __name__ == "__main__":
    main()


