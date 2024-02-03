import sympy as sp
import math

# Define the symbol and function using sympy
x = sp.symbols('x')
func = sp.cos(x) - x

def calculate_function_value(function, value):
    # Evaluate the function at the specified value
    return function.subs(x, value).evalf()

def secant_method( max_iterations, tolerance, initial_guess_1, initial_guess_2):
    prev_guess = initial_guess_1
    current_guess = initial_guess_2
    iteration_count = 0
    
    while iteration_count < max_iterations:
        # Calculate function values at the previous and current guesses
        function_value_prev = calculate_function_value(func, prev_guess)
        function_value_current = calculate_function_value(func, current_guess)
        
        # Compute the difference in function values
        function_value_difference = function_value_current - function_value_prev
        
        # Prevent division by zero
        if function_value_difference == 0:
            return print("Division by zero encountered. No solution found.")
        
        # Secant method formula to find the new guess
        new_guess = current_guess - function_value_current * (current_guess - prev_guess) / function_value_difference

        # Check for convergence
        if abs(new_guess - current_guess) <= tolerance:
            return print(f"The root is approximately {new_guess} after {iteration_count} iterations.")
        
        # Update the guesses for the next iteration
        prev_guess, current_guess = current_guess, new_guess
        iteration_count += 1

    return f"Exceeded the maximum of {max_iterations} iterations. Last approximation is {current_guess}."


# Example usage:
tol = (1*10**-8)
secant_method(10,tol,0.5,math.pi/4)