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

### Data
Since there was a lot of data used during the whole process, we sent only the mel spectrograms with 16000 sampling rate (the ones used in best model). They were made from the cleanraw recordings, they are split into training set and test set, they are cut into proper size, and there are necessary csv files as well.

### Models
```separate.py``` is used to separate the test set from training set (already done). ```training_model.ipynb``` has functions for cutting images and creating csv which were used before training the model (the outlook has already cut spectrograms and csv, so no need to use these really). The rest of the notebook is used for training the model, cells should be executed in their respective order. At the end there are functions for saving and simple testing of the model. ```results.ipynb``` allows to test the accuracy of models and calculate the F1. ```loss_plots.ipynb``` allows plotting the loss values which we got during our training. Since models were quite sizeable as well, we are sending only a couple of better ones but I think it is enough given that we are not sending all the data either. The replicable parts of ```results.ipynb``` and ```loss_plots.ipynb``` are at the top and explicitly described as such.

### App
All the app files are in App folder. To run the application user needs to run App/app.py file. Our best model is in file App/model.py.
