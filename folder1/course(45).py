## FUNKCJE ##
## def - inicjujemy funckę

def welcome_message(name):
    print("Hello", name)

welcome_message("Paulo")

names = ["rad", "pau", "kat", "ann"]

for name in names:
    welcome_message(name)

        

def reactangle_area(a,b):
    return a*b

#a = int(input("Give length of first side: "))
#b = int(input("Give length of second side: "))

#print(reactangle_area(a, b)*5)

def divison(a,b):
    if (b==0):
        return False
    return a/b

print(divison(10,0))

# none to false(bool)
'''
def sum_positives(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total += number
    
    return total

numbers = [-3, 0 , 23, 56]

print(sum_positives(numbers))