def getTwoSum(nums,target):
    res=[]
    for i in range(len(nums)):        
        j=0
        while(j != i and j<len(nums)):
            sum = nums[i]+nums[j]
            if(sum==target):
                res.append(i)
                res.append(j)
            j+=1
    return res

# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6
res = getTwoSum(nums,target)
print(res)