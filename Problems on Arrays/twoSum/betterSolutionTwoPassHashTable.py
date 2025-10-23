def getTwoSum(nums,target):
    hashMap={}
    for i in range(len(nums)):
        hashMap[nums[i]]=i
    print(hashMap)
    
    for i in range(len(nums)):
        complement = target-nums[i]
        if (complement in hashMap) and (hashMap[complement] != i):
            return [i,hashMap[complement]]
    return []


nums = [2,7,11,15]
target = 9
res = getTwoSum(nums,target)
print(res)