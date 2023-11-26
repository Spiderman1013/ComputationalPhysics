import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def main():
    # Read in the data
    data = pd.read_csv('sunspots.txt', sep='\t', header=None, names=['Month', 'Sunspots'],index_col=None)

    print(data.head())
    month = data['Month']
    sunspots = data['Sunspots']

    month = data['Month']
    sunspots = data['Sunspots']

    # Plot the data
    plt.plot(month,sunspots)
    plt.title("Number of Sunspots over Time")
    plt.xlabel("Months since Jan 1749")
    plt.ylabel("Sunspot Number")
    plt.show()

if __name__ == "__main__":
    main()