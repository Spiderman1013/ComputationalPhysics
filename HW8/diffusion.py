import numpy as np
import matplotlib.pyplot as plt

def main():
    # Parameters
    L = 1.0       # Length of the domain
    T = 1.0       # Total simulation time
    Nx = 100      # Number of spatial points
    Nt = 1000     # Number of time steps
    c = 1.0       # Wave speed
    dx = L / Nx   # Spatial step size
    dt = T / Nt   # Time step size

    # Create arrays for the spatial and time coordinates
    x = np.linspace(0, L, Nx)
    t = np.linspace(0, T, Nt)

    # Initialize the wave function
    u = np.zeros(Nx)

    # Initial conditions (e.g., Gaussian pulse)
    u0 = np.exp(-100 * (x - 0.5 * L) ** 2)

    # Set the initial condition
    u = u0.copy()

    # FTCS time-stepping loop
    for n in range(1, Nt):
        u[1:Nx-1] = u[1:Nx-1] - c * dt / dx * (u[2:Nx] - u[0:Nx-2])

    # Plot the final wave profile
    plt.plot(x, u)
    plt.xlabel('Position')
    plt.ylabel('Amplitude')
    plt.title('1D Wave Equation (FTCS)')
    plt.show()


if __name__ == "__main__":
    main()