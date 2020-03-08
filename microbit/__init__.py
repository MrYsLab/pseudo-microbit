"""micro:bit Micropython API

Everything directly related to interacting with the hardware lives in the
`microbit` module.  For ease of use it's recommended you start all scripts
with::

    from microbit import *

The following documentation assumes you have done this.

There are a few functions available directly::

    # sleep for the given number of milliseconds.
    sleep(ms)
    # returns the number of milliseconds since the micro:bit was last switched on.
    running_time()
    # makes the micro:bit enter panic mode (this usually happens when the DAL runs
    # out of memory, and causes a sad face to be drawn on the display). The error
    # code can be any arbitrary integer value.
    panic(error_code)
    # resets the micro:bit.
    reset()

The rest of the functionality is provided by objects and classes in the
microbit module, as described below.

Note that the API exposes integers only (ie no floats are needed, but they may
be accepted).  We thus use milliseconds for the standard time unit.
"""

from ._base_functions import *
from ._button import *
from ._pin import *
from ._image import *

# The following modules will get imported when using `from ... import *`
__all__ = [
        # base functions
        "panic", "reset", "sleep", "running_time", "temperature",
        # button
        "Button", "button_a", "button_b",
        # pins
        "pin0", "pin1", "pin2", "pin2", "pin3", "pin4", "pin5", "pin6", "pin7", "pin8", "pin9", "pin10", "pin11", "pin12", "pin13", "pin14", "pin15", "pin16", "pin19", "pin20",
        # Image
        "Image",
        # modules
        "display", "uart", "spi", "i2c", "accelerometer", "compass"
        ]


#NOTE: it seems to work to define an object here and then add its name to the __all__
#      then it will get exported when you do "import *" as well

# This is the output of `dir()`; so these values should be in global scope:
# ['Image', 'accelerometer', 'display', 'led', 'c4', 'c2', 'c3', 'c0', 'c1', 'c5', '__name__', 'temperature', 'c6', 'c7', 'c10', 'c8', 'c9', 'uart', 'c11', 'pin20', 'pin21', 'pin22', 'pin23', 'pin24', 'pin25', 'running_time', 'pin26', 'pin27', 'pin29', 'pin28', 'c12', 'c16', 'spi', 'panic', 'c17', 'c18', 'c19', 'c21', 'magnetometer', 'p1', 'p0', 'p3', 'p2']

