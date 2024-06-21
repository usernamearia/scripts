import subprocess
import os
import time
import pyautogui # type: ignore

# Path to VLC executable
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

# Path to the folder containing media files
media_folder_path = r"C:\Users\ariaa\Videos\the office"

def play_media_folder(vlc_path, media_folder_path):
    try:
        # Ensure the folder path is valid
        if not os.path.isdir(media_folder_path):
            print(f"Error: The folder '{media_folder_path}' does not exist.")
            return

        # Command to open VLC and play the media folder
        command = [vlc_path, media_folder_path]

        # Run the command
        subprocess.Popen(command)
        print(f"Playing media from folder: {media_folder_path}")

        # Wait for VLC to open and start playing
        time.sleep(1)  # Adjust this delay as needed

        # Send the "f" keystroke to enter full screen
        pyautogui.press('f')
        print("Toggled full screen mode in VLC")

        # Send the "ctrl + h" keystroke to hide controls
        pyautogui.hotkey('ctrl', 'h')
        print("Toggled hiding controls in VLC")

        # Send the "r" keystroke to turn on random
        pyautogui.press('r')
        print("Turned on random mode in VLC")

        # Send the "n" keystroke 5 times with 0 second delay
        for _ in range(5):
            pyautogui.press('n')
        print("Played the next episode 5 times in VLC")

        # Send the "s" keystroke to turn on subtitles
        pyautogui.press('s')
        print("Turned on subtitles in VLC")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    play_media_folder(vlc_path, media_folder_path)
