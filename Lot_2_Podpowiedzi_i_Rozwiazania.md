# Podpowiedzi i rozwiązania ✈️

Nie zaglądaj tu, dopóki nie spróbowałeś sam (albo utknąłeś na dobre). Dla każdego
zadania: delikatna podpowiedź → szczegółowa podpowiedź → typowe błędy →
pełne rozwiązanie → refaktoryzacja → czego miało nauczyć.

---

## Zadanie 1 — Boarding Pass Parser

### 1. Delikatna podpowiedź
Masz już w `Cwiczenie6.py` linijkę `oceny.split(",")`. To dokładnie ten sam
mechanizm, tylko z innym separatorem i większą liczbą pól.

### 2. Szczegółowa podpowiedź
`raw.split(";")` da Ci listę 5 elementów w ustalonej kolejności — możesz je
rozpakować od razu do zmiennych (`lot, wylot, przylot, godzina, miejsce = raw.split(";")`)
albo złożyć ręcznie w słownik. Do walidacji liczby pól: sprawdź `len(...)` przed
rozpakowaniem albo złap `ValueError` przy rozpakowaniu (za mało/za dużo wartości
do rozpakowania rzuca dokładnie ten wyjątek).

### 3. Typowe błędy
- Rozpakowanie do zmiennych bez sprawdzenia liczby elementów → `ValueError` przy
  złym wejściu (to akurat możesz świadomie złapać, patrz bonus).
- Mieszanie logiki parsowania z `print()` w jednej funkcji (zadanie wymaga dwóch
  osobnych funkcji — to nie przypadek, to trening na Zadanie 5 i Twój własny TODO
  z `Cwiczenie6.py` pkt 7).
- Zapominanie, że `split()` zwraca stringi — jeśli chcesz gdzieś użyć godziny jako
  danych do porównań, zostanie tekstem, nie obiektem czasu (tu to nie problem, ale
  warto to zauważyć).

### 4. Pełne rozwiązanie
```python
def parse_boarding_pass(raw: str) -> dict:
    pola = raw.split(";")
    if len(pola) != 5:
        raise ValueError(f"Zły format biletu: {raw!r} (oczekiwano 5 pól, jest {len(pola)})")
    lot, wylot, przylot, godzina, miejsce = pola
    return {
        "lot": lot,
        "wylot": wylot,
        "przylot": przylot,
        "godzina": godzina,
        "miejsce": miejsce,
    }


def print_boarding_pass(dane: dict) -> None:
    print("=" * 20)
    print(f"LOT: {dane['lot']}")
    print(f"Z: {dane['wylot']} -> DO: {dane['przylot']}")
    print(f"Godzina: {dane['godzina']}")
    print(f"Miejsce: {dane['miejsce']}")
    print("=" * 20)


def main():
    surowe_bilety = [
        "LO123;WAW;JFK;14:35;22A",
        "LH456;FRA;WAW;09:10;7C",
        "TO ZLY FORMAT",
    ]
    for raw in surowe_bilety:
        try:
            dane = parse_boarding_pass(raw)
            print_boarding_pass(dane)
        except ValueError as e:
            print(f"[BŁĄD] {e}")


if __name__ == "__main__":
    main()
```

**Omówienie:** `parse_boarding_pass` ma jedną odpowiedzialność — zamienić string
na słownik, i rzuca wyjątek, jeśli wejście jest złej postaci. `print_boarding_pass`
tylko wyświetla — nie wie nic o formacie wejściowym. Rozdzielenie tych dwóch rzeczy
to właśnie **separation of concerns**: łatwiej testować, łatwiej podmienić sposób
wyświetlania bez ruszania logiki parsowania.

### 5. Refaktoryzacja / bardziej pythonowe podejście
- Zamiast zwykłego `dict`, dla stałego zestawu pól świetnie pasuje
  `dataclass` (`from dataclasses import dataclass`) — dostajesz autouzupełnianie
  i czytelniejszy dostęp (`dane.lot` zamiast `dane["lot"]`). To poznasz przy OOP
  w tygodniu 5-6 roadmapy, na razie zapamiętaj że to istnieje.
