ilosc = 0
suma = 0
while True:
    x= int(input("Wprowadz liczbe: "))
    if x==0:
        break
    else:
        ilosc =ilosc+1
        suma= suma+x
        srednia= round(suma/ilosc,2)

print(f"Ilosc: {ilosc}, Suma: {suma}, Średnia: {srednia}")