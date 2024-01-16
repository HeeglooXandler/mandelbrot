import numpy as np
import matplotlib.pyplot as plt
#import randy

width = np.linspace(-2, 1, 1920)
height = np.linspace(-2, 2, 1080)

vals = np.meshgrid(width, range(1,1081))[0] + 1j*np.meshgrid(height, range(1,1921))[0].T

v = (1 - 2*np.random.random((1080,1920)))/10
while not np.isnan(v).any():
    mandle = v 
    v = mandle**2 + vals + (1 - 2*np.random.random((1080,1920)))/10

mandle = abs(mandle)
mandle[ mandle > 2 ] = 2+np.log10(mandle[ mandle > 2 ])

plt.imshow(mandle)
plt.show()