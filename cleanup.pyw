import os
import shutil
import ctypes
from ctypes import wintypes

# Function to empty the recycle bin
def empty_recycle_bin():
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 3)
        print("Recycle Bin emptied successfully.")
    except Exception as e:
        print(f"Failed to empty Recycle Bin: {e}")

# Function to clear the specified directory
def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

# Main function to run the tasks
def main():
    # Empty the recycle bin
    empty_recycle_bin()

    # Clear temp folder
    temp_folder = os.environ.get("TEMP")
    clear_folder(temp_folder)

    # Clear %temp% folder
    temp_percent_folder = os.environ.get("TMP")
    clear_folder(temp_percent_folder)

if __name__ == "__main__":
    main()
