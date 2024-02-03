import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Close all open figures
plt.close('all')
%matplotlib qt

# input parameters
# l = 4.0  # connecting rod length -> harmonic
l = 1.2  # connecting rod length -> non-harmonioc
#-----------------------------------------------------------------------------

r = 1.0  # crank radius
rot_num = 4  # number of crank rotations
increment = 0.1  # angle increment

# create the angle array, where the last angle is the number of rotations*2*pi
angles = np.arange(0, rot_num * 2 * pi + increment, increment)

X1 = np.zeros(len(angles))  # array of crank x-positions: Point 1
Y1 = np.zeros(len(angles))  # array of crank y-positions: Point 1
X2 = np.zeros(len(angles))  # array of rod x-positions: Point 2
Y2 = np.zeros(len(angles))  # array of rod y-positions: Point 2

for index, theta in enumerate(angles, start=0):
    x1 = r * cos(theta)  # x-coordinate of the crank: Point 1
    y1 = r * sin(theta)  # y-coordinate of the crank: Point 1
    x2 = 0  # x-coordinate of the rod: Point 2
    # y-coordinate of the rod: Point 2
    y2 = r * sin(theta) + sqrt(l**2 - (r * cos(theta))**2)

    X1[index] = x1  # crankshaft x-position
    Y1[index] = y1  # crankshaft y-position
    X2[index] = x2  # connecting rod x-position
    Y2[index] = y2  # connecting rod y-position

# set up the figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# subplot 1: Piston motion
ax1.set_aspect('equal')
ax1.set_xlim(-4, 4)
ax1.set_ylim(-2, 6)
ax1.grid(True)
ax1.set_title('Piston Motion Animation')
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
line1, = ax1.plot([], [], 'o-', lw=5, color='#de2d26')


# initialization function for subplot 1
def init1():
    line1.set_data([], [])
    return line1,


# animation function for subplot 1
def animate1(i):
    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]

    line1.set_data(x_points, y_points)
    return line1,


# call the animation for subplot 1
ani1 = animation.FuncAnimation(fig, animate1, init_func=init1, frames=len(X1), interval=40, blit=True, repeat=False)

# subplot 2: Piston oscillation
ax2.set_xlim(0, len(X1))
ax2.set_ylim(-2, 6)
ax2.grid(True)
ax2.set_title('Piston Position')
line2, = ax2.plot([], [], lw=2, color='red')

# remove axis ticks on the right subplot
ax2.axes.yaxis.set_ticklabels([])
ax2.axes.xaxis.set_ticklabels([])

# initialization function for subplot 2
def init2():
    line2.set_data([], [])
    return line2,


# animation function for subplot 2
def animate2(i):
    x_points = np.arange(i + 1)
    y_points = Y2[:i + 1]  # Use Y2 for piston oscillation

    line2.set_data(x_points, y_points)
    return line2,


# call the animation for subplot 2
ani2 = animation.FuncAnimation(fig, animate2, init_func=init2, frames=len(X1), interval=40, blit=True, repeat=False)

# show both animations
plt.show()
