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
    def __init__(self, posx=23, posy=8):

        # setup buffer
        self.buf = framebuf.FrameBuffer(
            bytearray(17 * 17 // 8), 17, 17, framebuf.MONO_HLSB)
        self.x = posx
        self.y = posy
        self.hitx = False
        self.hity = False

        # draw logo
        self.buf.fill(0)
        self.buf.rect(2, 3, 11, 3, 1)
        self.buf.rect(6, 5, 3, 9, 1)
        self.buf.pixel(3, 10, 1)
        self.buf.pixel(11, 10, 1)
        self.buf.pixel(14, 10, 1)

    def move(self, mx, my):
        
        # move logo
        self.x += mx
        self.y += my

        # check if corner of screen was hit
        self.hitx = False
        self.hity = False

        if(self.x < 0):
            self.x = 0
            self.hitx = True

        elif(self.x > 64-16):
            self.x = 64 - 16
            self.hitx = True

        if(self.y < 0):
            self.y = 0
            self.hity = True

        elif(self.y > 32-16):
            self.y = 32-16
            self.hity = True


def main():

    print("Started ..")
    slider = ADC(Pin('Y4'))             # setup slider
    lcd = LCD()                         # setup LCD
    logo = Logo()                       # init Logo

    last = -1
    direction = 1

    while True:
        pos = slider.read()              # get slider position
        lcd.clear()                      # clear screen

        lcd.blit(logo.buf, logo.x, logo.y)  # show logo
        lcd.text(pos, 0, 0)             # write slider position

        if(pos != last):
            last = pos
            print(pos)                  # print slider position if changed

        if(logo.hitx):                  # change direction if corner was hit
            direction = -direction

        logo.move(direction, 0)         # animate logo

        lcd.draw()                      # Draw on LCD
        sleep_ms(5)                     # sleep for while


main()                                  # run
