
def missingNumber(nums):
    res = len(nums)
    for i in range(len(nums)):
        res+= i - nums[i]
    return res
arr=[9,6,4,2,3,5,7,0,1]
res= missingNumber(arr)
print(res)