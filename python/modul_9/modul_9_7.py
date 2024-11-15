def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Простое' if len([i for i in range(1, result + 1) if result % i == 0]) == 2 else 'Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
