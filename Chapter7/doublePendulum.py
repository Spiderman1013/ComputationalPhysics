import numpy as np
import matplotlib.pyplot as plt
import vpython as vp

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

        delta = theta1 - theta2
        ftheta1 = omega1
        denom = 3 - np.cos(2*delta)
        fomega1 = -(((omega1**2) * np.sin(2*delta)) + (2 * (omega2**2) * np.sin(delta)) + ((g/l)*(np.sin(theta1-(2*theta2))+(3*np.sin(theta1))))) / denom
        ftheta2 = omega2
        fomega2 = ((4*(omega1**2)*np.sin(delta)) + ((omega2**2)*np.sin(2*delta)) + (2*(g/l)*(np.sin(2*theta1-theta2)-np.sin(theta2)))) / denom
        return np.array([ftheta1,fomega1,ftheta2,fomega2],float)
    
    #inital conditions
    theta1 = np.deg2rad(90)
    theta2 = np.deg2rad(90)
    omega1 = 0
    omega2 = 0

    r_0 = np.array([theta1,omega1,theta2,omega2],float)
    r_1 = np.array([theta1+0.1,omega1,theta2,omega2],float)
    tpoints, doublePendPoints = fourthOrderRungeKutta(doublePendulum, 0, 10, 1000, r_0)
    tpoints, doublePendPoints2 = fourthOrderRungeKutta(doublePendulum, 0, 10, 1000, r_1)
    doublePendPoints = np.array(doublePendPoints)

    def kineticEnergy(pendPoints):
        theta1 = pendPoints[0]
        omega1 = pendPoints[1]
        theta2 = pendPoints[2]
        omega2 = pendPoints[3]

        T = m*(l**2)*((omega1**2)+(0.5*(omega2**2))+(omega1*omega2*np.cos(theta1-theta2)))

        return T

    def potentialEnergy(pendPoints):
        theta1 = pendPoints[0]
        omega1 = pendPoints[1]
        theta2 = pendPoints[2]
        omega2 = pendPoints[3]

        V = -m*g*l*(2*np.cos(theta1)+np.cos(theta2))
        return V
    
    def totalEnergy(pendPoints):
        T = kineticEnergy(pendPoints)
        V = potentialEnergy(pendPoints)
        E = T + V
        return E

    kineticEnergyPoints = kineticEnergy(doublePendPoints)
    potentialEnergyPoints = potentialEnergy(doublePendPoints)
    totalEnergyPoints = totalEnergy(doublePendPoints)

    plt.plot(tpoints,kineticEnergyPoints,label="Kinetic Energy")
    plt.plot(tpoints,potentialEnergyPoints,label="Potential Energy")
    plt.plot(tpoints,totalEnergyPoints,label="Total Energy")
    plt.xlabel("Time (s)")
    plt.ylabel("Total Energy (J)")
    plt.title("Total Energy of the Double Pendulum")
    plt.legend()
    plt.show()

    # animate the double pendulum using vpython    
    # set up pendulum components
    top = vp.vector(0,0,0)
    middle = vp.vector(0,-l,0)
    bottom = vp.vector(0,-2*l,0)
    rod1 = vp.cylinder(pos=top,axis=middle,radius=0.01)
    rod2 = vp.cylinder(pos=middle,axis=middle,radius=0.01)
    bob1 = vp.sphere(pos=middle,color=vp.color.red,radius=0.1)
    bob2 = vp.sphere(pos=bottom,color=vp.color.red,radius=0.1,make_trail=True,interval=1,retain=10,trail_color=vp.color.green)

    #animate the double pendulum
    for theta1, omega1, theta2, omega2 in zip(doublePendPoints[0][::4], doublePendPoints[1][::4], doublePendPoints[2][::4], doublePendPoints[3][::4]):
        vp.rate(24)
        
        # Calculate positions of the pendulum components
        x1 = l * np.sin(theta1)
        y1 = -l* np.cos(theta1)
        x2 = x1 + (l * np.sin(theta2))
        y2 = y1 - (l * np.cos(theta2))
        
        # Update positions of the bob and rods
        bob1.pos = vp.vector(x1, y1, 0)
        rod1.axis = vp.vector(x1, y1, 0)
        rod2.pos = vp.vector(x1, y1, 0)
        rod2.axis = vp.vector(x2-x1, y2-y1, 0)
        bob2.pos = vp.vector(x2, y2, 0)
                
if __name__ == "__main__":
    main()


