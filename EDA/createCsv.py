import cv2
import numpy as np
import csv
import os
import pandas as pd
import cv2
import numpy as np
from skimage.feature import graycomatrix, graycoprops 
import matplotlib.pyplot as plt

def mean_color(image):
    mean_b = np.mean(image[:,:,0])  
    mean_g = np.mean(image[:,:,1])  
    mean_r = np.mean(image[:,:,2])  
    return mean_r, mean_g, mean_b


def mean_brightness(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.mean(gray_image)


def mean_saturation(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mean_s = np.mean(hsv_image[:,:,1])  # Nasycenie (S)
    return mean_s

def contrast(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.std(gray_image)

class_one_indicators = ['f1_', 'f7_', 'f8_', 'm3_', 'm6_', 'm8_'] 

class_one_test = ['f1_script2_cleanraw', 'f8_script3_cleanraw', 'f8_script5_cleanraw', 'm8_script2_cleanraw', 'm8_script3_cleanraw', 'm8_script4_cleanraw', 'f7_script4_ipadflat_confroom1', 'm3_script3_ipadflat_confroom1', 'm6_script1_ipadflat_confroom1', 'm6_script4_ipadflat_confroom1', 'f1_script2_ipadflat_office1', 'f7_script3_ipadflat_office1', 'f7_script4_ipadflat_office1', 'f8_script3_ipadflat_office1', 'm3_script3_ipadflat_office1', 'm3_script4_ipadflat_office1', 'f8_script3_ipad_balcony1', 'm3_script1_ipad_balcony1', 'f8_script4_ipad_bedroom1', 'm3_script2_ipad_bedroom1', 'm6_script3_ipad_bedroom1', 'm6_script5_ipad_bedroom1', 'm8_script3_ipad_bedroom1', 'f7_script2_ipad_confroom1', 'f8_script4_ipad_confroom1', 'm3_script4_ipad_confroom1', 'm6_script2_ipad_confroom1', 'm8_script2_ipad_confroom1', 'm8_script3_ipad_confroom1', 'f1_script3_ipad_confroom2', 'f7_script1_ipad_confroom2', 'f7_script2_ipad_confroom2', 'm3_script5_ipad_confroom2', 'm6_script2_ipad_confroom2', 'm6_script3_ipad_confroom2', 'm8_script1_ipad_confroom2', 'f7_script1_ipad_livingroom1', 'f7_script4_ipad_livingroom1', 'f8_script5_ipad_livingroom1', 'm3_script2_ipad_livingroom1', 'm6_script4_ipad_livingroom1', 'm6_script5_ipad_livingroom1', 'm8_script5_ipad_livingroom1', 'f1_script3_ipad_office1', 'f7_script1_ipad_office1', 'm8_script5_ipad_office1', 'f1_script4_ipad_office2', 'f7_script2_ipad_office2', 'm3_script2_ipad_office2', 'f1_script3_iphone_balcony1', 'f7_script5_iphone_balcony1', 'f8_script2_iphone_balcony1', 'f8_script3_iphone_balcony1', 'm3_script3_iphone_balcony1', 'm6_script3_iphone_balcony1', 'm6_script5_iphone_balcony1', 'f1_script2_iphone_bedroom1', 'f8_script3_iphone_bedroom1', 'f8_script4_iphone_bedroom1', 'm8_script5_iphone_bedroom1']

class_zero_test = ['f10_script2_cleanraw', 'f2_script3_cleanraw', 'f4_script4_cleanraw', 'f5_script1_cleanraw', 'f6_script5_cleanraw', 'f9_script2_cleanraw', 'm2_script5_cleanraw', 'm5_script2_cleanraw', 'f10_script5_ipadflat_confroom1', 'f4_script3_ipadflat_confroom1', 'f9_script3_ipadflat_confroom1', 'm1_script5_ipadflat_confroom1', 'm2_script4_ipadflat_confroom1', 'm4_script2_ipadflat_confroom1', 'm7_script4_ipadflat_confroom1', 'm9_script5_ipadflat_confroom1', 'f10_script4_ipadflat_office1', 'f2_script2_ipadflat_office1', 'f4_script1_ipadflat_office1', 'f5_script1_ipadflat_office1', 'f5_script5_ipadflat_office1', 'f6_script1_ipadflat_office1', 'm10_script1_ipadflat_office1', 'm2_script3_ipadflat_office1', 'm4_script3_ipadflat_office1', 'm7_script2_ipadflat_office1', 'm7_script3_ipadflat_office1', 'm9_script3_ipadflat_office1', 'f10_script3_ipad_balcony1', 'f2_script3_ipad_balcony1', 'f4_script5_ipad_balcony1', 'f5_script1_ipad_balcony1', 'f5_script3_ipad_balcony1', 'f5_script4_ipad_balcony1', 'f6_script4_ipad_balcony1', 'f9_script1_ipad_balcony1', 'f9_script3_ipad_balcony1', 'm10_script3_ipad_balcony1', 'm10_script4_ipad_balcony1', 'm1_script5_ipad_balcony1', 'm9_script4_ipad_balcony1', 'f2_script1_ipad_bedroom1', 'f4_script4_ipad_bedroom1', 'f6_script1_ipad_bedroom1', 'f9_script3_ipad_bedroom1', 'm4_script2_ipad_bedroom1', 'm7_script2_ipad_bedroom1', 'm7_script5_ipad_bedroom1', 'f10_script3_ipad_confroom1', 'f3_script4_ipad_confroom1', 'f5_script5_ipad_confroom1', 'f6_script5_ipad_confroom1', 'm4_script3_ipad_confroom1', 'm9_script4_ipad_confroom1', 'm9_script5_ipad_confroom1', 'f2_script2_ipad_confroom2', 'f4_script3_ipad_confroom2', 'm1_script2_ipad_confroom2', 'm1_script5_ipad_confroom2', 'm5_script5_ipad_confroom2', 'f2_script4_ipad_livingroom1', 'f3_script4_ipad_livingroom1', 'f4_script2_ipad_livingroom1', 'f5_script3_ipad_livingroom1', 'f6_script1_ipad_livingroom1', 'f6_script4_ipad_livingroom1', 'm10_script5_ipad_livingroom1', 'm2_script2_ipad_livingroom1', 'm2_script5_ipad_livingroom1', 'm4_script4_ipad_livingroom1', 'm4_script5_ipad_livingroom1', 'm5_script1_ipad_livingroom1', 'm9_script2_ipad_livingroom1', 'f10_script1_ipad_office1', 'f10_script2_ipad_office1', 'f10_script3_ipad_office1', 'f10_script5_ipad_office1', 'f2_script3_ipad_office1', 'f5_script1_ipad_office1', 'f6_script5_ipad_office1', 'f9_script1_ipad_office1', 'm10_script1_ipad_office1', 'm10_script4_ipad_office1', 'm1_script2_ipad_office1', 'm2_script1_ipad_office1', 'm2_script3_ipad_office1', 'm2_script4_ipad_office1', 'm2_script5_ipad_office1', 'm5_script2_ipad_office1', 'm7_script2_ipad_office1', 'm7_script5_ipad_office1', 'f2_script3_ipad_office2', 'f4_script1_ipad_office2', 'f5_script1_ipad_office2', 'm1_script2_ipad_office2', 'm2_script4_ipad_office2', 'm4_script1_ipad_office2', 'm4_script2_ipad_office2', 'm4_script4_ipad_office2', 'm4_script5_ipad_office2', 'm5_script2_ipad_office2', 'm5_script3_ipad_office2', 'm5_script5_ipad_office2', 'm7_script2_ipad_office2', 'f10_script1_iphone_balcony1', 'f10_script4_iphone_balcony1', 'f2_script3_iphone_balcony1', 'f2_script4_iphone_balcony1', 'f2_script5_iphone_balcony1', 'm1_script2_iphone_balcony1', 'm2_script2_iphone_balcony1', 'm2_script4_iphone_balcony1', 'm4_script4_iphone_balcony1', 'm4_script5_iphone_balcony1', 'm7_script3_iphone_balcony1', 'm7_script4_iphone_balcony1', 'm9_script2_iphone_balcony1', 'm9_script4_iphone_balcony1', 'f2_script5_iphone_bedroom1', 'f4_script3_iphone_bedroom1', 'f5_script2_iphone_bedroom1', 'f5_script4_iphone_bedroom1', 'f6_script2_iphone_bedroom1', 'f6_script3_iphone_bedroom1', 'm10_script3_iphone_bedroom1', 'm10_script4_iphone_bedroom1', 'm1_script2_iphone_bedroom1', 'm4_script3_iphone_bedroom1', 'm4_script5_iphone_bedroom1', 'm9_script3_iphone_bedroom1', 'f3_script4_iphone_livingroom1', 'f3_script5_iphone_livingroom1', 'f4_script2_iphone_livingroom1', 'f4_script5_iphone_livingroom1', 'f6_script1_iphone_livingroom1', 'f9_script2_iphone_livingroom1', 'm1_script2_iphone_livingroom1', 'm2_script4_iphone_livingroom1', 'm4_script4_iphone_livingroom1', 'm7_script1_iphone_livingroom1']

def calculate_texture_homogeneity(image_path):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    

    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    image = np.uint8(image / np.max(image) * 255)


           
    glcm = graycomatrix(image, distances=[1], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4], symmetric=True, normed=True)

    homogeneity = graycoprops(glcm, prop='homogeneity')
    
  
    average_homogeneity = np.mean(homogeneity)
    return average_homogeneity


def calculate_edge_density(image_path, low_threshold=100, high_threshold=200):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    

    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    edges = cv2.Canny(image, low_threshold, high_threshold)
    

    edge_pixels = np.count_nonzero(edges)  
    

    total_pixels = image.size

    edge_density = edge_pixels / total_pixels

    return edge_density







def save_features_to_csv(image_path, output_csv,class_one_indicators,class_one_test,class_zero_test):

    image = cv2.imread(image_path)
    
    if image is None:
        print("Błąd wczytywania obrazu.")
        return
    

    mean_r, mean_g, mean_b = mean_color(image)
    mean_brightness_value = mean_brightness(image)
    mean_saturation_value = mean_saturation(image)
    contrast_value = contrast(image)
    edge_density = calculate_edge_density(image_path, 100, 00)
    homogeneity = calculate_texture_homogeneity(image_path)

    with open(output_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        

        if file.tell() == 0:
            writer.writerow(["Image","Person","Gender","Script","AudioType","IsTestSet","Class", "Mean_R", "Mean_G", "Mean_B", "Mean_Brightness", "Mean_Saturation", "Contrast","Homogeneity","Edge_density"])
        split_string = image_path.split("\\")
        photoName = split_string[len(split_string)-1]
        gender = photoName[0]
        if any(indicator in photoName for indicator in class_one_indicators):
            PhotoClass = 1
        else:
            PhotoClass = 0
        if any(indicator in photoName for indicator in class_one_test):
            IsTestSet = 1  
        elif any(indicator in photoName for indicator in class_zero_test):
            IsTestSet = 1
        else:
            IsTestSet = 0
        if (gender == "f") :
            gender = "Female"
        else :
            gender = "Male"
        Person = photoName.split("_")[0]
        script = photoName.split("_")[1]
        AudioType = photoName.split("_")[2]
 
        writer.writerow([image_path,Person,gender,script,AudioType,IsTestSet ,PhotoClass, mean_r, mean_g, mean_b, mean_brightness_value, mean_saturation_value, contrast_value,homogeneity,edge_density])
    

output_csv = "featuresOld.csv"  
folder_path = 'C:\\studia\\IML\\cropedold'
image_extensions = ['.jpg',  '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']


image_files = []
i = 0

for file in os.listdir(folder_path):

    if any(file.lower().endswith(ext) for ext in image_extensions):
        i =i+1
        save_features_to_csv(os.path.join(folder_path, file), output_csv,class_one_indicators,class_one_test,class_zero_test) 
        print(f"Cecha obrazu {i} została zapisana.")

