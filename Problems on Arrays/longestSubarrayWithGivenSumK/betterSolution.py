# This solution works with every condition. If the array contains negative and zeros, it will also work
def getLongestSubArray(arr,givenSum):
    preSumMap={}
    sum =0
    subArrLength=0
    for i in range (len(arr)):
        sum += arr[i]
        if(sum==givenSum):
            if(i+1>subArrLength):
                subArrLength=i+1
        # sum = x, given sum = k, remaining sum = x-k
        remainingSum = sum - givenSum
        if(remainingSum in preSumMap):
            subArrLength = max(subArrLength, i - preSumMap[remainingSum])
        
        if(sum not in preSumMap):
            preSumMap[sum]=i
    return subArrLength

arr=[1,2,3,1,1,1,1,4,2,3]
k=3
res = getLongestSubArray(arr,k)
print(res)

# Time complexity: O(n)
# Space complexity: O(n)