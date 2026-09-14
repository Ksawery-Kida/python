#           Kalkulator ocen
# TODO:
# 1. Poprawić obsługę inputów od użytkownika (int/float)
# 2. Dodać zabezpieczenie try/except na błędne dane
# 3. Poprawić formatowanie ocen wpisywanych przez użytkownika:
#    - obsłużyć "5,4,3"
#    - obsłużyć "5, 4, 3"
#    - zamienić tekst na listę liczb
# 4. Zapisać średnią do zmiennej zamiast wywoływać funkcję kilka razy
# 5. Dokończyć pętlę programu dla wielu uczniów (while)
# 6. Poprawić menu questionary:
#    - użyć .ask()
#    - zapisać wybór użytkownika do zmiennej
#    - sprawdzać wynik zmiennej, a nie funkcji
# 7. Rozdzielić program na więcej funkcji:
#    - pobieranie danych ucznia
#    - pobieranie ocen
#    - liczenie średniej
#    - wyświetlanie wyniku
# 8. Dodać walidację ocen:
#    - ocena minimum 1
#    - ocena maksimum 6
# 9. Przetestować program na różnych przypadkach:
#    - poprawne oceny
#    - puste dane
#    - litery zamiast liczb
import questionary
print("Witaj w analizatorze ocen \n Podaj swoje imie:")
imie = input()
print("Podaj swoje naziwsko:")
nazwisko = input()


def przywitaj(imie, naziwsko):
    print(f"Witaj w moim programie, {imie} {nazwisko}!")
przywitaj(imie, nazwisko) 
print("Teraz obliczymy srednia twoich ocen.")
oceny = input("Podaj oceny oddzielone przecinkami: ")


def oblicz_srednia(oceny):
    oceny_list = [int(ocena)for ocena in oceny.split(",")]
    return sum(oceny_list) / len(oceny_list) 
    srednia = oblicz_srednia(oceny)
    print(srednia)
    if srednia <= 2:
        print("Niestety widzimy sie na poprawce")
    elif srednia <= 3:
        print("Twoja srednia jest dostateczna, ale mozesz sie poprawic")
    elif srednia <= 4:
        print("Twoja srednia jest dobra, ale mozesz sie poprawic")
    elif srednia <= 5:
        print("Twoja srednia jest bardzo dobra, ale mozesz sie poprawic")
    else:
        print("Twoja srednia jest celujaca, gratulacje!")
    print("Czy chcesz obliczyc srednia dla innego ucznia?")
print(oblicz_srednia(oceny))
print("Czy chcesz obliczyc srednia dla innego ucznia?")

def choice():
    choice = questionary.select(
    "Wybierz opcje:",
    choices=[
        "Tak",
        "Nie"
    ])
    return choice.ask()
choice()

if choice() == "Tak":
    przywitaj(imie, nazwisko)
    oblicz_srednia(oceny)
elif choice()  == "Nie":
    print("Dziekuje za skorzystanie z mojego programu, do zobaczenia!")
