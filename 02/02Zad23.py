kwota = input("Podaj kwote produktu: ")
kwota = float(kwota)
vat = round(kwota *0.23, 2)

print(f"Cena to {kwota}, a podatek VAT to: {vat}")