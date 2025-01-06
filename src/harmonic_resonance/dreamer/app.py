"""
run the main app
"""
from .dreamer import Dreamer

def run() -> None:
    """
    Runs the Dreamer application with an example audio file.
    """
    example_audio_file = "example.mp3"  # Placeholder for an actual audio file path
    reply = Dreamer(example_audio_file).run()
    print(reply)
