def return_string(array):
    print (', '.join(map(str, array)))
    
    
array = [5,4,3,2,6,5]
print(f"Array: {array}")
print("String: ", end="")
return_string(array)