from tinyec import registry

# Define the curve parameters for y^2 = x^3 + ax + b
a, b = 0, 7  # Curve parameters for y^2 = x^3 + ax + b
p = 17  # Prime modulus

# Define the generator point G and its order n
G = (15, 13)  # Generator point
n = 18  # Order of the generator point

# Get the curve parameters for the predefined curve secp256r1
curve = registry.get_curve('secp256r1')

# Perform point multiplication
k = 6  # Scalar multiplier
P = k * G  # Result of point multiplication

print(f"Generator point G: {G}")
print(f"Result of point multiplication (k*G) for k={k}: {P}")
