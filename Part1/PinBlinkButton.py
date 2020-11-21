from time import sleep_ms
import machine
import pyb

# The LED is connected to our virtual pin Y12
y12 = machine.Pin('Y12')

print("Pin LED blink :) Start ! ")

while True:
    if pyb.Switch().value():
        y12(0)
        break
    y12(0 if y12() else 1)
    sleep_ms(50)
    
print("Pin LED end")

