# **Prototyping tutorial Part 2 - more complex examples with Sense HAT and Python**

sense hat

<br/>

# Things used in this project

### **Hardware components**
- SenseHAT
- Raspberry Pi 3 or 4
 
### **Software apps and online services**
- [Trinket online editor](https://trinket.io/)
<br/>

# Intro to Unicorn dev environment used in this tutorial

...

What is a Sense HAT?
The Sense HAT is an add-on board for the Raspberry Pi, made especially for the Astro Pi competition. The board allows you to make measurements of temperature, humidity, pressure, and orientation, and to output information using its built-in LED matrix.

![SenseHAT parts](/img/sensehat-parts.png)

## **Trinket’s built ins**
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


## Step 2: second code try Pin attached virtual LED

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


## Step 3: next code will give you example of how to use Servo and Slider together

In example we will use a Pin and attached virtual servo and Slider on pin Y4. Make sure you have both Servo and ADC checkboxes marked.

![Servo and Slider](/img/PYBSliderServo.png)


```python

# In this example we are going use Servo and Slider by reading using the ADC
# Make sure you have the Servo checkbox marked!
# Make sure you have the ADC checkbox marked!
# use the reset button to stop example

from machine import Pin
from pyb import ADC, Servo
from time import sleep_ms

# The slider is connected to pin Y4, try adjusting it
slider = ADC(Pin('Y4'))

# The pyboard has four simple servo connections
servo = Servo(1)

# calculate the basic step
STEP = 255 / 180
last =-1

print("Servo and Slider demo started..")

while True:
    pos=slider.read()
    
    if (pos != last):
        angle = int((pos / STEP) - 90)         # get the angle
        print("Slider position: ", pos, " Servo angle: ", angle)
        servo.angle(angle, 100)                 # set servo angle
        last =pos
    
    sleep_ms(10)

```

## Step 4: next code will give you example of how to write on LCD values and graphic

In example we will use a virtual I2C LCD(scl pin X9, sda pin X10) and Slider on pin Y4. Make sure you have both I2C LCD and ADC checkboxes marked.

![LCD and Slider](/img/PYBSliderLCD.png)

```python

# A fully simulated I2C bus and LCD Display
# The framebuf class simplifies graphics in MicroPython
# Use the hardware i2c in example Pong for faster performance
# Make sure you have the I2C LCD checkbox marked!

from machine import Pin, I2C
from pyb import ADC
from time import sleep_ms
import framebuf


class LCD:

    def __init__(self):
        
        # setup I2C
        self._i2c = I2C(scl=Pin('X9'), sda=Pin('X10'))              
        
        # setup buffer
        self._fbuf = framebuf.FrameBuffer(
            bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

    def clear(self):
        self._fbuf.fill(0)                  # clear buffer 

    def text(self, msg, x, y):
        self._fbuf.text(str(msg), x, y)     # write text to position

    def blit(self, buf, x, y):
        self._fbuf.blit(buf, x, y)          # draw buffer

    def draw(self):
        self._i2c.writeto(8, self._fbuf)    # draw buffer to LCD via I2C


class Logo:
    def __init__(self, posx=45, posy=15):
         
         # setup buffer
        self.buf = framebuf.FrameBuffer(
            bytearray(17 * 17 // 8), 17, 17, framebuf.MONO_HLSB)
        self.x = posx                        
        self.y = posy

        # draw logo
        self.buf.fill(0)

        self.buf.hline(2, 3, 11, 1)
        self.buf.hline(2, 4, 11, 1)
        self.buf.hline(2, 5, 11, 1)

        self.buf.vline(6, 5, 9, 1)
        self.buf.vline(7, 5, 9, 1)
        self.buf.vline(8, 5, 9, 1)

        self.buf.hline(3, 10, 1, 1)
        self.buf.hline(11, 10, 1, 1)
        self.buf.hline(14, 10, 1, 1)


def main():

    print("Started ..")
    slider = ADC(Pin('Y4'))         # setup slider
    lcd = LCD()                     # setup LCD
    logo = Logo()                   # init Logo

    pos = slider.read()             # get slider position

    lcd.clear()                     # Draw on LCD
    lcd.blit(logo.buf, logo.x, logo.y)
    lcd.text(pos, 0, 0)
    lcd.draw()
    print(pos)                      # write slider position


main()                              # run

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