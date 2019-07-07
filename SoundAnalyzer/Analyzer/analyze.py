from scipy.io import wavfile


def get_sample_rate(audio_file):
    rate, data = wavfile.read(audio_file)
    return rate
