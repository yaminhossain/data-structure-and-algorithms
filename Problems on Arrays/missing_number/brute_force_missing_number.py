# Brute Force: This solution is provided by using Linear search
def missing_number(arr):
    arr_len = int(len(arr))
    for i in range(arr_len+1):
        res=False
        for j in range(arr_len):
            if(i == arr[j]):
                res = True
                break
        if(res==False): return i

# arr=[3,0,1]
# arr = [0,1]
arr=[9,6,4,2,3,5,7,0,1]
res= missing_number(arr)
print(res)

# Time complexity: O(n^2) in worst case
# Space complexity: O(1) because we are not using any extra space