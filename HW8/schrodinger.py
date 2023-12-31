import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def createSquareBandedMatrix(N, v1, v2):
    '''
    Creates a Banded Matrix of NxN with v1 and v2 as entries
    '''
    array = np.zeros((N, N), complex)
    # populate the matrix
    for i in range(1, N - 1):
        array[i, i] = v1
        array[i - 1, i] = v2
        array[i + 1, i] = v2
    # boundaries
    array[0, 0] = v1
    array[1, 0] = v2
    array[N - 1, N - 1] = v1
    array[N - 2, N - 1] = v2
    return array

def crank_nicolson_step(psi, Ainv, B):
    v = np.dot(B, psi)
    #mutliply with inverse of A
    psi_next = np.dot(Ainv, v)
    return psi_next

def main():
    # Constants
    L = 10e-8
    N = 1000
    a = L / N
    h = 10e-18
    hbar = 1.05e-34
    m = 9.109e-31
    x_0 = L/2
    s = 1e-10
    k = 5e10

    # Set up matrices A and B
    a1 = 1 + ((h * 1j * hbar) / (2 * m * (a**2)))
    a2 = -((h * 1j * hbar) / (4 * m * (a**2)))
    b1 = 1 - ((h * 1j * hbar) / (2 * m * (a**2)))
    b2 = ((h * 1j * hbar) / (4 * m * (a**2)))
    B = createSquareBandedMatrix(N, b1, b2)
    A = createSquareBandedMatrix(N, a1, a2)
    Ainv = np.linalg.inv(A)

    # Initial psi function
    psi_func = lambda x: np.exp(-((x - x_0)**2) / (2 * (s**2))) * np.exp(1j * k * x)
    x_values = np.arange(0, L, a)
    psi_initial = np.array(list(psi_func(x_values)))
    psi_initial[0] = 0
    psi_initial[-1] = 0

    # Set up the figure and axes for the animation
    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    ax.set_ylim(0, 1)
    line, = ax.plot(x_values, psi_initial.real**2)

    def update(frame):
        nonlocal psi_initial
        psi_next = crank_nicolson_step(psi_initial, Ainv, B)
        psi_initial = psi_next
        line.set_data(x_values, psi_initial.real**2)
        return line,

    # Create the animation
    animation_object = animation.FuncAnimation(
        fig, update, frames=range(int(10e5)), interval=20, blit=True
    )

    plt.title('Wave Function Evolution in Box')
    plt.show()

if __name__ == "__main__":
    main()