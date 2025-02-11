import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

#Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4], use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])

ax.plot(x,z)
ax.set_xlabel('X')
ax.set_ylabel('Z')

ax2.plot(x,y)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('zoom')
ax2.set_xlim(20,22) #Set limit
ax2.set_ylim(30,50) #Set limit

plt.show()

# Use plt.subplots(nrows=1, ncols=2) to create the plot below, plot (x,y) and (x,z) on the axes. Play around with the linewidth and style
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
plt.show()


#resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))
axes[0].plot(x,y,color="blue", lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x,z,color="red", lw=3, ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
plt.show()
