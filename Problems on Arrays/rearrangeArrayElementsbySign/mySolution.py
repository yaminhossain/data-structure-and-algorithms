
def rearrange(nums):
    temp=[]
    res=[]
    n = len(nums)
    for i in range(n):
        if(nums[i]>0):
            temp.append(nums[i])
    for i in range(n):
        if(nums[i]<0):
            temp.append(nums[i])
    L=0
    R = n//2
    while(L < n//2):
        res.append(temp[L])
        res.append(temp[R])
        L+=1
        R+=1
    return res
nums = [3,1,-2,-5,2,-4]
res= rearrange(nums)
print(res)