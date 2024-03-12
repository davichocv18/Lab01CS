from sympy import mod_inverse

# Define the curve parameters
a, b, p = 0, 7, 17

# Define the points P1 and P2
x1, y1 = 5, 8
x2, y2 = 12, 6

# Calculate the slope
s = (y2 - y1) * mod_inverse(x2 - x1, p) % p

# Calculate the x-coordinate of the sum
x3 = (s**2 - x1 - x2) % p

# Calculate the y-coordinate of the sum
y3 = (s * (x1 - x3) - y1) % p

print(f"The sum of P1 and P2 is ({x3}, {y3})")