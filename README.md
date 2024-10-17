![logo](https://raw.github.com/MrYsLab/pseudo-microbit/master/docs/images/logo.png)

# pseudo-microbit

This library is a _pseudo_ implementation of the micro:bit micropython API used in 
conjunction
with PyCharm to check for syntax errors and to provide type hints.

In addition, instructions are provided to integrate 
[python-minimizer](https://github.com/agroden/python-minimizer), 
[uflash](https://github.com/ntoll/uflash), and [microfs](https://github.com/ntoll/microfs)
into PyCharm.

**Python-minimizer** removes white space from Python files, allowing one to upload
the largest possible file to the micro:bit.

**Uflash** is a utility to flash Python scripts to the micro:bit

**Microfs** is a utility that interacts with the limited file system
provided by MicroPython on the BBC micro:bit.

Integrates the typehints from https://github.com/vlasovskikh/intellij-micropython
with typehints specific to the micro:bit API.

A full tutorial may be found here: https://mryslab.github.io/pseudo-microbit/

<br>

This project was developed using ![](https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm_icon.svg) [Pycharm](https://www.jetbrains.com/pycharm/).  