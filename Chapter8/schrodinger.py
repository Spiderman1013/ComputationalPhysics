import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def createSquareBandedMatrix(N, v1, v2):
    '''
    Creates a banded matrix of size NxN with diagonals v1 and off-diagonals v2
    '''
    # Create an empty matrix
    matrix = np.zeros((N, N), dtype=complex)

    # Fill the diagonals and off-diagonals
    main_diag = np.full(N, v1, dtype=complex)
    off_diag = np.full(N - 1, v2, dtype=complex)

    # Assign diagonals and off-diagonals to the matrix
    np.fill_diagonal(matrix, main_diag)
    np.fill_diagonal(matrix[1:], off_diag)
    np.fill_diagonal(matrix[:, 1:], off_diag)

    # Handle periodic boundary conditions
    matrix[0, -1] = v2
    matrix[-1, 0] = v2

    return matrix


def crank_nicolson_step(psi, A, B):
    v = np.dot(B, psi)
    psi_next = la.solve_banded((1, 1), A, v)
    return psi_next

def main():
    # Constants
    L = 10e-8
    N = 1000
    a = L / N
    h = 1e-16  # Adjusted time step
    hbar = 1.05e-34
    m = 9.109e-31
    x_0 = L / 2
    s = 1e-10
    k = 5e10

    # Set up matrices A and B
    a1 = 1 + ((h * 1j * hbar) / (2 * m * (a ** 2)))
    a2 = -((h * 1j * hbar) / (4 * m * (a ** 2)))
    b1 = 1 - ((h * 1j * hbar) / (2 * m * (a ** 2)))
    b2 = ((h * 1j * hbar) / (4 * m * (a ** 2)))
    B = createSquareBandedMatrix(N, b1, b2)
    A = np.empty((3,N),complex)
    A[0,:] = a2
    A[1,:] = a1
    A[2:,] = a2

    # Initial psi function
    psi_func = lambda x: np.exp(-((x - x_0) ** 2) / (2 * (s ** 2))) * np.exp(1j * k * x)
    x_values = np.arange(0, L, a)
    psi = np.zeros(N, dtype=complex)
    psi[:] = psi_func(x_values)

    # Set up the figure and axes for the animation
    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    ax.set_ylim(-1, 1)
    line, = ax.plot(x_values, psi.real)

    def update(frame):
        nonlocal psi
        psi = crank_nicolson_step(psi, A, B)
        line.set_ydata(psi.real)
        return line,

    # Create the animation
    animation_object = animation.FuncAnimation(
        fig, update, frames=range(int(10e5)), interval=1, blit=True
    )

    plt.title('Wave Function Evolution in Box')
    plt.show()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()