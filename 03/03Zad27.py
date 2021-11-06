'''
for i in range(6,-1,-3):
    for j in range(1,4):
        print(f' {i+j}',end='')
    print()
'''
i=6
j=1
while i<=6 and i>=-1:
    while j>=1 and j<=3:
        print(f' {i+j}',end='')
        j=j+1
    print()
    i=i-3
    j=1