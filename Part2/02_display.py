import pygal

# series of sensors data 
temp = []
press = []
humm = []

file = open("weather.txt", 'r')         # open file for read
for line in file.read().splitlines():   # read each line
    if line:
        val = line.split()              # get values
        print(val)                      # debug print

        # append sensors values
        temp.append(float(val[0]))
        press.append(float(val[1]))
        humm.append(float(val[2]))


file.close()                            # close file

# draw line chart
weather = pygal.Line()
weather.title = "Weather"

weather.add("temp", temp)               # temperature

# weather.add("press",press)            # pressure
# weather.add("humm",humm)              # humidity

weather.x_labels = range(1, len(temp)+1)    # add x axis labels
# weather.x_labels=range(1,len(press)+1)
# weather.x_labels=range(1,len(humm)+1)
weather.render()                        # draw chart