- `raw.split(";")` z bezpośrednim rozpakowaniem (`lot, wylot, przylot, godzina, miejsce = pola`)
  jest bardziej "pythonowe" niż budowanie słownika ręcznie po indeksach.
- Format ramki z `"=" * 20` jest bardziej DRY niż wpisywanie `"===================="` ręcznie.

### 6. Czego to miało nauczyć
Parsowania stringów o ustalonym formacie (bardzo częsty temat na LeetCode i w
prawdziwych parserach logów — pamiętaj, że to jeden z Twoich celów 3-miesięcznych),
rozdzielania funkcji wg odpowiedzialności oraz pierwszego świadomego użycia
`raise`/`except ValueError` zamiast pozwalania programowi się wywalić.

---

## Zadanie 2 — Turbulence Counter

### 1. Delikatna podpowiedź
"Zliczanie ile razy coś wystąpiło" to zawsze schemat: pusty słownik →
pętla → `słownik[klucz] = słownik.get(klucz, 0) + 1`.

### 2. Szczegółowa podpowiedź
Do najdłuższej serii pod rząd potrzebujesz dwóch liczników: bieżącej długości serii
i najdłuższej znalezionej do tej pory. Przy każdym elemencie: jeśli kategoria to
`"niebezpiecznie"`, zwiększ bieżącą serię i zaktualizuj maksimum jeśli trzeba; jeśli
nie — wyzeruj bieżącą serię do 0. To klasyczny wzorzec "running max", warto go
zapamiętać, bo wraca na LeetCode (np. "longest consecutive...").

### 3. Typowe błędy
- Zapominanie zresetować licznik bieżącej serii, gdy trafisz kategorię inną niż
  `"niebezpiecznie"` — wtedy serie "sklejają się" nieprawidłowo.
- Dzielenie przez `len(odczyty)` bez sprawdzenia, czy lista nie jest pusta (choć
  zadanie zakłada niepustą listę, dobry nawyk to i tak sprawdzać).
- Twarde wpisanie czterech kategorii w kodzie licznika zamiast pozwolić słownikowi
  rosnąć dynamicznie — zadanie specjalnie tego zabrania, żeby wymusić użycie `.get()`.

### 4. Pełne rozwiązanie
```python
def klasyfikuj(poziom: int) -> str:
    if poziom <= 2:
        return "spokojnie"
    elif poziom <= 5:
        return "lekko"
    elif poziom <= 8:
        return "mocno"
    else:
        return "niebezpiecznie"


def podsumuj(odczyty: list) -> dict:
    licznik = {}
    for poziom in odczyty:
        kategoria = klasyfikuj(poziom)
        licznik[kategoria] = licznik.get(kategoria, 0) + 1
    return licznik


def najdluzsza_seria_niebezpieczna(odczyty: list) -> int:
    najdluzsza = 0
    biezaca = 0
    for poziom in odczyty:
        if klasyfikuj(poziom) == "niebezpiecznie":
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
    print(f'Najdłuższa seria "niebezpiecznie": {najdluzsza_seria_niebezpieczna(odczyty)} odczyty z rzędu')


if __name__ == "__main__":
    main()
```

### 5. Refaktoryzacja / bardziej pythonowe podejście
- `licznik.get(kategoria, 0) + 1` możesz zastąpić `collections.Counter`:
  `from collections import Counter; licznik = Counter(klasyfikuj(p) for p in odczyty)`.
  To jest dokładnie to narzędzie do tego zadania — warto poznać `Counter` teraz,
  bo używa się go bardzo często.
- Formatowanie procentu `{procent:.1f}` zamiast ręcznego zaokrąglania to dobry
  nawyk f-stringowy, którego już zaczynasz używać.

### 6. Czego to miało nauczyć
Wzorca "zliczanie w słowniku" (jeden z najczęstszych wzorców w całym programowaniu),
techniki "running max/current streak" do serii pod rząd, oraz pracy z procentami
i formatowaniem liczb we f-stringach.

---

## Zadanie 3 — Password Strength Checker

