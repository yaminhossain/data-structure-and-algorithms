def subArraySum(nums, givenSum):
    currSum,count = 0,0
    preSumMap={0:1}
    for i in range(len(nums)):
        currSum += nums[i] 
        diff = currSum - givenSum
        # count += prefixSums.get(diff,0)
        if diff in preSumMap:
            count += preSumMap[diff]
        # prefixSums[curSum]= 1 + prefixSums.get(curSum,0)
        if currSum in preSumMap:
            preSumMap[currSum] += 1
        else:
            preSumMap[currSum] = 1
    return count

nums = [0,0,0]
k=0
res = subArraySum(nums, k)
print("Count :", res)




# =======================My Solution=============================================
# def getSubArraySum(nums,givenSum):
#     sum = 0
#     count = 0
#     prefixSums={}
#     for i in range(len(nums)):
#         sum +=nums[i]
#         if(sum == givenSum):
#             count +=1
#         remaining = sum - givenSum
#         for key in prefixSums:
#             if (prefixSums[key] == remaining):
#                 count+=1
#         prefixSums[i]=sum
#     return count

# nums = [0,0,0]
# k = 0
# res=getSubArraySum(nums, k)
# print(res)

