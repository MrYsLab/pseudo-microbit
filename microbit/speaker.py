"""
The micro:bit V2 has a built-in speaker located on the rear of the board.
speaker on rear of micro:bit V2

By default, sound output will be via the edge connector on
pin 0 and the built-in speaker V2. You can connect wired headphones or a
speaker to pin 0 and GND on the edge connector to hear the sounds.

The speaker can be turned off or on using the functions listed here.
"""


def off() -> None:
    """
    Use off() to turn off the speaker. This does not disable sound
    output to an edge connector pin.
    """


def on() -> None:
    """
    Use on() to turn on the speaker.
    """