### 1. Delikatna podpowiedź
Python ma gotowe metody stringów do sprawdzania typu znaku: `c.isdigit()`,
`c.isupper()`, `c.islower()`. Nie musisz porównywać ręcznie z zakresami ASCII.

### 2. Szczegółowa podpowiedź
Każda funkcja pomocnicza (`ma_cyfre`, `ma_wielka_litere` itd.) może iterować po
znakach hasła i zwracać `True` przy pierwszym trafieniu — to dokładnie sytuacja na
`any()`: `any(c.isdigit() for c in haslo)` zamiast pętli z flagą. Do znaków
specjalnych zdefiniuj sobie z góry zbiór znaków (np. `"!@#$%^&*()-_=+"`) i sprawdź
przynależność. Punktację zbuduj jako sumę spełnionych kryteriów (0-4) plus bonus za
długość, i zmapuj sumę na etykiety.

### 3. Typowe błędy
- Sprawdzanie tylko pierwszego znaku hasła zamiast wszystkich.
- `except:` bez podania typu wyjątku (złap konkretnie `TypeError`/`AttributeError`,
  bo złapanie wszystkiego ukrywa prawdziwe błędy w Twoim kodzie).
- Zapomnienie, że iterowanie po incie (np. `for c in 12345`) samo w sobie rzuci
  `TypeError` — to jest właśnie Twoja szansa na `try/except` w praktyce, tak jak
  planowałeś w TODO z `Cwiczenie6.py`.
- Za sztywna punktacja (np. tylko `if/elif` bez żadnej logiki sumującej) — trudno
  to potem rozszerzyć.

### 4. Pełne rozwiązanie
```python
ZNAKI_SPECJALNE = set("!@#$%^&*()-_=+[]{};:,.<>?")


def ma_cyfre(haslo: str) -> bool:
    return any(c.isdigit() for c in haslo)


def ma_wielka_litere(haslo: str) -> bool:
    return any(c.isupper() for c in haslo)


def ma_mala_litere(haslo: str) -> bool:
    return any(c.islower() for c in haslo)


def ma_znak_specjalny(haslo: str) -> bool:
    return any(c in ZNAKI_SPECJALNE for c in haslo)


def policz_punkty(haslo: str) -> int:
    punkty = 0
    if len(haslo) >= 8:
        punkty += 1
    if ma_cyfre(haslo):
        punkty += 1
    if ma_wielka_litere(haslo):
        punkty += 1
    if ma_mala_litere(haslo):
        punkty += 1
    if ma_znak_specjalny(haslo):
        punkty += 1
    return punkty


def ocen_haslo(haslo: str) -> str:
    punkty = policz_punkty(haslo)
    if punkty <= 1:
        return "za słabe"
    elif punkty == 2:
        return "słabe"
    elif punkty == 3:
        return "średnie"
    elif punkty == 4:
        return "silne"
    else:
        return "bardzo silne"


def main():
    haslo_lista = ["1234", "Kotek123", "Zx9!kLm2@Qw", 12345, "aaaa"]
    for haslo in haslo_lista:
        try:
            ocena = ocen_haslo(haslo)
            print(f'"{haslo}" -> {ocena}')
        except TypeError:
            print(f"[BŁĄD] Element {haslo!r} nie jest tekstem - pominięto")


if __name__ == "__main__":
    main()
```

### 5. Refaktoryzacja / bardziej pythonowe podejście
- Zamiast czterech osobnych funkcji `ma_*`, można zbudować listę par
  `(warunek, funkcja)` i sumować przez `sum(f(haslo) for f in [ma_cyfre, ...])` —
  ale na Twoim etapie jawne funkcje są czytelniejsze niż lista funkcji jako
  wartości, to zostaw sobie na później.
- `isinstance(haslo, str)` na wejściu funkcji `ocen_haslo` to alternatywa dla
  `try/except` — warto znać oba podejścia: "zapytaj najpierw" (`isinstance`) vs
  "spróbuj i obsłuż błąd" (`try/except`, tzw. EAFP — bardziej pythonowe i to,
  czego użyliśmy tutaj).

