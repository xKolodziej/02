
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    if j==5:
        for i in range(1,5):
            for j in range(5,i,-1):
                print("*", end = " ")
            print()    
