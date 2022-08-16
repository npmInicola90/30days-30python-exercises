import numpy as np
import matplotlib.pyplot as plt

# initial conditions
v0 = 10
theta = np.pi/4
g = 9.81

# time
t = np.linspace(0, 2*v0*np.sin(theta)/g, 100)

# x and y components of the velocity
vx = v0*np.cos(theta)
vy = v0*np.sin(theta)

# x and y positions
x = vx*t
y = vy*t - 0.5*g*t**2

# plot the trajectory
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
