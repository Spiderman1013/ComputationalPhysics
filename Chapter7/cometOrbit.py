import numpy as np
import matplotlib.pyplot as plt

def fourthOrderRungeKutta(f, a, b, N, inital_condition):
    '''
    Calculates analytical solution to ODE given by f using fourth order Runge-Kutta method
    Returns a the time values and a phase space result array
    Parameters:
        f: differential equation to be solved
        a: left endpoint of interval
        b: right endpoint of interval
        N: number of steps
        inital_condition: N-Dimensional vector with inital value of all dependent variables
    '''
    h = (b-a)/N
    tpoints = np.arange(a, b, h)

    result = []
    r = np.zeros(len(inital_condition))

    #created a result array with the same number of lists as the inital condition
    for i in range(len(inital_condition)):
        result.append([])
        r[i] = inital_condition[i]

    for t in tpoints:
        for i in range(len(result)):
            result[i].append(r[i])
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1, t + 0.5*h)
        k3 = h*f(r + 0.5*k2, t + 0.5*h)
        k4 = h*f(r + k3, t + h)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    return tpoints, result


def main():
    #constants 
    G = 6.67408e-11 #m^3 kg^-1 s^-2
    M = 1.989e30 #kg
    
    #inital conditions
    x0 = 4e12 #m
    y0 = 0 #m
    vx0 = 0 #m/s
    vy0 = 500 #m/s

    def cometOrbit(r,t):
        x = r[0]
        xdot = r[1]
        y = r[2]
        ydot = r[3]
        R = np.sqrt(x**2 + y**2)
        factor = (-G*M)/(R**3)
        fx = xdot
        fxdot = -factor*x
        fy = ydot
        fydot = -factor*y
        return np.array([fx,fxdot,fy,fydot],float)
    
    r_0 = np.array([x0,vx0,y0,vy0],float)

    t, result = fourthOrderRungeKutta(cometOrbit, 0, 4*2.5e9, 10e5, r_0)
    X = result[0]
    Y = result[2]

    plt.plot(X,Y)
    plt.xlim(-2*min(X),2*max(X))
    plt.ylim(-4*min(Y)-4e12,2*max(Y))
    plt.title("Comet Orbit")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.show()

if __name__ == "__main__":
    main() 



