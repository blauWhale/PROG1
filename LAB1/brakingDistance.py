# Constants
g = 9.81  # gravitational acceleration in m/s^2

# Function to compute braking distance
def braking_distance(v0_kmh, mu):
    v0_ms = v0_kmh * (1000 / 3600)  # Convert velocity from km/h to m/s
    d = 0.5 * (v0_ms ** 2) / (mu * g) if mu > 0 else 0  # Compute braking distance using the formula, handle zero mu
    return d

# Taking input from the user, using 0 if input is empty
v0_kmh_input = input("Enter the initial velocity of the car (km/h): ")
mu_input = input("Enter the friction coefficient (mu): ")

# Convert input to float or use 0 if input is empty
v0_kmh = float(v0_kmh_input) if v0_kmh_input else 0
mu = float(mu_input) if mu_input else 0

# Compute braking distance
d = braking_distance(v0_kmh, mu)

# Output the result
print(f"The braking distance is approximately {d:.2f} meters.")
