import sympy as sp
import math
# Define the symbol and function using sympy
x = sp.symbols('x')
func = x**2 -6

def calculate_function_value(func, point):
    # Evaluate the function at the specified point
    return func.subs(x, point).evalf()

def derivative_function(func, point):
    # Take the derivative of the function with respect to the variable
    derivative = sp.diff(func, x)
    # Evaluate the derivative at the specified point
    return derivative.subs(x, point).evalf()

def newtons_raphson_method(limit, tolerance, starting_point):
    current_point = starting_point
    iteration = 0
    while iteration < limit:
        # Calculate function value and derivative at the current point
        f_value = calculate_function_value(func, current_point)
        f_prime_value = derivative_function(func, current_point)
        
        if f_prime_value == 0:
            return print("Derivative was zero. No solution found.")
        
        # Newton's method formula
        next_point = current_point - f_value / f_prime_value

        if abs(next_point - current_point) <= tolerance:
            return print(f"The number of iterations: {iteration}. The convergent point is: {next_point}")
        else:
            iteration += 1
            current_point = next_point

    return print(f"The number of iterations: {iteration} exceeded the limit. The current point is {current_point}")

# Example usage:

tol = (1*10**-9)
newtons_raphson_method(10,tol,1)