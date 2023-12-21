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
        inital_condition: N-Dimensional vector initial value of output at a 
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
        for i in range(len(r)):
            result[i].append(r[i])
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1, t + 0.5*h)
        k3 = h*f(r + 0.5*k2, t + 0.5*h)
        k4 = h*f(r + k3, t + h)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

    return tpoints, result

def main():
    #constants
    g = 9.81 #m/s^2
    m = 1 #kg
    R = 8e-2 #m
    C = 0.47
    p = 1.22 #kg/m^3

    #define the position of a ball through air as four first order ODEs.
    #takes in x, xdot, y, ydot, (collectively as r) and t
    #returns d(theta1)/dt, d(omega1)/dt, d(theta2)/dt, d(omega2)/dt
    def trajectoryWithResistance(r,t):
        x = r[0]
        xdot = r[1]
        y = r[2]
        ydot = r[3]
        factor = (-C*p*np.pi*(R**2))/(2*m)
        fx = xdot
        fxdot = factor*xdot*np.sqrt(xdot**2 + ydot**2)
        fy = ydot
        fydot = -g + (factor * ydot * np.sqrt(xdot**2 + ydot**2))
        return np.array([fx,fxdot,fy,fydot],float)
    
    #inital conditions
    theta = 30 #degrees
    v = 100 #m/s
    vx = v*np.cos(np.radians(theta))
    vy = v*np.sin(np.radians(theta))
    x = 0
    y = 0
    r_0 = np.array([x,vx,y,vy],float)

    tpoints, trajectoryPoints = fourthOrderRungeKutta(trajectoryWithResistance, 0, 10, 1000, r_0)

    #plot x versus y to get the trajectory
    plt.plot(trajectoryPoints[0],trajectoryPoints[2])
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectory of a Ball with Air Resistance")
    plt.show()
    
        
if __name__ == "__main__":
    main()