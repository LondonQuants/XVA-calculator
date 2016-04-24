import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(0, 2*math.pi)
plt.plot(x, np.sin(x), label=r'$\sin(x)$')
plt.plot(x, np.cos(x), 'ro', label=r'$\cos(x)$')
plt.title(r'Two plots in a graph')
plt.legend()