"""
Ingrese por teclado un número positivo y muestre su tabla de multiplicar (considere que la tabla sea de 1 a 10).
"""
num = int(input("Ingrese un número positivo: "))
if num < 0:
    print("El número debe ser positivo")
else:
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
