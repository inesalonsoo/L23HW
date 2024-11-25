import numpy as np
import matplotlib.pyplot as plt


def plot_sine_wave(frequency=1, amplitude=1, duration=2, sample_rate=1000):
    """
    This function plots a sine wave.

    The parameters are the following:
        duration: duration of the wave in seconds
        amplitude: amplitude of the sine wave
        frequency: frequency of the sine wave (Hz)
        sample_rate: number of samples per second
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Time axis
    y = amplitude * np.sin(2 * np.pi * frequency * t)  # Sine wave formula
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label=f'{frequency} Hz Sine Wave')
    plt.title('Sine Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()
    plt.show()


# Example usage
if __name__ == "__main__":
    plot_sine_wave(frequency=10, amplitude=1)


