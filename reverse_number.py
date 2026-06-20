# Print reverse of a number

def num_reverse(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

print("Reverse : ", num_reverse(1234))