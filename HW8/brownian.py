import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    # Set the size of the lattice and the number of steps
    L = 1001
    num_steps = 1000000

    def update(frame, i, j):
        direction = np.random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            if j[0] < L - 1:
                j[0] += 1
        elif direction == 'down':
            if j[0] > 0:
                j[0] -= 1
        elif direction == 'left':
            if i[0] > 0:
                i[0] -= 1
        elif direction == 'right':
            if i[0] < L - 1:
                i[0] += 1

        particle.set_data((i[0],), (j[0],))  # Convert to tuples to avoid MatplotlibDeprecationWarning
        return particle,

    # Initialize the particle in the center of the lattice
    i, j = [L // 2], [L // 2]

    # Create a figure and axis for the animation
    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    particle, = ax.plot(i, j, 'bo')  # Initial position of the particle

    # Create an animation
    ani = animation.FuncAnimation(fig, update, fargs=(i, j), frames=num_steps, interval=10, blit=True)

    # Display the animation
    plt.show()

if __name__ == "__main__":
    main()