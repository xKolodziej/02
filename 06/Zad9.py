def month(n):
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[n-1]
n = int(input("Enter the number of month: "))
print(month(n))