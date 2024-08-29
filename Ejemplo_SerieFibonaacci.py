
n = int(input("Numero de valores para la sucesion despues de los primeros dos digitos: "))
a = 0
b = 1

print(a)
print(b)

for i in range(n):
    Sum = a + b
    print(Sum)
    a = b
    b = Sum