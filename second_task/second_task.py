import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, data = wavfile.read('../resources/3.wav')

data_count = data.shape[0]

duration = data_count / sample_rate
t = np.linspace(0, duration, data_count)

plt.plot(t, data)
plt.xlim([0, duration])
plt.yticks(np.linspace(np.floor(np.min(data)), np.ceil(np.max(data)), 9))
plt.grid(True)
plt.tight_layout()
plt.show()

print(duration)

step = 1 / sample_rate

print(step)

w_size = 0.002
w_size_half = w_size / 2
