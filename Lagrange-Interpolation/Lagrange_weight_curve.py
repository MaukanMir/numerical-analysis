from sympy import symbols, prod

# Define the symbol
x = symbols('x')

# Data points from the table for Sample 1
x_values_sample1 = [0, 6, 10, 13, 17, 20, 28]
y_values_sample1 = [6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74]

# Data points from the table for Sample 2
x_values_sample2 = [0, 6, 10, 13, 17, 20, 28]
y_values_sample2 = [6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89]

# Function to calculate Lagrange basis polynomials
def lagrange_basis(x_values, i):
    return prod([(x - x_values[j]) / (x_values[i] - x_values[j]) for j in range(len(x_values)) if j != i])

# Calculate the Lagrange interpolating polynomial for Sample 1
P_x_sample1 = sum(y_values_sample1[i] * lagrange_basis(x_values_sample1, i) for i in range(len(x_values_sample1)))

# Calculate the Lagrange interpolating polynomial for Sample 2
P_x_sample2 = sum(y_values_sample2[i] * lagrange_basis(x_values_sample2, i) for i in range(len(x_values_sample2)))

print(f"Lagrange Polynomial for Sample 1:\n{P_x_sample1}")
print(f"Lagrange Polynomial for Sample 2:\n{P_x_sample2}")
