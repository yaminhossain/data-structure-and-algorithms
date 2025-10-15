# Better Solution: This solution will be using ing technique
# Array will contain numbers from 1 to N. Not 0 to N.

def get_missing_number(arr):
    arr_len = len(arr)
    hash_array=[0]*(arr_len+2)
    for i in range(arr_len):
        hash_array[arr[i]]+=1
    print(hash_array)
    for i in range(1,len(hash_array)):
        if(hash_array[i]==0): return i

arr=[1,2,4,5]
res=get_missing_number(arr)
print(res)

# Time complexity: TC = O(n)+O(n) = O(2n) // Time for hashing + time for retrieving data for hash array
# Space complexity: SC = O(n) // As we are using a extra hash array for storing data