import math

def calculate_function_value(input):
  
  return ((input + 3 - input ** 4) / 2) ** 0.5

def fixed_point_iteration(limit,tolerance, starting_point):
  
  iteration = 0
  current_point = starting_point
  while iteration < limit:
    
    next_point = calculate_function_value(current_point)
    
    if abs(next_point - current_point) <= tolerance:
      return next_point
    else:
      iteration+=1.0
      current_point= next_point
  
  
  return print(f"The number of iterations: {iteration} exceeded the limit. The current point is {next_point}")

tol = (1*10**-8)
fixed_point_iteration(4,tol,0)
