"""
The machine module contains specific functions related to the
micro:bit hardware. Most functions in this module allow to
achieve direct and unrestricted access to and control of hardware blocks o
n a system (like CPU, timers, buses, etc.). Used incorrectly,
this can lead to malfunction, lockups,
crashes of your board, and in extreme cases, hardware damage.
"""


def unique_id() -> bytes:
    """
    Returns a byte string with a unique identifier of a board.
    It will vary from one board instance to another.
    """


def reset() -> None:
    """
    Resets the device in a manner similar to pushing the external RESET button.
    """


def freq() -> int:
    """
    Returns CPU frequency in hertz.
    """


def disable_irq() -> int:
    """
    Disable interrupt requests. Returns the previous IRQ state
    which should be considered an opaque value.
    This return value should be passed to the machine.enable_irq()
    function to restore interrupts to their original state,
    before machine.disable_irq() was called.
    """


def enable_irq(state: int) -> None:
    """
    Re-enable interrupt requests.
    The state parameter should be the value that was returned
    from the most recent call to the machine.disable_irq() function.
    """


def time_pulse_us(pin: int, pulse_level: int, timeout_us: int = 1000000):
    """
    Time a pulse on the given pin, and return the duration of
    the pulse in microseconds. The pulse_level argument should be
    0 to time a low pulse or 1 to time a high pulse.

    If the current input value of the pin is different to pulse_level,
    the function first (*) waits until the pin input becomes equal to pulse_level,
    then (**) times the duration that the pin is equal to pulse_level.
    If the pin is already equal to pulse_level then timing starts straight away.

    The function will return -2 if there was timeout waiting for
    condition marked (*) above, and -1 if there was timeout during the
    main measurement, marked (**) above. The timeout is the same for
    both cases and given by timeout_us (which is in microseconds).

    """
