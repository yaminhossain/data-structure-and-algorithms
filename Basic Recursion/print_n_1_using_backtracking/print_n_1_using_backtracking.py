n = int(input("How many times?\n"))
print("-----------------------------------")

def print_n_to_1_with_backtracking(i,n):
    if(i>n):
        return
    print_n_to_1_with_backtracking(i+1,n)
    print(i)

print_n_to_1_with_backtracking(1,n)