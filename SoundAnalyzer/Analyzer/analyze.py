from scipy.io import wavfile
from scipy import signal
import scipy
import numpy as np


def get_sample_rate(audio_file):
    rate, data = wavfile.read(audio_file)
    return rate


def analyze(audio_file):
    downscaling = 11
    rate, data = wavfile.read(audio_file)
    time = calculate_time(len(data), rate)
    data = signal.decimate(data[:, 0], downscaling)
    time = signal.decimate(time[:], downscaling)
    spectrogram = signal.spectrogram(data, fs=rate, mode='psd')
    return data.tolist(), time.tolist(), spectrogram


def calculate_time(number_of_samples, sample_rate):
    time = np.arange(0, number_of_samples)
    dT = 1.0 / sample_rate
    time = np.dot(time, dT)
    return time
