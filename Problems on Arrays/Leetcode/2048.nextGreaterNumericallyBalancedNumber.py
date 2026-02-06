def nextGreaterNumericalBalancedNumber(n):
    for i in range(n+1, 1224444):
        temp = i
        countMap={}
        while(i !=0):
            digit = i % 10
            if digit in countMap:
                countMap[digit] +=1
            else:
                countMap[digit] = 1
            i = i//10
        res=False
        for key in countMap:
            if(key != countMap[key]):
                res= False
                break
            else:
                res = True
        if res == True: return temp
n=122
res = nextGreaterNumericalBalancedNumber(n)
print(res)