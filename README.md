### Cleaning and pre-processing
There is dedicated notebook for denoising of audio called ```denoiseAudio_notebook.ipynb``` and for spectrogram creation called ```Spectrogram_notebook.ipynb```. Other files such as ```denoiseAudio.py``` and ```Spectrogram.ipynb``` contain mostly the same code but ready for final solution use.

### EDA
main files used to perform EDA are located in EDA folder. 

Stanislaw Janowicz
* createCSV - was beeing used to extract selected features from spectogrms>  
* testEDA2 and NewEDA - contain functions used to create plots helping discover features of spectograms
* EDA_plots - contains plots on which data interpretation was based (main results of exploration are included in report) \

Lukasz Gorski
* performEDA - runs simple EDA on wav files and some on spectgrams 
* EDAplots - plots acquired with perform EDA

### Models

### App
All the app files are in App folder. To run the application user needs to run App/app.py file. Our best model is in file App/model.py.
