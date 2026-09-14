# Podpowiedzi i rozwiązania: Bunkier na zombie apokalipsę 🧟

Nie zaglądaj tu, dopóki nie spróbowałeś sam. Dla każdego zadania: delikatna
podpowiedź → szczegółowa podpowiedź → typowe błędy → pełne rozwiązanie →
refaktoryzacja → czego miało nauczyć.

---

## Zadanie 1 — Parser sygnałów SOS

### 1. Delikatna podpowiedź
To ten sam mechanizm co `oceny.split(",")` z Twojego `Cwiczenie6.py`, tylko
z innym separatorem i większą liczbą pól.

### 2. Szczegółowa podpowiedź
`raw.split(";")` da listę 5 elementów w ustalonej kolejności — rozpakuj je od
razu do zmiennych albo zbuduj słownik ręcznie. Do walidacji liczby pól sprawdź
`len(...)` przed rozpakowaniem, albo złap `ValueError` przy samym rozpakowaniu
(za mało/za dużo wartości do rozpakowania rzuca dokładnie ten wyjątek).

### 3. Typowe błędy
- Rozpakowanie bez sprawdzenia liczby elementów → `ValueError` przy złym wejściu.
- Mieszanie logiki parsowania z `print()` w jednej funkcji.
- Traktowanie `liczba_osob` jako liczby bez konwersji — po `split()` wszystko
  jest stringiem, jeśli chcesz z tym liczyć, musisz jawnie zrobić `int(...)`.

### 4. Pełne rozwiązanie
```python
def parse_sygnal(raw: str) -> dict:
    pola = raw.split(";")
    if len(pola) != 5:
        raise ValueError(f"Zły format sygnału: {raw!r} (oczekiwano 5 pól, jest {len(pola)})")
    id_, lokalizacja, liczba_osob, zapasy, godzina = pola
    return {
        "id": id_,
        "lokalizacja": lokalizacja,
        "liczba_osob": liczba_osob,
        "zapasy": zapasy,
        "godzina": godzina,
    }


def print_sygnal(dane: dict) -> None:
    print("=" * 20)
    print(f"SYGNAŁ OD: {dane['id']}")
    print(f"Lokalizacja: {dane['lokalizacja']}")
    print(f"Osób: {dane['liczba_osob']}")
    print(f"Zapasy: {dane['zapasy']}")
    print(f"Godzina: {dane['godzina']}")
    print("=" * 20)


def main():
    surowe_sygnaly = [
        "S07;MAGAZYN-B;4;NISKI;03:12",
        "S12;RATUSZ;2;WYSOKI;22:47",
        "TO ZLY FORMAT",
    ]
    for raw in surowe_sygnaly:
        try:
            dane = parse_sygnal(raw)
            print_sygnal(dane)
        except ValueError as e:
            print(f"[BŁĄD] {e}")


if __name__ == "__main__":
    main()
```

**Omówienie:** `parse_sygnal` ma jedną odpowiedzialność (string → słownik) i rzuca
wyjątek przy złym wejściu; `print_sygnal` tylko wyświetla i nie wie nic o
formacie wejściowym. To ten sam podział, który już ćwiczyłeś przy locie — celowo,
żeby wzorzec się utrwalił niezależnie od tematu.

### 5. Refaktoryzacja / bardziej pythonowe podejście
- Przy stałym zestawie pól `dataclass` (poznasz przy OOP) byłaby czystsza niż
  goły `dict`.
- Rozpakowanie bezpośrednio do zmiennych (`id_, lokalizacja, ... = pola`) jest
  bardziej pythonowe niż budowanie słownika po indeksach.

### 6. Czego to miało nauczyć
To samo co w wersji lotniczej — parsowanie stringów o ustalonym formacie i
rozdzielanie logiki wg odpowiedzialności — ale rozwiązane w innym kontekście,
żeby sprawdzić, czy naprawdę rozumiesz wzorzec, a nie tylko pamiętasz konkretny
kod.

---

## Zadanie 2 — Licznik warczenia

### 1. Delikatna podpowiedź
Zliczanie wystąpień to zawsze: pusty słownik → pętla →
`słownik[klucz] = słownik.get(klucz, 0) + 1`.

