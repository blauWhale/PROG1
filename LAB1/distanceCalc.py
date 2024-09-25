import math

def distance_between_planes(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1 = float(input("x-Koordinate des ersten Punktes: "))
y1 = float(input("y-Koordinate des ersten Punktes: "))
x2 = float(input("x-Koordinate des zweiten Punktes: "))
y2 = float(input("y-Koordinate des zweiten Punktes: "))

print(f"Die Entfernung zwischen den Punkten beträgt {distance_between_planes(x1, y1, x2, y2)} Einheiten.")
