""" 
GCD = Greatest Common Divisor
HCF = Highest Common Factors
GCD can be calculated using euclidean algorithm an this provides the optimal solution.
"""
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

def gcd_calculator(a,b):
    a, b = abs(a), abs(b)   # make sure we only deal with non-negative values
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for both numbers being zero.")
    
    while (a>0 and b>0):
        if (a>b):
            a = a%b
        else:
            b = b%a
    if (a==0):
        return b
    else:
        return a

gcd=gcd_calculator(a, b)

print("GCS: ",gcd)