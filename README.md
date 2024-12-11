# 3D Heart Visualization

This repository contains a Python script that generates a beautiful 3D heart shape using matplotlib.

## Requirements

To run this script, you'll need the following Python packages:
- numpy
- matplotlib

You can install them using pip:
```bash
pip install numpy matplotlib
```

## Usage

Simply run the Python script:
```bash
python heart_3d.py
```

This will display a 3D heart shape in a matplotlib window. You can rotate and zoom the visualization using your mouse.

## Features
- Generates a smooth 3D heart shape
- Uses matplotlib's 3D plotting capabilities
- Customizable appearance (color, size, etc.)

## How it works
The script uses parametric equations to generate a 3D heart shape. It creates a surface plot using:
- A cylindrical coordinate system (phi, z)
- A radius function that depends on the z-coordinate
- Conversion to Cartesian coordinates (x, y, z)

The resulting shape is rendered using matplotlib's 3D plotting capabilities.