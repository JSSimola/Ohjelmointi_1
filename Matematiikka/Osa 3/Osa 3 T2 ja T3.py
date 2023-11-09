from matplotlib import pyplot as plt, patches
import numpy as np
from matplotlib.figure import Figure

plt.rcParams["figure.figsize"] = (19.2, 4.8)
plt.annotate('Selite',xy=(-3*np.pi,1) , xycoords='data', horizontalalignment='left', verticalalignment='top', fontsize=20)

X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=False)
C,S = np.cos(X), np.sin(X)

steps = np.arange(-3*np.pi, 3*np.pi+1, step=(np.pi/2))
plt.xticks(steps, ['-3π', '-5π/2', '-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π'])

plt.plot(X,C, '--', color='red')
plt.plot(X,S, ':', color='purple')

plt.show()
