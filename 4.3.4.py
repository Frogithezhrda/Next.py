def get_fibo():
    start_number = 0
    next_addition = 1
    while True:
        yield start_number
        start_number, next_addition = next_addition, start_number + next_addition


gen = get_fibo()
for _ in range(10):
    print(next(gen))
