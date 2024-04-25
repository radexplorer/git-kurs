'''
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

