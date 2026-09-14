# Zadania: Bunkier na zombie apokalipsę 🧟

Ten sam poziom trudności co w zestawie lotniczym, ten sam trening (parsowanie,
zliczanie w słowniku, funkcje pomocnicze, siatki 2D, menu w pętli), ale motyw
inny, żeby się nie zanudzić. Zero wskazówek tutaj — te są w
`Bunkier_2_Podpowiedzi_i_Rozwiazania.md`.

---

## Zadanie 1 — Parser sygnałów SOS
**Trudność: krótkie (10–15 min)**

### Opis
Ocalali wysyłają krótkie sygnały radiowe zakodowane jako jeden string. Musisz je
sparsować i wypisać w czytelnej formie na ekranie centrum dowodzenia.

### Wymagania funkcjonalne
- Funkcja `parse_sygnal(raw: str) -> dict`, przyjmująca string w formacie
  `"ID_OCALALEGO;LOKALIZACJA;LICZBA_OSOB;POZIOM_ZAPASOW;GODZINA"`
  (np. `"S07;MAGAZYN-B;4;NISKI;03:12"`) i zwracająca słownik z kluczami:
  `id`, `lokalizacja`, `liczba_osob`, `zapasy`, `godzina`.
- Funkcja `print_sygnal(dane: dict)`, wypisująca sformatowany komunikat w ramce
  tekstowej.
- Program obsługuje listę min. 3 surowych sygnałów.

### Ograniczenia
- Tylko standardowa biblioteka.
- Parsowanie i wypisywanie w osobnych funkcjach.

### Przykładowe wejście
```
"S07;MAGAZYN-B;4;NISKI;03:12"
```

### Oczekiwane wyjście
```
==================
SYGNAŁ OD: S07
Lokalizacja: MAGAZYN-B
Osób: 4
Zapasy: NISKI
Godzina: 03:12
==================
```

### Bonus
Jeśli sygnał ma złą liczbę pól, program wypisuje czytelny komunikat błędu
zamiast się wywalić.

---

## Zadanie 2 — Licznik warczenia (czujniki ruchu)
**Trudność: krótkie (15–20 min)**

### Opis
Czujniki ruchu wokół bunkra co jakiś czas mierzą poziom hałasu/zagrożenia
(skala 0–10). Masz listę odczytów z całej nocy i robisz podsumowanie zmiany.

### Wymagania funkcjonalne
- Funkcja `klasyfikuj(poziom: int) -> str` zwracająca kategorię:
  `"cisza"` (0–2), `"szmery"` (3–5), `"warczenie"` (6–8), `"horda"` (9–10).
- Pętla po liście odczytów, zlicza wystąpienia każdej kategorii (słownik-licznik).
- Podsumowanie: dla każdej kategorii — liczba wystąpień i procent całej nocy.
- Najdłuższy ciąg pod rząd odczytów z kategorii `"horda"` (jeśli wystąpił).

### Ograniczenia
- Lista dowolnej (niepustej) długości.
- Licznik działa dynamicznie na słowniku, bez zakładania z góry liczby kategorii.

### Przykładowe wejście
```python
odczyty = [1, 2, 4, 7, 9, 9, 9, 3, 0, 6, 8, 9]
```

### Oczekiwane wyjście (przykładowo)
```
cisza: 3 (25.0%)
szmery: 2 (16.7%)
warczenie: 3 (25.0%)
horda: 4 (33.3%)
Najdłuższa seria "horda": 3 odczyty z rzędu
```

### Bonus
Funkcja wypisująca prosty tekstowy "wykres" (gwiazdki) liczności każdej kategorii.

---

## Zadanie 3 — Sprawdzarka kodów do drzwi bunkra
**Trudność: średnie (20–40 min)**

### Opis
Dowódca bunkra chce ocenić, czy kody dostępu do śluzy są wystarczająco trudne
do złamania, zanim ktoś się włamie i zje wam zapasy.

### Wymagania funkcjonalne
- Funkcja `ocen_kod(kod: str) -> str` zwracająca jedną z ocen:
  `"do wyrzucenia"`, `"słaby"`, `"średni"`, `"mocny"`, `"twierdza"` na podstawie
  długości oraz obecności małych/wielkich liter, cyfr, znaków specjalnych
  (punktację projektujesz sam, spójnie).
- Osobne funkcje sprawdzające pojedyncze kryteria (np. `ma_cyfre`,
  `ma_wielka_litere`) — nie jedna wielka funkcja.
- Program iteruje po liście kodów i wypisuje ocenę dla każdego.
- Jeśli w liście trafi się coś, co nie jest stringiem, program obsługuje to przez
  `try/except` bez crashowania całości.

