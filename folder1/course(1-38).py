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
'''
szukanaLiczba = 40
zgdaywanaLiczba = 0

while zgdaywanaLiczba != szukanaLiczba:
    zgdaywanaLiczba = int(input("Odgadnij liczbę: "))

    if (zgdaywanaLiczba > szukanaLiczba):
        print("Mniej")
    elif (zgdaywanaLiczba < szukanaLiczba):
        print("Więcej")
    else:
        print("Brawo")
        '''
### LISTA ###


'''
for name in names:
    print(name)

print(names[-1])
names[-1] = "Wera"
print(names)
'''
## IN, NOT IN
'''
print("Kasa" in names)

if ("Paula" not in names):
    print("Siema")
else:
    print("Nie ma")

print(3* numbers)
print([4, 5]+numbers)
numbers = [4,45]+numbers
print(numbers)


name = input("Podaj imie: ")
name = name.capitalize

if name in names:
    print("You have access")
else: 
    print("You don't have access")
'''
### OPERACJE NA LISTACH
'''
names = ["Paula", "Ania", "Beata", "Kasia", "Gienek"]
numbers = [2, 43, 56, 67, 324]

print(len(names))
names.append(4)
print(names)
names.insert(2, "Radek")
print(names)
#numbers.append([123, 3456, 547])  #dodaje listę jako całośc do listy podst.
numbers.extend([123, 3456, 547])  #dodaje każdy el. jako osobny 
print(numbers)
names.insert(0, "Maria")
print(names)
print(numbers.index(43))

numbers.sort(reverse=True)
print(numbers) 
print(numbers.count(67))

numbers.pop()
print(numbers)

# reverse - odwraca kolejnośc
# clear - czyści tablice
# remove(x) - usuwa xrr
'''

## KROTKA ## TUPLE
'''
krotka = (1, 23, 456, -5)

krotka[0] = 0
'''
## SŁOWNIK ## DICTIONARY
'''
pokoje = {23: "Radosław Rudnik", 69: "Paula Głowacka"}

pokoje[23] = "Ania głowacka"

print(pokoje.get(23))

pokoje.update({400: "Jan kowalski"})

del(pokoje[400])

print(pokoje.popitem())  #usuwa ostatni element 

print(len(pokoje))

print(pokoje)
'''

## ZBIÓR ###
'''
A = {1, 34, 456, 678, 45}
B = {3245, 2, 45, 12, 67}


A.add(5)
A.discard(1) #zadziała nawet jak nie ma takiej wartości
#A.remove(1)  #kiedy nie ma takiej wartości to wyrzuci błąd 
print(A)
print(set(A)) ## set usuwa duplikaty, zmiana listy w zbiór
print(A|B)
print(A^B)
print(A-B)
print(A.issubset(B))
'''

## TYPY ZAGNIEŻDŻONE ## lista w liście

'''
imie = "Radosław"
wiek = 32
płeć = "men"

imie2 = "Paula"
wiek2= 31
płeć2 = "women"

osoba1 = ("Radosław", 32, "men")
osoba2 = ("Paula", 31, "women")

listaGości = {
    ("Radosław", 32, "men"),
    ("P", 31, "women")
}
#print(listaGości[1][2])
#listaGości[0][0] = "Błażej"
print(listaGości)

## krotka w liście ##  

listaGości2 = {
    ("R", 32, "men"),
    ("Paula", 31, "women")
}
#listaGości2[0][0] = "Błażej" ##NIE MOŻNA ZMIENIAĆ STANU KROTKI
#listaGości2.append(("Marcin", 37, "men"))
print(listaGości2)

listaGości3 = listaGości | listaGości2
print(listaGości3)

for imie, wiek, płeć in listaGości3:
    print("imie: ", imie)
    print("wiek: ", wiek)
    print("płeć: ", płeć)
    print("\n")
'''

## ZAWARTOŚĆ SŁOWNIKA ZAGNIEŻDŻONEGO W LIŚCIE/słowniku ##

people = {
    "c43ctwi37gh87w4hg587why": {"name": "Paula", "age": 31, "sex": "female" },
    "chuaewfa34t45yxoiujhg55": {"name": "Kasia", "age": 5, "sex": "female" },
    "c234r23r234r34t45y54y4y": {"name": "Błażej", "age": 14, "sex": "male" }
} # Dodawanie nowych pozycji do słownika jest szybsze (worek)

people2 = [
    {"id": "c43ctwi37gh87w4hg587why", "name": "Paula", "age": 31, "sex": "female" },
    {"id": "chuaewfa34t45yxoiujhg55", "name": "Kasia", "age": 5, "sex": "female" },
    {"id": "chuaewfa34t45yxoiujhg55", "name": "Błażej", "age": 14, "sex": "male" }
]

people3 = ["Paula",
           "Kasia",
           "Błażej"
]

ratings1 = {
    "Paula": (2, 3, 5, 6, 2),
    "Błażej": (4, 4, 4, 2, 2)
}

ratings2 = [
    {"name": "Paula", "ratings": (2, 3, 5, 6, 2), "behavior": 4},
    {"name": "Błażej", "ratings": (4, 4, 4, 2, 2), "behavior": 2}
]

ratings3 = {
    "Paula": {"ratings": (2, 3, 5, 6, 2), "behavior": 4},
    "Błażej": {"ratings": (4, 4, 4, 2, 2), "behavior": 2}
}
'''
for key in ratings1:
    print(ratings1[key])

for key in ratings1:
    print(key, ": oceny", ratings1[key])

for dictionary in people2:
    for key in dictionary:
        print(key,": ", dictionary[key])

print(people["chuaewfa34t45yxoiujhg55"])
'''
'''
for key in people:
    print("ID: ", key)
    for secondaryKey in people[key]:
        print(secondaryKey, people[key][secondaryKey])

for key in ratings1:
    print(key, "oceny: ", ratings1[key])
'''

print(people.items())
print(people)

for id, dictionary in people.items():
    print("ID: ", id)
    for key in dictionary:
        print(key, dictionary[key])


