def check_sorted(arr):
    for i in range(int(len(arr))-1):
        print(i)
        if (arr[i] > arr[i+1]):
            return False
        else: 
            return True
# arr=[1,2,2,3,3,4]
# arr=[1,2,3,5]
arr = [3,1,4,2,1]
result =check_sorted(arr)
print(result)