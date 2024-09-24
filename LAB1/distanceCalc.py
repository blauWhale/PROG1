import math

# Function to compute the distance between two points in a 2D plane
def distance_between_planes(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Taking input from the user for the first plane
x1 = float(input("Enter the x-coordinate of the first plane: "))
y1 = float(input("Enter the y-coordinate of the first plane: "))

# Taking input from the user for the second plane
x2 = float(input("Enter the x-coordinate of the second plane: "))
y2 = float(input("Enter the y-coordinate of the second plane: "))

# Compute the distance between the two planes
distance = distance_between_planes(x1, y1, x2, y2)

# Output the result
print(f"The distance between the two planes is approximately {distance:.2f} units.")
