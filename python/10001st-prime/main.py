from math import floor, sqrt, ceil, log

def is_prime(num):
    if (num == 1): 
        return False
    sqrt_num = int(floor(sqrt(num)))
    for i in range(2, sqrt_num):
        if num % i == 0: 
            return False
    return True

def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

def upper_bound_for_p_n(num):
    if num < 6:
        return 100
    return ceil(num * (log(num) + log(log(num))))

def find_n_prime(num):
    primes = list(find_primes(upper_bound_for_p_n(num)))
    return primes[num - 1]

print(find_n_prime(10001))