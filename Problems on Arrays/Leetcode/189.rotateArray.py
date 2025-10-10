def reverse(arr, start, end):
    while (start<end):
        temp = arr[start]
        arr[start]= arr[end]
        arr[end]= temp
        start +=1
        end -=1

def rightRotate(arr, k):
    lastIndex = int(len(arr))-1
    # Must check total number of rotations otherwise if k>size than it will not behave accordingly
    k=int(k%int(len(arr))) 
    reverse(arr, 0, lastIndex-k)
    reverse(arr, lastIndex-k+1,lastIndex)
    reverse(arr, 0, lastIndex)


arr =[1,2,3,4,5,6]
result = rightRotate(arr,3)
print(result)