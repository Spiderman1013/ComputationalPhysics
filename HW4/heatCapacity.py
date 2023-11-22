import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#integrate using gaussian quadrature   
def integrateGauss(f, a, b, n):
    '''Integrate f from a to b using Gaussian quadrature with n nodes'''
    x, w = np.polynomial.legendre.leggauss(n)
    return (b-a)/2 * np.sum(w * f((b-a)/2 * x + (b+a)/2))

def cv(T):
    #define constants
    p=6.022e28
    T_D=428
    V = p*1000*1e-6
    k_B=1.38064852e-23
    return 9 * V * p* k_B * ((T/T_D)**3) * integrateGauss(lambda x: (x**4)*np.exp(x)/((np.exp(x)-1)**2), 0, T_D/T, 50)

def main():    
    #define temperature range
    T = np.linspace(5,500,1000)
    
    #calculate heat capacity
    C_v = np.vectorize(cv)(T)
    
    #plot heat capacity
    plt.plot(T,C_v)
    plt.xlabel('Temperature (K)')
    plt.ylabel('Heat Capacity (J/K)')
    plt.title('Heat Capacity of a Solid')
    plt.show()
    
    #find maximum heat capacity
    print('The maximum heat capacity is', np.max(C_v), 'J/K at', T[np.argmax(C_v)], 'K')

if __name__ == "__main__":
    main()