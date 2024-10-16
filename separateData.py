import os
import shutil

def separate_audio_files(root_folder, target_folder, class_one_indicators):
    # Create class directories if they don't exist
    class_one_folder = os.path.join(target_folder, 'Class_One')
    class_two_folder = os.path.join(target_folder, 'Class_Two')

    os.makedirs(class_one_folder, exist_ok=True)
    os.makedirs(class_two_folder, exist_ok=True)

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.wav'):
                full_path = os.path.join(dirpath, filename)

                # Check if any of the class one indicators are in the filename
                if any(indicator in filename for indicator in class_one_indicators):
                    # Move it to class one folder
                    shutil.move(full_path, class_one_folder)
                    print(f"Copied {full_path} to {class_one_folder}")
                else:
                    # Move it to class two folder
                    shutil.move(full_path, class_two_folder)
                    print(f"Copied {full_path} to {class_two_folder}")

# Example usage
root_folder = "C:\\Users\\lgors\\Downloads\\daps\\daps"  # Replace with your root folder path
target_folder = "C:\\Users\\lgors\\Downloads\\daps\\daps"  # Replace with the destination folder path
class_one_indicators = ['f1', 'f7', 'f8', 'm3', 'm6', 'm8']  # Replace with your actual indicators

separate_audio_files(root_folder, target_folder, class_one_indicators)
