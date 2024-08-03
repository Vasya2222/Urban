numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for i in numbers:

    counter = 0

    if i == 1:
        continue

    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    
    if counter == 2:
        primes.append(i)
    else:
        not_primes.append(i)

print("Primes:", primes)
print("Not primes:", not_primes)
