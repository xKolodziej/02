odd=[]
even=[]
array2=[]
def evenandodd(array):
    for i in array:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    array2.extend([even,odd])
    print(f"Result: {array2}")
    
    
array=[4,2,8,4,7,9,5]
print(f"Array: {array}")
evenandodd(array)