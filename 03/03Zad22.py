
for i in range(1,31):
    if i%3==0 and i%5==0:
        print("BINGO")
    elif i%3==0:
        print("TRZY")
    elif i%5==0:
        print("PIĘĆ")
    else:
        print(i)