### 2. Szczegółowa podpowiedź
Najdłuższa seria pod rząd = dwa liczniki: bieżąca długość serii i najdłuższa
znaleziona do tej pory. Przy każdym odczycie: jeśli kategoria to `"horda"`,
zwiększ bieżącą serię i zaktualizuj maksimum; w przeciwnym razie wyzeruj bieżącą
serię. To wzorzec "running max/current streak" — pamiętaj go, wraca na LeetCode.

### 3. Typowe błędy
- Brak resetu bieżącej serii przy kategorii innej niż `"horda"`.
- Twarde wpisanie czterech kategorii w kodzie licznika zamiast dynamicznego
  słownika.
- Dzielenie przez `len(odczyty)` bez pomyślenia o pustej liście (dobry nawyk,
  nawet jeśli zadanie zakłada niepustą).

### 4. Pełne rozwiązanie
```python
def klasyfikuj(poziom: int) -> str:
    if poziom <= 2:
        return "cisza"
    elif poziom <= 5:
        return "szmery"
    elif poziom <= 8:
        return "warczenie"
    else:
        return "horda"


def podsumuj(odczyty: list) -> dict:
    licznik = {}
    for poziom in odczyty:
        kategoria = klasyfikuj(poziom)
        licznik[kategoria] = licznik.get(kategoria, 0) + 1
    return licznik


def najdluzsza_seria_hordy(odczyty: list) -> int:
    najdluzsza = 0
    biezaca = 0
    for poziom in odczyty:
        if klasyfikuj(poziom) == "horda":
            biezaca += 1
            najdluzsza = max(najdluzsza, biezaca)
        else:
            biezaca = 0
    return najdluzsza


def main():
    odczyty = [1, 2, 4, 7, 9, 9, 9, 3, 0, 6, 8, 9]
    licznik = podsumuj(odczyty)
    total = len(odczyty)
    for kategoria, ile in licznik.items():
        procent = ile / total * 100
        print(f"{kategoria}: {ile} ({procent:.1f}%)")
    print(f'Najdłuższa seria "horda": {najdluzsza_seria_hordy(odczyty)} odczyty z rzędu')


if __name__ == "__main__":
    main()
```

### 5. Refaktoryzacja / bardziej pythonowe podejście
- `licznik.get(kategoria, 0) + 1` → `collections.Counter`:
  `Counter(klasyfikuj(p) for p in odczyty)`. Poznaj `Counter` teraz, używa się
  go bardzo często.
- `{procent:.1f}` we f-stringu zamiast ręcznego zaokrąglania.

### 6. Czego to miało nauczyć
Ten sam wzorzec zliczania i "running streak" co w wersji lotniczej — powtórka
w innym przebraniu, żeby sprawdzić transfer wiedzy między kontekstami.

---

## Zadanie 3 — Sprawdzarka kodów do drzwi bunkra

### 1. Delikatna podpowiedź
`c.isdigit()`, `c.isupper()`, `c.islower()` załatwiają sprawdzanie typu znaku
bez ręcznego porównywania z zakresami ASCII.

### 2. Szczegółowa podpowiedź
Każda funkcja `ma_*` iteruje po znakach i zwraca `True` przy pierwszym trafieniu
— to `any(c.isdigit() for c in kod)` zamiast pętli z flagą. Znaki specjalne:
zdefiniuj zbiór z góry (np. `"!@#$%^&*()-_=+"`) i sprawdź przynależność.
Punktacja: suma spełnionych kryteriów (0-4) plus bonus za długość, zmapowana na
etykietę.

### 3. Typowe błędy
- Sprawdzanie tylko pierwszego znaku zamiast wszystkich.
- Gołe `except:` bez podania typu wyjątku — złap konkretnie `TypeError`.
- Iterowanie po incie (`for c in 12345`) rzuca `TypeError` — to Twoja szansa na
  `try/except` w praktyce.

