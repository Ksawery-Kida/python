#   Tabliczka mnozenia:
import questionary
print("Witam w programie do tabliczki mnozenia")
number = int(input("Podaj liczbe do ktorej chcesz zobaczyc tabliczke mnozenia: "))
for number2 in range(1, 11):
    print(f"{number} x {number2} = {number * number2}")
while True: 
    choice = questionary.select(
        "Czy chcesz zobaczyc tabliczke mnozenia dla innej liczby?",
        choices=["1. Tak", "2. Nie"]).ask()
    if choice == "1. Tak":
        number = int(input("Podaj liczbe do ktorej chcesz zobaczyc tabliczke mnozenia: "))
        for number2 in range(1, 11):
            print(f"{number} x {number2} = {number * number2}")
    else:
        print("Dziekuje za skorzystanie z programu!")
        break