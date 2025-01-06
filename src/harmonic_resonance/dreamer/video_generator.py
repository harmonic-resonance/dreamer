"""
video_generator.py - Handles the creation of video frames based on audio features.
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class VideoGenerator:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.y, self.sr = librosa.load(audio_file)
        self.spectrogram = librosa.feature.melspectrogram(y=self.y, sr=self.sr)
        self.rms = librosa.feature.rms(y=self.y)[0]
        self.tempo, self.beat_frames = librosa.beat.beat_track(y=self.y, sr=self.sr)

    def generate_frames(self):
        """
        Generates video frames based on the provided audio features.
        """
        fig, ax = plt.subplots()
        circle = plt.Circle((0.5, 0.5), 0.1, color='blue')
        ax.add_artist(circle)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')

        def update(frame):
            circle.set_radius(self.rms[frame % len(self.rms)] * 0.5)
            return circle,

        ani = animation.FuncAnimation(fig, update, frames=range(len(self.y)), blit=True)
        ani.save('audio_visualization.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

def test_video_generation():
    """
    Test function to generate video frames from a test audio file.
    """
    audio_file = "test.wav"
    video_generator = VideoGenerator(audio_file)
    video_generator.generate_frames()
    print("Test video generation completed for test.wav")

