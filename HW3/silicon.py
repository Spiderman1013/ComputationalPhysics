import numpy as np
import matplotlib.pyplot as plt

# Load data from stm.dat
data = np.loadtxt('stm.txt')

# Create a density plot
plt.imshow(data, cmap='viridis', interpolation='nearest', origin='lower', aspect='auto')
plt.colorbar(label='Height')
plt.title('Density Plot of STM Measurements for Silicon Surface')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
