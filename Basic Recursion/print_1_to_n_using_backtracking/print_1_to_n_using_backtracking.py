n = int(input("How many times?\n"))
print("-----------------------------------")

def print_1_to_n_with_backtracking(n):
    if(n<1):
        return
    print_1_to_n_with_backtracking(n-1)
    print(n)

print_1_to_n_with_backtracking(n)