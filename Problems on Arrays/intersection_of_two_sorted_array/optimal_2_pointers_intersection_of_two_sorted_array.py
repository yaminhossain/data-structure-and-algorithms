# This is the optimal solution using two pointers approach

def get_intersection(a,b):
    a_len = int(len(a))
    b_len = int(len(b))
    intersect=[]
    i=0
    j=0
    while(i<a_len and j<b_len):
        if(a[i] < b[j]): i+=1
        elif(b[j] < a[i]): j+=1
        else:
            intersect.append(a[i])
            i+=1
            j+=1
    return intersect

arr1=[1,2,2,3,4,5,6]
arr2=[2,3,3,5,6,7]

# arr1=[2,5,6]
# arr2=[2,5,6,6]

result = get_intersection(arr1, arr2)
print(result)

# Time complexity: O(n1+n2)
# Space Complexity: O(1) // As no extra space is using