def power(x,n):
    if n==0:
        return 1
    if n>=1:
        return x*power(x,n-1)
x=6
n=3
print(f"Result: {power(x,n)}")
    