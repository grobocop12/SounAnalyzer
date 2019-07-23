from scipy.io import wavfile
from scipy import signal
import numpy as np


def get_sample_rate(audio_file):
    rate, data = wavfile.read(audio_file)
    return rate


def get_first_channel(audio_file):
    downsampling = 11
    rate, data = wavfile.read(audio_file)

    time = calculate_time(len(data), rate)
    data = signal.decimate(data[:, 0], downsampling)
    time = signal.decimate(time[:], downsampling)
    return data.tolist(), time.tolist()


def calculate_time(number_of_samples, sample_rate):
    time = np.arange(0, number_of_samples)
    dT = 1.0 / sample_rate
    time = np.dot(time, dT)
    return time