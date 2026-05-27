import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2,2,200)
y = np.linspace(-2,2,200)

X,Y = np.meshgrid(x,y)

# Polinomio 1
Z1 = X**4 + Y**4

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z1)
ax.set_title("P1(x,y)=x^4+y^4")
plt.show()

# Polinomio 2
Z2 = X**3*Y - X*Y**3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z2)
ax.set_title("P2(x,y)=x^3y - xy^3")
plt.show()

# Referencias
# Suma de Euler: https://share.google/tDIUJD67Kjpo1GlAP