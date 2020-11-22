from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    sleep(5)
    myfile = open("weather.txt", 'a')

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    myfile.write("{0} {1} {2}\n".format(t, p, h))

    myfile.close
