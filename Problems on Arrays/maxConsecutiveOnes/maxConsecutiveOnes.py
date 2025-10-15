def get_max(arr):
    temp =[]
    count=0
    for i in range(len(arr)):
        if(arr[i]==1):
            count+=1
            temp.append(count)
        else:
            count=0
    max=-1
    for i in range(len(temp)):
        if(temp[i]>max):
            max=temp[i]
    return max

nums = [1,0,1,1,0,1]

res = get_max(nums)
print(res)