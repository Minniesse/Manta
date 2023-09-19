from moviepy.editor import VideoFileClip
import os
import time
import matplotlib.pyplot as plt

# Change file name to wanted video file
mp4_file = 'song.mp4'

# Change to the name of the desired output name
output_directory = 'Frame_song'
os.makedirs(output_directory, exist_ok=True)

# Load the video clip
video = VideoFileClip(mp4_file)

# Initialize variables
frame_count = 0
frames_from_last = 0
frame_save_interval_seconds = 60  # Set the frame save interval to one minute (60 seconds)

# Iterate through the video frames and save one frame every minute
for frame in video.iter_frames(fps=1):  # You can adjust the fps as needed
    frames_from_last += 1

    # Check if it's time to save a frame (every minute)
    if frames_from_last >= frame_save_interval_seconds:
        output_file = os.path.join(output_directory, f'frame_{frame_count:04d}.png')
        plt.imsave(output_file, frame)
        frame_count += 1
        frames_from_last = 0

print(f"Conversion complete. {frame_count} PNG images created in the '{output_directory}' directory.")