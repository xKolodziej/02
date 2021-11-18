array1=["water","book","sky"]
array2=["water","book","sky"] 
def compare(array1,array2):
    print("Array1: ", end="")
    for i in array1:
        print(i, end=" ")
    print()
    print("Array2: ", end="")
    for j in array2:
        print(j, end=" ")
    print()
    
    if array1==array2:
        print("Arrays are the same")
        return True
    else:
        print("Arrays are not the same")
        return False
print(compare(array1,array2))
