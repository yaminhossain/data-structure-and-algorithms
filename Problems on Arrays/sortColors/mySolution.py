def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def getSortedColors(nums):
    while(isSorted(nums) == False and len(nums)>1):
        for i in range(len(nums)-1):
            if (nums[i]> nums[i+1]):
                nums[i],nums[i+1]= nums[i+1], nums[i]
    return nums

# nums = [2,0,2,1,1,0]
# nums = [1,2,3]
nums=[1]
res = getSortedColors(nums)
print("Result: ",res)