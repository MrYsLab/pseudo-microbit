"""Definitions related to the hardware buttons."""


class Button:
    """Represents a button.

    .. note::
        This class is not actually available to the user, it is only used by
        the two button instances, which are provided already initialized.
        """

    def is_pressed(self) -> bool:
        """returns True or False to indicate if the button is pressed at the time of
        the method call.
        """

    def was_pressed(self) -> bool:
        """ returns True or False to indicate if the button was pressed since the device
        started or the last time this method was called.
        """

    def get_presses(self) -> int:
        """Returns the running total of button presses, and resets this total
        to zero before returning.
        """


button_a: Button = Button()
"""A ``Button`` instance (see below) representing the left button."""


button_b: Button = Button()
"""Represents the right button."""
