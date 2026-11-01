from PIL import Image

img = Image.open("probe/foto.jpg").convert("RGB")
canale = list(img.tobytes())
mesaj = b"FLAG{ascuns_in_pixeli}"
biti = "".join(f"{x:08b}" for x in mesaj + b"\x00")

for i, bit in enumerate(biti):
    canale[i] = (canale[i] & ~1) | int(bit)

Image.frombytes("RGB", img.size, bytes(canale)).save("stego.png")
print("salvat stego.png")


img = Image.open("stego.png").convert("RGB")
biti = "".join(str(c & 1) for c in img.tobytes())

octeti = bytearray()
for i in range(0, len(biti) - 7, 8):
    b = int(biti[i:i + 8], 2)
    if b == 0:
        break
    octeti.append(b)

print("mesaj:", octeti.decode())