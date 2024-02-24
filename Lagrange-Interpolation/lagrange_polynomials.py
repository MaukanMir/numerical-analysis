from sympy import symbols, prod

# Define the symbol
x = symbols('x')

# Data points
x_values = [-0.50, -0.25, 0.25, 0.50]
y_values = [1.53, 1.33, 0.57, 1.70]

# Function to calculate Lagrange basis polynomials
def lagrange_basis(x_values, i):
    return prod([(x - x_values[j]) / (x_values[i] - x_values[j]) for j in range(len(x_values)) if j != i])

# Calculate the Lagrange interpolating polynomial
P_x = sum(y_values[i] * lagrange_basis(x_values, i) for i in range(len(x_values)))

# Evaluate P(0)
P_0 = P_x.subs(x, 0)
P_x, P_0