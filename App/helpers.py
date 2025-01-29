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


def denoise_audio(path, RMS_percentile = 25, lowcut = 100, highcut = 1000, order = 4):
    """Gets audio file and removes background noise"""
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
    sf.write("App/audio/audio.wav", reduced_noise, sr)


def remove_silence():
    """Removes silence parts from denoised audio"""
    audio_format = "wav"
    # Reading and splitting the audio file into chunks
    sound = AudioSegment.from_file("App/audio/audio.wav", format = audio_format) 
    audio_chunks = split_on_silence(sound, min_silence_len = 100, silence_thresh = -45, keep_silence = 50)
    
    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    
    print("Audio silenced")
    combined.export("App/audio/audio_silenced.wav", format = audio_format)




def split_audio_to_segments(data, sample_rate, segment_duration = 2):
    """Splits silenced and denoised audio into segments of specified duration ready to be saved"""
    segment_samples = int(segment_duration * sample_rate)
    segments = []

    for i in range(len(data)//segment_samples):
        segment = data[i * segment_samples:(i + 1) * segment_samples]
        segments.append(segment)

    return segments

def segments_to_wav(segments, sample_rate):
    """Saves segments into .wav files"""

    for i, segment in enumerate(segments):
        path = f"App/audio/parts/audio_silenced_part_{i+1}.wav"
        wavfile.write(path, sample_rate, segment)

def cut_file(segments_duration = 2):
    """Splits audio file and saves it into .wav files"""

    clean_folder("App/audio/parts")
    file_path = "App/audio/audio_silenced.wav"
    sample_rate, data = wavfile.read(file_path)

    # Checking if stereo (using only mono)
    if len(data.shape) == 2:
        data = data[:0]

    segments = split_audio_to_segments(data, sample_rate, segments_duration)
    segments_to_wav(segments, sample_rate)




def create_mel_spectrograms(path, path_out="App/images"):
    """Creates spectrograms for denoised and silenced audio parts"""
    clean_folder("App/images")

    for file in os.listdir(path):
        if(file.endswith(".wav")):
            data, sample_rate = librosa.load(f"{path}/{file}", sr = 16000)
            base_name = os.path.splitext(os.path.basename(file))[0]

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

            plt.title(base_name)
            plt.ylabel('Frequency [Hz]')
            plt.xlabel('Time [sec]')
            plt.savefig(f"{path_out}/image_{base_name}.jpg")
            plt.close()


def predict(path):
    """Uses best model to predict class for file"""
    num_classes = 2
    model = Net(num_classes)
    model.load_state_dict(torch.load("App/model_15_7.pth", map_location=torch.device('cpu')))
    model.eval()

    positives = 0
    all = 0
    result = 0

    for file in os.listdir(path):
        if(file.endswith(".jpg")):
            image = prepare_image(file)
            output = model(image)

            _, predicted_class = torch.max(output, 1)
            
            all += 1
            positives += predicted_class.item()

    ratio = positives / all
    if ratio > 0.7:
        result = 1
    else:
        result = 0

    return result



def prepare_image(file):
    """Prepares image to passing it to model"""
    transform = transforms.Compose(
        [transforms.Resize((96, 194)),transforms.ToImage(),\
        transforms.ToDtype(torch.float32, scale=True),\
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    left = 125
    top = 60
    right = 901
    bottom = 446

    image = Image.open(f"App/images/{file}")
    image = image.crop((left, top, right, bottom))
    image = transform(image)
    image = image.unsqueeze(0)

    return image


def clean_folder(path):
    """Cleans folder before adding new files"""
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        os.remove(file_path)