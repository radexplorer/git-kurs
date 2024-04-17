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
wynik = 0

i=0

while i<4:
    x = int(input("Podaj liczbe: "))
    wynik += x
    i += 1
print("Wynink to : ", wynik)