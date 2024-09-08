import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


def main():
    # Read in the data
    price = np.loadtxt('dow.txt')

    coeff = np.fft.rfft(price)
    #only keep first 2 percent of coefficients 
    percent = 2
    start_index = int(len(coeff) * (percent / 100))
    coeff[start_index:] = 0

    reconstructed_price = np.fft.irfft(coeff)

    # Plot the data
    plt.plot(price,label='Actual Data')
    plt.plot(reconstructed_price,label='Moving Average')
    plt.title("Dow Jones Industrial Average")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()