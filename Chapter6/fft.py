import numpy as np
import matplotlib.pyplot as plt

def fastFourierTransform(y):
    '''
    Computes the fast fourier transform of the input signal y assuming 2^N points in y
    '''
    N = len(y)
    c_k = np.zeros(N, dtype=complex)

    # Base case
    if N <= 1: 
        return y
    
    #Recursive Step
    else:
       #split into even and odd subproblems
        even = fastFourierTransform(y[0::2])
        odd = fastFourierTransform(y[1::2])

        #combine results
        for k in range(N//2):
            twiddle = np.exp(-2j*np.pi*k/N)
            c_k[k] = even[k] + twiddle*odd[k]
            c_k[k+N//2] = even[k] - twiddle*odd[k]

    return c_k

def main():
    input = np.loadtxt('pitch.txt')
    fourier = np.array(fastFourierTransform(input))
    plt.plot(abs(fourier))
    plt.xlim(0,513)
    plt.show()

if __name__ == '__main__':
    main()