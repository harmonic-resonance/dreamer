"""
dreamer.py - Main module to process audio and generate video.
"""

import sys
from .audio_processor import AudioProcessor
from .video_generator import VideoGenerator
from .utils import log_message

def run(audio_file="test.wav"):
    """
    Runs the audio analysis and video generation process.
    """
    log_message(f"Starting dreamer for {audio_file}")

    # Analyze the audio
    processor = AudioProcessor(audio_file)
    features = processor.analyze()

    # Generate video frames
    generator = VideoGenerator(audio_file)
    generator.generate_frames()

    log_message("Dreamer process completed")

if __name__ == "__main__":
    audio_file = sys.argv[1] if len(sys.argv) > 1 else "test.wav"
    run(audio_file)

