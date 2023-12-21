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

    # Constants for the pendulum
    g = 9.81  # acceleration due to gravity (m/s^2)
    l = 1.0   # length of the pendulum (m)

    #define the nonlinear Pendulum as two first order ODEs. 
    #Define r as (theta,omega)
    #takes r and t, returns d(theta)/dt and d(omega)/dt
    def pendl(r,t):
        theta = r[0]
        omega = r[1]
        ftheta = omega
        fomega = -(g/l)*np.sin(theta)
        return np.array([ftheta,fomega],float)
    
    #inital values for pendulum
    theta0 = 179 * np.pi / 180  # initial angle (in radians)
    omega0 = 0.0  # initial angular velocity (rad/s)
    r_0 = np.array([theta0,omega0],float)

    timeValues, resultValues = fourthOrderRungeKutta(pendl, 0, 10, 1000, r_0)

    #plot theta vs time
    plt.plot(timeValues, resultValues[0])
    plt.xlabel("Time (s)")
    plt.ylabel("Theta (rad)")
    plt.title("Theta vs Time")
    plt.show()

if __name__ == "__main__":
    main()