import matplotlib.pyplot as pyplot

Fig, ax = pyplot.subplots()
for i, (mark, color) in enumerate(zip(
    ['s', 'o', 'D', 'v'], ['r', 'g', 'b', 'purple'])):
    ax.plot(i+1, i+1, color=color,
            marker=mark,
            markerfacecolor='None',
            markeredgecolor=color,
            linestyle = 'None',
            label='i')

ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.legend(numpoints=1)
pyplot.show()