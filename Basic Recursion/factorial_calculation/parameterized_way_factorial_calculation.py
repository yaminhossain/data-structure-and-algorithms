""" This program is written using the functional way for recursion. 
Which means recursive function termination does not depend on parameters """

""" n = int(input("Enter a number:\n"))
print("-----------------------------------")

def fact(i, n, res):
    if(i>n):
        return res
    return fact(i+1,n,res*i)

result = fact(1,n,1)
print("Result: ",result)
"""

# Alternative solution: With out returning any value. Pure parameterized

n = int(input("Enter a number:\n"))
print("-----------------------------------")

def fact(i, n, res):
    if(i>n):
        print("Result: ",res)
        return
    return fact(i+1,n,res*i)

fact(1,n,1)

