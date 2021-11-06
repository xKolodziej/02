import random

print("Komputer rzuca...")
rzut = random.randrange(1, 7)

wybor = input("Sprobuj zgadnac ile oczek wyrzucił komputer: ")
wybor = int(wybor)

if wybor == rzut:
    print("Trafiłes")
else:
    print("Nie udało sie")