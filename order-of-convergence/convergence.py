import math
# Calculate the value of n
target_accuracy = 5 * 10**-2
n = (1 / target_accuracy)**(1/3)

n_ceil = math.ceil(n)  # Smallest integer greater than or equal to n
print(n_ceil)