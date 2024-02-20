import numpy as np
import matplotlib.pyplot as plt
import math

# Close all open figures
plt.close('all')

def plot_harmonic_oscillator(frequencies, amplitudes, offsets, phases=None, damping_coefficients=None, duration=3, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration))

    num_oscillations = len(frequencies)
    num_plots = num_oscillations  # Number of subplots

    # Calculate the number of rows and columns for the subplot grid
    num_rows = num_plots
    num_cols = 1   

    # Calculate the figure size based on the screen size
    fig_width = 14 # Limit the figure width to 20 inches
    fig_height = 7  # Limit the figure height based on the number of rows

    plt.figure(figsize=(fig_width, fig_height))
    legend_entries = []  # Store legend entries for each oscillator

    for i, (freq, amp, off, phase, damping) in enumerate(zip(frequencies, amplitudes, offsets, phases, damping_coefficients), start=1):

        signal = amp * np.sin(2 * np.pi * freq * t + phase) * np.exp(-damping * t) + off
        plt.plot(t, signal, label=r'A: {}, $\omega$: {:.1f} rad/s, $\varphi$: {:.2f} rad'.format(amp, freq, phase))
        plt.ylabel('Amplitude',fontsize=16)
        plt.xlabel('time',fontsize=16)
        x_min = np.min(signal)
        x_max = np.max(signal)
        x_mean = (x_max + x_min) / 2
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.legend(loc='upper right', fontsize=16)
        plt.ylim([-3, 3])
        plt.grid(True)



    # Adjust layout and fine-tune the figure
    plt.show()
