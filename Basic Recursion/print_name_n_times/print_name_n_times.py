n=int(input("How many times you want to print?\n"))

def print_name(i,n):
    if (i>n):
        return
    print("i: ", i, ",", "n: ", n)
    print_name(i+1,n)
    print("Yamin")

print_name(1,n)