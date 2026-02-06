
def frequentElem( nums, k):
    elemDict = {}
    for num in nums:
        if num in elemDict:
            elemDict[num] +=1
        else:
            elemDict[num] = 1
    
    temp=[]
    for number,count in elemDict.items():
        temp.append([count, number])
    temp.sort(reverse=1)
    
    result=[]
    for i in range(k):
        result.append(temp[i][1])
    return result


nums = [1,1,1,2,2,3,3,3]
k = 2
result = frequentElem( nums, k)
print(result)