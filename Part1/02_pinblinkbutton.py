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

