import subprocess
import pyautogui
import time
import ctypes
import sys

def is_admin():
    """ Check if the script is running with admin privileges """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# If the script is not running with admin privileges, restart it as admin
if not is_admin():
    print("Requesting admin privileges...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

# Define paths to programs
cheat_engine_path = r"C:\Program Files\Cheat Engine 7.5\Cheat Engine.exe"
wizard101_shortcut_path = r"C:\Users\aria\Desktop\wiz.lnk"

# Step 1: Open Cheat Engine
subprocess.Popen(cheat_engine_path)

# Wait for Cheat Engine to load
time.sleep(2)  # Adjust the sleep time if needed for Cheat Engine to fully open

# Step 2: Open Wizard101 using the desktop shortcut
subprocess.Popen(wizard101_shortcut_path, shell=True)

# Wait for Wizard101 to load
time.sleep(5)  # Adjust the sleep time for Wizard101 to fully load the login screen

# Step 3: Automate typing username and password
username = ""
password = ""

# Type the username
pyautogui.write(username)
pyautogui.press('tab')  # Press tab to move to the password field

# Type the password
pyautogui.write(password)
pyautogui.press('enter')  # Press Enter to submit

print("Automation completed.")
