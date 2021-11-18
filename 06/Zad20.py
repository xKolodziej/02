def occurs(n,array):
    print(F"Number: {n}")
    print("Array:", end=" ")
    
    for i in array:
        print(i, end=" ")
    x= array[0]
    print()
    for i in array:
        
        if n == x:
            print(f"Result: number {n} appears in the array")
            break
        else:
            x=i        
    
    
n=23
array = [15,38,7,23,14]
occurs(n,array)