import numpy as np
import matplotlib.pyplot as plt
import math

# Close all open figures
plt.close('all')

def plot_superimposed_oscillations(frequencies, amplitudes, offsets, phases=None, damping_coefficients=None, duration=3, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate * duration))

    num_oscillations = len(frequencies)
    num_plots = num_oscillations + 1  # Number of subplots

    # Calculate the number of rows and columns for the subplot grid
    num_rows = num_plots
    num_cols = 1   

    # Calculate the figure size based on the screen size
    screen_size = plt.rcParams["figure.figsize"]
    fig_width = min(20, screen_size[0])  # Limit the figure width to 20 inches
    fig_width = 10 # Limit the figure width to 20 inches
    fig_height = min(6 * num_rows, screen_size[1])  # Limit the figure height based on the number of rows
    fig_height = 10  # Limit the figure height based on the number of rows

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(fig_width, fig_height), sharex=True)

    for i, (freq, amp, off, phase, damping) in enumerate(zip(frequencies, amplitudes, offsets, phases, damping_coefficients), start=1):
        if num_cols > 1:
            row = (i - 1) // num_cols
            col = (i - 1) % num_cols
            subplot = axes[row, col]
        else:
            subplot = axes[i - 1]

        signal = amp * np.sin(2 * np.pi * freq * t + phase) * np.exp(-damping * t) + off
        subplot.plot(t, signal, label=f'Frequency: {freq} Hz, Amplitude: {amp}, Phase: {phase} rad, Damping: {damping}')
        subplot.set_title(f'Individual Oscillation {i}')
        subplot.set_ylabel('Amplitude')
        x_min = np.min(signal)
        x_max = np.max(signal)
        x_mean = (x_max + x_min) / 2
        subplot.axhline(y=x_max, linestyle='--', color='black')
        subplot.axhline(y=x_min, linestyle='--', color='black')
        subplot.axhline(y=x_mean, linestyle='--', color='black')
        subplot.set_yticks([x_min, x_mean, x_max, 0],
                           [f'$x_{{\min}}$ = {x_min:.1f}', f'$\overline{{x}}$ = {x_mean:.1f}',
                            f'$x_{{\max}}$ = {x_max:.1f}', '0'],
                           fontsize=16)
        subplot.legend()
        subplot.grid(True)

    superimposed_signal = np.sum([amp * np.sin(2 * np.pi * freq * t + phase) * np.exp(-damping * t) + off for freq, amp, off, phase, damping in
                                  zip(frequencies, amplitudes, offsets, phases, damping_coefficients)], axis=0)

    row_superimposed = num_rows - 1
    col_superimposed = num_cols - 1
    if num_cols > 1:
        subplot_superimposed = axes[row_superimposed, col_superimposed]
    else:
        subplot_superimposed = axes[row_superimposed]

    subplot_superimposed.plot(t, superimposed_signal, linewidth=2, color='red')
    if max(abs(superimposed_signal))<1e-5:
        subplot_superimposed.set_ylim([-1, 1])
    subplot_superimposed.set_title('Superimposed Oscillation')
    subplot_superimposed.set_xlabel('Time (seconds)')
    subplot_superimposed.set_ylabel('Amplitude')
    x_min = np.min(superimposed_signal)
    x_max = np.max(superimposed_signal)
    x_mean = (x_max + x_min) / 2
    subplot_superimposed.axhline(y=x_max, linestyle='--', color='black')
    subplot_superimposed.axhline(y=x_min, linestyle='--', color='black')
    subplot_superimposed.axhline(y=x_mean, linestyle='--', color='black')
    subplot_superimposed.set_yticks([x_min, x_mean, x_max, 0],
                                     [f'$x_{{\min}}$ = {x_min:.1f}', f'$\overline{{x}}$ = {x_mean:.1f}',
                                      f'$x_{{\max}}$ = {x_max:.1f}', '0'],
                                     fontsize=16)
    subplot_superimposed.grid(True)

    # Adjust layout and fine-tune the figure
    plt.tight_layout()
    plt.subplots_adjust(top=0.95, right=0.95, hspace=0.5)
    plt.show()
