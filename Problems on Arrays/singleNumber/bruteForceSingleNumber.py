#Brute Force solution: Using linear Search
def getSingleNumber(nums):
    for i in range(len(nums)):
        count =0
        for j in range(len(nums)):
            if(nums[i]==nums[j]):
                count +=1
        if (count == 1):
            return nums[i]

nums = [5,4,2,1,2,3,5,3]
res=getSingleNumber(nums)
print(res)

# Time complexity= O(n^2), Think about 4 at the last place. Although 5, 2, 3 already checked for the fist time but it will again be checked.
# Space complexity = O(1)