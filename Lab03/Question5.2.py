import sys
from libnum import ecc

# y^2 = x^3 + ax + b (mod p)
a = 0
b = 7
p = 89

# Verificar si se proporcionan argumentos en la línea de comandos
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    a = int(sys.argv[1])
if len(sys.argv) > 2 and sys.argv[2].isdigit():
    b = int(sys.argv[2])
if len(sys.argv) > 3 and sys.argv[3].isdigit():
    p = int(sys.argv[3])

c = ecc.Curve(a, b, p)
print("y^2 = x^3 + %dx + %d (mod %d)\n" % (a, b, p))

points = c.find_points_in_range(1, p-1)

# Imprimir los primeros cinco puntos
print("First Five Points:")
for i, point in enumerate(points):
    if i < 5:
        print(point)
    else:
        break