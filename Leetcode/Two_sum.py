nums=[1,2,3,4,3,2]
target=6
for i in range(len(nums)):
    for j in range(len(nums)):
        if (i!=j and nums[i]+nums[j]==target):
            print(i,j)