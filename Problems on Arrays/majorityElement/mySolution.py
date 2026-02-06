# This solution is wrong in as sense that this algorithm is getting the most frequent element to determine the majority element.
# But majority element and most frequent element are not the same this.
# Majority element is the element which occurs more than n/2 times where n = size of the array.
# See the brute force solution for the correct answer
def majorityElement(nums):
    majorityMap={}
    for i in range(len(nums)):
        if (nums[i] in majorityMap):
            majorityMap[nums[i]] += 1
        else:
            majorityMap[nums[i]] = 1
    
    maxElem=0
    count=0
    for elem in majorityMap:
        if (majorityMap[elem]>count):
            count = majorityMap[elem]
            maxElem = elem
    return maxElem

nums = [-42]
res = majorityElement(nums)
print("Result:", res)