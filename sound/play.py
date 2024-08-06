# This Code is Only for Bluetooth Devices 
# THE BLUETOOTH DEVICE AS CONNECTED DOES SUCCESSFULLY

import pygame

def play_sound(sound_file):
    """
    Play a specific sound file.

    Args:
        sound_file (str): Path to the sound file (e.g., .wav, .mp3)
    """
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
play_sound("connect.mp3")
play_sound("call.mp3")
