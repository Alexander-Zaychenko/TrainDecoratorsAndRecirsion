def print_numbers(n):
    if n >= 1:
        print_numbers(n - 1)
    else:
        return ValueError
    print(n)

print_numbers(13)
print('-----------')
print_numbers(5)
print('-----------')
print_numbers(-2)