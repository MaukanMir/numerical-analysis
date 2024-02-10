import math

def calculate_function_value(input):
  
  return (3*input +4)**0.33333333333

def fixed_point_iteration(limit,tolerance, p0):
  
  iteration = 0
  current_point = p0
  while iteration < limit:
    
    p = calculate_function_value(current_point)
    print(f"P is is {p}")
    if abs(p- current_point) <= tolerance:
      iteration+=1
      return print(f"The current iteration is: {iteration}, the current point is: {p}")
    else:
      iteration+=1.0
      current_point= p
  
  return print(f"The number of iterations: {iteration} exceeded the limit. The current point is {current_point}")

tol = (1*10**-2)
fixed_point_iteration(10,tol,2.5)
