##imie = (input("Jak masz na imie: "))
##wiek = (int(input("Cześc " + imie + " ile masz lat: ")))
##print("Za rok bedziesz miał", wiek+1, "lat")

'''
import math

choice = input("* - możenie, / - dzielenie, + - dodawanie,  - - odejmowanie: ")

a = int(input("First number: "))
b = int(input("Second number: "))

if (choice == "*"):
    print(a*b)
elif (choice == "/"):
    if(b==0):
        print("Nie dziel przez 0")
    else:
        print(a/b)
elif (choice == "+"):
    print(a+b)
elif(choice=="-"):
    print(a-b)

x = int(input("Podaj liczbe: "))

if x < 0:
    x = -x
print(x)
'''

#Pętla od  1 do 5
'''
liczba = 100

while liczba >= 0:
    print(liczba)
    liczba -= 1
'''
'''
wynik = 0

i=0

while i<4:
    x = int(input("Podaj liczbe: "))
    wynik += x
    i += 1
print("Wynink to : ", wynik)
'''
'''
wynik = 0 

for i in range (200):
    if (i % 5 == 0 and i % 7 != 0):
        print(("liczba", i, "podz. przez 5 i niepodz. przez 7"))
print("Wynik to: ", wynik)
'''

#### BREAK AND CONTINUE
'''
wynik = 0 

for i in range (3):
    x=int(input("Give number bigger than 0: "))
    if (x>0):
        wynik += x
    else:
        print("Miała byc liczba dodatnia")
        break
    print("Aktualny wynik dodawania to: ", wynik)
'''
'''
wynik = 0
i = 0

while i < 3:
    x=int(input("Give number bigger than 0: "))
    if (x>0):
        wynik += x
    else:
        print("Miała byc liczba dodatnia")
        continue
    print("Aktualny wynik dodawania to: ", wynik)
    i += 1

'''
'''
wynik = 0
i = 0

while i < 3:
    x=int(input("podaj parzystą liczbę: "))
    if (x>0 and x%2==0):
        wynik += x
    else:
        print("Miała być parzysta")
        continue
    print("Aktualny wynik dodawania to: ", wynik)
    i += 1
'''
#Zgadywana liczba

szukanaLiczba = 40
zgdaywanaLiczba = 0

while zgdaywanaLiczba != szukanaLiczba:
    zgdaywanaLiczba = int(input("Odgadnij liczbę: "))

    if (zgdaywanaLiczba > szukanaLiczba):
        print("Mniej")
    elif (zgdaywanaLiczba <)
    else:
        print("Try again")