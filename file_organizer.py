import os
import shutil

# EN: Function to organize files by their extensions
# AZ: Faylları uzantılarına görə qruplaşdıran funksiya
def organize_my_files(directory_path):
    # EN: Check if the path exists / AZ: Yolun mövcudluğunu yoxla
    if not os.path.exists(directory_path):
        print("Path not found! / Yol tapılmadı!")
        return

    # EN: List all files / AZ: Bütün faylları siyahıla
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        # EN: Skip if it's a folder / AZ: Əgər qovluqdursa, keç
        if os.path.isdir(filepath):
            continue

        # EN: Get the file extension (e.g., 'pdf', 'jpg')
        # AZ: Faylın uzantısını götür (məsələn, 'pdf', 'jpg')
        file_ext = filename.split('.')[-1].lower() if '.' in filename else 'others'

        # EN: Create a target folder for this extension
        # AZ: Bu uzantı üçün hədəf qovluğu yarat
        target_folder = os.path.join(directory_path, file_ext)
        
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # EN: Move the file / AZ: Faylı köçür
        try:
            shutil.move(filepath, os.path.join(target_folder, filename))
            print(f"Moved / Köçürüldü: {filename} -> {file_ext}/")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

# Usage / İstifadə:
# target = input("Enter folder path / Qovluq yolunu daxil edin: ")
# organize_my_files(target)
