# Kapitel 4

## 4.1 Execute a Python Script
[Link to division.py](./division.py)

```python
a = 144
result = a / 2
print(result)
```

## 4.2 Braking Distance – Compute the Distance It Takes to Stop a Car
[Link to brakingDistance.py](./brakingDistance.py)

```python
def braking_distance(v0_kmh, mu):
    v0_ms = v0_kmh * (1000 / 3600)
    return 0.5 * (v0_ms ** 2) / (mu * 9.81) if mu > 0 else 0

v0_kmh = float(input("Velocity (km/h): ") or 0)
mu = float(input("Friction coefficient (mu): ") or 0)

print(f"Braking distance: {braking_distance(v0_kmh, mu)} meters")
```

## 4.3 Celsius to Fahrenheit – Convert Degrees Celsius to Degrees Fahrenheit
[Link to celsius2fahrenheit.py](./celsius2fahrenheit.py)

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Temperatur in Celsius: ") or 0)

print(f"{celsius}°C sind {celsius_to_fahrenheit(celsius)}°F.")
```

## 4.4 Distance Between Two Aircrafts
[Link to distanceCalc.py](./distanceCalc.py)

```python
import math

def distance_between_planes(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

x1 = float(input("x-Koordinate des ersten Punktes: "))
y1 = float(input("y-Koordinate des ersten Punktes: "))
x2 = float(input("x-Koordinate des zweiten Punktes: "))
y2 = float(input("y-Koordinate des zweiten Punktes: "))

print(f"Die Entfernung zwischen den Punkten beträgt {distance_between_planes(x1, y1, x2, y2)} Einheiten.")
```

## 4.5 Litres to Kilograms – Another Conversion Task
[Link to liter2kilogram.py](./liter2kilogram.py)

```python
quantity = float(input("Menge in Litern: "))
density = float(input("Dichte in kg/L: "))

print(f"Das Gewicht beträgt {quantity * density} kg.")
```
