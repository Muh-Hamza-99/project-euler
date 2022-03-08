def fib(num):
    if num == 0:
        return 1
    elif num == 1:
        return 2
    else:
        return fib(num-1) + fib(num-2)

total = 0
start_num = 0

while fib(start_num) <= 4000000:
    if fib(start_num) % 2 == 0:
        total += fib(start_num)
    start_num += 1
print(total, start_num)