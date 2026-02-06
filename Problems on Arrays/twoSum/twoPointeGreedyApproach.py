# This problem is slightly different from the LeetCode problem as LeetCode problem wants to return array of indices where here wants to return True or False

def getTwoSum(nums, target):
    nums.sort()
    left,right=0, len(nums)-1
    while(left<right):
        sum = nums[left]+nums[right]
        if (sum>target):
            right-=1
        elif (sum<target):
            left+=1
        # (sum == target)
        else:
            return True
    return False

nums = [3,2,4]
target = 6
res = getTwoSum(nums,target)
print(res)