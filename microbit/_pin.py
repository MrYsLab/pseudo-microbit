"""Definitions related to the hardware pins."""


class MicroBitDigitalPin:
    """
    The pull mode for a pin is automatically configured when the pin changes to an
    input mode. Input modes are when you call ``read_analog`` / ``read_digital`` /
    ``is_touched``. The pull mode for these is, respectively, ``NO_PULL``,
    ``PULL_DOWN``, ``PULL_UP``. Only when in ``read_digital`` mode can you call
    ``set_pull`` to change the pull mode from the default.
    """

    NO_PULL: int = 0
    PULL_UP: int = 1
    PULL_DOWN: int = 2

    def read_digital(self) -> int:
        """Return 1 if the pin is high, and 0 if it's low."""

    def set_pull(self, value: int = (NO_PULL or PULL_UP or PULL_DOWN)) -> None:
        """Set the pull state to one of three possible values: ``pin.PULL_UP``,
        ``pin.PULL_DOWN`` or ``pin.NO_PULL`` (where ``pin`` is an instance of
        a pin). See below for discussion of default pull states.
        """

    def write_digital(self, value: int) -> None:
        """Set the pin to high if ``value`` is 1, or to low, if it is 0."""

    def write_analog(self, value: int) -> None:
        """Output a PWM signal on the pin, with the duty cycle proportional to
        the provided ``value``. The ``value`` may be either an integer or a
        floating point number between 0 (0% duty cycle) and 1023 (100% duty).
        """

    def set_analog_period(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in
        milliseconds. The minimum valid value is 1ms.
        """

    def set_analog_period_microseconds(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in
        microseconds. The minimum valid value is 35µs.
        """


class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    def read_analog(self) -> int:
        """Read the voltage applied to the pin, and return it as an integer
        between 0 (meaning 0V) and 1023 (meaning 3.3V).
        """


class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    def is_touched(self) -> bool:
        """Return ``True`` if the pin is being touched with a finger, otherwise
        return ``False``.

        This test is done by measuring the capacitance of the pin together with
        whatever is connected to it. Human body has quite a large capacitance,
        so touching the pin gives a dramatic change in reading, which can be
        detected.
        """


pin0: MicroBitTouchPin = MicroBitTouchPin()
"""Pad 0."""

pin1: MicroBitTouchPin = MicroBitTouchPin()
"""Pad 1."""

pin2: MicroBitTouchPin = MicroBitTouchPin()
"""Pad 2."""

pin2: MicroBitAnalogDigitalPin = MicroBitAnalogDigitalPin()
"""Pad 2."""

pin3: MicroBitAnalogDigitalPin = MicroBitAnalogDigitalPin()
"""Column 1."""

pin4: MicroBitAnalogDigitalPin = MicroBitAnalogDigitalPin()
"""Column 2."""

pin5: MicroBitDigitalPin = MicroBitDigitalPin()
"""Button A."""

pin6: MicroBitDigitalPin = MicroBitDigitalPin()
"""Row 2."""

pin7: MicroBitDigitalPin = MicroBitDigitalPin()
"""Row 1."""

pin8: MicroBitDigitalPin = MicroBitDigitalPin()

pin9: MicroBitDigitalPin = MicroBitDigitalPin()
"""Row 3."""

pin10: MicroBitAnalogDigitalPin = MicroBitAnalogDigitalPin()
"""Column 3."""

pin11: MicroBitDigitalPin = MicroBitDigitalPin()
"""Button B."""

pin12: MicroBitDigitalPin = MicroBitDigitalPin()

pin13: MicroBitDigitalPin = MicroBitDigitalPin()
"""SPI MOSI."""

pin14: MicroBitDigitalPin = MicroBitDigitalPin()
"""SPI MISO."""

pin15: MicroBitDigitalPin = MicroBitDigitalPin()
"""SPI SCK."""

pin16: MicroBitDigitalPin = MicroBitDigitalPin()

pin19: MicroBitDigitalPin = MicroBitDigitalPin()
"""I2C SCL."""

pin20: MicroBitDigitalPin = MicroBitDigitalPin()
"""I2C SDA."""
