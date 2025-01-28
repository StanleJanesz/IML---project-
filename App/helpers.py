import numpy as np
import librosa
import os
import noisereduce
import soundfile as sf
import matplotlib.pyplot as plt
import glob
from scipy.signal import butter, filtfilt
from scipy.io import wavfile
from pydub import AudioSegment
from pydub.silence import split_on_silence

import os
import torch
import torchvision.transforms.v2 as transforms
from PIL import Image
from model import Net


def denoise_audio(path, RMS_percentile = 25, lowcut = 100, highcut = 500, order = 4):
    data, sr = librosa.load(path, sr = 16000)

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

    # Save denoised audio
    print("Audio denoised")
    sf.write("App/audio/audio_temp.wav", reduced_noise, sr)


def remove_silence():
    audio_format = "wav"
    # Reading and splitting the audio file into chunks
    sound = AudioSegment.from_file("App/audio/audio_temp.wav", format = audio_format) 
    audio_chunks = split_on_silence(sound, min_silence_len = 100, silence_thresh = -45, keep_silence = 50)
    
    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    
    print("Audio silenced")
    combined.export("App/audio/audio_silenced_temp.wav", format = audio_format)


def create_mel_spectrogram():
    data, sample_rate = librosa.load("App/audio/audio_silenced_temp.wav", sr = 16000)

    mel_spectrogram = librosa.feature.melspectrogram(y = data, sr = sample_rate)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref = np.max)

    plt.figure(figsize=(10,5))
    librosa.display.specshow(
        mel_spectrogram_db,
        y_axis = "log",
        x_axis = "time",
        sr = sample_rate,
        cmap = "gray",
    )

    plt.title("Test spectrogram")
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')

    print("Spectrogram created")
    plt.savefig("App/images/image_temp.jpg")
    plt.close()


def predict():
    num_classes = 2
    model = Net(num_classes)
    model.load_state_dict(torch.load("App/model_15_7.pth", map_location=torch.device('cpu')))
    model.eval()

    image = prepare_image()
    output = model(image)

    _, predicted_class = torch.max(output, 1)
    return predicted_class


def prepare_image():
    transform = transforms.Compose(
        [transforms.Resize((96, 194)),transforms.ToImage(),\
        transforms.ToDtype(torch.float32, scale=True),\
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    left = 125
    top = 60
    right = 901
    bottom = 446

    image = Image.open("App/images/image_temp.jpg")
    image = image.crop((left, top, right, bottom))
    image = transform(image)
    image = image.unsqueeze(0)

    return image