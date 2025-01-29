import tkinter as tk
import time
from tkinter import filedialog
import sounddevice as sd
from scipy.io.wavfile import write
from scipy import signal
import threading
import matplotlib.pyplot as plt


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Audio Recorder")
        self.geometry("300x150")

        self.recordingName = None  # Name of the recording
        self.recording = None     # Data of the recording
        self.freq = 44100         # Sample frequency
        self.duration = 6         # Duration in seconds

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



    def upload(self):
        file_path = filedialog.askopenfilename(filetypes=[('Audio files', '*.wav')])
        if not file_path:
            self.recordingLabel.config(text="Error")
            return
        
        self.recognize(file_path)

    def start_recording(self):
        if not self.recordingName:
            self.recordingLabel.config(text="Enter a name first!")
            self.after(2000, self.reset_label)
            return
        
        thread = threading.Thread(target=self.record)
        #thread.start()

    def record(self):
        try:         
            self.recordingLabel.config(text="Recording...")
            # Start recording
            self.recording = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=2)
            sd.wait()  # Wait until recording is finished

            # Save the recording
            #file_path = f"App/audio/recorded_{self.recordingName}.wav"
            file_path = f"App/recordings/recording.wav"
            write(file_path, self.freq, self.recording)

            # Update label to indicate recording has stopped
            self.recordingLabel.config(text="Saved!")
            self.update()
            
            #self.recognize(file_path, cut=False)
            
        except Exception as e:
            self.recordingLabel.config(text=f"Error: {e}")
        finally:
            self.after(5000, self.reset_label)
 
    def accept_name(self):
        name = self.recordingNameTextBox.get().strip()
        if name:
            self.recordingName = name
        else:
            self.recordingLabel.config(text="Enter a valid name!")
            self.after(3000, self.reset_label)

    def reset_label(self):
        self.recordingLabel.config(text="")
        self.update()

    def recognize(self, file_path, cut=True):
        from helpers import denoise_audio, remove_silence, cut_file, create_mel_spectrograms, predict
        
        self.recordingLabel.config(text="Processing...")
        self.update()

        denoise_audio(file_path)
        remove_silence()
        if cut:
            cut_file()
            create_mel_spectrograms('App/audio/parts')
            predicted_class = predict('App/images')
        else:
            create_mel_spectrograms('App/recordings', 'App/recordings')
            predicted_class = predict('App/recordings')

        print(f"Predicted class: {predicted_class}")
        if predicted_class == 1:
            self.recordingLabel.config(text="Voice accepted!", fg="green")
        else:
            self.recordingLabel.config(text="Voice declined!", fg="red")


if __name__ == '__main__':
    app = App()
    app.mainloop()
