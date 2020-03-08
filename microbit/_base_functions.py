"""Top-level functions defined in micro:bit's Micropython."""


def panic(n: int) -> None:
    """Enter a panic mode. Requires restart. Pass in an arbitrary integer <= 255
    to indicate a status::

        microbit.panic(255)
    """


def reset() -> None:
    """Restart the board."""


def sleep(n: int) -> None:
    """Wait for ``n`` milliseconds. One second is 1000 milliseconds, so::

        microbit.sleep(1000)

    will pause the execution for one second.  ``n`` can be an integer or
    a floating point number.
    """


def running_time() -> int:
    """Return the number of milliseconds since the board was switched on or
    restarted.
    """


def temperature() -> int:
    """Return the temperature of the micro:bit in degrees Celcius."""
