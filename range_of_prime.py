# Check prime numbers upto N.


def is_prime(n):
    if n <= 1:
        return false
    if n == 2:
        return True
    if n % 2 == 0: 
        return False

    i =3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

prime_range = 25

for num in range(2, prime_range):
    if is_prime(num):
        print(num, end=" ")