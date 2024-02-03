import sympy as sp
import math
# Define the symbol and function using sympy
x = sp.symbols('x')
func = -x**3 - 2*x**2 -5

def calculate_function_value(func, point):
    # Evaluate the function at the specified point
    return func.subs(x, point).evalf()

def derivative_function(func, point):
    # Take the derivative of the function with respect to the variable
    derivative = sp.diff(func, x)
    # Evaluate the derivative at the specified point
    return derivative.subs(x, point).evalf()

def newtons_raphson_method(limit, tolerance, p0):
    iteration = 0
    while iteration < limit:
        # Calculate function value and derivative at the current point
        f_value = calculate_function_value(func, p0)
        f_prime_value = derivative_function(func, p0)
        
        if f_prime_value == 0:
            return print("Derivative was zero. No solution found.")
        
        # Newton's method formula
        p = p0 - f_value / f_prime_value

        if abs(p - p0) <= tolerance:
            return print(f"The number of iterations: {iteration}. The convergent point is: {p}")
        else:
            iteration += 1
            p0= p

    return print(f"The number of iterations: {iteration} exceeded the limit. The current point is {p0}")

# Example usage:

tol = (1*10**-4)
newtons_raphson_method(10,tol,2)