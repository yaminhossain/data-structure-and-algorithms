import math

n=int(input("Enter an integer number: "))

def prime_number(n):    
    count=0
    #condition: for(int i=1; i<=sqrt(n), i++)
    for i in range(1, int(math.sqrt(n))+1):
        if (int(n%i)==0):
            count+=1
            if (n//i!=i):
                count+=1
    return count

count = prime_number(n)
if (count==2):
    print(True)
else:
    print(False)
    
#Time complexity: O(sqrt of n)