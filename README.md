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
```separate.py``` is used to separate the test set from training set. ```training_model.ipynb``` has functions for cutting images and creating csv which are needed before training the model. The rest of the notebook is used for training the model, cells shoudl be executed in their respective order. At the end there are functions for saving and simple testing of the model. ```results.ipynb``` allows to test the accuracy of models and calculate the F1. ```loss_plots.ipynb``` allows plotting the loss values which we got during our training.

### App
All the app files are in App folder. To run the application user needs to run App/app.py file. Our best model is in file App/model.py.
