# program that uses matplotlib, numpy, and linspace to create and plot a 3D surface

# NOTE: the web-based version of Visual Studio Code (vscode.dev) doesn’t support rendering graphical output directly.

# Here are a couple of alternatives you can try:

# 1. Save the Plot as an Image: Modify your code to save the plot as an image file, which you can then view on your iPad.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define a function to generate z values
z = np.sin(np.sqrt(x**2 + y**2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Add labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')

# Save the plot as an image file
plt.savefig('3d_plot.png')

# Show the plot
plt.show()