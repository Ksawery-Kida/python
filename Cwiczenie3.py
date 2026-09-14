#   Zgadywanie liczb z przedziału 1-100 
import random
print("Witam w programie do zgadywania liczb z przedzialu 1-100")
print("Podaj swoja liczbe: ") 
licznik = 1
random_number = random.randint(1, 100)
while True:
    try: 
        user_number = int(input())
        break
    except ValueError:
        print("Podaj prawidlowa liczbe: ")
while user_number != random_number:
    licznik += 1
    if user_number < random_number:
        print("Twoja liczba jest za mala, sprobuj jeszcze raz")
    else:
        print("Twoja liczba jest za duza, sprobuj jeszcze raz")
    user_number = int(input())
print("Gratulacje! Zgadles liczbe!")
print(f"Twoja liczba prób: {licznik}")





