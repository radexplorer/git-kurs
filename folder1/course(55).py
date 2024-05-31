import module
from enum import IntEnum

##print(list(Enum('Menu Figury', ' kwadrat prostokat kolo trapez trojkat')))

Manu_Figury = IntEnum('Menu Figury', {'kwadrat': 4,  'prostokat':65,  'kolo': 23, 'trapez': 54,  'trojkat': 12})

print(list(Manu_Figury))

wybor = int(input("""Wybierz figurę:
      1. kwadrat
      2. prostokat
      3. koło
      4. trapez
      5. trojkat"""))

if (wybor == Manu_Figury.kwadrat.value):
    a = float(input("Podaj bok kwartatu: "))
    print("Pole kwadratu: ", module.pole_kwadratu(a))
elif (wybor == Manu_Figury.prostokat):
    a = float(input("Dlugosc 1 boku: "))
    b = float(input("Dlugosc 2 boku: "))
    print("Pole prostokata: ", module.pole_prostokąta(a, b))
elif (wybor == '3'):
    r = float(input("Podaj promien: "))
    print("Pole kola: ", module.pole_kola(r))
