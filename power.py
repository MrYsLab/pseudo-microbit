from typing import Tuple

"""
This module lets you manage the power modes of the micro:bit V2.

There are two micro:bit board low power modes that can be requested from MicroPython:

    Deep Sleep: Low power mode where the board can
                be woken up via multiple sources (pins, button presses,
                uart data, or a timer) and resume operation.

    Off: The power mode with the lowest power consumption, the only way
        to wake up the board is via the reset button, or by plugging the USB cable
        while on battery power. When the board wakes up it will
        restart and execute your programme from the beginning.

"""


def off() -> None:
    """
    Power down the board to the lowest possible power mode.

    This is the equivalent to pressing the reset button for a few second,
    to set the board in “Off mode”.

    The micro:bit will only wake up if the reset button is pressed or,
    if on battery power, when a USB cable is connected.

    When the board wakes up it will start for a reset state, so your
    programme will start running from the beginning.
    """


def deep_sleep(ms: int = None, wake_on: tuple = None, run_every: bool = True) -> None:
    """
    Set the micro:bit into a low power mode where it can wake
    up and continue operation.

    The programme state is preserved and when it wakes up it will
    resume operation where it left off.

    Deep Sleep mode will consume more battery power than Off mode.

    The wake up sources are configured via arguments.

    The board will always wake up when receiving UART data, when
    the reset button is pressed (which resets the board) or,
    in battery power, when the USB cable is inserted.

    When the run_every parameter is set to True (the default),
    any function scheduled with microbit.run_every will momentarily wake
    up the board to run and when it finishes it will go back to sleep.

    Parameters:

            ms – A time in milliseconds to wait before it wakes up.

            wake_on – A single instance or a tuple of pins and/or buttons
                      to wake up the board, e.g. deep_sleep(wake_on=button_a)
                      or deep_sleep(wake_on=(pin0, pin2, button_b)).

            run_every – A boolean to configure if the functions scheduled
                        with microbit.run_every will continue to run while it sleeps.


    """