# This solution utilizes the summation of n natural number: (n*(n+1))/2

def getMissingNumber(nums):
    numsLen = len(nums)
    sumAllNumber= (numsLen * (numsLen+1))//2 #ignoring 0 as it has no visible consequences
    sumArrNums=0
    for i in range(numsLen):
        sumArrNums = sumArrNums + nums[i]
    return sumAllNumber - sumArrNums

nums = [9,6,4,2,3,5,7,0,1]
res = getMissingNumber(nums)
print(res)

# Time Complexity: O(n)
# Space Complexity: O(1)