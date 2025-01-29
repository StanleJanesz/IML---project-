import os
import scipy.io.wavfile as wv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import filedialog as fd
import time
from joblib import Parallel, delayed
from itertools import chain
from operator import methodcaller
import seaborn as sns
import librosa
from sklearn.preprocessing import LabelEncoder

# Calculate the hours and minutes from seconds
def output_duration(length): 
    hours = length // 3600
    length %= 3600
    mins = length // 60
    length %= 60
    seconds = length
  
    return hours, mins, seconds 

# Collect all the wav files for analysis
def collect_wav_files(root_folder):
    wav_files = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.wav'):
                full_path = os.path.join(dirpath, filename)
                wav_files.append(full_path)
    return wav_files

# Read the wav file and return the time and sample rate
def get_audio_length(file):
    sample_rate, data = wv.read(file)
    len_data = len(data)
    t = len_data / sample_rate

        
    return t, sample_rate

# Manually find the maximum, minimum and mean value of amplitude from the file, iterating over each array entry
def get_audio_minmax(file):
    _, data = wv.read(file)
    minVal = 100000
    maxVal = -100000
    sumVal = 0.0
    for datapoint in data:
        if(datapoint<minVal):
            minVal = datapoint
        if(datapoint>maxVal):
            maxVal = datapoint
        sumVal += datapoint

    meanVal = sumVal / len(data)
    return maxVal, minVal, meanVal

def create_plots(file, foldername):

    # Create folders for the plots to be created
    plotdirname = foldername + "/Plots"
    wvdirname = plotdirname + "/Waveforms"
    sptdirname = plotdirname + "/Spectrograms"
    fftdirname = plotdirname + "/FFTs"

    # Get the file name without the path
    basefilename, _ = os.path.splitext(os.path.basename(file))

    # Use librosa to load the audio
    y, sample_rate = librosa.load(file)
    audio_file, _ = librosa.effects.trim(y)

    # Display the waveform
    plt.figure(figsize = (16,6))
    librosa.display.waveshow(y = audio_file, sr = sample_rate, color = "#C0FFEE")
    plt.title(f'Sound waves for file {os.path.basename(file)}', fontsize=23)

    # Save the waveform to the appropriate folder
    os.chdir(wvdirname)
    plt.savefig(basefilename+"_waveform"+".jpg")
    os.chdir(foldername)

    # Create an STFT of the audio file - unused in the actual EDA process or the project, just an experiment. The STFT are also pretty time-consuming to create, so use with caution 
    n_fft = 2048
    hop_length = 512

    D = np.abs(librosa.stft(audio_file, n_fft=n_fft, hop_length=hop_length))
    plt.figure(figsize=(16,6))
    plt.plot(D)

    os.chdir(fftdirname)
    plt.savefig(basefilename+"_fft"+".jpg")
    os.chdir(foldername)
    

def get_folder_paths():
    print('Please select the directory with class one files.')
    classOne = fd.askdirectory()
    print('Now, please select the directory with class zero files.')
    classZero = fd.askdirectory()
    return classOne, classZero

def analyze_file(file, foldername):
    maxVal, minVal, meanVal, = get_audio_minmax(file)
    t, sr = get_audio_length(file)

    # Function for creating the plots, but it does take some time
    # create_plots(file, foldername)

    return {
        'file_name': file,
        'duration': t,
        'amplitude_max': maxVal,
        'amplitude_min': minVal,
        'amplitude_mean': meanVal
    }

