# This solution works with every condition. If the array contains negative and zeros, it will also work

def getLongestSubArray(arr,givenSum):
    lenOfSubArray=0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum=0
            for k in range(i, j+1):
                sum +=arr[k]
            if(sum==givenSum and j-i+1> lenOfSubArray):
                lenOfSubArray = j-i+1
    return lenOfSubArray

arr=[1,2,3]
k=3
res = getLongestSubArray(arr,k)
print(res)

# Time complexity: O(n^3)
# Space complexity: O(1)