import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


def get_psk_signal(mod_signal, carrier_frequency):
    return np.sin(carrier_frequency * 2 * np.pi * np.linspace(0, 1, mod_signal.size) + np.pi * mod_signal)


def main():
    bits_count = 25
    carrier_frequency = 5000
    width = 10000

    mod_sequence = np.random.randint(0, 2, bits_count)

    mod_signal = np.repeat(mod_sequence, width)
    psk_signal = get_psk_signal(mod_signal, carrier_frequency)

    plt.figure(figsize=(14, 5))
    plt.grid(True)
    plt.plot(psk_signal)
    plt.plot(mod_signal, '--')
    plt.show()

    wavfile.write("msg.wav", width, psk_signal)

    np.savetxt('source_sequence.txt', mod_sequence, fmt="%i", newline=' ')


main()
