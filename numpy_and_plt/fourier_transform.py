import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.arange(0, 1, 1 / fs)
f1 = 1

signal = 1* np.sin(2 * np.pi * f1 * t)

fft = np.fft.fft(signal) / len(signal)

fft_magnitude = abs(fft)

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.grid()

plt.subplot(2, 1, 2)

length = len(signal)
f = np.linspace(-(fs / 2), fs / 2, length)

plt.stem(f, np.fft.fftshift(fft_magnitude))
plt.ylim(0, 2.5)
plt.grid()

plt.show()