### 6. Czego to miało nauczyć
Dzielenia jednego złożonego warunku na małe, nazwane funkcje pomocnicze (dokładnie
punkt 7 z Twojego własnego TODO w `Cwiczenie6.py`), pracy z `try/except` na
realnym przykładzie błędu typu, oraz wzorca "zbieraj punkty → zmapuj na etykietę"
(bardzo przydatny wzorzec ogólny, nie tylko do haseł).

---

## Zadanie 4 — Airplane Seat Map Booking Simulator

### 1. Delikatna podpowiedź
"Lista list" to po prostu tabela: `mapa[i]` to cały rząd `i`, a `mapa[i][j]` to
konkretne miejsce. Do stworzenia takiej struktury na starcie przyda się
list comprehension — coś, czego już użyłeś w `Cwiczenie6.py` (`[int(ocena) for ocena in ...]`).

### 2. Szczegółowa podpowiedź
Litery A-F możesz zamienić na indeks przez `"ABCDEF".index(litera)`. Rząd
użytkownika (od 1) zamień na indeks listy przez `rzad - 1`. Zanim cokolwiek
zrobisz z `mapa[rzad-1][indeks_miejsca]`, sprawdź czy `rzad-1` i `indeks_miejsca`
mieszczą się w granicach (`0 <= rzad-1 < len(mapa)`) — inaczej dostaniesz
`IndexError` zamiast eleganckiego `False`.

### 3. Typowe błędy
- Klasyczny błąd "off-by-one" — mylenie rzędu 1 z indeksem 0.
- Tworzenie siatki przez `[["wolne"] * 6] * 10` zamiast list comprehension —
  to tworzy 10 referencji do tej samej wewnętrznej listy, więc rezerwacja
  jednego miejsca "zajmie" to samo miejsce we wszystkich rzędach naraz. To
  bardzo pouczająca pułapka, warto ją samemu złapać.
- Brak sprawdzenia zakresu przed indeksowaniem → `IndexError` zamiast
  kontrolowanego `False`/komunikatu.

### 4. Pełne rozwiązanie
```python
import random

LITERY = "ABCDEF"


def stworz_mape(liczba_rzedow: int = 10) -> list:
    return [["wolne" for _ in LITERY] for _ in range(liczba_rzedow)]


def rezerwuj(mapa: list, rzad: int, miejsce: str, pasazer: str) -> bool:
    idx_rzad = rzad - 1
    if miejsce not in LITERY:
        return False
    idx_miejsce = LITERY.index(miejsce)
    if not (0 <= idx_rzad < len(mapa)):
        return False
    if mapa[idx_rzad][idx_miejsce] != "wolne":
        return False
    mapa[idx_rzad][idx_miejsce] = pasazer
    return True


def wypisz_mape(mapa: list) -> None:
    for i, rzad in enumerate(mapa, start=1):
        opis_rzedu = " | ".join(
            f"{litera}:{'---' if m == 'wolne' else m}" for litera, m in zip(LITERY, rzad)
        )
        print(f"Rząd {i:2}: {opis_rzedu}")


def znajdz_wolne(mapa: list) -> list:
    wolne = []
    for i, rzad in enumerate(mapa, start=1):
        for litera, m in zip(LITERY, rzad):
            if m == "wolne":
                wolne.append((i, litera))
    return wolne


def losuj_zajetosc(mapa: list, procent: float) -> None:
    wszystkie = [(i + 1, litera) for i in range(len(mapa)) for litera in LITERY]
    ile_zajac = int(len(wszystkie) * procent / 100)
    do_zajecia = random.sample(wszystkie, ile_zajac)
    for rzad, litera in do_zajecia:
        rezerwuj(mapa, rzad, litera, "zajęte (system)")


def main():
    mapa = stworz_mape()
    losuj_zajetosc(mapa, 30)

    ok1 = rezerwuj(mapa, 3, "B", "Ksawery")
    ok2 = rezerwuj(mapa, 3, "B", "Anna")
    print(f"Rezerwacja 3B dla Ksawery: {'OK' if ok1 else 'ODRZUCONA (miejsce zajęte)'}")
    print(f"Rezerwacja 3B dla Anna: {'OK' if ok2 else 'ODRZUCONA (miejsce zajęte)'}")

    ok3 = rezerwuj(mapa, 99, "A", "Ktoś")
    print(f"Rezerwacja 99A: {'OK' if ok3 else 'ODRZUCONA (nieprawidłowy rząd)'}")

    wypisz_mape(mapa)
    print(f"Wolnych miejsc: {len(znajdz_wolne(mapa))}")


if __name__ == "__main__":
    main()
```

