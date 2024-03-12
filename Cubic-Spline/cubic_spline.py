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
first_derivative_approx = spline(0.5, 1)  # 1st derivative
print(integral, exact_integral, error)
print("First Derivative (Approximation):", first_derivative_approx)


# Update the function and given points
x_points = np.array([0, 0.25, 0.5, 0.75, 1.0])
y_points = np.cos(np.pi * x_points)

# Create a natural cubic spline
spline = CubicSpline(x_points, y_points, bc_type='natural')

# Integrate the spline over [0, 1]
integral, _ = quad(lambda x: spline(x), 0, 1)

# Approximate the first and second derivatives at x = 0.5
first_derivative_approx = spline(0.5, 1)  # 1st derivative
second_derivative_approx = spline(0.5, 2)  # 2nd derivative

# Actual first and second derivatives of cos(pi*x) at x = 0.5
first_derivative_actual = -np.pi * np.sin(np.pi * 0.5)
second_derivative_actual = -np.pi**2 * np.cos(np.pi * 0.5)

print("Integral:", integral)
print("First Derivative (Approximation):", first_derivative_approx)
print("First Derivative (Actual):", first_derivative_actual)
print("Second Derivative (Approximation):", second_derivative_approx)
print("Second Derivative (Actual):", second_derivative_actual)