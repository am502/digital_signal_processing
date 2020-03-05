import matplotlib.pyplot as plt
import numpy as np
import statistics


def quantize(signal, max_amplitude, bits):
    levels = 2 ** bits / 2
    step = max_amplitude / levels
    return np.round(signal / step) * step


def calculate_snr_by_power(signal, noise):
    power_s = (signal * signal).sum()
    power_n = (noise * noise).sum()
    return 10 * np.log10(power_s / power_n)


def calculate_snr_by_st_dev(signal, noise):
    st_dev_s = statistics.stdev(signal)
    st_dev_n = statistics.stdev(noise)
    return 10 * np.log10(st_dev_s * st_dev_s / st_dev_n / st_dev_n)


def calculate_snr(bits):
    return 6.02 * bits - 7.2


def first_signal(bits):
    time_of_view = 1

    amplitude = 32767
    sample_rate = 1000
    frequency = 10

    phase = 0

    time_vector = np.linspace(0, time_of_view, sample_rate)

    signal = amplitude * np.sin(2 * np.pi * frequency * time_vector + phase)

    quantized_signal = quantize(signal, amplitude, bits)

    plt.plot(time_vector, signal)
    plt.stem(time_vector, quantized_signal, 'r', markerfmt='ro', use_line_collection=True)
    plt.xlim([0, time_of_view])
    plt.yticks(np.linspace(np.floor(np.min(signal)), np.ceil(np.max(signal)), 9))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    noise = signal - quantized_signal

    print('First signal.\nSNR (power): %f\nSNR (standard deviation): %f' % (calculate_snr_by_power(signal, noise),
                                                                            calculate_snr_by_st_dev(signal, noise)))


def second_signal(bits):
    high = 32767
    low = -32767

    signal = np.random.uniform(low, high, 1000)

    quantized_signal = quantize(signal, high, bits)

    noise = signal - quantized_signal

    print('Second signal.\nSNR (power): %f\nSNR (standard deviation): %f' % (calculate_snr_by_power(signal, noise),
                                                                             calculate_snr_by_st_dev(signal, noise)))


def main():
    bits = 16

    print('Theoretical SNR: %f' % calculate_snr(bits))
    first_signal(bits)
    second_signal(bits)


main()
