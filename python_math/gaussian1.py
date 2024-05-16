import numpy as np
import math

import matplotlib.pyplot as plt

a = int(input("Enter a: "))

x = np.linspace(-2,2,50)

y = np.exp(-a * x ** 2)

plt.plot(x, y , 'go-')

plt.grid()
plt.show()