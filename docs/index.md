<div style="text-align:center;color:#990033; font-family:times, serif;font-size:3.5em">
<i>Using PyCharm</i></div>

<div style="text-align:center;color:#990033; font-family:times, serif;font-size:3.5em"><i>To Program The</i></div>

<div style="text-align:center;color:#990033; font-family:times, serif;
font-size:4.0em"><i>micro:bit</i></div>

![](./images/space.png)
![](./images/logo3.png)
![](./images/mb3.gif)

<br>

[PyCharm,](https://www.jetbrains.com/pycharm/)
my go-to Integrated Development Environment (IDE) 
for creating and [publishing open-source Python projects](https://github.com/MrYsLab), 
has significantly improved my development process. 
Its user-friendly interface and extensive features not only 
expedite development but also enhance the quality of the final product.

When attempting to develop code for the [micro:bit](http://www.microbit.org/), 
I was sad to discover that  PyCharm currently does not have built-in support 
for [micro:bit MicroPython](http://microbit-micropython.readthedocs.io/en/latest/index.html).  Since my development efforts often consist 
of desktop components and components that reside on a physical computing device,
such as the micro:bit, I prefer to do all of my development 
using one tool and not have to keep the project in sync over multiple tools. 
Because PyCharm is so highly flexible and easily adaptable, 
I was able to extend the current version of PyCharm to support 
micro:bit MicroPython software development.
In this tutorial, I will show you how to configure the free PyCharm 
Community Edition (or the cost-based Professional Edition) to provide:

* micro:bit aware source code editing, including type hinting
* the ability to flash your code to the micro:bit directly from PyCharm
* the ability to manage the micro:bit local persistent file system directly from PyCharm
* the ability to minimize the size of the Python source file within PyCharm