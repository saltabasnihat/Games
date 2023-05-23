import os
import shutil

def create_folder_structure():
    base_directory = '/home/pi'
    folders = [
        'cst8254/backup',
        'cst8254/python',
        'Linux/Labs/Lab1',
        'Linux/Labs/Lab2',
        'Linux/Labs/Lab3',
        'Linux/Lectures/Week1',
        'Linux/Lectures/Week2',
        'Linux/Lectures/Week3'
    ]

    for folder in folders:
        full_path = os.path.join(base_directory, folder)
        os.makedirs(full_path, exist_ok=True)

    print("Folder structure created successfully!")

if __name__ == '__main__':
    create_folder_structure()
