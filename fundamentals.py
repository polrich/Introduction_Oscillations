import numpy as np
import matplotlib.pyplot as plt

# Close all open figures
plt.close('all')

# Function to plot sine and cosine oscillations with annotations
def plot_sine_cosine(amplitude_sine, amplitude_cosine, mean, phi):
    # Calculate the frequency for two oscillations within the range [0, 4*pi]
    frequency = 2 / (4 * np.pi)

    # Generate time values from 0 to 4pi with a small time step for smooth plotting
    t = np.linspace(0, 4 * np.pi, 1000)

    # Calculate sine and cosine signals
    sine_signal = amplitude_sine * np.sin(2 * np.pi * frequency * t - phi) + mean
    cosine_signal = amplitude_cosine * np.cos(2 * np.pi * frequency * t - phi)

    # Plot the sine and cosine signals with different colors
    plt.figure(figsize=(10, 6))

    plt.plot(t, sine_signal, label=r'x(t) = A sin($\omega$ t - $\varphi$) + $\overline{x}$', linestyle='-', color='blue')
    # plt.plot(t, cosine_signal, label=r'x(t) = A2 cos($\omega$ t - $\varphi$)', linestyle='-', color='red')

    # Highlight amplitude with dashed lines
    plt.axhline(y=amplitude_sine, linestyle='--', color='blue', linewidth=1)
    # plt.axhline(y=amplitude_cosine, linestyle='--', color='red', linewidth=1)

    # Highlight phase with dashed lines
    plt.axvline(x=0, linestyle='--', color='black', linewidth=1, alpha=0.7)
    plt.axvline(x=phi / (2 * np.pi * frequency), linestyle='--', color='black', linewidth=1, alpha=0.7)

    # Set x-ticks to show two periods
    plt.xticks([0, phi, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
               ['0', r'$\varphi$', '$\pi$', '$2\pi$', '$3\pi$', '$4\pi$'], fontsize=16)
    
    # Set plot title and labels
    plt.title('periodic (harmonic) oszillation', fontsize=16)
    plt.xlabel('Time', fontsize=16)
    plt.ylabel('Amplitude', fontsize=16)
    plt.legend(loc='upper right', fontsize=16)
    plt.grid(True)
    
    T = 1 / frequency  # Assuming the first frequency defines the period
    plt.axvline(x=T / 2 + phi, linestyle='--', color='black')
    plt.axvline(x=3 * T / 2 + phi, linestyle='--', color='black')

    plt.text(T / 2 + phi + 0.05, amplitude_sine + 0.1, r'$x(t)$', color='black', ha='left', fontsize=16)
    plt.text(3 * T / 2 + phi + 0.05, amplitude_sine + 0.1, r'$x(t+T)$', color='black', ha='left', fontsize=16)
    
    
    plt.tight_layout()  # Adjust layout to make sure everything is visible
    
    plt.show()

# User-defined parameters
A1 = 2
A2 = 0.5
mean = 1
phi = np.pi / 4  # Phase in radians

# Call the function to generate the plot

plot_sine_cosine(A1, A2, mean, phi)
