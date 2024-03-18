import numpy as np
from scipy.interpolate import CubicSpline

# Data points
distances = np.array([0.25, 0.5, 1, 1.25])  # in miles
times = np.array([22.35, 45.73, 96.06, 121.57])  # in seconds

# Fit a cubic spline to the data
spline = CubicSpline(distances, times)
# Predict the time at the 3/4 mile pole
predicted_time_34_mile = spline(0.75)
print(spline)
print(predicted_time_34_mile)