"""Based on the documentation at
https://github.com/bbcmicrobit/micropython/blob/afcd63a202e932e89940b28af6471e79738e4d2e/docs/micropython.rst
"""
from typing import TypeVar, overload

_T = TypeVar('T')

def const(expr: _T) -> _T:
    """
    Used to declare that the expression is a constant so that the compiler can
    optimise it. The use of this function should be as follows:

    .. code-block:: python

        from micropython import const
        CONST_X = const(123)
        CONST_Y = const(2 * CONST_X + 1)

    Constants declared this way are still accessible as global variables from
    outside the module they are declared in. On the other hand, if a constant
    begins with an underscore then it is hidden, it is not available as a
    global variable, and does not take up any memory during execution.
    """



@overload
def opt_level() -> int:
    """See opt_level(level)"""


@overload
def opt_level(level: int) -> None:
    """
    If level is given then this function sets the optimisation level for
    subsequent compilation of scripts, and returns None. Otherwise it returns
    the current optimisation level.

    The optimisation level controls the following compilation features:

    *   Assertions: at level 0 assertion statements are enabled and compiled
        into the bytecode; at levels 1 and higher assertions are not compiled.

    *   Built-in ``__debug__`` variable: at level 0 this variable expands to
        True; at levels 1 and higher it expands to False.

    *   Source-code line numbers: at levels 0, 1 and 2 source-code line number
        are stored along with the bytecode so that exceptions can report the
        line number they occurred at; at levels 3 and higher line numbers are
        not stored.

    The default optimisation level is usually level 0.
    """


def mem_info(verbose = False) -> None:
    """
    Print information about currently used memory. If the verbose argument is
    given then extra information is printed.
    """


def qstr_info(verbose = False) -> None:
    """
    Print information about currently interned strings. If the verbose argument
    is given then extra information is printed.

    This includes the number of interned strings and the amount of RAM they
    use. In verbose mode it prints out the names of all RAM-interned strings.
    """


def stack_use() -> int:
    """
    Return an integer representing the current amount of stack that is being
    used. The absolute value of this is not particularly useful, rather it
    should be used to compute differences in stack usage at different points.
    """


def heap_lock() -> None:
    """
    See heap_unlock()
    """


def heap_unlock() -> None:
    """
    Lock or unlock the heap. When locked no memory allocation can occur and a
    ``MemoryError`` will be raised if any heap allocation is attempted.
    """


def kbd_intr(chr: int) -> None:
    """
    Set the character that will raise a KeyboardInterrupt exception. By default
    this is set to 3 during script execution, corresponding to Ctrl-C. Passing
    -1 to this function will disable capture of Ctrl-C, and passing 3 will
    restore it.

    This function can be used to prevent the capturing of Ctrl-C on the
    incoming stream of characters that is usually used for the REPL, in case
    that stream is used for other purposes
    """