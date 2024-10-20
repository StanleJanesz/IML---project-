import os
import scipy.io.wavfile as wv
import matplotlib.pyplot as plt
import numpy as np

def output_duration(length): 
    hours = length // 3600  # calculate in hours 
    length %= 3600
    mins = length // 60  # calculate in minutes 
    length %= 60
    seconds = length  # calculate in seconds 
  
    return hours, mins, seconds 

def collect_wav_files(root_folder):
    wav_files = []  # List to store the paths of .wav files
    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.wav'):
                # Construct the full file path and append to the list
                full_path = os.path.join(dirpath, filename)
                wav_files.append(full_path)
    return wav_files

def get_audio_length(file):
    sample_rate, data = wv.read(file)
    len_data = len(data)
    t = len_data / sample_rate
        
    return t, sample_rate

def get_audio_minmax(file):
    _, data = wv.read(file)
    return max(data), min(data)

    
    

# Example usage
folder_path_one = "C:\\Users\\lgors\\Downloads\\daps\\daps\\Class_One"
folder_path_two = "C:\\Users\\lgors\\Downloads\\daps\\daps\\Class_Two"
wav_files_one = collect_wav_files(folder_path_one)
wav_files_two = collect_wav_files(folder_path_two)

print('Wav files collected. Beginning analysis...')

t1 = 0
t2 = 0
srprev = 0
isSame = True
isSame2 = True
srSum = 0
srSum2 = 0
maxSum = 0.0
minSum = 0.0
maxMax = 0.0
minMin = 1000000.0
it = 1


for file in wav_files_one:
    print('Loading: {:.2f}%'.format(it/1500 * 100))
    it += 1
    t, sr = get_audio_length(file)
    if srprev != 0:
        if sr != srprev:
            isSame = False
    srprev = sr
    t1 += t
    srSum += sr

    maxTemp, minTemp = get_audio_minmax(file)
    maxSum += maxTemp
    minSum += minTemp
    if maxTemp > maxMax:
        maxMax = maxTemp
    if minTemp < minMin:
        minMin = minTemp

classOneMax = maxMax
classOneMin = minMin
classOneMeanMax = maxSum / len(wav_files_one)
classOneMeanMin = minSum / len(wav_files_one)
maxSum = 0.0
minSum = 0.0
maxMax = 0.0
minMin = 1000000.0

srprev = 0
for file in wav_files_two:
    print('Loading: {:.2f}%'.format(it/1500 * 100))
    t, sr = get_audio_length(file)
    if srprev != 0:
        if sr != srprev:
            isSame2 = False
    srprev = sr
    t2 += t
    srSum += sr

    maxTemp, minTemp = get_audio_minmax(file)
    maxSum += maxTemp
    minSum += minTemp
    if maxTemp > maxMax:
        maxMax = maxTemp
    if minTemp < minMin:
        minMin = minTemp

classZeroMax = maxMax
classZeroMin = minMin
classZeroMeanMax = maxSum / len(wav_files_two)
classZeroMeanMin = minSum / len(wav_files_two)

if(isSame == False or isSame2 == False):
    print("Sample rates differ")
    

hoursOne, minutesOne, secondsOne = output_duration(int(t1))
hoursTwo, minutesTwo, secondsTwo = output_duration(int(t2))

print('ANALYSIS COMPLETE!')

print(f"Number of files in class One: {len(wav_files_one)}")
print(f"Number of files in class Zero: {len(wav_files_two)}")

print('Total duration of Class One files: {}:{}:{}'.format(hoursOne, minutesOne, secondsOne))
print('Total duration of Class Zero files: {}:{}:{}'.format(hoursTwo, minutesTwo, secondsTwo))

print('Mean sample rate for Class One: {}'.format(srSum/len(wav_files_one)))
print('Mean sample rate for Class Zero: {}'.format(srSum/len(wav_files_two)))

print('Maximum amplitude for class one: {}'.format(classOneMax))
print('Minimum amplitude for class one: {}'.format(classOneMin))
print('Mean maximum amplitude for files in class one: {}'.format(classOneMeanMax))
print('Mean minimum amplitude for files in class one: {}'.format(classOneMeanMin))

print('Maximum amplitude for class zero: {}'.format(classZeroMax))
print('Minimum amplitude for class zero: {}'.format(classZeroMin))
print('Mean maximum amplitude for files in class zero: {}'.format(classZeroMeanMax))
print('Mean minimum amplitude for files in class zero: {}'.format(classZeroMeanMin))


      