### 5. Refaktoryzacja / bardziej pythonowe podejście
- `zip(LITERY, rzad)` do parowania liter z wartościami to bardziej pythonowe
  niż `range(len(rzad))` + indeksowanie — unikasz ręcznego liczenia indeksów
  tam, gdzie nie musisz.
- `enumerate(mapa, start=1)` zamiast `for i in range(len(mapa))` — to samo,
  czytelniej.
- Jeśli kiedyś rozbudujesz ten projekt, miejsce jako `dataclass Seat(status, pasazer)`
  byłoby czystsze niż goły string `"wolne"`/imię — na razie string wystarczy.

### 6. Czego to miało nauczyć
Struktur dwuwymiarowych (lista list) i pułapek przy ich tworzeniu (aliasing przy
`* n`), zamiany współrzędnych "ludzkich" (rząd od 1, litera) na indeksy Pythona
(od 0), oraz defensywnego sprawdzania granic przed indeksowaniem zamiast łapania
wyjątku po fakcie.

---

## Zadanie 5 — Trip Expense & Itinerary Tracker

### 1. Delikatna podpowiedź
To jest dokładnie Twój kalkulator ocen z `Cwiczenie6.py`, tylko dokończony zgodnie
z Twoim własnym TODO: prawdziwa pętla `while`, `try/except` przy inpucie, i podział
na osobne funkcje. Zacznij od szkieletu pętli menu, zanim dopracujesz logikę środka.

### 2. Szczegółowa podpowiedź
Struktura głównej pętli:
```python
while True:
    wybor = input("Wybierz opcję: ")
    if wybor == "1":
        dodaj_wydatek(wydatki)
    elif wybor == "2":
        ...
    elif wybor == "5":
        break
```
Do walidacji kwoty: `float(input(...))` w bloku `try`, a w `except ValueError`
poproś ponownie — najprościej przez pętlę `while True` wewnątrz samej funkcji
pobierającej kwotę, która robi `return` dopiero gdy dane są poprawne. Podsumowanie
wg kategorii to ten sam wzorzec zliczania co w Zadaniu 2, tylko sumujesz kwoty
zamiast liczyć wystąpienia — a sortowanie malejące to `sorted(..., key=..., reverse=True)`.

### 3. Typowe błędy
- Cała logika wciśnięta w pętlę `while True` w `main()` zamiast rozbita na funkcje
  (dokładnie to, co masz zaplanowane poprawić w `Cwiczenie6.py`, pkt 7).
- Brak pętli ponawiającej przy błędnym inpucie — jedno złe wejście i program się
  kończy albo krzyczy błędem zamiast poprosić ponownie.
- Kwota ujemna albo `0` przechodzi walidację, bo sprawdzasz tylko czy to liczba,
  a nie czy jest dodatnia.
- Zapominanie zresetować/odczytać budżet raz na starcie i porównywanie go przy
  każdym dodaniu wydatku osobno zamiast trzymać sumę bieżącą.

