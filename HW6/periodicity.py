import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

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
    # Read in the data
    data = pd.read_csv('sunspots.txt', sep='\t', header=None, names=['Month', 'Sunspots'],index_col=None)

    month = data['Month']
    sunspots = data['Sunspots']

    c_k = discreteFourierTransform(sunspots)

    # Plot the data
    plt.plot(np.power(abs(c_k),2))
    plt.plot(np.power(abs(np.fft.rfft(sunspots)),2))
    plt.title("Fourier Graph of Sunspots")
    plt.xlabel("K Value")
    plt.ylabel("|C_k|^2")
    plt.show()

if __name__ == "__main__":
    main()