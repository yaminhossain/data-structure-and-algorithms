def frequentElements(nums, k):
    frequency={}
    temp=[]
    for i in range(len(nums)):
        frequency[nums[i]] = 1+frequency.get(nums[i],0)
    for key in frequency:
        temp.append(frequency[key])
    temp.sort(reverse=True)
    temp[0:k]
    print(temp)
    return True

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

res = frequentElements(nums, k)
print(res)