def linear_search(arr,key):
    for i in range(int(len(arr))-1):
        if(arr[i]==key):
            return True
    return False

def union_of_arrays(a, b):
    union_array=[]
    i=0
    j=0
    a_size = int(len(a))
    b_size = int(len(b))
    while(i<a_size and j<b_size):
        if(a[i]<=b[j]):
            # negative indexing [-1] will not work on empty array. So we have to check the size for the first time.
            if(int(len(union_array))==0 or union_array[-1] != a[i]): 
                union_array.append(a[i])
            i+=1
        else:
            # negative indexing [-1] will not work on empty array. So we have to check the size for the first time.
            if(int(len(union_array))==0 or union_array[-1] != b[j]):
                union_array.append(b[j])
            j+=1
    #If array b exhaust and no index left for iteration still a array has some elements left. Add remaining elements of a.
    while(i<a_size):
            # negative indexing [-1] will not work on empty array. So we have to check the size for the first time.
            if(int(len(union_array))==0 or union_array[-1] != a[i]):
                union_array.append(a[i])
            i+=1
    #If array a exhaust and no index left for iteration still b array has some elements left. Add remaining elements of b.
    while(j<b_size):
            # negative indexing[-1] will not work on empty array. So we have to check the size for the first time.
            if(int(len(union_array))==0 or union_array[-1] != b[j]):
                union_array.append(b[j])
            j+=1
    return union_array


# a=[1,1,2,3,4,5]
# b=[2,3,4,4,5,6]
a=[6]
b=[3,4]

result = union_of_arrays(a,b)
print(result)