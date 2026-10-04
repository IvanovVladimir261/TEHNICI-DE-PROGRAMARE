import csv
import json
import re
import socket
import ssl
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse

import requests

TIMEOUT = 10
DEFAULT_HEADERS = {"User-Agent": "WebLab-NumeleVostru"}

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]


def fetch(url: str):
    return requests.get(url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)


def get_status(url: str) -> int:
    return fetch(url).status_code


def get_title(html: str) -> str | None:
    start = html.find("<title>")
    if start == -1:
        return None
    start += len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()


def security_headers(url: str) -> dict[str, bool]:
    response = fetch(url)
    return {name: name in response.headers for name in SECURITY_HEADERS}


def score_headers(results: dict[str, bool]) -> str:
    return f"{sum(results.values())}/{len(results)}"


def extract_links(html: str) -> list[str]:
    links = re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(links))


def split_links(links: list[str], domain: str) -> tuple[list[str], list[str]]:
    site = urlparse(domain).netloc
    internal, external = [], []
    for link in links:
        full = urljoin(domain, link)
        if urlparse(full).netloc == site:
            internal.append(full)
        else:
            external.append(full)
    return internal, external


def fetch_robots(base: str) -> str | None:
    response = fetch(urljoin(base, "/robots.txt"))
    return response.text if response.status_code == 200 else None


def disallowed_paths(robots_text: str | None) -> list[str]:
    if robots_text is None:
        return []
    paths = []
    for line in robots_text.splitlines():
        line = line.strip()
        if line.lower().startswith("disallow:"):
            value = line[len("disallow:"):].strip()
            if value:
                paths.append(value)
    return paths


def resolve(hostname: str) -> str:
    return socket.gethostbyname(hostname)


def cert_days_left(hostname: str) -> int:
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure:
            cert = secure.getpeercert()
    expires = ssl.cert_time_to_seconds(cert["notAfter"])
    return int((expires - time.time()) // 86400)


def check_paths(base: str, paths: list[str]) -> list[dict]:
    rows = []
    for path in paths:
        rows.append({
            "path": path,
            "status": get_status(urljoin(base, path)),
            "checked_at": datetime.now().isoformat(),
        })
        time.sleep(1)
    return rows


def save_csv(rows: list[dict], filename: str = "report.csv") -> None:
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["path", "status", "checked_at"])
        writer.writeheader()
        writer.writerows(rows)


def redirect_chain(url: str) -> list[str]:
    http_url = "http://" + urlparse(url).netloc
    response = requests.get(http_url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    steps = [f"{r.url} ({r.status_code})" for r in response.history]
    steps.append(f"{response.url} ({response.status_code})")
    return steps


def site_report(url: str) -> dict:
    host = urlparse(url).netloc
    response = fetch(url)
    html = response.text
    internal, external = split_links(extract_links(html), url)

    report = {
        "url": url,
        "status": response.status_code,
        "final_url": response.url,
        "title": get_title(html),
        "ip": resolve(host),
        "redirects": redirect_chain(url),
        "security_score": score_headers(security_headers(url)),
        "cert_days_left": cert_days_left(host),
        "links_internal": len(internal),
        "links_external": len(external),
        "disallowed": disallowed_paths(fetch_robots(url)),
    }

    print(f"=== Raport site: {url} ===")
    print(f"Cod de stare:    {report['status']} (URL final: {report['final_url']})")
    print(f"Titlu:           {report['title']}")
    print(f"Adresă IP:       {report['ip']}")
    print(f"Redirecționări:  {' -> '.join(report['redirects'])}")
    print(f"Scor securitate: {report['security_score']}")
    print(f"Certificat:      {report['cert_days_left']} de zile rămase")
    print(f"Legături:        {report['links_internal']} interne, {report['links_external']} externe")
    print(f"Căi interzise:   {', '.join(report['disallowed']) or 'niciuna'}")

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)
    print("Salvat în report.json")
    return report


if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))

    # La python webtools.py variabila __name__ este "__main__", deci autotestul rulează; la python main.py modulul este doar importat, __name__ este "webtools", iar autotestul nu rulează.
# DEFAULT_HEADERS este o constantă de modul, folosită în fetch() pentru ca toate cererile să trimită același User-Agent, și poate fi importată în main.py.

