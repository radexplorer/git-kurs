
Program:
1. Dodaje definicje
2. Wyszukuje definiecje
3. Usuwa wybrane definicje

definitions = {}

while(True):
    print("1. Add definition")
    print("2. Search definition")
    print("3. Remove definition")
    print("4. End")

    choice = input("What do you want to do? ")

    if choice == "1":
        key = input("Give a key(word) to define: ")
        definition = input("Give a definition: ")
        definitions[key] = definition
        print("Definition added successfully")
    #    print(definitions)
    elif choice == "2":
        key = input("Give a key(word) to search: ")
        if key in definitions:
            print(definitions[key])
        else:
            print("There's no key like that")
    elif choice == "3":
        key = input("Give a key(word) to remove: ")
        if key in definitions: 
            del definitions[key]
            print(key, "is removed")
    else:
        break
'''
### TRANSFORMACJA LISTY ###
'''
numbers = [1, 2, 3, 4, 5, 6, 7]

potegaDwojki = []
for element in numbers:
    potegaDwojki.append(element*2)

liczbyParzyste = []
for element in numbers:
    if (element%2 == 0):
        liczbyParzyste.append(element)

print(potegaDwojki)
print(liczbyParzyste)

potegaDwojki2 = [element**5 for element in range(20)]

liczbyParzyste2 = [element 
                  for element in numbers
                  if (element % 2 == 0)]

print(potegaDwojki2, liczbyParzyste2)
'''

## GENERATORS ## 
'''
import sys

evenNumbers = [element
    for element in range(1000)
    if (element % 2 == 0)
    ]


evenNumbersGen = (element
    for element in range(1000)
    if (element % 2 == 0)
)#wybieramy elementy

for item in evenNumbersGen:
    print(item) #generujemy elementy na bieżąco

print(evenNumbers)

print(sum(evenNumbers))
print(sys.getsizeof(evenNumbersGen))
print(sys.getsizeof(evenNumbers))
'''

## WYRAŻENIE SŁOWNIKOWE ##
'''
names = {"rad", "pau", "kat", "ann"}

numbers = [1, 2, 3, 4, 5]

celsius = {'t1': 4, 't2': 2, 't3': 7, 't4': 78}

namesLength = {
    name : len(name)
    for name in names
    if name.startswith("P")
}
print(namesLength)

mulitpliedNumbers = {
    number : number*3
    for number in numbers
}
print(mulitpliedNumbers)
print(celsius.items())

fahrenheit = {
    key: value*1.8+32
    for key, value in celsius.items()
    if value >= 5
}
print(fahrenheit)
print(names)
names = {name.capitalize() for name in names}
print(names)
'''
'''
## ZADANIE ##

range(100, 471)

for numbers in range(100, 471):
    if numbers % 7 == 0 and numbers % 5 != 0:
        print(numbers)

#GEN



