import os
import shutil

def transfer_files(text_file, source_folder, destination_folder, ext):
    os.makedirs(destination_folder, exist_ok=True)

    with open(text_file, 'r') as file:
        file_names = [line.strip() for line in file]

    for file_name in file_names:
        source_path = os.path.join(source_folder, f"{file_name}.{ext}")
        destination_path = os.path.join(destination_folder, f"{file_name}.{ext}")
        shutil.copy(source_path, destination_path)

text_files = ['data_prep/ImageSets/Main/train.txt',
    'data_prep/ImageSets/Main/val.txt',
    'data_prep/ImageSets/Main/test.txt']
source_folder = ['data_prep/JPEGImages', 'data_prep/BBoxtexts']
destination_folders = ['images/training', 'images/validation', 'images/testing',
    'labels/training', 'labels/validation', 'labels/testing']

transfer_files(text_files[0], source_folder[0], destination_folders[0], "jpg")
transfer_files(text_files[1], source_folder[0], destination_folders[1], "jpg")
transfer_files(text_files[2], source_folder[0], destination_folders[2], "jpg")

transfer_files(text_files[0], source_folder[1], destination_folders[3], "txt")
transfer_files(text_files[1], source_folder[1], destination_folders[4], "txt")
transfer_files(text_files[2], source_folder[1], destination_folders[5], "txt")

print("File transfer completed.")
