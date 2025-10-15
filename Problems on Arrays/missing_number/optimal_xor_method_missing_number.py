# This solution utilizes xor operation. The solution in here is most optimized using xor.

def getMissingNumber(nums):
    xorAllNumbers=0
    xorArrNumbers=0
    for i in range(len(nums)):
        xorArrNumbers ^= nums[i]
        xorAllNumbers ^= i
    return xorAllNumbers ^ xorArrNumbers ^ len(nums)


nums=[9,6,4,2,3,5,7,0,1]
res = getMissingNumber(nums)
print(res)

# Time complexity: TC = O(n)
# Space Complexity: SC = O(1)