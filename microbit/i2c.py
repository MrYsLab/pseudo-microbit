"""The ``i2c`` module lets you communicate with devices connected to your board
using the I²C bus protocol. There can be multiple slave devices connected at
the same time, and each one has its own unique address, that is either fixed
for the device or configured on it. Your board acts as the I²C master.

We use 7-bit addressing for devices because of the reasons stated
`here <http://www.totalphase.com/support/articles/200349176-7-bit-8-bit-and-10-bit-I2C-Slave-Addressing>`_.

This may be different to other micro:bit related solutions.

How exactly you should communicate with the devices, that is, what bytes to
send and how to interpret the responses, depends on the device in question and
should be described separately in that device's documentation.

You should connect the device's ``SCL`` pin to micro:bit pin 19, and the
device's ``SDA`` pin to micro:bit pin 20. You also must connect the device's
ground to the micro:bit ground (pin ``GND``). You may need to power the device
using an external power supply or the micro:bit.

There are internal pull-up resistors on the I²C lines of the board, but with
particularly long wires or large number of devices you may need to add
additional pull-up resistors, to ensure noise-free communication.
"""

from . import pin19, pin20
from typing import Union


def init(freq: int = 100000, sda: int = pin20, scl: int = pin19) -> None:
    """Re-initialize peripheral with the specified clock frequency ``freq`` on the
    specified ``sda`` and ``scl`` pins.

    .. warning::

        Changing the I²C pins from defaults will make the accelerometer and
        compass stop working, as they are connected internally to those pins.
    """


def read(addr: int, n: int, repeat: bool = False) -> bytes:
    """Read ``n`` bytes from the device with 7-bit address ``addr``. If ``repeat``
    is ``True``, no stop bit will be sent.
    """


def write(addr: int, buf: Union[bytes, bytearray], repeat=False) -> None:
    """Write bytes from ``buf`` to the device with 7-bit address ``addr``. If
    ``repeat`` is ``True``, no stop bit will be sent.
    """