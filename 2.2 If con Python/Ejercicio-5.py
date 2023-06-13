"""
Ingrese tres números enteros, si son mayores a cero y par, entonces súmelos, sino cuéntelos
"""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if num1 > 0 and num2 > 0 and num3 > 0:
    if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
        suma = num1 + num2 + num3
        print("La suma de los números es: ", suma)
    else:
        print("Alguno de los números no es par")
