def getTwoSum(nums,target):
    hashMap={}
    for i in range(len(nums)):
        complement = target-nums[i]
        if (complement in hashMap):
            return [i, hashMap[complement]]
        hashMap[nums[i]]=i
    return []


nums = [2,7,11,15]
target = 9
res = getTwoSum(nums,target)
print(res)