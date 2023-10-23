# -*- coding: utf-8 -*-
"""
Created on Wed Nov 9 12:45:54 2022

@author: Fady_
"""
import os
import csv
from heic2png import HEIC2PNG

# Source and destination folders
source_folder = "~/put/your/Source/path/folder"
destination_folder = "~/put/your/destination/path"

# Create the destination folder if it doesn't exist☺
os.makedirs(destination_folder, exist_ok=True)

# Function to split a list into chunks of a given size
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

# Get a list of HEIC files in the source folder
heic_files = [filename for filename in os.listdir(source_folder) if filename.lower().endswith(".heic")]

# Calculate the number of subfolders needed
num_subfolders = (len(heic_files) + 49) // 50

# Create subfolders and convert images
total_converted = 0
total_failed = 0
all_errors = []

for i, chunk in enumerate(chunk_list(heic_files, 50)):
    subfolder_path = os.path.join(destination_folder, f"subfolder_{i+1}")
    os.makedirs(subfolder_path, exist_ok=True)
    
    converted_in_subfolder = 0
    failed_in_subfolder = []
    
    for filename in chunk:
        heic_path = os.path.join(source_folder, filename)
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(subfolder_path, png_filename)
        
        try:
            # Convert HEIC to PNG
            heic_img = HEIC2PNG(heic_path)
            heic_img.save(png_path)
            print(f"Converted {filename} to {png_filename} in subfolder_{i+1}")
            converted_in_subfolder += 1
            total_converted += 1
        except Exception as e:
            print(f"Error converting {filename}: {e}")
            failed_in_subfolder.append(filename)
            all_errors.append({"Filename": filename, "Error": str(e)})
            total_failed += 1
    
    print(f"Subfolder_{i+1} stats: Converted: {converted_in_subfolder}, Failed: {len(failed_in_subfolder)}")
    print(f"Failed images in Subfolder_{i+1}: {failed_in_subfolder}")
    print("-------------------------")

print("Conversion complete.")
print(f"Total Converted: {total_converted}, Total Failed: {total_failed}")

# Export errors to a CSV file
csv_file = "C:/Users/Fady/Downloads/MU/conv1/conversion_errors.csv"
with open(csv_file, mode="w", newline="") as file:
    fieldnames = ["Filename", "Error"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_errors)

print(f"Conversion errors exported to '{csv_file}'.")
