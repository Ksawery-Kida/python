# Learning about loops in Python
print("Program który wypisuje liczby od 1 do 10")
for i in range(1, 11):
    print(i)
print("Program który wypisuje liczby od 1 do 10, ale tylko parzyste")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print("Program który wypisuje liczby od 1 do 10, ale tylko nieparzyste")
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
print("Suma tych wszystkich liczb wynosi: ")
suma = 0
for i in range (1, 101):
    suma += i
print(suma)
    