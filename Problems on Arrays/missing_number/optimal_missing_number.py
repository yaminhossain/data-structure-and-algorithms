# This solution utilizes the indices of each element.
#For better understanding, check youtube

def missingNumber(nums):
    res = len(nums)
    for i in range(len(nums)):
        res+= i - nums[i]
    return res
arr=[9,6,4,2,3,5,7,0,1]
res= missingNumber(arr)
print(res)

#Time complexity: O(n)
# Space complexity: O(1) // As no extra spaces are being used