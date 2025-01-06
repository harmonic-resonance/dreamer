"""
dreamer.py - Main module to process audio and generate video.
"""

from audio_processor import AudioProcessor
from video_generator import VideoGenerator
from utils import log_message

def main(audio_file):
    log_message("Starting dreamer process")

    # Process audio
    audio_processor = AudioProcessor(audio_file)
    audio_features = audio_processor.analyze()

    # Generate video
    video_generator = VideoGenerator(audio_features)
    video_generator.generate_frames()

    log_message("Dreamer process completed")

if __name__ == "__main__":
    main("example_audio.mp3")
