def GCD(n1, n2):
    if n1 == 0:
        return n2, 0, 1
    gcd, s1, t1 = GCD(n2 % n1, n1)
    s = t1 - (n2 // n1) * s1
    t = s1
    return gcd, s, t

# Define the pairs
pairs = [(7001, 10), (4539, 6)]

# Calculate and print the GCD and coefficients for each pair
for n1, n2 in pairs:
    gcd, s, t = GCD(n1, n2)
    print(f"The GCD of {n1} and {n2} is {gcd}. And {gcd} = {s} * {n1} + {t} * {n2}")