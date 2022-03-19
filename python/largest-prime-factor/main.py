from math import sqrt

num = 600851475143
answers = []

while num % 2 == 0:
    answers.append(2)
    num //= 2
limit = sqrt(num + 1)
i = 3
while i <= limit:
    if num % i == 0:
        answers.append(i)
        num //= i 
        limit = sqrt(num + 1)
    else:
        i += 2
if num != 1:
    answers.append(num)

print(max(answers))