import re
from PIL import Image
from PIL.ExifTags import TAGS
import zipfile
def tip_real(cale):
    cap = open(cale, "rb").read(8)
    if cap.startswith(b"%PDF"):
        return "pdf"
    if cap.startswith(b"\x89PNG"):
        return "png"
    if cap.startswith(b"\xff\xd8"):
        return "jpeg"
    if cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    return cap.hex()

print(tip_real("probe/foto.jpg"))
print(tip_real("probe/ascuns.png"))


date = open("probe/ascuns.png", "rb").read()
for m in re.findall(rb"[ -~]{4,}", date):
    print(m.decode())


exif = Image.open("probe/foto.jpg").getexif()
for id, val in exif.items():
    print(TAGS.get(id, id), "=", val)

gps = exif.get_ifd(34853)

def zecimale(dms, ref):
    g, m, s = (float(x) for x in dms)
    v = g + m / 60 + s / 3600
    return -v if ref in ("S", "W") else v

print("lat:", zecimale(gps[2], gps[1]))
print("lon:", zecimale(gps[4], gps[3]))


date = open("probe/ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")
if i != -1:
    open("probe/gasit.zip", "wb").write(date[i:])
    print("arhiva extrasa de la octetul", i)
    with zipfile.ZipFile("probe/gasit.zip") as z:
        for nume in z.namelist():
            print(nume, z.read(nume))