import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the music mixer
mixer.init()

# Create the main window
window = tk.Tk()
window.title("Music Player")
window.geometry("250x300")  # Set the desired window size
window.configure(bg="lightgray")  # Set the background color

# Function to select and load a music file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        mixer.music.load(file_path)

# Function to play the loaded music file
def play_music():
    mixer.music.play()

# Function to pause the music
def pause_music():
    mixer.music.pause()

# Function to resume the paused music
def resume_music():
    mixer.music.unpause()

# Function to stop the music
def stop_music():
    mixer.music.stop()

# Create a label for the background image

# Create buttons for controlling the music
select_button = tk.Button(window, text="Select File", command=select_file)
select_button.pack()

play_button = tk.Button(window, text="Play", command=play_music)
play_button.pack()

pause_button = tk.Button(window, text="Pause", command=pause_music)
pause_button.pack()

resume_button = tk.Button(window, text="Resume", command=resume_music)
resume_button.pack()

stop_button = tk.Button(window, text="Stop", command=stop_music)
stop_button.pack()

# Run the main window
window.mainloop()
