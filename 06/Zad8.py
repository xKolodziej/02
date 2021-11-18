nums= [-15, 8, -31, 47, -2, 19]
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
print(maximum)
print(minimum)