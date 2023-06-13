"""
Ingrese por teclado dos números enteros e indique cuál de ellos es el mayor.
"""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    print("El primer número es mayor que el segundo")
elif num1 < num2:
    print("El segundo número es mayor que el primero")
else:
    print("Los números son iguales")
