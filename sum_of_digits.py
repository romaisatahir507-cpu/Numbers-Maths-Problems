# Print Sum of Dihits of a given Number.

def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10

    return sum

print("Sum of Digits :", sum_of_digits(125))