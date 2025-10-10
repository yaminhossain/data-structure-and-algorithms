def reverse(arr, start, end):
    while (start<end):
        temp = arr[start]
        arr[start]= arr[end]
        arr[end]= temp
        start +=1
        end -=1

def leftRotate(arr,d):
    reverse(arr, 0, d-1)
    reverse(arr, d, int(len(arr))-1)
    reverse(arr, 0, int(len(arr))-1)
    return arr

arr=[1,2,3,4,5,6]
d=3
rotatedArray = leftRotate(arr,d)
print(rotatedArray)