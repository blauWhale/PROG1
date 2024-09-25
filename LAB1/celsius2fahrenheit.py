def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatur in Celsius: ") or 0)

print(f"{celsius}°C sind {celsius_to_fahrenheit(celsius)}°F.")
