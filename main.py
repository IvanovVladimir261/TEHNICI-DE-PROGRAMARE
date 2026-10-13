from checker import build_url, is_https, show_response, check_site, \
    scan_sites, check_headers, retry_check

#1
print("build_url fără slash:", build_url("example.com", "login"))
print("build_url cu slash:", build_url("example.com", "/login"))
print("is_https cu https:", is_https("https://example.com"))
print("is_https cu http:", is_https("http://example.com"))

#2
print("show_response example.com:")
show_response("https://example.com")
print("show_response httpbin.org/json:")
show_response("https://httpbin.org/json")

#3
print("check_site site care merge:",
      check_site("https://example.com"))
print("check_site site inexistent:",
      check_site("http://this-site-does-not-exist.invalid"))

#4
print("scan_sites:")
scan_sites()

#5
print("check_headers example.com:",
      check_headers("https://example.com"))
print("check_headers httpbin.org/html:",
      check_headers("https://httpbin.org/html"))

#6
print("retry_check 200:",
      retry_check("https://httpbin.org/status/200"))
print("retry_check 404:",
      retry_check("https://httpbin.org/status/404"))
print("retry_check 500:",
      retry_check("https://httpbin.org/status/500"))
print("retry_check 500, attempts=2:",
      retry_check("https://httpbin.org/status/500", attempts=2))
print("retry_check site inexistent:",
      retry_check("http://this-site-does-not-exist.invalid"))