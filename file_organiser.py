

import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Archives": [".zip", ".rar"]
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(directory, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, other_path)

    print("Files organized successfully.")

if __name__ == "__main__":
    path = input("Enter directory path to organize: ")
    organize_files(path)
