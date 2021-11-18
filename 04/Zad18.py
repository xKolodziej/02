def suma(a):
   s=0
   while a>0:
       
       s=s+a%10
       a= int(a/10)
   return s
a=int(input("Enter number: "))
print(f"Sum is: {suma(a)}")
       
