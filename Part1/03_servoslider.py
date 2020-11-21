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