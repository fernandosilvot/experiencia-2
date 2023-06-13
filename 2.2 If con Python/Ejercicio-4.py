"""
Ingrese por teclado un número entero mayor a 1 y menor a 101 por teclado, luego indique si es par o impar.
"""
num = int(input("Ingrese un número entero mayor a 1 y menor a 101: "))
if num < 2 or num > 100:
    print("El número debe ser mayor a 1 y menor a 101")
else:
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
