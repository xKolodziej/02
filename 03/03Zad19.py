ludzkie_lata = input("Podaj ilosc lat ludzkich: ")
ludzkie_lata = int(ludzkie_lata )
wiek_psa=0


while(ludzkie_lata>0):
    if ludzkie_lata >= 3:
        ludzkie_lata = ludzkie_lata-1
        wiek_psa = wiek_psa+4
    elif ludzkie_lata <= 2:
        ludzkie_lata = ludzkie_lata-1
        wiek_psa = wiek_psa+10.5
    elif ludzkie_lata <= 1:
        ludzkie_lata = ludzkie_lata-1
        wiek_psa = wiek_psa+10.5
        break
    
print(f"Wiek psa w latach psa wynosi: {int(wiek_psa)} lata") 