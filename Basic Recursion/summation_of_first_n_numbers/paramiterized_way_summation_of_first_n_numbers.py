""" This program is written using the parameterized way for recursion. 
Which means recursive function termination depends on parameters """

""" n = int(input("Enter a number\n"))
print("-----------------------------------")

def sum (i, n):
    if(i>n):
        return 0
    return i+sum(i+1,n)
sum=sum(1,n)
print("Sum: ",sum) """

#Alternative-1

""" n = int(input("Enter a number\n"))
print("-----------------------------------")

def sum_tail(i, n, acc):
    if i > n:
        return acc
    return sum_tail(i+1, n, acc+i)

result = sum_tail(1, n, 0)
print("Sum:", result)
"""

# Alternative-2

n = int(input("Enter a number\n"))
print("-----------------------------------")

def sum_param(i, n, current_sum):
    if i > n:
        print("Sum:", current_sum)
        return
    sum_param(i+1, n, current_sum+i)

sum_param(1, n, 0)

# Another alternative could be setting a counter variable at the top of the function like counter =0, then increase the value on each loop.