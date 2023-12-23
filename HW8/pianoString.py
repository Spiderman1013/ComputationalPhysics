import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def main():
    # Constants
    v = 100 # m/s
    L = 1 # m
    d = 0.1 # m
    C = 1 # big C 
    s = 0.3 # sigma

    #Parameters
    T = 1.0 # Time to simulate (seconds)
    N = 100 # Number of points to simulate
    Nx = N + 1 # Number of points to plot
    dx = L / N # Distance between points
    dt = 0.001 # Time step

    # Initial conditions
    X = np.linspace(0, L, Nx)
    Y = np.zeros(Nx)


    fig, ax = plt.subplots()


    ani = FuncAnimation()
    plt.show()