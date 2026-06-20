# Check if a number is prime.


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:            # 2 is only even number that is prime.
        return True
    if n % 2 == 0:        # other even numbers are not prime.
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

n = 33

if is_prime(n):
    print(f"{n} is Prime Number.")
else:
    print(f"{n} is NOT prime number.")