def checkArraySortedAndRotated(nums):
    N = len(nums)
    count=1
    if(N==1): 
        return True
    for i in range(1,2*N):
        if( nums[(i-1)%N] <= nums[i %N]):
            count +=1
        else:
            count = 1
        if(count==N):
            return True
    return False
    
    
nums = [3,4,5,1,2]
res=checkArraySortedAndRotated(nums)
print(res)