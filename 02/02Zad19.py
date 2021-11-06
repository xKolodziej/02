
a= input("Podaj bok a: ")
b= input("Podaj bok b: ")
c= input("Podaj bok c: ")

a = int(a)
b = int(b)
c = int(c)

p=  (a+b+c)/2

Pole = (p*(p-a)*(p-b)*(p-c))**(1/2)

print(f"Pole jest rowne {int(Pole)}")