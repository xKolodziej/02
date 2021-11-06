import time
x=0
y=1
suma=x+y
print("Fibonacci sequence: ")
while True:
    time.sleep(1)  
    print(suma)
    suma=x+y
    x=y
    y=suma
    