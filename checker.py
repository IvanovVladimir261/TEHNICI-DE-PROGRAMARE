from http import server
from tabnanny import check
import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login.""" 
    if not path.startswith('/'):
        path= path +'/'
    return f"https://{host}{path}"

def is_https(url):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    if url.startswith("https://"):
        print("True")
    else:
        print("False")
   


def show_response(url):
    """Trimite un GET la url și afișează statusul și Content-Type."""
    response=requests.get(url)
    print(f"Status: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException as e:
        return {"status": None, "error": str(e)}
    return {
        "status": response.status_code,
        "content_type": response.headers.get("Content-Type"),
        "length": len(response.content),
        "server": response.headers.get("Server", "unknown"),
    }



def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
    results=[]
    for url in SITES:
        response=check_site(url)
        if response["status"]==200:
            results.append(response)

    results.sort(key=lambda x: x["status"], reverse=True)
    for url,response in results:
        print(f"{url}: {response['status']}, {response['content_type']}, {response['length']}, {response['server']}")

    successful = 0
    failed = 0
    for url in SITES:
        response=check_site(url)
        if response["status"]==200:
            successful += 1
        else:
            failed += 1
    print(f"Reusite: {successful}, Esuate: {failed}")



def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
    response = requests.get(url, timeout=5)
    present = []
    missing = []
    for header in SECURITY_HEADERS:
        if header in response.headers:
            present.append(header)
        else:
            missing.append(header)

    score = len(present) * 100 // len(SECURITY_HEADERS)

    return {
        "present": present,
        "missing": missing,
        "score": score,
    }
    


def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
    status = None
    error = None
    made = 0
    for _ in range(attempts):
        made += 1
        try:
            response = requests.get(url, timeout=5)
        except requests.RequestException as e:
            error = str(e)
            continue

        status = response.status_code
        if status < 500:
            break

    result = {"status": status}
    if status is None:
        result["error"] = error
    result["attempts"] = made
    return result
    
