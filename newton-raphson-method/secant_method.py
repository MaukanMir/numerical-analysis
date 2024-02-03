import sympy as sp

# Define the symbol and function using sympy
x = sp.symbols('x')
func = -x**3 - sp.cos(x)

def calculate_function_value(function, value):
    # Evaluate the function at the specified value
    return function.subs(x, value).evalf()

def secant_method(max_iterations, tolerance, initial_guess_1, initial_guess_2):
    p0 = initial_guess_1
    p1 = initial_guess_2
    iteration_count = 0
    
    for _ in range(max_iterations):
        q0 = calculate_function_value(func, p0)
        q1 = calculate_function_value(func, p1)
        
        if q1 - q0 == 0:
            raise ValueError("Division by zero encountered. No solution found.")
        
        # Compute the next approximation using the secant method formula
        p = p1 - (q1 * (p1 - p0) / (q1 - q0))
        
        # Update the guesses for the next iteration
        p0, p1 = p1, p
        iteration_count += 1
        
        # Check for convergence
        if abs(p - p0) < tolerance:
            return p, iteration_count

    return p, iteration_count  # Return the last computed approximation

# Example usage:
tol = (1*10**-5)  # Tolerance is less strict for the sake of demonstration
approximation, iterations = secant_method(2, tol, -1,0)
print(approximation, iterations)