### 4. Pełne rozwiązanie
```python
ZNAKI_SPECJALNE = set("!@#$%^&*()-_=+[]{};:,.<>?")


def ma_cyfre(kod: str) -> bool:
    return any(c.isdigit() for c in kod)


def ma_wielka_litere(kod: str) -> bool:
    return any(c.isupper() for c in kod)


def ma_mala_litere(kod: str) -> bool:
    return any(c.islower() for c in kod)


def ma_znak_specjalny(kod: str) -> bool:
    return any(c in ZNAKI_SPECJALNE for c in kod)


def policz_punkty(kod: str) -> int:
    punkty = 0
    if len(kod) >= 8:
        punkty += 1
    if ma_cyfre(kod):
        punkty += 1
    if ma_wielka_litere(kod):
        punkty += 1
    if ma_mala_litere(kod):
        punkty += 1
    if ma_znak_specjalny(kod):
        punkty += 1
    return punkty


def ocen_kod(kod: str) -> str:
    punkty = policz_punkty(kod)
    if punkty <= 1:
        return "do wyrzucenia"
    elif punkty == 2:
        return "słaby"
    elif punkty == 3:
        return "średni"
    elif punkty == 4:
        return "mocny"
    else:
        return "twierdza"


def main():
    kody = ["1234", "Bunkier123", "Zx9!kLm2@Qw", 12345, "aaaa"]
    for kod in kody:
        try:
            ocena = ocen_kod(kod)
            print(f'"{kod}" -> {ocena}')
        except TypeError:
            print(f"[BŁĄD] Element {kod!r} nie jest tekstem - pominięto")


if __name__ == "__main__":
    main()
```

### 5. Refaktoryzacja / bardziej pythonowe podejście
- `isinstance(kod, str)` na wejściu to alternatywa "zapytaj najpierw" wobec
  `try/except` ("spróbuj i obsłuż" — EAFP, bardziej pythonowe, użyte tutaj).
- Warto docelowo poznać wzorzec "lista funkcji jako wartości" do zsumowania
  kryteriów w pętli, ale na teraz jawne funkcje są czytelniejsze.

### 6. Czego to miało nauczyć
Dokładnie to samo co Zadanie 3 z wersji lotniczej: dzielenie warunku na małe
nazwane funkcje pomocnicze, `try/except` na realnym błędzie typu, wzorzec
"zbieraj punkty → zmapuj na etykietę".

---

## Zadanie 4 — Siatka koi w bunkrze

### 1. Delikatna podpowiedź
Lista list to tabela: `mapa[i]` to całe pomieszczenie `i`, `mapa[i][j]` to
konkretna koja. List comprehension (już użyta w `Cwiczenie6.py`) świetnie się
nada do zbudowania takiej struktury na starcie.

### 2. Szczegółowa podpowiedź
Litery A-D zamień na indeks przez `"ABCD".index(litera)`. Numer pomieszczenia
od użytkownika (od 1) zamień na indeks listy przez `pomieszczenie - 1`. Zanim
cokolwiek zrobisz z `mapa[idx][idx2]`, sprawdź granice — inaczej dostaniesz
`IndexError` zamiast eleganckiego `False`.

### 3. Typowe błędy
- Błąd "off-by-one" — mylenie pomieszczenia 1 z indeksem 0.
- Tworzenie siatki przez `[["wolna"] * 4] * 8` zamiast list comprehension — to
  tworzy 8 referencji do tej samej wewnętrznej listy, więc przydział jednej koi
  "zajmuje" tę samą kolumnę we wszystkich pomieszczeniach naraz.
- Brak sprawdzenia zakresu przed indeksowaniem.

