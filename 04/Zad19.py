def check():
    minimum= int(input("Enter minimum range: "))
    maximum= int(input("Enter maximum range: "))
    x = int(input("Enter your number: "))
    if x>=minimum and x<=maximum:
        return True
    else:
        return False
print(check())
    
    
    
