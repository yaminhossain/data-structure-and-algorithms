def linear_search(arr,key):
    for i in range(int(len(arr))-1):
        if(arr[i]==key):
            return i
    return -1

arr=[6,7,8,4,1]
key=5

result = linear_search(arr,key)
print("The value is in index: ",result)