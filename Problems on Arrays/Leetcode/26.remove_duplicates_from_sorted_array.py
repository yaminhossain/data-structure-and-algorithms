#Two pointers solution
def remove_duplicates(nums):
    i = 0
    for j in range(1, int(len(nums))):
        if(nums[j] != nums[i]):
            nums[i+1]=nums[j]
            i +=1
    return i+1

nums = [1,1,2]
k= remove_duplicates(nums)
print("Result: ", k)

#Time complexity: TC = O(n)
#Space complexity: SC = O(1)