### 4. Pełne rozwiązanie
```python
import random

LITERY = "ABCD"


def stworz_mape(liczba_pomieszczen: int = 8) -> list:
    return [["wolna" for _ in LITERY] for _ in range(liczba_pomieszczen)]


def przydziel(mapa: list, pomieszczenie: int, koja: str, osoba: str) -> bool:
    idx_pom = pomieszczenie - 1
    if koja not in LITERY:
        return False
    idx_koja = LITERY.index(koja)
    if not (0 <= idx_pom < len(mapa)):
        return False
    if mapa[idx_pom][idx_koja] != "wolna":
        return False
    mapa[idx_pom][idx_koja] = osoba
    return True


def wypisz_mape(mapa: list) -> None:
    for i, pomieszczenie in enumerate(mapa, start=1):
        opis = " | ".join(
            f"{litera}:{'---' if k == 'wolna' else k}" for litera, k in zip(LITERY, pomieszczenie)
        )
        print(f"Pomieszczenie {i:2}: {opis}")


def znajdz_wolne(mapa: list) -> list:
    wolne = []
    for i, pomieszczenie in enumerate(mapa, start=1):
        for litera, k in zip(LITERY, pomieszczenie):
            if k == "wolna":
                wolne.append((i, litera))
    return wolne


def losuj_zajetosc(mapa: list, procent: float) -> None:
    wszystkie = [(i + 1, litera) for i in range(len(mapa)) for litera in LITERY]
    ile_zajac = int(len(wszystkie) * procent / 100)
    do_zajecia = random.sample(wszystkie, ile_zajac)
    for pomieszczenie, litera in do_zajecia:
        przydziel(mapa, pomieszczenie, litera, "zajęte (grupa startowa)")


def main():
    mapa = stworz_mape()
    losuj_zajetosc(mapa, 30)

    ok1 = przydziel(mapa, 3, "B", "Rick")
    ok2 = przydziel(mapa, 3, "B", "Michonne")
    print(f"Przydział 3B dla Rick: {'OK' if ok1 else 'ODRZUCONY (koja zajęta)'}")
    print(f"Przydział 3B dla Michonne: {'OK' if ok2 else 'ODRZUCONY (koja zajęta)'}")

    ok3 = przydziel(mapa, 99, "A", "Ktoś")
    print(f"Przydział 99A: {'OK' if ok3 else 'ODRZUCONY (nieprawidłowe pomieszczenie)'}")

    wypisz_mape(mapa)
    print(f"Wolnych koi: {len(znajdz_wolne(mapa))}")


if __name__ == "__main__":
    main()
```

### 5. Refaktoryzacja / bardziej pythonowe podejście
- `zip(LITERY, pomieszczenie)` zamiast `range(len(...))` + indeksowanie.
- `enumerate(mapa, start=1)` zamiast ręcznego liczenia indeksu.

### 6. Czego to miało nauczyć
To samo co Zadanie 4 z wersji lotniczej: struktury 2D, pułapka aliasingu przy
`* n`, zamiana współrzędnych "ludzkich" na indeksy Pythona, defensywne
sprawdzanie granic przed indeksowaniem.

---

## Zadanie 5 — Tracker racjonowania zapasów

### 1. Delikatna podpowiedź
To Twój kalkulator ocen z `Cwiczenie6.py`, dokończony zgodnie z własnym TODO:
prawdziwa pętla `while`, `try/except` przy inpucie, podział na funkcje. Zacznij
od szkieletu pętli menu.

### 2. Szczegółowa podpowiedź
```python
while True:
    wybor = input("Wybierz opcję: ")
    if wybor == "1":
        zapisz_zuzycie(historia)
    elif wybor == "5":
        break
```
Walidacja ilości: `float(input(...))` w `try`, w `except ValueError` poproś
ponownie — najprościej pętlą `while True` wewnątrz funkcji pobierającej ilość,
która robi `return` dopiero przy poprawnych danych. Podsumowanie wg kategorii to
ten sam wzorzec co Zadanie 2, tylko sumujesz ilości. Sortowanie malejące:
`sorted(..., key=..., reverse=True)`.

### 3. Typowe błędy
- Cała logika wciśnięta w `while True` w `main()` zamiast rozbita na funkcje.
- Brak pętli ponawiającej przy błędnym inpucie.
- Ilość ujemna albo `0` przechodzi walidację, bo sprawdzasz tylko typ, nie znak.
- Brak trzymania bieżącej sumy zużycia — liczenie budżetu od nowa za każdym
  razem zamiast raz na wywołanie.

