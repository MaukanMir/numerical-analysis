from sympy import symbols, diff, solve, Poly



def calculate_maximum_average_weight(polynomial, x):
  """_summary_
  """

  # Compute the derivative of the polynomial
  polynomial_derivative = diff(polynomial, x)

  # Solve for the roots of the derivative to find critical points
  critical_points = solve(polynomial_derivative, x)

  # Since the roots can be complex, we only want the real ones and within a reasonable range
  critical_points_real = [cp.evalf() for cp in critical_points if cp.is_real]

  # Now we will evaluate the polynomial at these points to find the maximum
  critical_values = [(cp, polynomial.subs(x, cp)) for cp in critical_points_real]

  # Sort the critical values by the second item in the tuple (the polynomial value) to find the maximum
  critical_values_sorted = sorted(critical_values, key=lambda cv: cv[1], reverse=True)

  # The first item in the sorted list is the maximum
  return critical_values_sorted[0]

# Define the symbol
x = symbols('x')
# Define the polynomial for Sample 1
sample_1 = 6.67 - 42.6434*x + 16.1427*x**2 - 2.09464*x**3 + 0.126902*x**4 - 0.00367168*x**5 + 0.0000409458*x**6
sample_2 = 6.67 - 5.67821*x + 2.91281*x**2 - 0.413799*x**3 + 0.0258413*x**4 - 0.000752546*x**5 + 0.00000836160*x**6

print(calculate_maximum_average_weight(sample_1,x))
print(calculate_maximum_average_weight(sample_2,x))
