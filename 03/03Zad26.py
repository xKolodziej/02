poprawny = '0805'
liczba_prob = 0
pin= input("Wprowadź kod PIN: ")

'''
while True:
    if liczba_prob == 2:
            print("Przepraszamy, Twoja  karta płatnicza  została  zablokowana.")
            break
    if pin != poprawny:
        print("Niepoprawny PIN..")
        liczba_prob = liczba_prob+1
        pin = input("Wprowadź kod PIN: ")
'''
for i in range(3):
    if liczba_prob == 2:
            print("Przepraszamy, Twoja  karta płatnicza  została  zablokowana.")
            break
    if pin != poprawny:
        print("Niepoprawny PIN..")
        liczba_prob = liczba_prob+1
        pin = input("Wprowadź kod PIN: ")