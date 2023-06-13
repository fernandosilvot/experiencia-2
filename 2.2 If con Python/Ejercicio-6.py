"""
Ingrese 3 números enteros por teclado e indique ¿cuántos son menores a cero?
"""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 < 0 and num2 < 0 and num3 < 0:
    print("Los tres números son menores a cero")
elif num1 < 0 and num2 < 0:
    print("Dos números son menores a cero")
elif num1 < 0 and num3 < 0:
    print("Dos números son menores a cero")
elif num2 < 0 and num3 < 0:
    print("Dos números son menores a cero")
elif num1 < 0:
    print("Un número es menor a cero")
elif num2 < 0:
    print("Un número es menor a cero")
elif num3 < 0:
    print("Un número es menor a cero")