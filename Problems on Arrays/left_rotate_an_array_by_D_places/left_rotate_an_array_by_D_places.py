#D is the given number. It can be any number.
# There is another brute force solution to it using an extra array space.

def left_rotate_d_places(d, arr):
    for i in range(int(d)):
        temp = arr[0]
        for i in range(1,int(len(arr))):
            arr[i-1]=arr[i]
        arr[int(len(arr))-1]= temp
    return arr

arr = [1,2,3,4,5,6,7]
rotated_array= left_rotate_d_places(3, arr)
print(rotated_array)