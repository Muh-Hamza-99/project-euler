def pascals_triangle(num):
    starting_array = [[1]]
    for i in range(num - 1):
        starting_array.append([sum(i) for i in zip([0] + starting_array[-1], starting_array[-1] + [0])])
    return starting_array

triangle = pascals_triangle(41)
num_of_paths = triangle[40][20]

print(num_of_paths)