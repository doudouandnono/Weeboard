import keyboard
from loguru import logger
from os.path import exists
from playsound import playsound
from threading import Thread


def play_sound(sound_file_path):
    playsound(sound_file_path)

def on_key_press(event):
    if event.name.isalpha():
        sound_file_path = f"sound/{event.name}.wav"
        if not exists(sound_file_path):
            return logger.warning(f"Key {event.name.upper()} is missing a sound effect.")
        thread = Thread(target=play_sound, args=(sound_file_path,))
        return thread.start()

logger.info("Script is ready, type something! ;)")
try:   
    keyboard.on_press(on_key_press)
    keyboard.wait()
except KeyboardInterrupt:
    logger.info("Weeboard Script Terminated")