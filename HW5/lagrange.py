import numpy as np
import math

def newtons_method(f, df, x0, tol, maxiter):
    
    for i in range(maxiter): 
        x1 = x0 - f(x0)/df(x0) 
        if abs(x1 - x0) < tol: 
            return x1 
        x0 = x1 
    return x1 

def main():
    #constants
    G = 6.67408e-11 #m^3 kg^-1 s^-2
    M = 5.972e24 #kg
    m = 7.348e22 #kg
    R = 3.844e8 #m
    w = 2.662e-6 #s^-1

    #initial conditions
    r_guess = 0.5 * R
    f = lambda r: G*M/r**2 - G*m/(R-r)**2 - w**2*r
    df = lambda r: -2*G*M/r**3 + 2*G*m/(R-r)**3 - w**2

    r_real = newtons_method(f, df, r_guess, 1e-4, 100)
    print("the distance from earth is",r_real,"meters")
    #define functions

if __name__=="__main__":
    main()