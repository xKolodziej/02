names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest=names[0]
print("Names: ", end="")
for i in names:
    print(i, end=" ")
print()
print("Longest name: ", end="")
for i in names:
    if len(longest)<len(i):
        longest=i
    else:
        longest=longest
print(longest)
    