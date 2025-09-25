""" This program is written using the functional way for recursion. 
Which means recursive function termination do not depend on parameters """

n = int(input("Enter a number\n"))
print("-----------------------------------")

def sum(n):
    if (n == 0):
        return 0
    return n+sum(n-1)

print("Sum: ",sum(n))
