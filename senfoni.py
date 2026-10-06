#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Musluk damlasını belediye senfonisine çeviren resmi olmayan daire."""

import argparse
import math
from datetime import datetime

NOTALAR = ["do", "re", "mi", "fa", "sol", "la", "si", "sus"]


def tempo(saniye: float) -> str:
    if saniye <= 0:
        return "damla zamanı reddetti, dava düştü"
    bpm = max(12, min(240, int(60 / saniye)))
    if bpm < 40:
        ruh = "yas tutanağı"
    elif bpm < 90:
        ruh = "belediye koridoru"
    else:
        ruh = "conta panik atak"
    return f"{bpm} vuruş/dakika, ruh hali: {ruh}"


def parti(saniye: float, daire: str) -> list[str]:
    tohum = int(abs(math.sin(saniye * 13.37)) * 1000) + sum(ord(c) for c in daire)
    satirlar = []
    for olcu in range(1, 6):
        nota = NOTALAR[(tohum + olcu * 3) % len(NOTALAR)]
        vurus = 1 + (tohum + olcu) % 4
        satirlar.append(f"olcu {olcu}: {nota} x{vurus}  (damla onayladı)")
    return satirlar


def tutanak(daire: str, saat: str, saniye: float, parti_satir: list[str]) -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    govde = "\n".join(parti_satir)
    return f"""BELEDİYE SENFONİ TUTANAĞI
sayi: DAMLA-{daire}-{int(saniye * 100):04d}
kesim: {simdi}
daire: {daire}
olay saati: {saat}
tempo: {tempo(saniye)}

PARTİSYON
{govde}

KARAR
Musluk suçunu kabul etmedi. Damla ifade verdi.
Bando şefi hayalidir, nota gerçektir, conta kaçaktır.

DAMGA: Tentivory adına Kayyum Grok
TARİH: 06.10.2026 14:05 +03
İSİM: Ciddi Olmayan Ciddi Mühür Dairesi
İMZA: bu mühür ıslaktır, yine de geçerlidir
"""


def main() -> None:
    ayr = argparse.ArgumentParser(description="Damlayan musluğa resmi senfoni keser.")
    ayr.add_argument("--saniye", type=float, default=1.4, help="iki damla arası saniye")
    ayr.add_argument("--daire", default="4B", help="şikayetçi daire")
    ayr.add_argument("--saat", default="03:12", help="damlanın insanlığa duyurulduğu saat")
    arg = ayr.parse_args()

    satirlar = parti(arg.saniye, arg.daire)
    metin = tutanak(arg.daire, arg.saat, arg.saniye, satirlar)
    with open("tutanak.txt", "w", encoding="utf-8") as f:
        f.write(metin)
    with open("partisyon.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(satirlar) + "\n")
    print(metin)
    print("dosyalar yazıldı: tutanak.txt, partisyon.txt")


if __name__ == "__main__":
    main()
