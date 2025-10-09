import math

#    0 1 2 3 4 5
arr = [3,1,1,2]

# Assuming smallest element is the first element of the array
smallest= arr[0]

#Assuming array can have 10^9 as max element
second_smallest = math.pow(10,6)

for i in range(int(len(arr))):
    if (arr[i]< smallest):
        second_smallest = smallest
        smallest = arr[i]
    # elif (arr[i]>smallest and arr[i] < second_smallest):
    elif (arr[i]!=smallest and arr[i] < second_smallest):
        second_smallest = arr[i]

print("Smallest: ",smallest)
print("Second smallest number is: ", second_smallest)