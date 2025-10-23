# This solution works with every condition. If the array contains negative and zeros, it will also work
def getLongestSubArray(arr,givenSum):
    lenOfSubArr=0
    sum=0
    i,j=0,0
    while(j<len(arr)):
        sum +=arr[j]
        while(sum>givenSum and i<=j):
            sum -= arr[i]
            i+=1
        if(sum==givenSum):
            lenOfSubArr=max(lenOfSubArr, j-i+1)
        j+=1
    return lenOfSubArr
# arr=[1,0,2,0,3]
arr=[1,1,1,1]
# k=3
k=2
# res = getLongestSubArray(arr,k)
# print(res)
# ========================================================================================================
# def getLongestSubArray(arr,givenSum):
#     left,right=0,0 #right=j and left = i
#     sum = arr[0]
#     maxLen = 0
#     n = len(arr)
#     while(right<n):
#         while(left<=right and sum>givenSum):
#             sum -= arr[left]
#             left +=1
#         if(sum==givenSum):
#             maxLen = max(maxLen, right-left+1)
#         right+=1
#         if(right<n):
#             sum+=arr[right]
#     return maxLen

# arr=[1,2,3,1,1,1,1,3,3]
# arr=[1,0,2,0,3]
# arr=[1,1,1,1]
# k=6
# k=3
# k=2
res = getLongestSubArray(arr,k)
print(res)

# Time complexity: O(n^2)
# Space complexity: O(1)