# The main function for analysing the data
def analyze_files(folder, foldername):

    plotdirname = foldername + "/Plots"
    wvdirname = plotdirname + "/Waveforms"
    sptdirname = plotdirname + "/Spectrograms"
    fftdirname = plotdirname + "/FFTs"

    # Create the folders if they don't exist
    if not os.path.isdir(plotdirname):
        os.makedirs(plotdirname)

    if not os.path.isdir(wvdirname):
        os.makedirs(wvdirname)

    if not os.path.isdir(sptdirname):
        os.makedirs(sptdirname)    

    if not os.path.isdir(fftdirname):
        os.makedirs(fftdirname)

    # Process the files in parallel and save as a data frame
    results = Parallel(n_jobs=10, verbose = 10)(delayed(analyze_file)(file, foldername) for file in folder)
    results_df = pd.DataFrame(results)

    # Print the number of duplicate values
    print('Duplicate Values:')
    print(results_df.nunique())

    # Create histograms of numerical columns and plot them on a single page
    sns.set_style("darkgrid")
    numerical_columns = results_df.select_dtypes(include=["int64", "float64", "int16"]).columns
    plt.figure(figsize=(14, len(numerical_columns) * 3))
    for idx, feature in enumerate(numerical_columns, 1):
        plt.subplot(len(numerical_columns), 2, idx)
        sns.histplot(results_df[feature], kde=True)
        plt.title(f"{feature} | Skewness: {round(results_df[feature].skew(), 2)}")
    plt.tight_layout(pad=3)

    # Create a pairplot
    sns.set_palette("Pastel1")
    sns.pairplot(results_df)

    plt.tight_layout()
    plt.show()
    
    return results_df

# Function for processing the .csv file generated from spectrograms
def process_csv(file):
    csv = pd.read_csv(file)

    # Use LabelEncoder to enumerate variables like Person or Gender
    label_encoder = LabelEncoder()
    print(csv.head())

    print(csv.describe())

    print(csv.dtypes)

    # Drop redundant columns
    csv = csv.drop(['Image', 'Mean_Saturation', 'Mean_Brightness', 'Mean_G', 'Mean_B'], axis=1)
    categorical_columns = csv.select_dtypes(include=["object"]).columns
    for column in categorical_columns:
        csv[column] = label_encoder.fit_transform(csv[column])

    # Create histograms
    sns.set_style("darkgrid")
    numerical_columns = csv.select_dtypes(include=["int64", "float64", "int16"]).columns
    plt.figure(figsize=(14, len(numerical_columns) * 3), layout='constrained')
    for idx, feature in enumerate(numerical_columns, 1):
        plt.subplot(len(numerical_columns), 2, idx)
        sns.histplot(csv[feature], kde=True)
        plt.title(f"Skewness: {round(csv[feature].skew(), 2)}")
    plt.show()

    # Create box plots of the variables
    plt.figure(figsize=(14, len(numerical_columns) * 3), layout='constrained')
    for idx, feature in enumerate(numerical_columns, 1):
        plt.subplot(len(numerical_columns), 2, idx)
        sns.boxplot(x=csv[feature])
    plt.show()

    # Calculate the Interquantile Range
    Q1 = csv.quantile(0.25)
    Q3 = csv.quantile(0.75)
    IQR = Q3 - Q1
    print(IQR)

    # Generate a heat map
    plt.figure(figsize=(10,5), layout='constrained')
    c = csv.corr()
    sns.heatmap(c, cmap="BrBG", annot=True)

    plt.show()
    


    

def analyze_csv():

    file = fd.askopenfilename(title="Select a File", filetypes=[("Comma Separated Value Files", "*.csv")])
    if file:
        process_csv(file)
    


if __name__ == '__main__':

    # Analysis of .wav files is inefficient and provide little to no useful information, so the functions are commented out, and only the csv analysis is run
    '''
    folder_path_one, folder_path_zero = get_folder_paths()
    wav_files_one = collect_wav_files(folder_path_one)
    wav_files_zero = collect_wav_files(folder_path_zero)

    print('Wav files collected. Beginning analysis...')
    class_one_df = analyze_files(wav_files_one, folder_path_one)
    class_zero_df = analyze_files(wav_files_zero, folder_path_zero)
    '''
    analyze_csv()

    
      

