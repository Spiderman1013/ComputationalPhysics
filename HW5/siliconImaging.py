import numpy as np
import matplotlib.pyplot as plt

def two_dim_array_gradient(array,h):
    #returns the gradient of a 2d array
    gradient = np.gradient(array,h)
    return gradient


def main():
    #load in the data into a 2d array
    silicon = np.loadtxt('stm.txt')
    gradient = two_dim_array_gradient(silicon,2.5)
    x_gradient = gradient[0]
    y_gradient = gradient[1]
    phi = np.deg2rad(45)
    intensity = (np.cos(phi)*(x_gradient) + np.sin(phi)*(y_gradient))/np.sqrt((x_gradient)**2 + (y_gradient)**2 + 1)

    #plot the data
    plt.imshow(intensity, cmap='gray', aspect='auto')
    plt.colorbar(label='Height')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Surface of Silicon')
    plt.show()


if __name__ == '__main__':
    main()