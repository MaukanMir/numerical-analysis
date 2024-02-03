import sympy as sp

# Define the symbol and function using sympy
x = sp.symbols('x')
func = x**2 - 6

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
        p_next = p1 - (q1 * (p1 - p0) / (q1 - q0))
        
        # Update the guesses for the next iteration
        p0, p1 = p1, p_next
        iteration_count += 1
        
        # Check for convergence
        if abs(p_next - p0) < tolerance:
            return p_next, iteration_count

    return p_next, iteration_count  # Return the last computed approximation

# Example usage:
tol = (1*10**-5)  # Tolerance is less strict for the sake of demonstration
approximation, iterations = secant_method(3, tol, 3, 2)
print(approximation, iterations)
