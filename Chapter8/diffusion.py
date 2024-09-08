import random
import math
import matplotlib.pyplot as plt

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def simulate_DLA(grid_size):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    center = grid_size // 2
    r = 0

    def is_within_bounds(x, y):
        return 0 <= x < grid_size and 0 <= y < grid_size

    def start_random_point_on_circle(radius):
        angle = random.uniform(0, 2 * math.pi)
        x = int(center + radius * math.cos(angle))
        y = int(center + radius * math.sin(angle))
        return x, y

    while r < grid_size // 2:
        x, y = start_random_point_on_circle(r + 1)
        
        while True:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_within_bounds(new_x, new_y) and grid[new_x][new_y] == 1:
                    grid[x][y] = 1
                    distance_to_center = euclidean_distance(center, center, x, y)
                    if distance_to_center > r:
                        r = distance_to_center
                    break
            else:
                distance_from_center = euclidean_distance(center, center, x, y)
                if distance_from_center > 2 * r:
                    break
                angle = random.uniform(0, 2 * math.pi)
                x = int(center + (r + 1) * math.cos(angle))
                y = int(center + (r + 1) * math.sin(angle))

    return grid

# Set grid size
grid_size = 101

# Run simulation
resulting_grid = simulate_DLA(grid_size)

def plot_DLA(grid):
    plt.imshow(grid, cmap='Greys', interpolation='nearest')
    plt.title('Diffusion-Limited Aggregation (DLA)')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.colorbar(label='Aggregation')
    plt.show()

# Set grid size
grid_size = 101

# Run simulation
resulting_grid = simulate_DLA(grid_size)

# Plot the resulting aggregation pattern
plot_DLA(resulting_grid)
