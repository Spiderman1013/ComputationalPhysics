import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Planet:
    def __init__(self, name, color, size, radius=None, period=None):
        self.name = name # Name of the planet
        self.color = color # Any color that matplotlib understands
        self.size = size # In km
        self.angle = 0.0 # In radians
        self.orbital_speed = 0.0 # In radians per day
        self.radius = 0.0 # Distance from the Sun in km
        if radius is not None and period is not None:
            self.orbital_speed = (2 * np.pi) / period
            self.radius = radius

    def calculate_position(self):
        x = self.radius * np.cos(np.radians(self.angle))
        y = self.radius * np.sin(np.radians(self.angle))
        return x, y

    def update_position(self):
        step_size = 20 # In days
        self.angle += self.orbital_speed * step_size


class SolarSystem:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def update_positions(self):
        for planet in self.planets:
            planet.update_position()

# Set up the figure and axis
fig, ax = plt.subplots()

grid_size = 300e6

ax.set_xlim(-grid_size,grid_size)
ax.set_ylim(-grid_size,grid_size)

# Create a SolarSystem instance
solar_system = SolarSystem()

# Add planets to the solar system
#solar_system.add_planet(Planet(name='Mercury', radius=1, color='red', period=88, size=10))
solar_system.add_planet(Planet(name='Sun', radius = 1, period=1, color='yellow', size=695500))
solar_system.add_planet(Planet(name='Mercury', radius=57.9e6, color='gray', period=88, size=2500))
solar_system.add_planet(Planet(name='Venus', radius=108.2e6, color='orange', period=224.7, size=6052))
solar_system.add_planet(Planet(name='Earth', radius=149.6e6, color='blue', period=365.3, size=6371))
solar_system.add_planet(Planet(name='Mars', radius=227.9e6, color='red', period=687, size=3386))
#solar_system.add_planet(Planet(name='Jupiter', radius=778.5e6, color='orange', period=4331.6, size=69173))
#solar_system.add_planet(Planet(name='Saturn', radius=1433.4e6, color='brown', period=10759.2, size=57316))

# Initialize the planets at arbitrary starting positions
planet_markers = [ax.plot([], [], planet.color, marker='o', label=planet.name)[0] for planet in solar_system.planets]



# Function to update the plot in each frame
def update(frame):
    c1 = 0.0000002231833333333  # Scaling factor for planet size
    solar_system.update_positions()
    for i, planet in enumerate(solar_system.planets):
        x, y = planet.calculate_position()
        planet_markers[i].set_data([x], [y])  # Use lists to address the deprecation warning
        planet_markers[i].set_markersize(planet.size*c1/grid_size)  # Adjust the scaling factor if needed
    return planet_markers


# Create the animation
animation = FuncAnimation(fig, update, frames=range(88), interval=1, blit=True)

# Add labels and legend
ax.set_facecolor('black')
ax.set_aspect('equal', adjustable='box')
ax.set_title('Solar System Animation')

plt.show()