### 4. Pełne rozwiązanie
```python
def pobierz_kwote() -> float:
    while True:
        surowa = input("Kwota: ")
        try:
            kwota = float(surowa)
            if kwota <= 0:
                print("Kwota musi być dodatnia, spróbuj ponownie.")
                continue
            return kwota
        except ValueError:
            print("To nie jest liczba, spróbuj ponownie.")


def dodaj_wydatek(wydatki: list) -> None:
    kategoria = input("Kategoria: ").strip().lower()
    kwota = pobierz_kwote()
    opis = input("Opis: ").strip()
    wydatki.append({"kategoria": kategoria, "kwota": kwota, "opis": opis})
    print("Dodano wydatek.")


def pokaz_wydatki(wydatki: list) -> None:
    if not wydatki:
        print("Brak wydatków.")
        return
    for w in wydatki:
        print(f"{w['kategoria']}: {w['kwota']:.2f} zł - {w['opis']}")


def podsumowanie_wg_kategorii(wydatki: list) -> dict:
    sumy = {}
    for w in wydatki:
        sumy[w["kategoria"]] = sumy.get(w["kategoria"], 0) + w["kwota"]
    return sumy


def pokaz_podsumowanie(wydatki: list) -> None:
    sumy = podsumowanie_wg_kategorii(wydatki)
    if not sumy:
        print("Brak danych do podsumowania.")
        return
    for kategoria, suma in sorted(sumy.items(), key=lambda item: item[1], reverse=True):
        print(f"{kategoria}: {suma:.2f} zł")


def sprawdz_budzet(wydatki: list, budzet: float) -> None:
    suma = sum(w["kwota"] for w in wydatki)
    if suma > budzet:
        print(f"UWAGA: przekroczono budżet! Wydano {suma:.2f} zł z {budzet:.2f} zł.")
    elif suma > budzet * 0.8:
        print(f"Uwaga: wykorzystano {suma / budzet * 100:.1f}% budżetu.")
    else:
        print(f"W budżecie: {suma:.2f} zł / {budzet:.2f} zł.")


def main():
    wydatki = []
    budzet = pobierz_kwote_budzetu()

    while True:
        print("\n[Menu] 1) dodaj  2) pokaż wszystkie  3) podsumowanie  4) sprawdź budżet  5) wyjście")
        wybor = input("> ").strip()
        if wybor == "1":
            dodaj_wydatek(wydatki)
        elif wybor == "2":
            pokaz_wydatki(wydatki)
        elif wybor == "3":
            pokaz_podsumowanie(wydatki)
        elif wybor == "4":
            sprawdz_budzet(wydatki, budzet)
        elif wybor == "5":
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


def pobierz_kwote_budzetu() -> float:
    print("Podaj budżet na podróż:")
    return pobierz_kwote()


if __name__ == "__main__":
    main()
```

**Omówienie:** `pobierz_kwote()` hermetyzuje walidację raz, a jest użyta dwa razy
(budżet i wydatek) — to unika duplikacji, o której sam pisałeś w TODO
(`Cwiczenie6.py`, "powtórzony kod pobierania x/y"). `main()` jest teraz tylko
"dyspozytorem" — czyta wybór i woła odpowiednią funkcję, żadnej logiki biznesowej
w środku pętli. Podsumowanie wg kategorii to dokładnie ten sam wzorzec słownikowy
co w Zadaniu 2, tylko sumujesz zamiast liczyć wystąpienia.

### 5. Refaktoryzacja / bardziej pythonowe podejście
- `podsumowanie_wg_kategorii` da się skrócić `Counter`-podobnym podejściem, ale
  tu sumujemy kwoty, nie liczymy wystąpień, więc zwykły słownik + `.get()` jest
  właściwym narzędziem (albo `collections.defaultdict(float)`, jeśli chcesz uniknąć
  `.get(kategoria, 0)` — warto poznać `defaultdict` jako naturalny następny krok).
- `sum(w["kwota"] for w in wydatki)` to generator expression zamiast pętli z
  ręcznym akumulatorem — bardziej pythonowe i krótsze.
- Docelowo (przy bonusie z plikiem) zamiast ręcznego formatu tekstowego do zapisu
  warto poznać moduł `json` — `json.dump(wydatki, plik)` zapisuje listę słowników
  w jednej linijce, bez ręcznego parsowania przy wczytywaniu.

### 6. Czego to miało nauczyć
To zadanie spina wszystko naraz: pętlę `while True` jako menu (Twój zaległy punkt
z `Cwiczenie6.py`), podział programu na małe funkcje o jasnej odpowiedzialności,
walidację danych wejściowych z `try/except` w pętli ponawiającej, oraz pracę ze
strukturą "lista słowników" — to jest dokładnie kształt danych, z którym będziesz
pracować przy scraperze cen (Twój cel 3-miesięczny) i przy większości zadań na
LeetCode operujących na rekordach danych.
