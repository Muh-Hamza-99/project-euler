from functools import reduce

def find_divisors(num):
    exp_list = []
    count = 0
    divisor = 2
    while divisor <= num:
        while num % divisor == 0:
            num = num / divisor
            count += 1
        if count != 0:
            exp_list.append(count + 1)
        divisor += 1
        count = 0
    return reduce(lambda x, y: x * y, exp_list, 1)

def find_triangle_number_with_n_divisors(num):
    natural = 1
    triangular = 0
    while True:
        triangular += natural
        natural += 1
        if find_divisors(triangular) > num:
            break
    return triangular

print(find_triangle_number_with_n_divisors(500))