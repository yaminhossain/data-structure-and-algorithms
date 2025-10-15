#Better solution: Using Array Hash

def getSingleNumber(nums):
    # Get the maximum value to set the size of hash array
    maxElem = -1
    for i in range(len(nums)):
        maxElem = max(maxElem,nums[i])

    #Initializing hash arrays with 0s
    hashArray=[0]*(maxElem+1)

    for i in range(maxElem+1): 
        hashArray[nums[i]] +=1
    
    # Getting element from the hash array
    for i in range(1, len(hashArray)):
        if(hashArray[i] == 1): return i

nums = [4,1,2,1,2]
res=getSingleNumber(nums)
print(res)

# Time complexity: O(n) + O(n) + O(n) = O(3n) // maxElement + Hashing + Getting data from hashing
# Space complexity: O(n) // For extra hash array
