x= input("Podaj wspołrzedna x: ")
y= input("Podaj wspołrzedna y: ")
x = int(x)
y = int(y)

if x>0 and y>0:
    print(f"Punkt P({x},{y}), znajduje sie w pierwszym kwadrancie układu współrzędnych")
    
elif x<0 and y>0:
    print(f"Punkt P({x},{y}), znajduje sie w drugim kwadrancie układu współrzędnych")
elif x<0 and y<0:
    print(f"Punkt P({x},{y}), znajduje sie w trzecim kwadrancie układu współrzędnych")    
elif x>0 and y<0:
    print(f"Punkt P({x},{y}), znajduje sie w czwartym kwadrancie układu współrzędnych")    
    