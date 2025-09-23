n = int(input("Enter a number:"))

for i in range(n):
    if n%(i+1) ==0:
        print(i+1)

#Time complexity is O(n)