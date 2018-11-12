def print_even(n):
    init_n = n
    num = 0
    while n >= 1:
        if num != init_n:
            print(num)
        if n%2 >= 0:
            n = n/2
            num = num +2
            
                

print_even(0)
print_even(1)
print_even(-1)
print_even(4)
print_even(5)