import numpy as np
import matplotlib.pyplot as plt

def adaptiveFourthOrderRungeKutta(f, a, b, N, initial_condition, tolerance):
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
    r = np.zeros(len(initial_condition))

    #created a result array with the same number of lists as the inital condition
    for i in range(len(initial_condition)):
        result.append([])
        r[i] = initial_condition[i]

    for t in tpoints:
        for i in range(len(r)):
            result[i].append(r[i])
        k1 = h*f(r, t)
        k2 = h*f(r + 0.5*k1, t + 0.5*h)
        k3 = h*f(r + 0.5*k2, t + 0.5*h)
        k4 = h*f(r + k3, t + h)
        y1 = r + (k1 + 2*k2 + 2*k3 + k4)/6
        y2 = r + (k1 + 2*k2 + 2*k3 + k4)/12
        error = np.max(np.abs(y1 - y2))
        h_new = h * min(max(0.1, min(5.0, 0.9 * (tolerance / error) ** 0.2)), 5.0)

        if error < tolerance:
            r = y1
        else:
            h = h_new
            r = y2

    return tpoints, result

def main():
    #constants
    G = 6.67e-11 #m^3/(kg*s^2)
    M = 1.989e30 #kg

    #define the position of a ball through air as four first order ODEs.
    #takes in x, xdot, y, ydot, (collectively as r) and t
    #returns d(theta1)/dt, d(omega1)/dt, d(theta2)/dt, d(omega2)/dt
    def trajectoryFromGravity(r,t):
        x = r[0]
        xdot = r[1]
        y = r[2]
        ydot = r[3]
        rad = np.sqrt(x**2 + y**2)
        fx = xdot
        fxdot = -G*M*x / (rad**3)
        fy = ydot
        fydot = -G*M*y / (rad**3)
        return np.array([fx,fxdot,fy,fydot],float)
    
    #inital conditions
    x_0 = 4*1e3*1e9 #m
    y_0 = 0
    xdot_0 = 0
    ydot_0 = 500 #m/s
    r_0 = np.array([x_0,xdot_0,y_0,ydot_0],float)

    tpoints, trajectoryPoints = adaptiveFourthOrderRungeKutta(trajectoryFromGravity, 0, 10e12, 10e5, r_0, 1)

    #plot x versus y to get the trajectory
    plt.plot(trajectoryPoints[0],trajectoryPoints[2])
    plt.xlim(-x_0,x_0)
    plt.ylim(-x_0,x_0)
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectory of Comet Around Sun")
    plt.show()
    
if __name__ == "__main__":
    main()