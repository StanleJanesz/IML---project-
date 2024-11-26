import cv2
import numpy as np
import csv
import os
# Funkcja obliczająca średni kolor obrazu w przestrzeni RGB
def mean_color(image):
    mean_b = np.mean(image[:,:,0])  # Średni kolor niebieski (B)
    mean_g = np.mean(image[:,:,1])  # Średni kolor zielony (G)
    mean_r = np.mean(image[:,:,2])  # Średni kolor czerwony (R)
    return mean_r, mean_g, mean_b

# Funkcja obliczająca średnią jasność obrazu
def mean_brightness(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.mean(gray_image)

# Funkcja obliczająca średnie nasycenie obrazu w przestrzeni HSV
def mean_saturation(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mean_s = np.mean(hsv_image[:,:,1])  # Nasycenie (S)
    return mean_s

# Funkcja obliczająca kontrast obrazu
def contrast(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.std(gray_image)

# Funkcja zapisująca cechy do pliku CSV
def save_features_to_csv(image_path, output_csv):
    # Wczytanie obrazu
    image = cv2.imread(image_path)
    
    if image is None:
        print("Błąd wczytywania obrazu.")
        return
    
    # Obliczenie cech
    mean_r, mean_g, mean_b = mean_color(image)
    mean_brightness_value = mean_brightness(image)
    mean_saturation_value = mean_saturation(image)
    contrast_value = contrast(image)
    
    # Zapis do pliku CSV  
    with open(output_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Zapis nagłówka, jeśli plik jest pusty
        if file.tell() == 0:
            writer.writerow(["Image","Person","Gender", "Mean_R", "Mean_G", "Mean_B", "Mean_Brightness", "Mean_Saturation", "Contrast"])
        split_string = image_path.split("\\")
        photoName = split_string[len(split_string)-1]
        gender = photoName[0]
        if (gender == "f") :
            gender = "Female"
        else :
            gender = "Male"
        Person = photoName.split("_")[0]
        # Zapis danych obrazu
        writer.writerow([image_path,Person,gender, mean_r, mean_g, mean_b, mean_brightness_value, mean_saturation_value, contrast_value])
    
   # print(f"Cecha obrazu {image_path} została zapisana.")

# Przykład użycia
image_paths = ["obraz1.jpg", "obraz2.jpg", "obraz3.jpg"]  # Lista ścieżek do obrazów
output_csv = "features.csv"  # Nazwa pliku CSV, do którego zapisujemy cechy
folder_path = 'C:\\studia\\IML\\croped'
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

    # List to store image file paths
image_files = []
i = 0
    # Loop through all files in the folder
for file in os.listdir(folder_path):
        # Check if the file has an image extension
    if any(file.lower().endswith(ext) for ext in image_extensions):
        i =i+1
        save_features_to_csv(os.path.join(folder_path, file), output_csv) 
        print(f"Cecha obrazu {i} została zapisana.")


# Example usage
#folder_path = 'path/to/your/folder'  # Replace with the path to your folder

#for image_path in image_paths:
   # save_features_to_csv(image_path, output_csv)
