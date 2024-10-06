import tkinter as tk
from tkinter import filedialog
import sounddevice as sd
from scipy.io.wavfile import read, write
from scipy import signal
import threading
import matplotlib.pyplot as plt


class App(tk.Tk):

    recordingName = None
    recording = None
    freq = 44100
    duration = 5
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Audio Recorder")
        self.geometry("300x150")

        # Create an entry text box and a label explaining it
        self.recordingNameTextBox = tk.Entry(self)
        self.recordingNameLabel = tk.Label(self, text="Recording name:")

        # Place entry field and label
        self.recordingNameTextBox.grid(row=0, column=1, columnspan=3, padx=3, pady=3, ipady=3)
        self.recordingNameLabel.grid(row=0, column=0, padx=3, pady=3)

        # Create buttons
        self.saveNameButton = tk.Button(self, text="Ok", command=self.accept_name, bg='powderblue', fg='black', height=1)
        self.recordButton = tk.Button(self, text="Record", command=self.start_recording, bg='blue', fg='white', width=10)
        self.uploadButton = tk.Button(self, text="Upload", command=self.upload, bg='green', fg='white', width=10)

        # Place buttons in the grid
        self.saveNameButton.grid(row=0, column=4, padx=2, pady=2)
        self.recordButton.grid(row=2, column=0, padx=10, pady=10)
        self.uploadButton.grid(row=2, column=1, padx=10, pady=10)

        # Label for recording status
        self.recordingLabel = tk.Label(self, text="", fg="red", font=("Arial", 14))
        self.recordingLabel.grid(row=3, columnspan=2)

    def start_recording(self):
        # Use threading to not block the GUI
        thread = threading.Thread(target=self.record)
        thread.start()

    def record(self):
        # If the user didn't provide a name, give a warning and cancel the operation
        if self.recordingName == None:
            self.recordingLabel.config(text="Enter a name!")
            self.update()
            self.after(3000, self.reset_label)
            return
        
        self.recordingLabel.config(text="Recording...")
        self.update()  # Update the UI to show the label immediately

        freq = self.freq  # Sample frequency
        duration = self.duration  # Recording duration (seconds)
        recName = self.recordingName + ".wav"

        # Start recording
        self.recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait()  # Wait until recording is finished

        # Save the recording
        write(recName, freq, self.recording)

        # Update label to indicate recording has stopped
        self.recordingLabel.config(text="")
        self.update()

        # Plot the recording
        self.plot_audio()

        # Create a spectrogram
        self.create_spectrogram()
        
    def upload(self):
        file = tk.filedialog.askopenfile(mode='r', filetypes=[('Audio files','*.wav')])
        if file is not None:
            Fs, self.recording = read(file.name)
            self.create_spectrogram()

    def accept_name(self):
        self.recordingName = self.recordingNameTextBox.get()
        if self.recordingName == "":
            self.recordingName = None
            self.recordingLabel.config(text="Name can't be empty")
            self.update()
            self.after(3000, self.reset_label)
            return
        self.recordingLabel.config(text="Accepted!", fg="green")
        self.recordingNameTextBox.delete(0, 'end')
        self.update()
        self.after(1000, self.reset_label)

    def reset_label(self):
        self.recordingLabel.config(text="", fg="red")
        self.update()

    def plot_audio(self):

        self.recording = self.recording[:,0]
        plt.figure()
        plt.plot(self.recording)
        plt.xlabel("Sample Index")
        plt.ylabel("Amplitude")
        plt.title("Recording Plot")
        plt.show()

    def create_spectrogram(self):

        self.recording = self.recording[:,0]
        frequencies, times, spectrogram = signal.spectrogram(self.recording, self.freq)

        plt.figure()
        plt.pcolormesh(times, frequencies, spectrogram)
        plt.imshow(spectrogram)
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()

if __name__ == '__main__':
    app = App()
    app.mainloop()
