"""
The utime module provides functions for
getting the current time and date, measuring
time intervals, and for delays.
"""


def sleep(seconds: int) -> None:
    """
    Sleep for the given number of seconds.
    You can use a floating-point number to sleep for a fractional
    number of seconds, or use the utime.sleep_ms()
    and utime.sleep_us() functions.
    """


def sleep_ms(ms: int) -> None:
    """
    Delay for given number of milliseconds, should be positive or 0.
    """


def sleep_us(us: int) -> None:
    """
    Delay for given number of microseconds, should be positive or 0.
    """


def ticks_ms() -> int:
    """
    Returns an increasing millisecond counter with an
    arbitrary reference point, that wraps around after some value.
    """


def ticks_us() -> int:
    """
    Just like utime.ticks_ms() above, but in microseconds.
    """


def ticks_add(ticks: int, delta: int) -> int:
    """
    Offset ticks value by a given number, which can be
    either positive or negative. Given a ticks value, this
    function allows to calculate ticks value delta ticks before or
    after it, following modular-arithmetic definition of tick values.
    """


def ticks_diff(ticks1: int, ticks2: int) -> int:
    """
    Measure ticks difference between values returned from utime.ticks_ms()
    or ticks_us() functions, as a signed value which may wrap around.

    The argument order is the same as for subtraction operator,
    ticks_diff(ticks1, ticks2) has the same meaning as ticks1 - ticks2.

    utime.ticks_diff() is designed to accommodate various usage patterns,
    among them:

    Polling with timeout. In this case, the order of events is known,
    and you will deal only with positive results of utime.ticks_diff():

    # Wait for GPIO pin to be asserted, but at most 500us
    start = time.ticks_us()
    while pin.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > 500:
            raise TimeoutError

    Scheduling events. In this case, utime.ticks_diff() result may be
    negative if an event is overdue:

    # This code snippet is not optimized
    now = time.ticks_ms()
    scheduled_time = task.scheduled_time()
    if ticks_diff(scheduled_time, now) > 0:
        print("Too early, let's nap")
        sleep_ms(ticks_diff(scheduled_time, now))
        task.run()
    elif ticks_diff(scheduled_time, now) == 0:
        print("Right at time!")
        task.run()
    elif ticks_diff(scheduled_time, now) < 0:
        print("Oops, running late, tell task to run faster!")
        task.run(run_faster=true)


    """