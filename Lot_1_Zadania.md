# Zadania na lot ✈️

5 zadań, rosnąca trudność. Zero wskazówek i rozwiązań tutaj — to masz w osobnym pliku
(`Lot_2_Podpowiedzi_i_Rozwiazania.md`), do którego zaglądasz dopiero gdy utkniesz albo
skończysz. Wszystko robisz offline, bez zewnętrznych bibliotek (poza `random`, jeśli
zaznaczone, i opcjonalnie `questionary` jeśli masz je już zainstalowane lokalnie).

---

## Zadanie 1 — Boarding Pass Parser
**Trudność: krótkie (10–15 min)**

### Opisdef
Lotniska kodują dane biletu pokładowego jako jeden ciąg znaków. Napisz program,
który taki surowy string zamienia na czytelny "bilet" wypisany w konsoli.

### Wymagania funkcjonalne
- Funkcja `parse_boarding_pass(raw: str) -> dict`, przyjmująca string w formacie
  `"NUMER_LOTU;LOTNISKO_WYLOTU;LOTNISKO_PRZYLOTU;GODZINA;MIEJSCE"`
  (np. `"LO123;WAW;JFK;14:35;22A"`) i zwracająca słownik z kluczami:
  `lot`, `wylot`, `przylot`, `godzina`, `miejsce`.
- Funkcja `print_boarding_pass(dane: dict)`, która wypisuje sformatowany bilet
  w ramce tekstowej (f-stringi + np. `"="` jako separator).
- Program obsługuje listę min. 3 surowych stringów i wypisuje każdy bilet.

### Ograniczenia
- Tylko standardowa biblioteka.
- Parsowanie i wypisywanie w osobnych funkcjach.

### Przykładowe wejście
```
"LO123;WAW;JFK;14:35;22A"
```

### Oczekiwane wyjście (format dowolny, ale czytelny)
```
==================
LOT: LO123
Z: WAW -> DO: JFK
Godzina: 14:35
Miejsce: 22A
==================
```

### Bonus
Jeśli string ma złą liczbę pól (nie 5), program wypisuje czytelny komunikat błędu
zamiast się wywalić.

---

## Zadanie 2 — Turbulence Counter
**Trudność: krótkie (15–20 min)**

### Opis
System pokładowy co jakiś czas mierzy poziom turbulencji (skala 0–10). Masz listę
odczytów z całego lotu i robisz z niej podsumowanie.

### Wymagania funkcjonalne
- Funkcja `klasyfikuj(poziom: int) -> str` zwracająca kategorię:
  `"spokojnie"` (0–2), `"lekko"` (3–5), `"mocno"` (6–8), `"niebezpiecznie"` (9–10).
- Pętla po liście odczytów, klasyfikuje każdy i zlicza wystąpienia każdej kategorii
  (słownik jako licznik).
- Podsumowanie na końcu: dla każdej kategorii — liczba wystąpień i procent całego lotu.
- Znajdź i wypisz najdłuższy ciąg pod rząd odczytów z kategorii `"niebezpiecznie"`
  (jeśli w ogóle wystąpił).

### Ograniczenia
- Lista może mieć dowolną (niepustą) długość.
- Nie zakładaj z góry liczby kategorii w kodzie licznika — działaj dynamicznie na słowniku.

### Przykładowe wejście
```python
odczyty = [1, 2, 4, 7, 9, 9, 9, 3, 0, 6, 8, 9]
```

### Oczekiwane wyjście (przykładowo)
```
spokojnie: 3 (25.0%)
lekko: 2 (16.7%)
mocno: 3 (25.0%)
niebezpiecznie: 4 (33.3%)
Najdłuższa seria "niebezpiecznie": 3 odczyty z rzędu
```

### Bonus
Funkcja wypisująca prosty tekstowy "wykres" (np. gwiazdki) pokazujący liczność
każdej kategorii.

---

## Zadanie 3 — Password Strength Checker
**Trudność: średnie (20–40 min)**

### Opis
Masz listę haseł-kandydatów (np. do przyszłej sieci domowej) i chcesz ocenić ich
siłę, zanim komukolwiek je polecisz.

### Wymagania funkcjonalne
- Funkcja `ocen_haslo(haslo: str) -> str` zwracająca jedną z ocen:
  `"za słabe"`, `"słabe"`, `"średnie"`, `"silne"`, `"bardzo silne"` na podstawie
  długości oraz obecności małych/wielkich liter, cyfr, znaków specjalnych
  (punktację projektujesz sam, ale ma być spójna i uzasadniona).
- Osobne funkcje sprawdzające pojedyncze kryteria (np. `ma_cyfre`, `ma_wielka_litere`)
  — nie pisz wszystkiego w jednej funkcji.
- Program iteruje po liście haseł i wypisuje ocenę dla każdego.
- Jeśli w liście trafi się coś, co nie jest stringiem (np. przez pomyłkę liczba),
  program obsługuje to przez `try/except` i wypisuje czytelny komunikat, zamiast
  crashować cały program.

### Ograniczenia
- Bez zewnętrznych bibliotek do walidacji haseł — logika ręczna.
- Minimum 4 osobne funkcje pomocnicze.

