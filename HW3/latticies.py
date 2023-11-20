import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_lattice(ax):
    colors = {'Na': 'blue', 'Cl': 'green'}
    atom_positions = {'Na': [(i, j, k) for i in range(10) for j in range(10) for k in range(10) if (i + j + k) % 2 == 0],
                      'Cl': [(i, j, k) for i in range(10) for j in range(10) for k in range(10) if (i + j + k) % 2 == 1]}

    for atom, positions in atom_positions.items():
        for position in positions:
            ax.scatter(*position, c=colors[atom], marker='o', s=50)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Sodium Chloride Crystal Lattice')
    plt.show()

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the lattice
plot_lattice(ax)