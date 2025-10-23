# This solution works with every condition. If the array contains negative and zeros, it will also work
def getLongestSubArray(arr,givenSum):
    lenOfSubArr=0
    for i in range(len(arr)):
        sum=0
        for j in range(i, len(arr)):
            sum+=arr[j]
            if(sum == givenSum):
                lenOfSubArr=max(lenOfSubArr,j-i+1)
    return lenOfSubArr
arr=[1,2,3,1,1,1,1,4,2,3]
k=3
res = getLongestSubArray(arr,k)
print(res)

# Time complexity: O(n^2)
# Space complexity: O(1)