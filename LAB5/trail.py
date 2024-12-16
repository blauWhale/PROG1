import math

def path_length(trail):
    total_length = 0
    for i in range(1, len(trail)):
        x1, y1 = trail[i - 1]
        x2, y2 = trail[i]
        total_length += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total_length

# Test mit dem Dreieckspfad
trail1 = [(1, 1), (2, 1), (1, 2), (1, 1)]
print("Total length of the triangular path:", path_length(trail1))

# Test mit dem Beispiel aus der Aufgabenstellung
trail2 = [
    (142.492, 208.536),
    (142.658, 207.060),
    (143.522, 205.978),
    (145.009, 205.546)
]
print("Total length of the example trail:", path_length(trail2))
