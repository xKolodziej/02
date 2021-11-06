x= 1
y= 2
z= 5
ile_razy_z = 0
ile_razy_x = 0
ile_razy_y = 0
kwota=input("Podaj kwote: ")
kwota = int(kwota)

print(f"Kwota {kwota} zł w monetach: ")
while(kwota>0):
    if kwota>=z:
        ile_razy_z=ile_razy_z+1
        kwota = kwota - z
    elif kwota>=y:
        ile_razy_y = ile_razy_y +1
        kwota = kwota - y
    elif kwota>=x:
        ile_razy_x = ile_razy_x +1
        kwota = kwota - x
        break

print(f"5zł - {ile_razy_z}, 2zł - {ile_razy_y}, 1zł - {ile_razy_x} ")