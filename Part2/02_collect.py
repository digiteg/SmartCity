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
