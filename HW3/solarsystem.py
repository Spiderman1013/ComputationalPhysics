from vpython import sphere, vector, color, rate
import math

# Scale factor for the sizes of planets
c1 = 50

# Scale factor for the speed of the animation
c2 = 1000

# Define the radius of the Sun
sun_radius = 10 * c1

# Create the Sun
sun = sphere(pos=vector(0, 0, 0), radius=sun_radius, color=color.yellow)

# Planets' data (average distances from the Sun and radii)
planets_data = [
    {"name": "Mercury", "distance": 58 * c1, "radius": 0.38 * c1, "color": color.gray(0.8)},
    {"name": "Venus", "distance": 108 * c1, "radius": 0.95 * c1, "color": color.orange},
    {"name": "Earth", "distance": 150 * c1, "radius": 1.0 * c1, "color": color.blue},
    {"name": "Mars", "distance": 228 * c1, "radius": 0.53 * c1, "color": color.red},
    # Add more planets as needed
]

# Create the planets
planets = []
for data in planets_data:
    planet = sphere(pos=vector(data["distance"], 0, 0), radius=data["radius"], color=data["color"])
    planets.append(planet)

# Animation loop
time_step = 0.01  # Adjust as needed
for t in range(1000):  # Adjust the number of steps as needed
    rate(30)  # Adjust the frame rate as needed
    for planet, data in zip(planets, planets_data):
        # Update the position of the planets
        angle = 2 * math.pi * t * c2  # Orbit completion in c2 times faster
        planet.pos = vector(data["distance"] * math.cos(angle), data["distance"] * math.sin(angle), 0)
