import matplotlib.pylab as pylab
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

# Close all open figures
plt.close('all')

from numpy import array  # Add this line to import the array function

def MassSpringDamper(state, t, omega_0, D):
    # unpack the state vector
    x, xd = state  # displacement,x and velocity x'
    # compute acceleration xdd = x''
    xdd = -2 * D * omega_0 * xd - omega_0 * x
    return [xd, xdd]

k = 1  # spring constant, kN/m
m = 1  # mass, Kg
omega_0 = np.sqrt(k / m)  # frequency
T = 2*np.pi/omega_0
    
state0 = [1, 0]  # initial conditions [x0 , v0]  [m, m/sec]
ti = 0.0  # initial time
tf = 20.0  # final time
step = 0.001  # step
t = np.arange(ti, tf, step)

# Plotting displacement for D = 0.05, 1, 2
pylab.rcParams['figure.figsize'] = (15, 12)
pylab.rcParams['font.size'] = 18
fig, ax1 = pylab.subplots()

for D_value in [0.05, 1, 2]:
    state = odeint(MassSpringDamper, state0, t, args=(omega_0, D_value,))
    x = array(state[:, [0]])
    ax1.plot(t, x , label=f'D={D_value}', linewidth=2.0)

# Set xticks at multiples of the period T with labels
xticks = np.arange(0, tf, T)
ax1.set_xticks(xticks)
ax1.set_xticklabels([f'{i} T' for i in range(len(xticks))])

pylab.title('Harmonic, Free, Damped Oscillation', fontsize=16)
ax1.set_xlabel('t', fontsize=16)
ax1.set_ylabel('x', fontsize=16)
ax1.legend(fontsize=16)
pylab.grid()
pylab.show()