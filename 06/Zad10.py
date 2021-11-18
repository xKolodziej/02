array=[4,3,7,1,3]
def array2str(array):
    for i in array:
        print(i, end=" ")
array2str(array)
print()
def suma(array):
    suma=0
    for i in array:
        suma=suma+i
    return suma
print(f"Sum of values: {suma(array)}")
    