def GCD(n1, n2):
    if n1 == 0:
        return n2, 0, 1
    gcd, s1, t1 = GCD(n2 % n1, n1)
    s = t1 - (n2 // n1) * s1
    t = s1
    return gcd, s, t

# Define the pairs
pairs = [(5435, 634), (5432, 634)]

# Check if each pair is coprime
for a, b in pairs:
    gcd, s, t = GCD(a, b)
    if gcd == 1:
        print(f"{a} and {b} are coprime. GCD: {gcd}. And the equation is: {gcd} = {s} * {a} + {t} * {b}")
    else:
        print(f"{a} and {b} are not coprime. GCD: {gcd}. And the equation is: {gcd} = {s} * {a} + {t} * {b}")