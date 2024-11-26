from PIL import Image
import os
training_directory = "C:\\studia\\IML\\spec\\Spectrograms_mel"
left = 125
top = 60
right = 901
bottom = 446
target = "C:\\studia\\IML\\croped\\"
# Opens a image in RGB mode
for filename in os.listdir(training_directory):
    fullpath = os.path.join(training_directory, filename) 
    im = Image.open(fullpath)
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
# width, height = im.size
 
# Setting the points for cropped image

 
# Cropped image of above dimension
# (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im1.save(target + filename)
# Shows the image in image viewer