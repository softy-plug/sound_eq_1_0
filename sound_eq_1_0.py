import os

os.system("pip install sox")

import sox

import subprocess

# Get all audio files in the current directory
audio_files = [f for f in os.listdir('.') if f.endswith('.wav')]

# Loop through the audio files and apply voice EQ
for audio_file in audio_files:
    # Create a new file name for the EQ'd audio
    eq_file = audio_file.replace('.wav', '_eq.wav')

    # Apply voice EQ using Sox
    subprocess.call(['sox', audio_file, eq_file, 'equalizer 200 1 0.5,400 1 1,800 1 1.5,1600 1 2,3200 1 2.5,6400 1 3,12800 1 3.5'])

# softy_plug