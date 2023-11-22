import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#integrate using gaussian quadrature   
def integrateGauss(f, a, b, n):
    '''Integrate f from a to b using Gaussian quadrature with n nodes'''
    x, w = np.polynomial.legendre.leggauss(n)
    return (b-a)/2 * np.sum(w * f((b-a)/2 * x + (b+a)/2))


def period(V, m,a):
    return np.sqrt(8*m) * integrateGauss(lambda x: 1/(np.sqrt(V(a))-np.sqrt(V(x))), 0, a, 50)

def main():    
    #define amplitude range
    a = np.linspace(0,2,1000)
    
    #calculate heat capacity
    V = lambda x: x**4
    m=1    
    period_result = np.vectorize(period)(V,m,a)
    
    #plot heat capacity
    plt.plot(a,period_result)
    plt.xlabel('Amplitude (m)')
    plt.ylabel('Period (s)')
    plt.title('Amplitude vs. Period of an Anharmonic Harmonic Oscillator')
    plt.show()
    
if __name__ == "__main__":
    main()