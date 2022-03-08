# sum_of_squares = 0
# square_of_sum = 0

# for i in range(101):
#     result = i ** 2
#     sum_of_squares += result

# for i in range(101):
#     square_of_sum += 1
# square_of_sum =  square_of_sum ** 2 

# print(square_of_sum - sum_of_squares)

def sum_square_difference(num):
    numbers = range(1, num + 1)
    sum_squares = sum(i**2 for i in numbers)
    square_sum = sum(numbers) ** 2
    return square_sum - sum_squares

print(sum_square_difference(100))