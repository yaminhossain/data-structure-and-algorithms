def getTwoSum(nums, target):
    nums.sort()
    left,right=0, len(nums)-1
    while(left<right):
        sum = nums[left]+nums[right]
        if (sum>target):
            right-=1
        elif (sum<target):
            left+=1
        # (sum == target)
        else:
            return [left,right]

nums = [3,2,4]
target = 6
res = getTwoSum(nums,target)
print(res)