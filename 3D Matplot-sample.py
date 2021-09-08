"""
This is a sample for 3D Math plot library

function:
     sin(x)^2  * cos(X)

@author: Manijeh Komeili
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

f = lambda x, y : np.cos(x) * np.sin(y)**2
x = np.linspace (-3,3,100)
y = np.linspace (-3,3,100)
X, Y = np.meshgrid(x,y)
F = f(X, Y)

fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
ax.plot_surface(X, Y, F, rstride=1, cstride=1, cmap=cm.viridis)
ax.view_init(elev=10, azim=14)
plt.show()




