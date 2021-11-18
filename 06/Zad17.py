nums1 = [4,36,12,28,9,44,5]
nums2 = [5,1,36]
x = len(nums1)
y = len(nums2)

if nums1 == nums2:
    print("Arrays are the same")
else:
    for i in range(x):
        for j in range(y):
            if nums1[i]==nums2[j]:
                break
        if (j ==  y- 1):
            print(nums1[i], end = " ")
            

