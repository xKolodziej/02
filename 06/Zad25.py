array2=[]
def minmax(array):
    maximum = array[0]
    minimum=array[0]
    for i in array:
        if maximum<i:
            maximum=i
        else:
            maximum=maximum
        if minimum>i:
            minimum=i
        else:
            minimum= minimum
    
    array2.extend([minimum,maximum])
    print(f"Result: {array2}")
    
    
    
   
array = [4,2,8,4,7,9,5]
print(f"Array: {array}")

minmax(array)