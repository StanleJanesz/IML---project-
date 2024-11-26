import numpy as np
import librosa
import noisereduce
from scipy.signal import butter, filtfilt

def denoise_audio(data, sr, RMS_percentile = 25, lowcut = 100, highcut = 1000, order = 4):

    rms = librosa.feature.rms(y = data)[0]
    threshold = np.percentile(rms, RMS_percentile)
    noise_indices = np.where(rms < threshold)[0]

    if len(noise_indices) > 0:
        noise_sample = data[noise_indices[0]*512 : noise_indices[0]*512 + int(sr * 2)]
        reduced_noise = noisereduce.reduce_noise(y = data, sr = sr, y_noise = noise_sample)
    else:
        nyquist = 0.5 * sr
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(order, [low, high], btype = 'bandstop', analog = False)
        reduced_noise = filtfilt(b, a, data)

    return reduced_noise