from sympy import symbols, prod

# Define the symbol
x = symbols('x')

# Data points
x_values = [1950,	1960,	1970,	1980,	1990,	2000, 2010, 2020]
y_values = [151326,	179323,	203302,	226542,	249633,	281422, 308746, 331449]

# Function to calculate Lagrange basis polynomials
def lagrange_basis(x_values, i):
    return prod([(x - x_values[j]) / (x_values[i] - x_values[j]) for j in range(len(x_values)) if j != i])

# Calculate the Lagrange interpolating polynomial
P_x = sum(y_values[i] * lagrange_basis(x_values, i) for i in range(len(x_values)))
print(P_x)
P_1940 = P_x.subs(x, 1940)
P_1985 = P_x.subs(x, 1985)
P_2030 = P_x.subs(x, 2030)

print(f"Population in 1940: {P_1940}")
print(f"Population in 1985: {P_1985}")
print(f"Population in 2030: {P_2030}")
