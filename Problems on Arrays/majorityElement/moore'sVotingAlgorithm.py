def majorityElement(nums):
    element = None
    count = 0
    for i in range(len(nums)):
        if(count==0):
            element = nums[i]
            count = 1
        elif(element == nums[i]):
            count +=1
        else:
            count-=1
    
    # Extra Checking: If it is not guaranteed to have a majority element
    majorityCount=0
    for i in range(len(nums)):
        if(nums[i]==element):
            majorityCount+=1
    if(majorityCount>len(nums)//2):
        return element
    else:
        return -1


nums = [2,2,1,1,1,2]
res = majorityElement(nums)
print(res)