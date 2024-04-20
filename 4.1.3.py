def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    if is_prime(n):
        return n
    else:
        gen = (n for n in range(n, n + 10) if is_prime(n))
        # next(prime_generator)
        return next(gen)


print(first_prime_over(100000))