### 4. Pełne rozwiązanie
```python
def pobierz_ilosc() -> float:
    while True:
        surowa = input("Ilość: ")
        try:
            ilosc = float(surowa)
            if ilosc <= 0:
                print("Ilość musi być dodatnia, spróbuj ponownie.")
                continue
            return ilosc
        except ValueError:
            print("To nie jest liczba, spróbuj ponownie.")


def zapisz_zuzycie(historia: list) -> None:
    kategoria = input("Kategoria: ").strip().lower()
    ilosc = pobierz_ilosc()
    opis = input("Opis: ").strip()
    historia.append({"kategoria": kategoria, "ilosc": ilosc, "opis": opis})
    print("Zapisano zużycie.")


def pokaz_historie(historia: list) -> None:
    if not historia:
        print("Brak zapisów.")
        return
    for w in historia:
        print(f"{w['kategoria']}: {w['ilosc']:.2f} jedn. - {w['opis']}")


def podsumowanie_wg_kategorii(historia: list) -> dict:
    sumy = {}
    for w in historia:
        sumy[w["kategoria"]] = sumy.get(w["kategoria"], 0) + w["ilosc"]
    return sumy


def pokaz_podsumowanie(historia: list) -> None:
    sumy = podsumowanie_wg_kategorii(historia)
    if not sumy:
        print("Brak danych do podsumowania.")
        return
    for kategoria, suma in sorted(sumy.items(), key=lambda item: item[1], reverse=True):
        print(f"{kategoria}: {suma:.2f} jedn.")


def sprawdz_zapasy(historia: list, magazyn: float) -> None:
    suma = sum(w["ilosc"] for w in historia)
    if suma > magazyn:
        print(f"UWAGA: zapasy wyczerpane! Zużyto {suma:.2f} z {magazyn:.2f} jedn.")
    elif suma > magazyn * 0.8:
        print(f"Uwaga: wykorzystano {suma / magazyn * 100:.1f}% zapasów.")
    else:
        print(f"W normie: {suma:.2f} / {magazyn:.2f} jedn.")


def pobierz_stan_magazynu() -> float:
    print("Podaj całkowity stan magazynu:")
    return pobierz_ilosc()


def main():
    historia = []
    magazyn = pobierz_stan_magazynu()

    while True:
        print("\n[Menu] 1) zapisz zużycie  2) historia  3) podsumowanie  4) sprawdź zapasy  5) wyjście")
        wybor = input("> ").strip()
        if wybor == "1":
            zapisz_zuzycie(historia)
        elif wybor == "2":
            pokaz_historie(historia)
        elif wybor == "3":
            pokaz_podsumowanie(historia)
        elif wybor == "4":
            sprawdz_zapasy(historia, magazyn)
        elif wybor == "5":
            print("Trzymaj się, kwatermistrzu.")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()
```

**Omówienie:** `pobierz_ilosc()` hermetyzuje walidację raz i jest użyta dwa razy
(stan magazynu i pojedyncze zużycie) — bez duplikacji, dokładnie to, co miałeś
poprawić w `Cwiczenie6.py`. `main()` jest tylko dyspozytorem menu, cała logika
biznesowa żyje w osobnych, nazwanych funkcjach.

### 5. Refaktoryzacja / bardziej pythonowe podejście
- `podsumowanie_wg_kategorii` można zapisać przez `collections.defaultdict(float)`
  zamiast `.get(kategoria, 0)` — naturalny następny krok po poznaniu `Counter`.
- `sum(w["ilosc"] for w in historia)` to generator expression zamiast pętli
  z ręcznym akumulatorem.
- Przy bonusie z plikiem: moduł `json` (`json.dump`/`json.load`) zamiast
  ręcznego formatu tekstowego — jedna linijka zamiast ręcznego parsowania.

### 6. Czego to miało nauczyć
To samo spięcie wszystkiego naraz co w wersji lotniczej — pętla `while True`
jako menu, podział na małe funkcje, walidacja z `try/except` w pętli ponawiającej,
struktura "lista słowników". Jeśli to zadanie poszło Ci wyraźnie szybciej niż
wersja z lotniska, to dobry sygnał, że wzorzec faktycznie wszedł Ci do głowy, a
nie tylko zapamiętałeś konkretny kod.
