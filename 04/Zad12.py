def suma(n):
    if n==0:
        return 0
    
    if n>=0:
        return n+suma(n-1)
        
x=10
print(f"Suma: {suma(x)} ")


        