#    Parser numerow lotow lotnicych
print(" Witaj w moim programie który parsuje numery lotów lotniczych tak, aby były czytelne! ")

#   Variables / shortcuts
WAW = "Warszawa".upper
KRK = "Kraków".upper
MNC = "Monachium".upper
FRA = "Frankfurt".upper
DUB = "Dublin".upper

#   Parser


def parser_boarding_pass(raw: str) -> dict:
    pola = raw.split(";")
    if len(pola) != 5:
        raise ValueError(
            f"Zły format biletu: {raw!r} (oczekiwano 5 pól, podanych zostało tylko {len(pola)})")
    lot, wylot, przylot, godzina, miejsce = pola
    return {
        "lot": lot,
        "wylot": wylot,
        "przylot": przylot,
        "godzina": godzina,
        "miejsce": miejsce,
    }


#   Reader lotów


def reader_boarding_pass(dane: dict) -> None:
    print("-" * 20)
    print(f"LOT: {dane['lot']}")
    print(f"wylot: {dane['wylot']}")
    print(f"przylot: {dane['przylot']}")
    print(f"godzina: {dane['godzina']}")
    print(f"miejsce: {dane['miejsce']}")
    print("-" * 20)

#   Bilety / Błędy


def main():
    tickets = [
        f"LO123;{WAW};JFK;14:35;22A",
        "LH456;FRA;{WAW};09:10;7C",
        "TO ZLY FORMAT",
    ]
    for raw in tickets:
        try:
            dane = parser_boarding_pass(raw)
            reader_boarding_pass(dane)
        except ValueError as e:
            print(f"[BŁĄD] {e}")


if __name__ == "__main__":
    main()
