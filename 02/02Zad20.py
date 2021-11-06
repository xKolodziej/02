wzrost = input("Podaj swoj wzrost w cm: ")
waga = input("Podaj swoja wage w kg: ")

wzrost = int(wzrost)
waga = int(waga)

bmi = round((waga)/(wzrost/100)**2, 1)

if bmi < 18.5:
    print(f"Twoj wskaznik BMI wynosi: {bmi}, a to oznacza ze masz niedowage")
elif bmi>=18.5 and bmi<25:
    print(f"Twoj wskaznik BMI wynosi: {bmi}, a to oznacza ze masz prawidłową wage")
elif bmi>=25 and bmi<30:
    print(f"Twoj wskaznik BMI wynosi: {bmi}, a to oznacza że masz nadwage ")
else:
    print(f"Twoj wskaznik BMI wynosi: {bmi}, a to oznacza ze jesteś chory na otyłość")