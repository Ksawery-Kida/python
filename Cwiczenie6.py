#           Kalkulator ocen
import questionary


def przywitaj(imie, nazwisko):
    print(f"Witaj w moim programie, {imie} {nazwisko}!")


def oblicz_srednia(oceny):
    oceny_list = [int(ocena) for ocena in oceny.split(",")]
    return sum(oceny_list) / len(oceny_list)


def opisz_srednia(srednia):
    if srednia <= 2:
        return "Niestety widzimy sie na poprawce"
    elif srednia <= 3:
        return "Twoja srednia jest dostateczna, ale mozesz sie poprawic"
    elif srednia <= 4:
        return "Twoja srednia jest dobra, ale mozesz sie poprawic"
    elif srednia <= 5:
        return "Twoja srednia jest bardzo dobra, ale mozesz sie poprawic"
    else:
        return "Twoja srednia jest celujaca, gratulacje!"


def chce_kontynuowac():
    return questionary.select(
        "Czy chcesz obliczyc srednia dla innego ucznia?",
        choices=["Tak", "Nie"]).ask()


def main():
    print("Witaj w analizatorze ocen!")
    while True:
        imie = input("Podaj swoje imie: ")
        nazwisko = input("Podaj swoje nazwisko: ")
        przywitaj(imie, nazwisko)
        oceny = input("Podaj oceny oddzielone przecinkami: ")
        srednia = oblicz_srednia(oceny)
        print(f"Twoja srednia to: {srednia:.2f}")
        print(opisz_srednia(srednia))
        if chce_kontynuowac() == "Nie":
            print("Dziekuje za skorzystanie z mojego programu, do zobaczenia!")
            break


if __name__ == "__main__":
    main()
