## FUNKCJE ##
## def - inicjujemy funckę

import module

def welcome_message(name):
    print("Hello", name)

welcome_message("Paulo")

names = ["rad", "pau", "kat", "ann"]

for name in names:
    welcome_message(name)

        

def reactangle_area(a,b):
    return a*b

print(reactangle_area(2,7))

#a = int(input("Give length of first side: "))
#b = int(input("Give length of second side: "))

#print(reactangle_area(a, b)*5)

def divison(a,b):
    if (b==0):
        return 
    return a/b

print(divison(10,0))

# none to false(bool)

def sum_positives(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total += number
    
    return total

numbers = [-3, 0 , 23, 56]

print(sum_positives(numbers))


print(module.pole_kwadratu(5))

wybor = input("""Wybierz figurę:
      1. kwadrat
      2. prostokat
      3. kolo
      4. trapez
      5. trojkat""")

if (wybor == '1'):
    a = float(input("Podaj bok kwartatu: "))
    print("Pole kwadratu: ", module.pole_kwadratu(a))
elif (wybor == '2'):
    a = float(input("Podaj dlugosc 1 boku: "))
    b = float(input("Podaj dlugosc 2 boku: "))
    print("Pole kwadratu: ", module.pole_prostokąta(a, b))