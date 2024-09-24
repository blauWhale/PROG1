# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Taking input from the user
celsius_input = input("Enter the temperature in Celsius: ")

# Convert input to float or use 0 if input is empty
celsius = float(celsius_input) if celsius_input else 0

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Output the result
print(f"{celsius:.2f}°C is approximately {fahrenheit:.2f}°F.")
