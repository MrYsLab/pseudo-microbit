def sleep(ms):
    pass


def running_time():
    pass


# noinspection PyUnusedLocal
def panic(error_code):
    pass


def reset():
    pass


def temperature():
    pass


class Button:
    def is_pressed(self):
        pass

    def was_pressed(self):
        pass

    def get_presses(self):
        pass


button_a = Button()
button_b = Button()


class display:
    @classmethod
    def get_pixel(cls, x, y):
        pass

    @classmethod
    def set_pixel(cls, x, y, val):
        pass

    @classmethod
    def clear(cls):
        pass

    @classmethod
    def show(cls, img, delay=0, wait=True, loop=False, clear=False):
        pass

    # keep pep8 happy
    show(3, 0)

    @classmethod
    def show(cls, iterable, delay=400, *, wait=True, loop=False, clear=False):
        pass

    @classmethod
    def scroll(cls, string, delay=400):
        pass


# noinspection SpellCheckingInspection
class MicroBitPin:
    def write_digital(self, value):
        pass

    def read_digital(self):
        pass

    def write_analog(self, value):
        pass

    def read_analog(self):
        pass

    def set_analog_period(self, intgr):
        pass

    def set_analog_periodMicroseconds(self, intgr):
        pass

    def is_touched(self):
        pass


pin0 = MicroBitPin()
pin1 = MicroBitPin()
pin2 = MicroBitPin()
pin3 = MicroBitPin()
pin4 = MicroBitPin()
pin5 = MicroBitPin()
pin6 = MicroBitPin()
pin7 = MicroBitPin()
pin8 = MicroBitPin()
pin9 = MicroBitPin()
pin10 = MicroBitPin()
pin11 = MicroBitPin()
pin12 = MicroBitPin()
pin13 = MicroBitPin()
pin14 = MicroBitPin()
pin15 = MicroBitPin()
pin16 = MicroBitPin()
pin19 = MicroBitPin()
pin20 = MicroBitPin()


# noinspection PyUnusedLocal
class Image:
    HEART = 0
    HEART_SMALL = 1
    HAPPY = 2
    SMILE = 3
    SAD = 3
    CONFUSED = 5
    ANGRY = 6
    ASLEEP = 7
    SURPRISED = 8
    SILLY = 9
    FABULOUS = 10
    MEH = 11
    YES = 12
    NO = 13
    CLOCK12 = 14
    CLOCK11 = 15
    CLOCK10 = 16
    CLOCK9 = 17
    CLOCK8 = 18
    CLOCK7 = 19
    CLOCK6 = 20
    CLOCK5 = 30
    CLOCK4 = 40
    CLOCK3 = 50
    CLOCK2 = 51
    CLOCK1 = 52
    ARROW_N = 53
    ARROW_NE = 54
    ARROW_E = 55
    ARROW_SE = 56
    ARROW_S = 57
    ARROW_SW = 58
    ARROW_W = 59
    ARROW_NW = 60
    TRIANGLE = 61
    TRIANGLE_LEFT = 62
    CHESSBOARD = 63
    DIAMOND = 64
    DIAMOND_SMALL = 65
    SQUARE = 66
    SQUARE_SMALL = 67
    RABBIT = 68
    COW = 69
    MUSIC_CROTCHET = 70
    MUSIC_QUAVER = 71
    MUSIC_QUAVERS = 72
    PITCHFORK = 73
    XMAS = 74
    PACMAN = 75
    TARGET = 76
    TSHIRT = 77
    ROLLERSKATE = 78
    DUCK = 79
    HOUSE = 80
    TORTOISE = 81
    BUTTERFLY = 82
    STICKFIGURE = 83
    GHOST = 84
    SWORD = 85
    GIRAFFE = 86
    SKULL = 87
    UMBRELLA = 88
    SNAKE = 89
    ALL_CLOCKS = 90
    ALL_ARROWS = 91

    def __init__(self, string=None, width=None, height=None, buffer=None):
        pass

    __init__(None, None, None, None)

    def __init__(self, width=None, height=None, buffer=None):
        pass

    def width(self):
        pass

    def height(self):
        pass

    def set_pixel(self, x, y, value):
        pass

    def get_pixel(self, x, y):
        pass

    def shift_left(self, n):
        pass

    def shift_right(self, n):
        pass

    def shift_up(self, n):
        pass

    def shift_down(self, n):
        pass

    def crop(self, x, y, w, h):
        pass

    def copy(self):
        pass

    def invert(self):
        pass

    def fill(self, value):
        pass

    def blit(self, src, x, y, w, h, xdest=0, ydest=0):
        pass


image = Image()


class uart:
    @classmethod
    def init(cls, baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None):
        pass

    @classmethod
    def any(cls):
        pass

    @classmethod
    def read(cls, n):
        pass

    @classmethod
    def readall(cls):
        pass

    @classmethod
    def readinto(cls, buf, n):
        pass

    @classmethod
    def readline(cls):
        pass

    @classmethod
    def write(cls, buf):
        pass


class accelerometer:
    @classmethod
    def get_x(cls):
        pass

    @classmethod
    def get_y(cls):
        pass

    @classmethod
    def get_z(cls):
        pass

    @classmethod
    def get_values(cls):
        pass

    @classmethod
    def get_current_gestures(cls):
        pass


class compass:
    @classmethod
    def calibrate(cls):
        pass

    @classmethod
    def is_calibrated(cls):
        pass

    @classmethod
    def clear_calibration(cls):
        pass

    @classmethod
    def get_x(cls):
        pass

    @classmethod
    def get_y(cls):
        pass

    @classmethod
    def get_z(cls):
        pass

    @classmethod
    def heading(cls):
        pass

    @classmethod
    def get_field_strength(cls):
        pass


class i2c:
    @classmethod
    def init(cls, freq=100000, sda=pin20, scl=pin19):
        pass

    @classmethod
    def read(cls, addr, n, repeat=False):
        pass

    @classmethod
    def write(cls, addr, buf, repeat=False):
        pass


class spi:
    @classmethod
    def init(cls, baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14):
        pass

    @classmethod
    def read(cls, nbytes):
        pass

    @classmethod
    def write(cls, buffer):
        pass

    @classmethod
    def write_readinto(cls, out, inp):
        pass




