#ex35.part4

# Laborator: funcții, metode și importuri pe web
# Student: Ivanov Vladimir

import urllib.parse

parsed_url = urllib.parse.urlparse("https://cybercor.org/path/to/resource?query=param#fragment")
print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.query)
print(parsed_url.fragment)

# Funcția urlparse împarte un URL în părți, iar atributele scheme, netloc, path, query și fragment dau protocolul, domeniul, calea, parametrii și ancora.