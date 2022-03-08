perimeter = 1000
for a in range(1, perimeter + 1):
    for b in range(a + 1, perimeter + 1):
        c = perimeter - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)