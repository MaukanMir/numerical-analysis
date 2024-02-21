import sympy as sp

# Define the symbol and function using sympy
x = sp.symbols('x')
func = x**2 - 2*x*sp.exp(-1*x) + sp.exp(-2*x)

def calculate_function_value(func, point):
    return func.subs(x, point).evalf()

def derivative_function(func, order, point):
    derivative = sp.diff(func, x, order)
    return derivative.subs(x, point).evalf()

def newtons_raphson_modified(limit, tolerance, p0):
    iteration = 0
    while iteration < limit:
        f_value = calculate_function_value(func, p0)
        f_prime_value = derivative_function(func, 1, p0)
        f_double_prime_value = derivative_function(func, 2, p0)

        if f_prime_value == 0:
            return "Derivative was zero. No solution found."

        # Corrected modified Newton's method formula
        denominator = f_prime_value**2 -  f_double_prime_value * f_value
        if denominator == 0:
            return "Denominator became zero. No solution found."

        p = p0 - (f_value * f_prime_value) / denominator

        print(f"Iteration {iteration + 1}: P is {p}, f-value: {f_value}, f_prime: {f_prime_value}, f_double_prime: {f_double_prime_value}")

        if abs(p - p0) < tolerance:
            return print(f"The number of iterations: {iteration + 1}. The convergent point is: {p}")

        p0 = p
        iteration += 1

    return f"The number of iterations: {iteration} exceeded the limit. The current point is {p0}"

# Example usage
tol = 1e-5
newtons_raphson_modified(20, tol, 0.5)
