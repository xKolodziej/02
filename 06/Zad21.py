def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
       
array = [5,1,9,6,1]
print(array)
bubblesort(array)
result = array[len(array)-2]
print(f"Result: {result}")