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

