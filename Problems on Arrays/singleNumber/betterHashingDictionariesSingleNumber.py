# Better solution: This solution utilizes python dictionaries or hash map

def getSingleNumber(nums):
    myDict={}
    for i in range(len(nums)):
        # Python does not return null like JavaScript if there is a key does not exist. It will throw an error instead.
        if(nums[i] not in myDict):
            myDict[nums[i]] =1
        else: myDict[nums[i]] +=1
    
    for i in myDict:
        if(myDict[i]==1):
            return i

nums = [4,1,2,1,2]
res=getSingleNumber(nums)
print(res)

# Time complexity: O(nlogN) + O(N/2 + 1) // If we use ordered map nlogN, or for unordered map it will be O(n)
# Space complexity: O(N/2 + 1)
