from scipy.interpolate import CubicSpline
from scipy.integrate import quad
import numpy as np

# Given points
x_points = np.array([0, 0.25, 0.75, 1.0])
y_points = np.sin(x_points)

# Create a cubic spline
spline = CubicSpline(x_points, y_points, bc_type='natural')

# Function to integrate the spline
def integrand(x):
    return spline(x)

# Integrate the spline over [0, 1]
integral, error = quad(integrand, 0, 1)

# The exact integral of sin(x) from 0 to 1
exact_integral = 1 - np.cos(1)

print(integral, exact_integral, error)