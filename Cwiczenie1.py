#   Maszyna do zadawania pytan uzytkownikowi i odpowiadania na nie.

print("Witaj w programie do zadawania pytań\nOdpowiedz teraz na trzy pytania i zobacz ilosc uzyskanych puntków!\nPytanie nr1: Ile to jest 2+2?")
a = int(input("Odpowiedz: "))
odpowiedź1 = "Dobrze!" if a == 4 else "Twoja odpowiedz jest niepoprawna, spróboj ponownie: "
print(odpowiedź1)
if a != 4:
    a = int(input("Odpowiedz: "))
    odpowiedź1 = "Dobrze!" if a == 4 else "Twoja odpowiedz jest niepoprawna!"
    print(odpowiedź1)
print("Pytanie nr 2: Jaka jest stolica Polski?")
b = (input("Odpowiedz:")).lower().strip()
odpowiedz2 = "Dobrze!" if b == "warszawa" else "Twoja odpowiedz jest niepoprawna! Spróboj ponownie:"
print(odpowiedz2)
if b != "warszawa":
    b = (input("Odpowiedz: ")).lower().strip()
    odpowiedz2 = "Dobrze!" if b == "warszawa" else "Twoja odpowiedz jest niepoprawna!"
    print(odpowiedz2)
print("Jakiego języka programowania uczę się teraz?")
c = (input("odpowiedz:")).lower().strip()
odpowiedz3 = "Dobrze!" if c == "python" else "Twoja odpowiedz jest niepoprawna! Spróboj ponownie:"
print(odpowiedz3)
if c != "python":
    c = input("odpowiedz: ").lower().strip()
    odpowiedz3 = "Dobrze!" if c == "python" else "Twoja odpowiedz jest niepoprawna!"
    print(odpowiedz3)
print("Dziękuję za udział w tescie! Twoje odpowiedzi to: ")
print(f"Pytanie 1: {a}")
print(f"Pytanie 2: {b}")
print(f"Pytanie 3: {c}")
print("Suma twoich punktów to: ")
suma_punktów = (1 if a == 4 else 0) + (1 if b ==
                                       'warszawa' else 0) + (1 if c == 'python' else 0)
print(suma_punktów)
if suma_punktów == 3:
    print("Gratulacje! Udało Ci się zdobyć maksymalną ilość punktów!")
elif suma_punktów == 2:
    print("Prawidłowo odpowiedziałeś na 2 pytania, gratulacje!")
else:
    print("Niestety, nie udało Ci się zdobyć wystarczającej ilości punktów. Spróbuj ponownie!")
