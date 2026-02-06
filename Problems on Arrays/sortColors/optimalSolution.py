# This solution uses Dutch National Flag algorithm by utilizing 3 pointers.
def sortedArray(nums):
    # swap function
    def swap(i, j): # No need to pass the array as the swap function is inside the sortedArray function and has access to the array.
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    # Three pointers
    low , mid, high = 0, 0, len(nums)-1 #low = left, mid = i, high = right
    while(mid <= high):
        if (nums[mid] == 0):
            swap(low, mid)
            low +=1
            mid +=1
        elif (nums[mid]==2):
            swap(high, mid)
            high -=1
        else: #(nums[mid] == 1)
            mid +=1

nums = [2,0,2,1,1,0]
sortedArray(nums)
print(nums)