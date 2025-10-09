arr =[]
n=int(input("Enter the length of the array: "))

for i in range(n):
    arr.append(int(input("")))

largest_element= arr[0]

for i in range(n):
    if (arr[i]>largest_element):
        largest_element = arr[i]

print("Largest element is: ", largest_element)

