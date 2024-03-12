p = int(input("Enter Prime number (p): "))
g = int(input("Enter Base (g): "))
a = int(input("Enter Alice's secret number (a): "))
b = int(input("Enter Bob's secret number (b): "))
A = (g**a)%p
B = (g**b)%p
print("A's public key is: ", A)
print("B's public key is: ", B)
KA = (B**a)%p
KB = (A**b)%p
if (KA == KB):
  print("The secret key of both match and their secret key is: ", KA)
else: 
  print("The secret keys are different. Alice's secret key is:", KA, " and, Bob's secret key is:", KB)