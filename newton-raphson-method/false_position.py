import sympy as sp

# Define the symbol and function using sympy
x = sp.symbols('x')
func = x**2 - 6

def calculate_function_value(function, value):
    # Evaluate the function at the specified value
    return function.subs(x, value).evalf()

def false_position_method(max_iterations, tolerance, initial_guess_1, initial_guess_2):
    p0 = initial_guess_1
    p1 = initial_guess_2
    q0 = calculate_function_value(func, p0)
    q1 = calculate_function_value(func, p1)
    
    for iteration_count in range(1, max_iterations+1):
        # Compute p using the false position formula
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        # Check for convergence
        if abs(p - p1) < tolerance:
            return f"The procedure was successful. The root is approximately {p} after {iteration_count} iterations."
        
        q = calculate_function_value(func, p)

        # Check if the sign changes
        if q * q1 < 0:
            p0, q0 = p1, q1
        
        p1, q1 = p, q

    return f"Method failed after {max_iterations} iterations."

# Example usage:
tol = 1e-8
result = false_position_method(10, tol, 3, 2)
print(result)
