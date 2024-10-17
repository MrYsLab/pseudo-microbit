"""
The microphone can respond to a pre-defined set of sound
events that are based on the amplitude and wavelength of the sound.

These sound events are represented by instances of the SoundEvent class,
accessible via variables in microbit.SoundEvent:

    microbit.SoundEvent.QUIET: Represents the transition of sound events,
    from loud to quiet like speaking or background music.

    microbit.SoundEvent.LOUD: Represents the transition of sound events,
    from quiet to loud like clapping or shouting.

    SOUND_EVENT_QUIET = 0
    SOUND_EVENT_LOUD = 1
    SOUND_EVENT_CLAP = 2

"""
import SoundEvent
from typing import Tuple


def current_event() -> SoundEvent:
    """
        Get the last recorded sound event.

    Returns:

        The event, SoundEvent('loud') or SoundEvent('quiet').
    """


def was_event(event: SoundEvent) -> bool:
    """
    Check if a sound was heard at least once since the last call.

    This call clears the sound history before returning.

    Parameters:

        event – The event to check for, such as SoundEvent.LOUD or SoundEvent.QUIET.

    Returns:

        True if sound was heard at least once since the last call, otherwise False.

    """


def is_event(event: SoundEvent) -> bool:
    """
        Check the most recent sound event detected.

    This call does not clear the sound event history.

    Parameters:

        event – The event to check for, such as SoundEvent.LOUD or SoundEvent.QUIET
    Returns:

        True if sound was the most recent heard, False otherwise.

    """


def get_events() -> Tuple:
    """
    Get the sound event history as a tuple.

    This call clears the sound history before returning.

    Returns:

        A tuple of the event history with the most recent event last.

    """


def set_threshold(event: SoundEvent, value: int) -> None:
    """
    Set the threshold for a sound event.

    The SoundEvent.LOUD event will be triggered when the sound level crosses this threshold upwards (from “quiet” to “loud”), and SoundEvent.QUIET event is triggered when crossing the threshold downwards (from “loud” to “quiet”).

    If the SoundEvent.LOUD value set is lower than SoundEvent.QUIET, then “quiet” threshold will be decreased to one unit below the “loud” threshold. If the SoundEvent.QUIET value is set higher than SoundEvent.LOUD, then the “loud” threshold will be set one unit above.

    Parameters:

            event – A sound event, such as SoundEvent.LOUD or SoundEvent.QUIET.

            value – The threshold level in the range 0-255.
            Values outside this range will be clamped.
    """


def sound_level() -> None:
    """
    Get the sound pressure level.

    Returns:

        A representation of the sound pressure level in the range 0 to 255.

    """

