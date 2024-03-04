def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def highest_prime_in_range(range_end):
    for i in range(range_end, 1, -1):
        if is_prime(i):
            return i

# Define the ranges
ranges = [100, 1000, 5000, 10000]

# Calculate and print the highest prime number in each range
for range_end in ranges:
    highest_prime = highest_prime_in_range(range_end)
    print(f"Highest prime number up to {range_end}: {highest_prime}")