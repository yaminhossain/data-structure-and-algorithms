import math
n = int(input("Enter a number: "))

def armstrong_number(n):
    armstrong_addition=0
    temp= n
    # getting the total number of digits in a number
    if n!=0:
        total_digits= int(math.log10(n)+1)
    else:
        return True
    
    while n !=0:
        extracted_number = int(math.fmod(n,10))
        n= int(n/10)
        armstrong_addition +=math.pow(extracted_number,total_digits)
        
    return int(armstrong_addition) == temp


print("Is the number a armstrong number:",armstrong_number(n))
