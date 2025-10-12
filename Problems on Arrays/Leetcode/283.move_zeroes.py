#Two pointers solution

def move_zeros(nums):
    j=-1
    for i in range(int(len(nums))):
        if(nums[i]==0):
            j=i
            break
    if(j==-1):
        return nums
    for i in range(j+1, int(len(nums))):
        if(nums[i]!=0):
            temp = nums[j]
            nums[j]=nums[i]
            nums[i]=temp
            j +=1
    return nums


nums=[1,0,2,3,2,0,0,4,5,1]
result=move_zeros(nums)
print(result)

#Time complexity: Tc = O(x)+O(n-x) = O(n)
#Space complexity: SC= O(1), as no extra arrays are being used.