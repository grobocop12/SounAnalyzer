from scipy.io import wavfile
from scipy import signal
import numpy as np

def get_sample_rate(audio_file):
    rate, data = wavfile.read(audio_file)
    return rate

def get_first_channel(audio_file):
    rate, data = wavfile.read(audio_file)
    print(data.shape)
    data = signal.decimate(data[:,0],10)
    return data.tolist()
