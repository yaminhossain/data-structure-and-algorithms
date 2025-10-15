def get_max(nums):
    count=0
    max=0
    for i in range(len(nums)):
        if (nums[i]==1):
            count +=1
            if(count>max):
                max = count
        else: count=0
    return max

nums=[1,1,0,1,1,1]
res = get_max(nums)

print(res)

# Time complexity: TC = O(n)
# Space complexity: SC = O(1)