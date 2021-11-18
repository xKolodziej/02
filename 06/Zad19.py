
array = [2,3,2,5,8,1,9,8]
print("Array:", end = " ")
for i in array:
    print(i, end=" ")
   
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]       
bubblesort(array)
def RemoveDuplicates(array):
    i = 0
    while i < len(array):
        cur = array[i]         
        cnt = 0
        while i < len(array) and cur == array[i]:
            cnt += 1
            i += 1
        if cnt == 1:
            print(cur, end=" ")
print()
print("Unique elements: ", end="")
RemoveDuplicates(array)
    
        
    