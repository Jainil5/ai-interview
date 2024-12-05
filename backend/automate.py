import os
import pygame

# Folder containing the audio files
audio_folder = "audio_files"

# Initialize pygame mixer
pygame.mixer.init()

# Get a sorted list of all audio files in the folder
audio_files = sorted(
    [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]
)

if not audio_files:
    print(f"No audio files found in the folder: {audio_folder}")
else:
    print("Starting audio playback. Press Enter after each file to play the next one.")
    for i, audio_file in enumerate(audio_files, 1):
        audio_path = os.path.join(audio_folder, audio_file)
        print(f"\nPlaying file {i}/{len(audio_files)}: {audio_file}")
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        # Wait for the user to press Enter before stopping playback
        input("Press Enter for the next audio...\n")
        pygame.mixer.music.stop()

    print("All audio files have been played.")
