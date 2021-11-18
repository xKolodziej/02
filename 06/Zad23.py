import statistics
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    
array = [6,8,3,1,0,5,7]
print(array)
bubblesort(array)
print(statistics.median(array))
        