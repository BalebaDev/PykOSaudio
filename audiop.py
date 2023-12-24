import tkinter as tk
import pygame
import os

# Initialize pygame
pygame.init()

# Create the GUI window
window = tk.Tk()
window.title("Audio Player")

# Get the list of audio files in the current directory
audio_files = [file for file in os.listdir() if file.endswith((".mp3", ".ogg", ".wav"))]

# Create a dropdown list to select the audio file
audio_var = tk.StringVar(window)
audio_var.set(audio_files[0])  # Set the default audio file

audio_dropdown = tk.OptionMenu(window, audio_var, *audio_files)
audio_dropdown.pack()

# Create the play button
def play_audio():
    pygame.mixer.music.load(audio_var.get())
    pygame.mixer.music.play()

play_button = tk.Button(window, text="Play", command=play_audio)
play_button.pack()

# Create the pause button
def pause_audio():
    pygame.mixer.music.pause()

pause_button = tk.Button(window, text="Pause", command=pause_audio)
pause_button.pack()

# Create the stop button
def stop_audio():
    pygame.mixer.music.stop()

stop_button = tk.Button(window, text="Stop", command=stop_audio)
stop_button.pack()

# Run the GUI window
window.mainloop()
