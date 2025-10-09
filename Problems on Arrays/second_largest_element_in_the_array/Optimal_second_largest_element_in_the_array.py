#    0 1 2 3 4 5
arr=[1,2,4,7,7,5]
# Assuming largest element is the first element of the array
largest_element= arr[0]
# Assuming there is no negative values in the array. If the array may contain negative values, then a large negative value should be taken instead
second_largest_element= -1 

for i in range(int(len(arr))):
    if (arr[i]> largest_element):
        second_largest_element = largest_element
        largest_element = arr[i]
    #The problem is with the last element 5. Where 5 is smaller than 7 and also greater than 4 which makes 5 as second largest element.
    elif (arr[i]<largest_element and arr[i]>second_largest_element): 
        second_largest_element = arr[i]

print("The second largest element is: ",second_largest_element)

#Time complexity : O(n)
