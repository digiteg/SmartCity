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
