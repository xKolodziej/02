def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
       
array = [6,4,22,11,2]
bubblesort(array)
print(array)