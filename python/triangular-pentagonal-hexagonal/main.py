t = 285
p = 165
h = 143

while True:
    triangle = t * (t + 1) // 2
    pentagon = p * (p * 3 - 1) // 2
    hexagon = h * (h * 2 - 1)
    lowest = min(triangle, pentagon, hexagon)
    highest = max(triangle, pentagon, hexagon)
    if lowest == highest: 
        print(triangle)
    if lowest == triangle: 
        t += 1
    if lowest == pentagon:
        p += 1
    if lowest == hexagon:
        h += 1