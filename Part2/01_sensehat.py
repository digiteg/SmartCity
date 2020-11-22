from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep

sense = SenseHat()              # initialize Sense HAT
sense.clear()                   # clear display


# joystick event handlers
def pushed_up(event):
    print(event.direction, event.action)


def pushed_down(event):
    print(event.direction, event.action)


def pushed_left(event):
    print(event.direction, event.action)


def pushed_right(event):
    print(event.direction, event.action)


def refresh():
    sense.clear()
 
# attach joystick event handlers
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh


while True:
    # Take readings from all three sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    print("Temperature: {0}C Pressure: {1}hPa Humidity: {2}%".format(t, p, h))

    # Read orientation
    o = sense.get_orientation()
    # print(o)

    pitch = round(o["pitch"], 1)
    roll = round(o["roll"], 1)
    yaw = round(o["yaw"], 1)

    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))

    # Read acceleration
    acceleration = sense.get_accelerometer_raw()
    # print(acceleration)

    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)
    z = round(acceleration['z'], 0)

    print("Acceleration x={0}, y={1}, z={2}".format(x, y, z))

    # Pause before the next arrow
    sleep(0.5)
