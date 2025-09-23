import math

n = int(input("Enter a number: "))

def print_all_divisors(n):
    a=[]
    for i in range(int(math.sqrt(n))):
        if(int(math.fmod(n,i+1))==0):
            a.append(int(i+1))
            if (n//(i+1) !=i+1):
                a.append(int(n/(i+1)))
    a.sort()
    for num in a:
        print(num)

print_all_divisors(n)
# Time complexity O(sqrt of n)