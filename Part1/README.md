# **Prototyping tutorial Part 1 - simple examples in Micropython and Pyboard**

I was digging on internet for some examples about testing on ESP8266 in Micropython just for myself education purpose and I didn't find too much useful examples for me. So I decided to fill this gap and I hope this can be  also useful for others who are willing to deal with the topic or teach their students about basics and how to automate testing. Why ESP8266 ? Because it is cost-effective and highly integrated Wi-Fi MCU for IoT / smart things... applications

C and C++ are common programming languages used in microcomputers and embedded devices, but they are also relatively high learning barriers for beginners in programming. Using the programming language processor ' MicroPython ' that is highly compatible with Python 3, you can easily program a microcomputer using the Python 3 grammar that is easy for beginners to understand.

MicroPython is a language processing system that allows programming of microcomputers and embedded devices using Python grammar. The code coverage rate showing the percentage of source code tested is 98.4% for the core part, and it corresponds to the instruction set such as x86 , ARM , Xtensa .


Thanks to the success of Python as a programming language, today many developers have chosen this language in their projects and more and more people are familiar with and experience this language. So why microcontrollers are still programmed in C?

Well, things seem to be taking another direction. MicroPython has been released, a development software that allows the programming of microcontrollers using exclusively Python as a programming language. In this article we will see in detail MicroPython. We will also talk about PyBoard, a microcontroller board specifically designed to be programmed into Python.


MicroPython is an application based entirely on Python 3. This application allows all developers to program microcontrollers using some Python libraries that have been optimized to work on microprocessors normally mounted on microcontrollers.

The development on MicroPython is really simple. It does not require any installation, just open the corresponding web page (see here) on the official micropython.org website. In fact MicroPython is an application that works online, and so instead of installing an application on your computer you can work directly from the browser.


<br/>

# Things used in this project




 ![Pyboard](/img/pybv10-pinout.jpg)

### **Hardware components**
- PYBv1.0. You can also view pinouts on the pictures above and below:
 ![Pyboard front and rear](/img/MicroPython-Pyboard-front-and-rear.jpg)



### **Software apps and online services**
- [MicroPython unicorn online editor](https://micropython.org/unicorn/)
<br/>

# Intro to Unicorn dev environment used in this tutorial

Unicorn offers implementation of a virtual microcontroller based on the Unicorn emulator. It also contains a port of MicroPython to that virtual microcontroller, and allows the virtual microcontroller to run in the browser. This will give us web dev environment with full MicroPython port running simulated-bare-metal pyboard in a web browser.

![Pyboard](/img/MicroPython-web-online.jpg)

## **Built in peripherals**
Web dev environment allows us to use with virtual pyboard various peripherals. 
![Pyboard](/img/PYBAll.png)

- Internal SWITCH - user button
- Internal LEDs - four on board LEDs numbered 1 to 4  (1=red, 2=green, 3=yellow, 4=blue)
- Internal Reset button - will restart virtual pyboard
- LED -  is connected to our virtual pin Y12
- I2C LCD - fully simulated I2C bus and LCD Display
- SERVO - simple servo connection
- ADC (Analogue to Digital Converter) - The slider is connected to pin Y4
<br/>



# Hurray let's start !
![Prototype](/img/prototypefun.gif)

## **Back to reality .. Start with baby steps**
Idea is to start always with small building blocks and try to test them and optimize your code. This is the best way how to build your solution iteratively and step by step learn how things work.

Try to copy and paste following code examples into Unicorn REPL


## Step 1: your first code Internal USR button and LEDs

In example the try use USR button on the pyboard to flash the all internal 1-4 LEDs in the row.

```python
# push the USR button on the pyboard to flash the LEDs!
# try using the reset button on the pyboard to quit this script!

from time import sleep_ms
from pyb import LED, Switch

last = i =1

print("Demo start ... Press button")

while True:
    if Switch().value():        # USR button pressed ?
        LED(i).on()
        last=i
        i=i%4 +1                # choose next internal led # 1-4
        print("Switch pressed...",i)
    else:
        LED(last).off()
    
    sleep_ms(50)                # sleep for while
```


## Step 2: second code Internal USR button and LEDs

In example we will use a Pin and attached virtual LED. Make sure you have the LED checkbox marked! The LED is connected to virtual pin Y12.

```python
# to flash the pinned red LED
# push the USR button on the pyboard to end this script
# try also using the reset button on the pyboard to find difference

from time import sleep_ms
from machine import Pin
from pyb import Switch

# The LED is connected to our virtual pin Y12
y12 = Pin('Y12')

print("Pin LED blink :) Start ! ")

while True:
    if Switch().value():    # USR button pressed ?
        y12(0)
        break               # break the loop

    y12(0 if y12() else 1)  # on / off of red LED
    sleep_ms(50)            # sleep for while
    
print("Pin LED end")

```

# Next steps

In second part of this tutorial I will cover complex scenario and related topics

# Resources

Further reading and useful links:
- [RealPython](https://realpython.com/pytest-python-testing/)
- [Guru99](https://www.guru99.com/software-testing.html)
- [Software Testing Help](https://www.softwaretestinghelp.com/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)
- [wikipedia Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number)
- [wikipedia Standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)


# Credits


# License
Unless otherwise noted, the contents of this document are licensed under a license
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

![Creative Commons](/img/cc.svg) ![by](/img/by.svg) ![nc-eu](/img/nc-eu.svg) ![sa](/img/sa.svg)