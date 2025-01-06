"""
run the main app
"""
from .dreamer import Dreamer


def run() -> None:
    reply = Dreamer().run()
    print(reply)
