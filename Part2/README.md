# **Prototyping tutorial Part 2 - more complex examples with Sense HAT and Python**

First part of this tutorial was covering intro to prototyping examples with MicroPython in virtual environment if you are interested please read more on Part 1 [link](/Part1/README.md)

## Hurray let's start !
Summary from part 1 of this tutorial is about Idea to start always with small building blocks and try to test them and optimize your code. This is the best way how to build your solution iteratively and step by step you will explore and learn how things work.

![Prototype](/img/prototypefun.gif)


<br/>

# Things used in this project

### **Hardware components**
- SenseHAT
- Raspberry Pi 3 or 4
 
### **Software apps and online services**
- [Trinket online editor](https://trinket.io/)
- Open the Weather Logger Starter Trinket: [jumpto.cc/weather-go.](http://jumpto.cc/weather-go)
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



## Example 1: **Sensing the environment**

The Sense HAT has a set of environmental sensors for detecting the surrounding conditions; it can measure pressure, temperature, and humidity.

The Sense HAT has also an IMU (Inertial Measurement Unit) chip which includes a set of sensors that detect movement:

- A gyroscope (for detecting which way up the board is)
- An accelerometer (for detecting movement)
- A magnetometer (for detecting magnetic fields)

You can detect when the Sense HAT’s joystick is pressed, held, and released in five different directions: up, down, left, right, and middle.

## main.py

In example we will learn all how to use Sense HAT sensors and build in joystick.
Try to copy and paste following code examples into Trinket main.py

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

## Example 2: **Weather Logger** creating simple chart from Sense HAT data


In this project you will collect data from the Sense HAT’s sensors and log it to a file. Then you will use the PyGal module to display that data as a line graph.
- Open the Weather Logger Starter Trinket: [jumpto.cc/weather-go.](http://jumpto.cc/weather-go)

![Chart](/img/sensehatgraph.png)

## collect.py

In following code we will collect and store Sense HAT sensor's data.
First let’s log the temperature to a file every 5 seconds. You can use the emulator to change the temperature.

```python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()                  # initialize Sense HAT

while True:
    sleep(5)                            # sleep for while
    myfile = open("weather.txt", 'a')   # open file for append

    # read sensors data
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # write data into file
    myfile.write("{0} {1} {2}\n".format(t, p, h))

    myfile.close                    # close file

```

## display.py
Now you’ve collected some temperature data let’s show it on a line graph.
In following code we draw graph from collected data. 

```python
import pygal

# series of sensors data 
temp = []
press = []
humm = []

file = open("weather.txt", 'r')         # open file for read
for line in file.read().splitlines():   # read each line
    if line:
        val = line.split()              # get values
        print(val)                      # debug print

        # append sensors values
        temp.append(float(val[0]))
        press.append(float(val[1]))
        humm.append(float(val[2]))


file.close()                            # close file

#  line graph
weather = pygal.Line()
weather.title = "Weather"

weather.add("temp", temp)               # temperature

# weather.add("press",press)            # pressure
# weather.add("humm",humm)              # humidity

weather.x_labels = range(1, len(temp)+1)    # add x axis labels
# weather.x_labels=range(1,len(press)+1)
# weather.x_labels=range(1,len(humm)+1)
weather.render()                        # draw graph

```

## weather.txt
Sample data for your experiments
```python

19.843592419453334 1012.9734563850519 44.34705568195707
19.843592419453334 1112.9734563850519 50.34705568195707
23.843592419453334 1212.9734563850519 64.34705568195707
45.843592419453334 1312.9734563850519 74.34705568195707
65.843592419453334 1412.9734563850519 84.34705568195707
75.843592419453334 1512.9734563850519 94.34705568195707
100.843592419453334 1612.9734563850519 144.34705568195707

```

# Next steps

This is end of initial tutorial about prototyping in virtual environments. I recommend you to check also my other articles especially I recommend intro to testing as it is connected to topic of this tutorials.

# Resources

Further reading and useful links:
- [Getting started with the Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)


# Credits


# License
Unless otherwise noted, the contents of this document are licensed under a license
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

![Creative Commons](/img/cc.svg) ![by](/img/by.svg) ![nc-eu](/img/nc-eu.svg) ![sa](/img/sa.svg)