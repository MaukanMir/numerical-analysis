import math

def calculate_function_value(input):
  
  return ((input + 3 - input ** 4) / 2) ** 0.5

def fixed_point_iteration(limit,tolerance, p0):
  
  iteration = 0
  current_point = p0
  while iteration < limit:
    
    p = calculate_function_value(current_point)
    
    if abs(p- current_point) <= tolerance:
      return p
    else:
      iteration+=1.0
      current_point= p
  
  
  return print(f"The number of iterations: {iteration} exceeded the limit. The current point is {next_point}")

tol = (1*10**-8)
fixed_point_iteration(4,tol,0)
