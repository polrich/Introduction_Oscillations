"""
Editor: Richard Polzer
Date: 19.01.2024

This code shall help students to play with oscillations.
User entries:
    frequencies [list]: provide a list of desired frequencies in hz
    amplidues [list]:: provide a list of corresponding amplitures
    means [list]:: provide a list of corresponding mean values
    phases [list]:: provide a list of corresponding phase values
"""

import numpy as np
%matplotlib qt

from free_harmonic_oscillator_plot import plot_harmonic_oscillator

# user entries
frequencies = [1, 0.5]  # frquencies in Hertz: f1, f2, f3, ...
amplitudes = [1, 1]  # corresponding amplitudes: A1, A2, A3, ...
means = [0, 0,]  # corresponding mean values: x_mean1, x_mean2, x_mean3, ...
phases = [0, 0]  # corresponding phasen; phi1, phi2, phi3,...
damping_coefficients = [0, 0] 
#  

# Plot individual oscillations
"""
This code will plot for each of your provided parameters the corresponding oscillation
x1(t) = A1 * sin(2 * pi * f1 *t + phi1) + x_mean1
x2(t) = A2 * sin(2 * pi * f2 *t + phi2) + x_mean2
...
"""
# plot_superimposed_oscillations(frequencies, amplitudes, means, phases=phases)
plot_harmonic_oscillator(frequencies, amplitudes, means, phases=phases, damping_coefficients=damping_coefficients)
