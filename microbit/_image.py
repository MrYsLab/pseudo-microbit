"""The definition of the class Image."""

from __future__ import annotations  # allow to define members of Image as Image
#                                     see https://stackoverflow.com/a/48973804/2165903
from typing import Any, List, overload


class Image:
    """The ``Image`` class is used to create images that can be displayed
    easily on the device's LED matrix. Given an image object it's possible to
    display it via the ``display`` API::

        display.show(Image.HAPPY)
    """

    @overload
    def __init__(self, string: str) -> None:
        """``string`` has to consist of digits 0-9 arranged into lines,
        describing the image, for example::

            image = Image("90009:"
                          "09090:"
                          "00900:"
                          "09090:"
                          "90009")

        will create a 5×5 image of an X. The end of a line is indicated by a
        colon. It's also possible to use a newline (\n) to indicate the end of
        a line like this::

            image = Image("90009\n"
                          "09090\n"
                          "00900\n"
                          "09090\n"
                          "90009")
        """

    @overload
    def __init__(self, width: int = None, height: int = None,
                 buffer: Any = None) -> None:
        """Create an empty image with ``width`` columns and ``height`` rows.
        Optionally ``buffer`` can be an array of ``width``×``height`` integers
        in range 0-9 to initialize the image.
        """

    def __init__(self) -> None:
        """Returns an Image with all LEDs off."""
        pass

    def width(self) -> int:
        """Return the number of columns in the image."""

    def height(self) -> int:
        """Return the numbers of rows in the image."""

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Set the brightness of the pixel at column ``x`` and row ``y`` to the
        ``value``, which has to be between 0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the built-in
        read-only images, like ``Image.HEART``.
        """

    def get_pixel(self, x: int, y: int) -> int:
        """Return the brightness of pixel at column ``x`` and row ``y`` as an
        integer between 0 and 9.
        """

    def shift_left(self, n: int) -> Image:
        """Return a new image created by shifting the picture left by ``n``
        columns.
        """

    def shift_right(self, n: int) -> Image:
        """Same as ``image.shift_left(-n)``."""

    def shift_up(self, n: int) -> Image:
        """Return a new image created by shifting the picture up by ``n``
        rows.
        """

    def shift_down(self, n: int) -> Image:
        """Same as ``image.shift_up(-n)``."""

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Return a new image by cropping the picture to a width of ``w`` and a
        height of ``h``, starting with the pixel at column ``x`` and row
        ``y``.
        """

    def copy(self) -> Image:
        """Return an exact copy of the image."""

    def invert(self) -> Image:
        """Return a new image by inverting the brightness of the pixels in the
        source image."""

    def fill(self, value: int) -> None:
        """Set the brightness of all the pixels in the image to the
        ``value``, which has to be between 0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the built-in
        read-only images, like ``Image.HEART``.
        """

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int = 0,
             ydest: int = 0) -> None:
        """Copy the rectangle defined by ``x``, ``y``, ``w``, ``h`` from the
        image ``src`` into this image at ``xdest``, ``ydest``. Areas in the
        source rectangle, but outside the source image are treated as having a
        value of 0.

        ``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()``
        and ``crop()`` can are all implemented by using ``blit()``.

        For example, img.crop(x, y, w, h) can be implemented as::

            def crop(self, x, y, w, h):
                res = Image(w, h)
                res.blit(self, x, y, w, h)
                return res
        """

    def __repr__(self) -> str:
        """Get a compact string representation of the image."""

    def __str__(self) -> str:
        """Get a readable string representation of the image."""

    def __add__(self, other: Image) -> Image:
        """Create a new image by adding the brightness values from the two
        images for each pixel.
        """

    def __mul__(self, n: float) -> Image:
        """Create a new image by multiplying the brightness of each pixel by
        ``n``.
        """


Image.HEART: Image = Image()
Image.HEART_SMALL: Image = Image()
Image.HAPPY: Image = Image()
Image.SMILE: Image = Image()
Image.SAD: Image = Image()
Image.CONFUSED: Image = Image()
Image.ANGRY: Image = Image()
Image.ASLEEP: Image = Image()
Image.SURPRISED: Image = Image()
Image.SILLY: Image = Image()
Image.FABULOUS: Image = Image()
Image.MEH: Image = Image()
Image.YES: Image = Image()
Image.NO: Image = Image()
Image.CLOCK12: Image = Image()
Image.CLOCK11: Image = Image()
Image.CLOCK10: Image = Image()
Image.CLOCK9: Image = Image()
Image.CLOCK8: Image = Image()
Image.CLOCK7: Image = Image()
Image.CLOCK6: Image = Image()
Image.CLOCK5: Image = Image()
Image.CLOCK4: Image = Image()
Image.CLOCK3: Image = Image()
Image.CLOCK2: Image = Image()
Image.CLOCK1: Image = Image()
Image.ARROW_N: Image = Image()
Image.ARROW_NE: Image = Image()
Image.ARROW_E: Image = Image()
Image.ARROW_SE: Image = Image()
Image.ARROW_S: Image = Image()
Image.ARROW_SW: Image = Image()
Image.ARROW_W: Image = Image()
Image.ARROW_NW: Image = Image()
Image.TRIANGLE: Image = Image()
Image.TRIANGLE_LEFT: Image = Image()
Image.CHESSBOARD: Image = Image()
Image.DIAMOND: Image = Image()
Image.DIAMOND_SMALL: Image = Image()
Image.SQUARE: Image = Image()
Image.SQUARE_SMALL: Image = Image()
Image.RABBIT: Image = Image()
Image.COW: Image = Image()
Image.MUSIC_CROTCHET: Image = Image()
Image.MUSIC_QUAVER: Image = Image()
Image.MUSIC_QUAVERS: Image = Image()
Image.PITCHFORK: Image = Image()
Image.XMAS: Image = Image()
Image.PACMAN: Image = Image()
Image.TARGET: Image = Image()
Image.TSHIRT: Image = Image()
Image.ROLLERSKATE: Image = Image()
Image.DUCK: Image = Image()
Image.HOUSE: Image = Image()
Image.TORTOISE: Image = Image()
Image.BUTTERFLY: Image = Image()
Image.STICKFIGURE: Image = Image()
Image.GHOST: Image = Image()
Image.SWORD: Image = Image()
Image.GIRAFFE: Image = Image()
Image.SKULL: Image = Image()
Image.UMBRELLA: Image = Image()
Image.SNAKE: Image = Image()
Image.ALL_CLOCKS: List[Image] = (Image.CLOCK12, Image.CLOCK1, Image.CLOCK2,
        Image.CLOCK3, Image.CLOCK4,
        Image.CLOCK5, Image.CLOCK6, Image.CLOCK7, Image.CLOCK8, Image.CLOCK9,
        Image.CLOCK10, Image.CLOCK11)
Image.ALL_ARROWS: List[Image] = (Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E,
        Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W,
        Image.ARROW_NW)
