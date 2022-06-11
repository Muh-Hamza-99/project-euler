from math import sqrt

def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    return all(num % j for j in range(3, int(sqrt(num)) + 1, 2))

results = 0
for number in range(2, 2000001):
    if is_prime(number):
        results += number

print(results)