"""
MicroPython contains an os module based upon the os module
in the Python standard library. It’s used for accessing what
would traditionally be termed as operating system dependent
functionality. Since there is no operating system in
MicroPython the module provides functions relating to
the management of the simple on-device persistent file
system and information about the current system.

To access this module you need to:

import os


"""

from typing import Tuple, List


def listdir() -> List[str]:
    """
    Returns a list of the names of all the files contained
    within the local persistent on-device file system.
    """


def remove(filename: str) -> None:
    """
    Removes (deletes) the file named in the argument filename. If the file does not exist
    an OSError exception will occur.
    """


def size(filename: str) -> int:
    """
    Returns the size, in bytes, of the file named in the argument filename.
    If the file does not exist an OSError exception will occur.
    """


def uname() -> Tuple[str, str, str, str, str]:
    """
        Returns information identifying the current operating system. The return value is an object with five attributes:

        sysname - operating system name

        nodename - name of machine on network (implementation-defined)

        release - operating system release

        version - operating system version

        machine - hardware identifier

    """