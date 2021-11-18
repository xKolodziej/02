nums= [5,1,9,6,1]
maximum = nums[0]
minimum=nums[0]
for i in nums:
    if maximum<i:
        maximum=i
    else:
        maximum=maximum
    if minimum>i:
        minimum=i
    else:
        minimum= minimum
print(nums)
result = maximum - minimum
print(f"Result: {result}")