from sympy import symbols, prod, expand, simplify

# Define the symbol
x = symbols('x')

# Data points for Sample 1 and Sample 2
x_values_sample1 = [0, 6, 10, 13, 17, 20, 28]
y_values_sample1 = [6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74]

x_values_sample2 = [0, 6, 10, 13, 17, 20, 28]
y_values_sample2 = [6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89]

# Function to calculate Lagrange basis polynomials
def lagrange_basis(x_values, i):
    return prod([(x - x_values[j]) / (x_values[i] - x_values[j]) for j in range(len(x_values)) if j != i])

# Function to calculate and simplify the Lagrange interpolating polynomial
def simplified_lagrange_polynomial(x_values, y_values):
    P_x = sum(y_values[i] * lagrange_basis(x_values, i) for i in range(len(x_values)))
    return simplify(expand(P_x))

# Calculate and simplify the Lagrange interpolating polynomials
P_x_sample1_simplified = simplified_lagrange_polynomial(x_values_sample1, y_values_sample1)
P_x_sample2_simplified = simplified_lagrange_polynomial(x_values_sample2, y_values_sample2)

print(f"Simplified Lagrange Polynomial for Sample 1:\n{P_x_sample1_simplified}")
print(f"Simplified Lagrange Polynomial for Sample 2:\n{P_x_sample2_simplified}")