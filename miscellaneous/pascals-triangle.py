def pascal_triangle():
    depth = int(input("How many rows of Pascal's triangle do you want to print? : "))
    for y in range(depth + 1):
        for ws in range(depth - y + 1):
            print("   ", end = "")
        for x in range(y + 1):
            if x == 0 or y == 0:
                count = 1
            else: 
                count = int(count *  (y - x + 1) / x)
            c = str(count).rjust(3, " ")
            print(f"{c}   ", end = "")
        print()

pascal_triangle()