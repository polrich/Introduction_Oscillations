import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

# Close all open figures
plt.close('all')

def damped_oscillation(t, omega_0, D, x_0, v_0):
    omega_d = omega_0 * np.sqrt(1 - D**2)
    if D < 1:
        A = np.sqrt((omega_d**2 * x_0**2 + (v_0**2+D*omega_0*x_0)**2)/omega_d**2)
        phi = np.arctan(omega_d*x_0/(v_0+D*omega_0*x_0))
        
        x = A * np.exp(-D * omega_0 * t) * np.sin(omega_d * t + phi)
        
    elif D>1:
        l_1 = -D*omega_0 - omega_0*np.sqrt(D**2 -1)
        l_2 = -D*omega_0 + omega_0*np.sqrt(D**2 -1)
        a_1 = (-v_0 + (-D + np.sqrt(D**2 -1))*omega_0*x_0)/(2*omega_0*np.sqrt(D**2-1))
        a_2 = (+v_0 + (+D + np.sqrt(D**2 -1))*omega_0*x_0)/(2*omega_0*np.sqrt(D**2-1))
        
        x = np.exp(-D*omega_0*t)*( a_1 * np.exp( -np.sqrt(D**2-1) * omega_0 * t ) + a_2 * np.exp( np.sqrt(D**2-1) * omega_0 * t ) )
        
    elif D==1:
        a_1 = x_0
        a_2 = v_0 + omega_0 * x_0
        
        x = (a_1 + a_2*t)*np.exp(-omega_0*D*t)
    return x

# Parameters
A = 1.0          # Amplitude
omega_0 = 1.0    # Angular frequency
T = 2*np.pi/omega_0
Ds = [0.05, 1, 2]  # Different values of Damping ratio

# Format the legend labels dynamically
legs = [f'D={D}' for D in Ds]

# Time values
t_end = 20
t = np.linspace(0, t_end, 1000)

# Plotting for different D values
plt.figure(figsize=(15, 8))
for D, leg in zip(Ds, legs):
    x = damped_oscillation(t, omega_0, D, 1, 0)
    plt.plot(t, x, label=leg)
    
# Set xticks at multiples of the period T with labels
xticks = np.arange(0, t_end, T)
plt.xticks(xticks, labels=[f'{i} T' for i in range(len(xticks))])



plt.title('Harmonic, Free, Damped Oscillation', fontsize=16)
plt.xlabel('t', fontsize=16)
plt.ylabel('x', fontsize=16)
plt.legend(fontsize=16)
plt.grid(True)
# plt.xticks([]) 
plt.show()