### Przykładowe wejście
```python
haslo_lista = ["1234", "Kotek123", "Zx9!kLm2@Qw", 12345, "aaaa"]
```

### Oczekiwane wyjście (przykładowo)
```
"1234" -> za słabe
"Kotek123" -> średnie
"Zx9!kLm2@Qw" -> bardzo silne
[BŁĄD] Element 12345 nie jest tekstem - pominięto
"aaaa" -> za słabe
```

### Bonus
Funkcja `generuj_sugestie(haslo)`, która mówi konkretnie czego brakuje
(np. "brakuje cyfry i znaku specjalnego").

---

## Zadanie 4 — Airplane Seat Map Booking Simulator
**Trudność: średnie (30–45 min)**

### Opis
Symulujesz system rezerwacji miejsc w samolocie — siatkę rzędów i miejsc,
z możliwością rezerwacji, sprawdzania zajętości i wypisywania mapy.

### Wymagania funkcjonalne
- Reprezentacja samolotu jako lista list (np. 10 rzędów × 6 miejsc: A–F), gdzie
  każde miejsce to `"wolne"` albo imię/inicjały pasażera.
- Funkcja `rezerwuj(mapa, rzad, miejsce, pasazer) -> bool` — próbuje zarezerwować
  miejsce, zwraca `True`/`False` (`False` jeśli zajęte lub poza zakresem).
- Funkcja `wypisz_mape(mapa)` — wypisuje czytelną siatkę miejsc w konsoli.
- Funkcja `znajdz_wolne(mapa) -> list` — zwraca listę wszystkich wolnych miejsc
  jako `(rzad, litera)`.
- Program obsługuje próbę rezerwacji nieistniejącego miejsca (np. rząd 99) bez
  wywalenia się — z komunikatem błędu.

### Ograniczenia
- Bez bibliotek zewnętrznych (żadnego numpy) — czysty Python, listy list.
- Indeksowanie rzędów od 1, nie od 0.

### Przykładowe wejście
```python
rezerwuj(mapa, 3, "B", "Ksawery")
rezerwuj(mapa, 3, "B", "Anna")  # to samo miejsce, drugi raz
```

### Oczekiwane wyjście
```
Rezerwacja 3B dla Ksawery: OK
Rezerwacja 3B dla Anna: ODRZUCONA (miejsce zajęte)
```

### Bonus
Funkcja `losuj_zajetosc(mapa, procent)`, która losowo zajmuje zadany procent
miejsc na starcie (symulacja już sprzedanych biletów), z użyciem modułu `random`.

---

## Zadanie 5 (mini projekt) — Trip Expense & Itinerary Tracker
**Trudność: największy mini projekt (60–120 min)**

### Opis
Budujesz mini-aplikację konsolową do śledzenia wydatków z podróży — rozbudowaną
wersję Twojego kalkulatora ocen, tylko dla wydatków, z pełnym menu działającym
w pętli.

### Wymagania funkcjonalne
- Menu tekstowe w pętli `while True` z opcjami:
  1. dodaj wydatek
  2. pokaż wszystkie wydatki
  3. pokaż podsumowanie wg kategorii
  4. sprawdź czy przekroczono budżet
  5. wyjście
- Każdy wydatek to słownik: `{"kategoria": ..., "kwota": ..., "opis": ...}`,
  wszystkie wydatki trzymane w liście.
- Dodawanie wydatku waliduje dane wejściowe (kwota musi być liczbą dodatnią) —
  `try/except`, w razie błędu użytkownik jest proszony ponownie zamiast crashu.
- Podsumowanie wg kategorii: zsumowana kwota per kategoria, posortowana malejąco
  wg sumy.
- Funkcja sprawdzająca budżet: użytkownik na starcie podaje budżet całkowity,
  program ostrzega, gdy suma wydatków przekroczyła 80% i 100% budżetu.
- Program podzielony na minimum 5 osobnych funkcji — żadnej logiki "na sztywno"
  w pętli głównej poza wywołaniami funkcji i obsługą wyboru menu.

### Ograniczenia
- Program działa w pętli, dopóki użytkownik nie wybierze "wyjście".
- Bez zewnętrznych bibliotek do menu (zwykły `input()` wystarczy; `questionary`
  opcjonalnie, jeśli masz je już zainstalowane offline).

### Przykładowa interakcja (skrócona)
```
Podaj budżet na podróż: 2000
[Menu]
> 1
Kategoria: jedzenie
Kwota: 120
Opis: lunch na lotnisku
> 3
jedzenie: 120.00 zł
> 5
Do zobaczenia!
```

### Oczekiwane wyjście
Czytelne, sformatowane podsumowania po każdej akcji, brak crashy przy błędnych danych.

### Bonus (jeśli zostanie czas)
Zapis wydatków do pliku tekstowego przy wyjściu z programu i wczytanie ich przy
starcie (persystencja między uruchomieniami). To będzie Twoje pierwsze zetknięcie
z zapisem do pliku w Pythonie — poszukaj `open()` i trybów `"w"`/`"r"`.
