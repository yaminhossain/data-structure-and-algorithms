def left_rotate(arr):
    temp = arr[0]
    for i in range(1,int(len(arr))):
        arr[i-1] = arr[i]
    arr[int(len(arr)) - 1]= temp
    return arr

arr=[1,2,3,4,5]
rotatedArray = left_rotate(arr)
print(rotatedArray)