def getTwoSum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[j]== target-nums[i]) :
                return [i,j]
    return []
# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
res = getTwoSum(nums, target)
print(res)