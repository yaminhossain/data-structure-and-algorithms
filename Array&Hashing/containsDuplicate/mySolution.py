def getDuplicate(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i] == nums[j] and i !=j):
                return True
    return False

nums = [1,2,3,4]
res = getDuplicate(nums)
print(res)