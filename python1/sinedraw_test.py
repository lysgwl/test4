import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]

fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2, label='Dashes set retroactively')
line1.set_dashes(dashes)

line2, = ax.plot(x, -1*np.sin(x), dashes=[30,5, 10, 5], label='Dashes set proactively')

ax.legend(loc='lower right')
plt.show()