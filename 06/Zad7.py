nums= [12,8,31,48,2,19]
even=0
odd=0
for i in nums:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(F"Amount of even numbers: {even}")
print(F"Amount of odd numbers: {odd}")