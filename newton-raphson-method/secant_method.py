import sympy as sp
import math
# Define the symbol and function using sympy
x = sp.symbols('x')
func = (x + sp.sqrt(x)) * (20 - x + sp.sqrt(20 - x)) - 145

def calculate_function_value(function, value):
    # Evaluate the function at the specified value
    return function.subs(x, value).evalf()

def secant_method(max_iterations, tolerance, initial_guess_1, initial_guess_2):
    p0 = initial_guess_1
    p1 = initial_guess_2
    iteration = 0
    
    for _ in range(max_iterations):
        q0 = calculate_function_value(func, p0)
        q1 = calculate_function_value(func, p1)
        
        if q1 - q0 == 0:
            raise ValueError("Division by zero encountered. No solution found.")
        
        # Compute the next approximation using the secant method formula
        p = p1 - (q1 * (p1 - p0) / (q1 - q0))
        
        # Update the guesses for the next iteration
        p0, p1 = p1, p
        iteration += 1
        print(f"Iteration: {iteration}")
        print(f"P: {p}")
        print(f"p0: {p0}, p1: {p1}")
        print(f"q0: {q0} q1: {q1}")
        # Check for convergence
        if abs(p - p0) < tolerance:
            print(f"The final result is: {p}")
            return p,iteration
    return p, iteration  # Return the last computed approximation

# Example usage:
tol = (1*10**-2)  # Tolerance is less strict for the sake of demonstration
approximation, iterations = secant_method(20, tol, 10,15)
print(approximation, iterations)
