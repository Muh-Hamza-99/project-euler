def divisible_by_nums_1_to_20(num):
    return all([num % divisor == 0 for divisor in range(20, 10, -1)])
number = 2520
while True:
    if divisible_by_nums_1_to_20(number):
        print(number)
        break
    number += 2520