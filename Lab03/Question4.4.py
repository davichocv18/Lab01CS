from sympy import mod_inverse

# Define the curve parameters
a, b, p = 0, 7, 17

# Define the point P
x, y = 3, 1

# Define the scalar k
k = 5

# Calculate the slope
s = (3 * x**2 + a) * mod_inverse(2 * y, p) % p

# Calculate the x-coordinate of the result
x_Q = (s**2 - 2 * x) % p

# Calculate the y-coordinate of the result
y_Q = (s * (x - x_Q) - y) % p

print(f"The result of multiplying P by k is ({x_Q}, {y_Q})")