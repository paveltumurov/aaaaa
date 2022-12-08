from matplotlib import pyplot
import numpy

t = [] #time
u = [] #voltage
count = 0
with open('data.txt', 'r') as data:
    for line in data.readlines():
        if line != '\n':
            count += 1
            x, y = tuple([float(item) for item in line.split()])
            t.append(x)
            u.append(y)
fig, ax = pyplot.subplots(figsize=(16, 10), dpi=400)
ax.axis(xmin = 0, xmax = max(t), ymin = 0, ymax=max(u)*1.2)
ax.set_xlabel('время t')
ax.set_ylabel('напряжение u')
ax.set_title('Зависимость напряжения от времени')
ax.plot(t, u, 'o-', ms = 10, c = 'orange', label = 'U(t)', markevery=1000)
ax.minorticks_on()#малые деления
ax.grid(which='major')
ax.grid(which='minor', linestyle = ':')
ax.legend()
ax.text(80, 1.2, 'Время зарядки конденсатора 138 с')
ax.text(80, 1, 'Время разрядки конденсатора 122 с')
fig.savefig('graph.png')
pyplot.show()