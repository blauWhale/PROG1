def braking_distance(v0_kmh, mu):
    v0_ms = v0_kmh * (1000 / 3600)
    return 0.5 * (v0_ms ** 2) / (mu * 9.81) if mu > 0 else 0

v0_kmh = float(input("Velocity (km/h): ") or 0)
mu = float(input("Friction coefficient (mu): ") or 0)

print(f"Braking distance: {braking_distance(v0_kmh, mu)} meters")
