def getLongestSubArray(arr,givenSum):
    lenOfSubArr=0
    sum=0
    i,j=0,0
    while(j<len(arr)):
        sum +=arr[j]
        while(sum>givenSum and i<=j):
            sum -= arr[i]
            if(sum==givenSum):
                lenOfSubArr=max(lenOfSubArr, j-i+1)
            i+=1
        if(sum==givenSum):
            lenOfSubArr=max(lenOfSubArr, j-i+1)
        j+=1
    return lenOfSubArr
arr=[1,2,3,1,1,1,1,3,3]
k=6
res = getLongestSubArray(arr,k)
print(res)