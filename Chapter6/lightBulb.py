import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def efficiency(T, wavelength1, wavelength2):
    '''
    This function takes in a temperature in Kelvin and returns the efficiency
    of a black body at that temperature.
    
    Parameters:
        T: Temperature in Kelvin in float
        wavelength1: Lower wavelength limit in nm
        wavelength2: Upper wavelength limit in nm
    '''
    # Define constants
    h = 6.626e-34 # Planck's constant
    c = 3e8 # Speed of light
    k = 1.38e-23 # Boltzmann constant
    lambda_1 = wavelength1*1e-9 # Lower wavelength limit
    lambda_2 = wavelength2*1e-9 # Upper wavelength limit

    # Calculate the efficiency
    lower_bound = (h*c)/(lambda_2*k*T)
    upper_bound = (h*c)/(lambda_1*k*T)

    # Calculate the integral
    integrand = lambda x: (x**3)/(np.exp(x)-1)
    integral, _ = integrate.quad(integrand, lower_bound, upper_bound)
    efficiency = (15*integral)/(np.pi**4)
    return efficiency

def goldenRatioSearch(f, a, b, tol):
    '''
    This function finds x value of the maximum of a function using the golden ratio search method.
    Parameters: 
        f: Function to be maximized
        a: Lower bound of the interval
        b: Upper bound of the interval
        tol: Tolerance of the maximum
    '''
    #Define golden ratio
    z = (1+np.sqrt(5))/2
    x1 = a
    x4 = b
    x2 = x4 - (x4-x1)/z
    x3 = x1 + (x4-x1)/z

    while x4-x1 > tol:
        # Check if f(x2) or f(x3) is greater
        if f(x2) > f(x3):
            x4 = x3
            x3 = x2
            x2 = x4 - (x4-x1)/z
        else:
            x1 = x2
            x2 = x3
            x3 = x1 + (x4-x1)/z

    return (x2+x3)/2

def main():
    temperatures = np.linspace(300, 10e4, 1000)
    efficiencies = []
    for temperature in temperatures:
        efficiencies.append(efficiency(temperature, 390, 750))
    f = lambda x: efficiency(x, 390, 750)
    maximum = goldenRatioSearch(f, 300, 10e4, 1)
    print("The most efficienct temperature for a blackbody in visual spectrum is",maximum,"K")
    plt.xlabel('Temperature (K)')
    plt.ylabel('Efficiency')
    plt.title('Efficiency of a Black Body')
    plt.plot(temperatures, efficiencies)
    plt.show()

if __name__ == '__main__':
    main()