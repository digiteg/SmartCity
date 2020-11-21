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
        self._i2c = I2C(scl=Pin('X9'), sda=Pin('X10'))
        self._fbuf = framebuf.FrameBuffer(
            bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

    def clear(self):
        self._fbuf.fill(0)

    def text(self, msg, x, y):
        self._fbuf.text(str(msg), x, y)

    def blit(self, buf, x, y):
        self._fbuf.blit(buf, x, y)

    def draw(self):
        self._i2c.writeto(8, self._fbuf)


class Logo:
    def __init__(self, posx=23, posy=8):
        self.buf = framebuf.FrameBuffer(
            bytearray(17 * 17 // 8), 17, 17, framebuf.MONO_HLSB)
        self.x = posx
        self.y = posy
        self.hitx = False
        self.hity = False
        
        self.buf.fill(0)
        self.buf.vline(6, 5, 9, 1)
        self.buf.vline(7, 5, 9, 1)
        self.buf.vline(8, 5, 9, 1)
        self.buf.hline(2, 3, 11, 1)
        self.buf.hline(2, 4, 11, 1)
        self.buf.hline(2, 5, 11, 1)
        self.buf.hline(3, 10, 1, 1)
        self.buf.hline(11, 10, 1, 1)
        self.buf.hline(14, 10, 1, 1)

    def move(self, mx, my):
        self.x += mx
        self.y += my

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
    slider = ADC(Pin('Y4'))
    lcd = LCD()
    logo = Logo()

    last = -1
    direction = 1

    while True:
        pos = slider.read()
        lcd.clear()

        lcd.blit(logo.buf, logo.x, logo.y)
        lcd.text(pos, 0, 0)

        if(pos != last):
            last = pos
            print(pos)

        if(logo.hitx):
            direction = -direction

        logo.move(direction, 0)

        lcd.draw()
        sleep_ms(5)


main()
