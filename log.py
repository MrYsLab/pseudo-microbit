"""
Data Logging V2

This module lets you log data to a MY_DATA file
saved on a micro:bit V2 MICROBIT USB drive.

See https://microbit-micropython.readthedocs.io/en/v2-docs/log.html
"""
from tkinter import BooleanVar
from typing import Tuple, Any

MILLISECONDS = 1
SECONDS = 10
MINUTES = 600
HOURS = 36000
DAYS = 864000


def set_labels(*labels: tuple[str, ...], timestamp: int = log.SECONDS):
    """

    Set up the log file header.

    This function accepts any number of positional arguments,
    each creates a column header, e.g. log.set_labels("X", "Y", "Z").

    Ideally this function should be called a single time,
    before any data is logged, to configure the data table header once.

    If a log file already exists when the programme starts,
    or if this function is called multiple times, it will check the
    labels already defined in the log file. If this function call
    contains any new labels not already present, it will generate a new
    header row with the additional columns.

    By default, the first column contains a time stamp for each row.
    The time unit can be selected via the timestamp argument, e.g.
    log.set_labels("temp", timestamp=log.MINUTES)

    Parameters:

            *labels – Any number of positional arguments, each
            corresponding to an entry in the log header.

            timestamp – Select the timestamp unit that will be
            automatically added as the first column in every row.
            Timestamp values can be one of log.MILLISECONDS,
            log.SECONDS, log.MINUTES, log.HOURS, log.DAYS or None to
            disable the timestamp. The default value is log.SECONDS.


    """


def set_mirroring(serial: bool) -> None:
    """
    Configure mirroring of the data logging activity to the serial output.

    Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

    Parameters:

        serial – True enables mirroring data to the serial output.

    """


def delete(full: bool = False) -> None:
    """
    Delete the contents of the log, including headers.

    To add the log headers again the set_labels function should to be
    called after this function.

    There are two erase modes; “full” completely removes the data from
    the physical storage, and “fast” invalidates the data without removing it.

    Parameters:

        full – True selects a “full” erase and False selects the “fast” erase method.

    """


def add(data_dictionary: dict[str, Any]) -> None:
    """
    log.add(data_dictionary, /, *, **kwargs)

    Add a data row to the log.

    There are two ways to log data with this function:

        Via keyword arguments, each argument name representing a label.

            e.g. log.add(X=compass.get_x(), Y=compass.get_y())

        Via a dictionary, each dictionary key representing a label.

            e.g. log.add({ "X": compass.get_x(), "Y": compass.get_y() })

    The keyword argument option can be easier to use, and the dictionary
    option allows the use of spaces (and other special characters),
    that could not be used with the keyword arguments.

    New labels not previously specified via the set_labels function,
    or by a previous call to this function, will trigger a new header
    entry to be added to the log with the extra labels.

    Labels previously specified and not present in a call to this
    function will be skipped with an empty value in the log row.

    Raises:

        OSError – When the log is full this function raises an
        OSError exception with error code 28 ENOSPC, which indicates
        there is no space left in the device.


    """
