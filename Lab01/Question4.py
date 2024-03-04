def linear_congruential_generator(a, X0, c, m, num_terms):
    sequence = []
    X = X0
    for _ in range(num_terms):
        X = (a * X + c) % m
        sequence.append(X)
    return sequence

# Define the initial values
a = 2175143
X0 = 3553
c = 10653
m = 1000000
num_terms = 4  # Number of terms in the sequence

# Generate the sequence
sequence = linear_congruential_generator(a, X0, c, m, num_terms)

print("a=2175143, seed=3553, c=10653, and m=1000000")
print("The generated sequence is:", sequence)