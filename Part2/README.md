# **Prototyping tutorial Part 2 - more complex examples with Sense HAT and Python**

First part of this tutorial was covering intro and testing examples if you are interested please read more on Part 1 link

Some summary from part 1 of this tutorial is about what could be considered and can make sense in your case if you develop IoT application with ESP8266 and Micropython

<br/>

# Things used in this project

### **Hardware components**
- SenseHAT
- Raspberry Pi 3 or 4
 
### **Software apps and online services**
- [Trinket online editor](https://trinket.io/)
<br/>

# What is a Sense HAT?


The Sense HAT is an add-on board for the Raspberry Pi, made especially for the Astro Pi competition. The board allows you to make measurements of temperature, humidity, pressure, and orientation, and to output information using its built-in LED matrix.

![SenseHAT parts](/img/sensehat-parts.png)

## **Trinket’s online dev environment**
Trinket lets you run and write code in any browser, on any device. Trinkets work instantly, with no need to log in, download plugins, or install software. Easily share or embed the code with your changes when you're done.

![Trinket emulator](/img/Emulator.png)
The new emulator builds on Trinket’s existing Python-in-browser platform, and provides the following features:

- Virtual Sense HAT with environmental controls and joystick input
- Full Python syntax highlighting
- Contextual auto-complete
- Intuitive error reporting and highlighting
- Image upload
- HTML page embedding
- Social media integration
- Project sharing via direct URL
- Project download as zip (for moving to Raspberry Pi)
- All major browsers supported



The Sense HAT has temperature, pressure and humidity sensors, and can change its behaviour according to the values they report. The Sense HAT emulator has sliders you can move to change these values, so you can test how your code responds to environmental variables.

![SenseHAT](/img/sense_hat_sliders-500x51.png)


<br/>

# Hurray let's start !
![Prototype](/img/prototypefun.gif)

## **Back to reality .. Start with baby steps**
Idea is to start always with small building blocks and try to test them and optimize your code. This is the best way how to build your solution iteratively and step by step learn how things work.

Try to copy and paste following code examples into Unicorn REPL


## Step 1: your first code Internal USR button and LEDs

In example we will learn all how to use sensors and buid   

```python
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep

sense = SenseHat()              # initialize Sense HAT
sense.clear()                   # clear display


# joystick event handlers
def pushed_up(event):
    print(event.direction, event.action)


def pushed_down(event):
    print(event.direction, event.action)


def pushed_left(event):
    print(event.direction, event.action)


def pushed_right(event):
    print(event.direction, event.action)


def refresh():
    sense.clear()
 
# attach joystick event handlers
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh


while True:
    # Take readings from all three sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    print("Temperature: {0}C Pressure: {1}hPa Humidity: {2}%".format(t, p, h))

    # Read orientation
    o = sense.get_orientation()
    # print(o)

    pitch = round(o["pitch"], 1)
    roll = round(o["roll"], 1)
    yaw = round(o["yaw"], 1)

    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))

    # Read acceleration
    acceleration = sense.get_accelerometer_raw()
    # print(acceleration)

    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)
    z = round(acceleration['z'], 0)

    print("Acceleration x={0}, y={1}, z={2}".format(x, y, z))

    # Pause before the next arrow
    sleep(0.5)


```

## **Back to reality .. Start with baby steps**

## Step 2: second code try Pin attached virtual LED

In example we will use 

```python

```

## Step 3: next code 

```python

```

## Step 4: next code will 

```python


```

# Next steps

In second part of this tutorial I will cover complex scenario and related topics

# Resources

Further reading and useful links:
- [Pyboard MicroPython](http://docs.micropython.org/en/latest/pyboard/quickref.html)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)


# Credits


# License
Unless otherwise noted, the contents of this document are licensed under a license
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

![Creative Commons](/img/cc.svg) ![by](/img/by.svg) ![nc-eu](/img/nc-eu.svg) ![sa](/img/sa.svg)