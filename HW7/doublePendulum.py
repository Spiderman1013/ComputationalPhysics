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
    m  = 1.0 # mass of the pendulum (kg)

    #define the double nonlinear Pendulum as four first order ODEs.
    #takes in theta1, omega1, theta2, omega2, and t
    #returns d(theta1)/dt, d(omega1)/dt, d(theta2)/dt, d(omega2)/dt
    def doublePendulum(r,t):
        theta1 = r[0]
        omega1 = r[1]
        theta2 = r[2]
        omega2 = r[3]
        ftheta1 = omega1
        fomega1 = (m*g*np.sin(theta2)*np.cos(theta1-theta2) - m*np.sin(theta1-theta2)*(l*omega1**2*np.cos(theta1-theta2) + l*omega2**2) - (m+m)*g*np.sin(theta1))/(l*(m+m*(np.sin(theta1-theta2))**2))
        ftheta2 = omega2
        fomega2 = ((m+m)*l*omega1**2*np.sin(theta1-theta2) + (m+m)*g*np.sin(theta2) + m*l*omega2**2*np.sin(theta1-theta2)*np.cos(theta1-theta2))/(l*(m+m*(np.sin(theta1-theta2))**2))
        return np.array([ftheta1,fomega1,ftheta2,fomega2],float)
    
    #inital conditions
    theta1 = 90
    theta2 = 90
    omega1 = 0
    omega2 = 0

    r_0 = np.array([theta1,omega1,theta2,omega2],float)
    tpoints, doublePendPoints = fourthOrderRungeKutta(doublePendulum, 0, 10, 10e6, r_0)
    doublePendPoints = np.array(doublePendPoints)

    def totalEnergy(theta1,omega1,theta2,omega2):
        T = m*l**2*(omega1**2 + 0.5*omega2**2 + omega1*omega2*np.cos(theta1-theta2))
        V = -m*g*l*(2*np.cos(theta1) + np.cos(theta2))
        return T + V
    
    totalEnergyValues = totalEnergy(doublePendPoints[0],doublePendPoints[1],doublePendPoints[2],doublePendPoints[3])

    plt.plot(tpoints,totalEnergyValues)
    plt.xlabel("t")
    plt.ylabel("Total Energy")
    plt.show()

if __name__ == "__main__":
    main()


