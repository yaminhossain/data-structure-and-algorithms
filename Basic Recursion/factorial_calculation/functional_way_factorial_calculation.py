""" This program is written using the functional way for recursion. 
Which means recursive function termination does not depend on parameters """

n = int(input("Enter a number:\n"))
print("-----------------------------------")

def fact(n):
    if (n == 1):
        return 1
    return n*fact(n-1)

print("Factorial of the number",n,"is: ",fact(n))
