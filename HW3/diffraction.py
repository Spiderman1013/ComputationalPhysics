import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

def c(d):
    '''
    Returns the transmission function for a certain seperation d
    '''
    a = 2*np.pi/d
    b = 0.5 * a
    return lambda z: ((np.sin(a*z))**2) *  ((np.sin(b*z))**2) 

def intensity(N,L,f,w):
    '''
    Returns the intensity of the diffraction pattern for a certain seperation d
    '''
    d = N/w
    trans = c(d) 
    integrand = lambda x, z: np.sqrt(trans(z)) * np.exp(-1j * 2 * x * np.pi * z / (L * f))
    integral = lambda z: (integrate.quad(lambda x: integrand(x, z), -w / 2, w / 2)[0])**2
    return integral 

def main():
    w = 10e-2
    N = 10
    L = 500e-9
    f = 1
    d = np.linspace(-w/2, w/2, 200)
    intensityFunc = intensity(N,L,f,w)
    intensities = [intensityFunc(x) for x in d]

    # Create a density plot with a colormap resembling a diffraction pattern
    plt.imshow([intensities], cmap='gray', extent=[min(d), max(d), 0, 1], aspect='auto')
    plt.colorbar(label='Intensity')
    plt.xlabel('Separation (d)')
    plt.ylabel('Intensity')
    plt.title('Diffraction Pattern')
    plt.show()



if __name__ == "__main__":
    main()