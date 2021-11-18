
def compare(n,nums):
    greater =0
    for i in nums:
        if n>i:
            greater = greater+1
    print(f"Number of elements that are greater than your number: {greater}")
            
    
    
    
    
n=int(input("Enter the number: "))
nums = [7,3,5,12,4]
compare(n,nums)    