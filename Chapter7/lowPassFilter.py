import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def fourthOrderRungeKutta(f, a, b, N, inital_condition):
    '''
    Calculates analytical solution to ODE given by f using fourth order Runge-Kutta method
    Parameters:
        f: differential equation to be solved
        a: left endpoint of interval
        b: right endpoint of interval
        N: number of steps
        inital_condition: initial value of output at a
    '''
    output = inital_condition
    h = (b-a)/N
    tpoints = np.arange(a, b, h)
    xpoints = []
    for t in tpoints:
        xpoints.append(output)
        k1 = h*f(output, t)
        k2 = h*f(output + 0.5*k1, t + 0.5*h)
        k3 = h*f(output + 0.5*k2, t + 0.5*h)
        k4 = h*f(output + k3, t + h)
        output += (k1 + 2*k2 + 2*k3 + k4)/6

    return tpoints,xpoints
        
def main():
    #defining the differential equation
    def V_in(t):
        if(np.floor(2*t)%2 == 0):
            return 1
        else:
            return -1
    RC = 0.01
    ode = lambda V_out, t: (V_in(t) - V_out)/RC

    timeValues,v_outValues = fourthOrderRungeKutta(ode, 0, 10, 1000, 0)

    #solving the differential equation
    V_inValues = []
    for t in timeValues:
        V_inValues.append(V_in(t))
    plt.plot(timeValues, v_outValues)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage Out (V)")
    plt.show()

if __name__ == "__main__":
    main()