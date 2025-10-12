# This is the Brute Force approach

def get_intersection(a,b):
    a_len = int(len(a))
    b_len = int(len(b))
    visit=[0]*(b_len-1)
    intersect=[]
    for i in range(a_len):
        for j in range(b_len):
            if(a[i]==b[j] and visit[j]==0):
                intersect.append(a[i])
                visit[j] +=1
                break
            if(a[i]<b[j]): break
    return intersect


arr1=[1,2,2,3,3,4,5,6]
arr2=[2,3,3,5,6,7]

result = get_intersection(arr1, arr2)
print(result)

# Time complexity: O(n1*n2),n1 for array 1 and n2 for array 2
# Space Complexity: O(n2),because we are taking the size of visit as per second array which is smaller than first array