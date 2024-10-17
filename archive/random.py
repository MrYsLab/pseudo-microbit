"""
This module is based upon the random module in the
Python standard library. It contains functions for generating random behaviour.

To access this module you need to:

    # import random

"""
from typing import List, Any, overload


def getrandbits(n: int) -> int:
    """
    Returns an integer with n random bits.
    """


def seed(n: int) -> None:
    """
    Initialize the random number generator with a known integer n.
    This will give you reproducibly deterministic randomness from a
    given starting state (n).
    """


def randint(a: int, b: int) -> int:
    """
    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    """


@overload
def randrange(stop: int) -> int:
    """
    Return a randomly selected integer between zero and up to
    (but not including) stop.
    """


@overload
def randrange(start: int, stop: int) -> int:
    """
    Return a randomly selected integer from range(start, stop).
    """


def randrange(start: int, stop: int, step: int) -> int:
    """
    Return a randomly selected element from range(start, stop, step).
    """


def choice(seq: list) -> Any:
    """
    Return a random element from the non-empty sequence seq.
    If seq is empty, raises IndexError.
    """


def random() -> float:
    """
    Return the next random floating point number in the range [0.0, 1.0)
    """


def uniform(a: float, b:float) -> float:
    """
    Return a random floating point number N such that
    a <= N <= b for a <= b and b <= N <= a for b < a.
    """