import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data for the 3D heart shape
phi = np.linspace(0, 2 * np.pi, 1000)
z = np.linspace(-1.5, 1.5, 500)
phi, z = np.meshgrid(phi, z)
r = 1 - np.abs(z)
x = r * np.sin(phi)
y = r * np.cos(phi)

# Create the 3D plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='red', edgecolor='none')

# Customize the plot
ax.set_title("3D Heart Shape")
ax.axis('off')  # Hide axes for better aesthetics
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

# Show the 3D heart shape
plt.show()