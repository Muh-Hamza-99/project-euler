palindrome = 0
for i in range(1000):
    for j in range(999, 1, -1):
        string_num = str(i * j)
        if string_num == string_num[::-1]:
            if palindrome < i * j:
                palindrome = i * j
                break
print(palindrome)