"""
Ingrese por teclado dos números enteros positivos, súmelos y entregue su resultado.
"""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 < 0 or num2 < 0:
    print("Los números deben ser positivos")
else:
    suma = num1 + num2
    print("La suma de los números es: ", suma)
    