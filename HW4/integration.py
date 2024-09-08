import math
import numpy as np
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to complete.")
        return result
    return wrapper

def trapIntegral(f, a, b, n):
    '''
    Calculate the trapzoidal integral of f from a to b with n subintervals.
    
    Parameters:
        f (function): The integrand function.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        N (int): The number of subintervals.
    
    Returns:
        float: Approximation of the definite integral.

    '''
    h = (b-a)/n
    x_values = np.linspace(a,b,n+1)
    integral = h*(0.5*f(a)+0.5*f(b)+sum(f(x_values[1:n])))
    return integral

@time_it
def adaptiveTrapIntegral(f,a,b,epsilon):
    '''
    Finds the trapezoidal integral of f from a to b with an error less than epsilon.

    Parameters:
        f (function): The integrand function.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        epsilon (float): The maximum error allowed.

    Returns the integral, the error, and the number of subintervals used.
    '''
    N = 1
    integralPrev = trapIntegral(f,a,b,N)
    while True:
        N *= 2
        integralCurrent = trapIntegral(f,a,b,N)
        error = abs(integralCurrent - integralPrev) / 3.0
        if error < epsilon:
            return integralCurrent, error, N
        else:
            integralPrev = integralCurrent

@time_it
def adaptive_romberg_integration(f,a,b,epsilon):
    '''
    Finds the Romberg integral of f from a to b with an error less than epsilon.

    Parameters:
        f (function): The integrand function.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        epsilon (float): The maximum error allowed.

    Returns the integral, the error, and the number of rows used.
    '''
    rombergPrevious = []
    rombergCurrent = []
    i = 1

    # Initialize the error to a value greater than epsilon for the first iteration
    error = epsilon + 1
    while True:
        #calculate the first entry of the current romberg row
        rombergCurrent.append(trapIntegral(f,a,b,(2**i)))
        
        #calculate the rest of the entries of the current romberg row using the previous row
        for m in range(2, i+1):
            rombergCurrent.append(rombergCurrent[m-1-1]+((rombergCurrent[m-1-1]-rombergPrevious[m-1-1])/((4**(m-1))-1)))
        
        if(i > 2):
            error = abs((rombergCurrent[i-1-1]-rombergPrevious[i-1-1]))/(4**(i-1)-1)

        if error < epsilon:
            return rombergCurrent[i-1], error, i
        else:
            i += 1
            rombergPrevious = rombergCurrent
            rombergCurrent = []

def main():
    f = lambda x: (np.sin(np.sqrt(100*x)))**2
    a = 0
    b = 1
    e = 10e-6
    result = adaptiveTrapIntegral(f,a,b,e)
    result2 = adaptive_romberg_integration(f,a,b,e)
    print("The integration result is",result[0],"with an error of",result[1],"using",result[2],"subintervals with the adaptive trapezoidal method.")
    print("The integration result is",result2[0],"with an error of",result2[1],"using",result2[2],"rows with adaptive Romberg integration.")

if __name__ == "__main__":
    main()