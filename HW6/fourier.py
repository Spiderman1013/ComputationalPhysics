import numpy as np
import matplotlib.pyplot as plt
import cmath as m 

def discreteFourierTransform(y):
    '''
    Computes the discrete fourier tranform given an input value
    '''
    N = len(y)
    c = np.zeros(N//2 +1, dtype=complex)
    for k in range(N//2 +1):
        for n in range(N):
            c[k] += y[n] * np.exp(-2j * np.pi * k * n / N)
    return c

def main():
    N = 1000
    input_X = np.linspace(0, 2*np.pi, N)
    square_wave = np.sign(np.sin(input_X))
    square_fourier = discreteFourierTransform(square_wave)
    plt.plot(abs(square_fourier))
    plt.xlim(0, 500)
    plt.title('Square Wave')
    plt.show()

    sawtooth_wave = np.sign(np.tan(input_X))
    sawtooth_fourier = discreteFourierTransform(sawtooth_wave) 
    plt.plot(abs(sawtooth_fourier))
    plt.xlim(0, 500)
    plt.title('Sawtooth Wave')
    plt.show()

    modulatedSin = lambda x: np.sin(x) * np.sin(20*x)
    modulatedSin_wave = modulatedSin(input_X)
    modulatedSin_fourier = discreteFourierTransform(modulatedSin_wave)
    plt.plot(abs(modulatedSin_fourier))
    plt.xlim(0, 500)
    plt.title('Modulated Sin Wave')
    plt.show()


if __name__ == '__main__':
    main()