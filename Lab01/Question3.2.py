def c(M, e, p):
    return (M ** e) % p

# Define the inputs
inputs = [(101, 7, 293), (4, 11, 79), (5, 5, 53)]

# Calculate and print the results
for M, e, p in inputs:
    C = c(M, e, p)
    print(f"For M = {M}, e = {e}, p = {p}: C = {C}")