numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_primes = []
is_prime = True
for i in numbers:
    if i == 1:
        continue
    if i == 2:
        Primes.append(i)
        continue
    for j in range(2, i):
        is_prime = True
        if i % j == 0:
            is_prime = False
            break
        elif i % j != 0:
            is_prime = True
            continue
    if is_prime == True:
        Primes.append(i)
    else:
        Not_primes.append(i)
print('Primes: ', Primes)
print('Not_primes: ', Not_primes)
