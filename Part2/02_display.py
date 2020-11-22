import pygal

temp = []
press = []
humm = []

file = open("weather.txt", 'r')
for line in file.read().splitlines():
    if line:
        val = line.split()
        print(val)
        temp.append(float(val[0]))
        press.append(float(val[1]))
        humm.append(float(val[2]))


file.close()

weather = pygal.Line()
weather.title = "Weather"

weather.add("temp", temp)
# weather.add("press",press)
# weather.add("humm",humm)

weather.x_labels = range(1, len(temp)+1)
# weather.x_labels=range(1,len(press)+1)
# weather.x_labels=range(1,len(humm)+1)
weather.render()
