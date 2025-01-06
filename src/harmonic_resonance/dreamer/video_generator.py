"""
video_generator.py - Handles the creation of video frames based on audio features.
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import subprocess

class VideoGenerator:
    def __init__(self, audio_file):
        self.audio_file = audio_file
        self.y, self.sr = librosa.load(audio_file)
        
        # Audio features
        self.spectrogram = librosa.feature.melspectrogram(y=self.y, sr=self.sr)
        self.rms = librosa.feature.rms(y=self.y)[0]
        self.tempo, self.beat_frames = librosa.beat.beat_track(y=self.y, sr=self.sr)
        self.onset_env = librosa.onset.onset_strength(y=self.y, sr=self.sr)
        self.chromagram = librosa.feature.chroma_stft(y=self.y, sr=self.sr)
        
        # Normalize features
        self.spec_norm = librosa.power_to_db(self.spectrogram, ref=np.max)
        self.spec_norm = (self.spec_norm - self.spec_norm.min()) / (self.spec_norm.max() - self.spec_norm.min())

    def generate_frames(self):
        """
        Generates video frames with multiple visualization layers based on audio features.
        """
        fig, ax = plt.subplots(figsize=(10, 10))
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_aspect('equal')
        ax.axis('off')

        # Create visualization elements
        main_circle = plt.Circle((0, 0), 0.2, color='white', alpha=0.8)
        freq_circles = [plt.Circle((0, 0), r, color='blue', alpha=0.2) 
                       for r in np.linspace(0.3, 0.8, 5)]
        particles = [plt.Circle((np.random.uniform(-1, 1), np.random.uniform(-1, 1)), 
                              0.02, color='white', alpha=0.5) for _ in range(20)]
        
        # Add all artists
        ax.add_artist(main_circle)
        for circle in freq_circles:
            ax.add_artist(circle)
        for particle in particles:
            ax.add_artist(particle)

        def update(frame):
            frame = frame % len(self.rms)
            
            # Update main circle based on RMS
            rms_value = self.rms[frame]
            main_circle.set_radius(0.2 + rms_value * 0.3)
            
            # Color based on chromagram
            chroma = self.chromagram[:, frame % self.chromagram.shape[1]]
            hue = np.argmax(chroma) / 12.0
            main_circle.set_color(plt.cm.hsv(hue))
            
            # Update frequency circles based on spectrogram
            spec_slice = self.spec_norm[:, frame % self.spec_norm.shape[1]]
            for i, circle in enumerate(freq_circles):
                freq_band = spec_slice[i * 10:(i + 1) * 10].mean()
                circle.set_radius(0.3 + i * 0.1 + freq_band * 0.2)
                circle.set_alpha(0.2 + freq_band * 0.5)
            
            # Update particles
            onset_strength = self.onset_env[frame % len(self.onset_env)]
            for particle in particles:
                if np.random.random() < 0.1:
                    particle.center = (np.random.uniform(-1, 1), np.random.uniform(-1, 1))
                x, y = particle.center
                angle = np.arctan2(y, x)
                r = np.sqrt(x**2 + y**2)
                r += onset_strength * 0.1
                if r > 1:
                    r = np.random.uniform(0, 0.2)
                new_x = r * np.cos(angle)
                new_y = r * np.sin(angle)
                particle.center = (new_x, new_y)
            
            # Beat detection effect
            if frame in self.beat_frames:
                main_circle.set_color('red')
                for circle in freq_circles:
                    circle.set_alpha(0.8)
            
            return [main_circle] + freq_circles + particles

        # Reduce the number of frames by using a smaller subset of the audio data
        num_frames = min(1000, len(self.rms))  # Limit to 1000 frames or the length of RMS
        ani = animation.FuncAnimation(fig, update, frames=range(num_frames), blit=True)
        # Save video without audio first
        temp_video = 'temp_visualization.mp4'
        ani.save(temp_video, fps=30, extra_args=['-vcodec', 'libx264'])
        
        # Merge video with audio using ffmpeg
        output_video = 'audio_visualization.mp4'
        cmd = [
            'ffmpeg', '-y',
            '-i', temp_video,
            '-i', self.audio_file,
            '-c:v', 'copy',
            '-c:a', 'aac',
            output_video
        ]
        subprocess.run(cmd)
        
        # Clean up temporary file
        subprocess.run(['rm', temp_video])

def test_video_generation():
    """
    Test function to generate video frames from a test audio file.
    """
    audio_file = "test.wav"
    video_generator = VideoGenerator(audio_file)
    video_generator.generate_frames()
    print("Test video generation completed for", audio_file)

if __name__ == "__main__":
    test_video_generation()

