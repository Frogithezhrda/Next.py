def is_prime(number):
    return number > 1 and not any(number % divisor == 0 for divisor in range(2, int(number ** 0.5) + 1))

print(is_prime(43))
