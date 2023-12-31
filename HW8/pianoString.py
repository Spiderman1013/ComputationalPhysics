import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def eulerMethod(psi, phi, Nx, dx, dt, v):
    '''
    Performs one step of the Euler Method
    '''
    # Calculate psi_next
    psi[1:Nx-1] = psi[1:Nx-1] + dt * phi[1:Nx-1]
    phi[1:Nx-1] = phi[1:Nx-1] + dt * v**2 * (psi[2:Nx] - 2 * psi[1:Nx-1] + psi[0:Nx-2]) / (dx**2)
    return psi, phi

def main():
    # Constants
    v = 100  # m/s
    L = 1    # m
    d = 0.1  # m
    C = 1    # big C
    s = 0.3  # sigma

    # Parameters
    T = 1.0   # Time to simulate (seconds)
    N = 100   # Number of points to simulate
    Nx = N + 1  # Number of points to plot
    dx = L / N  # Distance between points
    dt = 10e-6  # Time step

    # Initial conditions
    x_values = np.linspace(0, L, Nx)
    phi = np.zeros(Nx)
    psi_initial = lambda x: C * (x * (L - x) / (L**2)) * np.exp(-(x - d)**2 / (2 * s**2))
    psi = psi_initial(x_values)
    # Setting initial conditions for phi (may need adjustment based on problem)
    phi = np.zeros(Nx)  # Placeholder for initial conditions of phi

    fig, ax = plt.subplots()
    graph, = ax.plot(x_values, psi)
    ax.set_xlim(0, L)
    ax.set_ylim(-1, 1)

    # Plot the initial conditions
    def update(frame):
        nonlocal psi
        nonlocal phi
        psi, phi = eulerMethod(psi, phi, Nx, dx, dt, v)
        graph.set_ydata(psi)
        return graph,

    ani = FuncAnimation(fig, update, frames=range(10000), interval=0.001, blit=True)
    plt.show()


if __name__ == "__main__":
    main()
