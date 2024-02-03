import sympy as sp
import math

# Define the symbol and function using sympy
x = sp.symbols('x')
func = x**2 -6

def calculate_function_value(function, value):
    # Evaluate the function at the specified value
    return function.subs(x, value).evalf()

def false_position_method( max_iterations, tolerance, initial_guess_1, initial_guess_2):
    prev_guess = initial_guess_1
    current_guess = initial_guess_2
    iteration_count = 0
    
    while iteration_count < max_iterations:
        # Calculate function values at the previous and current guesses
        function_value_prev = calculate_function_value(func, prev_guess)
        function_value_current = calculate_function_value(func, current_guess)
        
        # Compute the difference in function values
        function_value_difference = function_value_current - function_value_prev*(function_value_current- function_value_prev)/(function_value_current - function_value_prev)
        # Prevent division by zero
        if abs(function_value_difference - function_value_current) <= tolerance:
            return print(f"The procedure was succesful. The point is:{function_value_difference}")
        
        check_negative = calculate_function_value(func, function_value_difference)
        
        if check_negative * function_value_current <0:
          prev_guess, current_guess = function_value_current, function_value_prev
        else:
          current_guess = function_value_difference
        
        iteration_count += 1
    return print(f"Exceeded the maximum of {max_iterations} iterations. Last approximation is {current_guess}.")


# Example usage:
tol = (1*10**-8)
false_position_method(3,tol,3,2)