### Ograniczenia
- Bez zewnętrznych bibliotek — logika ręczna.
- Minimum 4 osobne funkcje pomocnicze.

### Przykładowe wejście
```python
kody = ["1234", "Bunkier123", "Zx9!kLm2@Qw", 12345, "aaaa"]
```

### Oczekiwane wyjście (przykładowo)
```
"1234" -> do wyrzucenia
"Bunkier123" -> średni
"Zx9!kLm2@Qw" -> twierdza
[BŁĄD] Element 12345 nie jest tekstem - pominięto
"aaaa" -> do wyrzucenia
```

### Bonus
Funkcja `generuj_sugestie(kod)` mówiąca konkretnie czego brakuje.

---

## Zadanie 4 — Siatka koi w bunkrze
**Trudność: średnie (30–45 min)**

### Opis
Bunkier ma ograniczoną liczbę koi w kilku pomieszczeniach. Musisz zarządzać
przydziałem ocalałych do wolnych miejsc do spania.

### Wymagania funkcjonalne
- Reprezentacja bunkra jako lista list (np. 8 pomieszczeń × 4 koje: A–D), gdzie
  każda koja to `"wolna"` albo imię ocalałego.
- Funkcja `przydziel(mapa, pomieszczenie, koja, osoba) -> bool` — próbuje
  przydzielić koję, zwraca `True`/`False` (`False` jeśli zajęta lub poza
  zakresem).
- Funkcja `wypisz_mape(mapa)` — wypisuje czytelną siatkę w konsoli.
- Funkcja `znajdz_wolne(mapa) -> list` — zwraca listę wolnych koi jako
  `(pomieszczenie, litera)`.
- Próba przydziału do nieistniejącego pomieszczenia (np. nr 99) nie wywala
  programu — tylko czytelny komunikat.

### Ograniczenia
- Bez bibliotek zewnętrznych — czysty Python, listy list.
- Numeracja pomieszczeń od 1, nie od 0.

### Przykładowe wejście
```python
przydziel(mapa, 3, "B", "Rick")
przydziel(mapa, 3, "B", "Michonne")  # ta sama koja, drugi raz
```

### Oczekiwane wyjście
```
Przydział 3B dla Rick: OK
Przydział 3B dla Michonne: ODRZUCONY (koja zajęta)
```

### Bonus
Funkcja `losuj_zajetosc(mapa, procent)`, losowo zajmująca zadany procent koi na
starcie (symulacja grupy, która już tu mieszka), moduł `random`.

---

## Zadanie 5 (mini projekt) — Tracker racjonowania zapasów
**Trudność: największy mini projekt (60–120 min)**

### Opis
Jesteś kwatermistrzem bunkra. Budujesz aplikację konsolową do śledzenia zużycia
zapasów (jedzenie, woda, amunicja, leki) i pilnowania, żeby starczyło do wiosny.

### Wymagania funkcjonalne
- Menu tekstowe w pętli `while True` z opcjami: 1) zapisz zużycie zapasu,
  2) pokaż całą historię zużycia, 3) pokaż podsumowanie wg kategorii zapasu,
  4) sprawdź czy zbliżacie się do wyczerpania zapasów, 5) wyjście.
- Każdy wpis zużycia to słownik: `{"kategoria": ..., "ilosc": ..., "opis": ...}`,
  wszystkie wpisy trzymane w liście.
- Zapis zużycia waliduje dane (ilość musi być liczbą dodatnią) — `try/except`,
  w razie błędu ponowna prośba zamiast crashu.
- Podsumowanie wg kategorii: zsumowana ilość zużyta per kategoria, posortowana
  malejąco.
- Funkcja sprawdzająca zapasy: na starcie podajesz początkowy stan magazynu
  (łączna dostępna ilość), program ostrzega, gdy zużycie przekroczyło 80% i 100%
  dostępnych zapasów.
- Program podzielony na minimum 5 osobnych funkcji.

### Ograniczenia
- Program działa w pętli, dopóki nie wybierzesz "wyjście".
- Bez zewnętrznych bibliotek do menu (zwykły `input()` wystarczy).

### Przykładowa interakcja (skrócona)
```
Podaj całkowity stan magazynu: 500
[Menu]
> 1
Kategoria: woda
Ilość: 20
Opis: dzienne racje dla 4 osób
> 3
woda: 20.00 jednostek
> 5
Trzymaj się, kwatermistrzu.
```

### Oczekiwane wyjście
Czytelne, sformatowane podsumowania po każdej akcji, brak crashy przy błędnych
danych.

### Bonus (jeśli zostanie czas)
Zapis historii zużycia do pliku tekstowego przy wyjściu i wczytanie jej przy
starcie (persystencja między uruchomieniami) — `open()`, tryby `"w"`/`"r"`.
